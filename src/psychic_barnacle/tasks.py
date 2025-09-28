"""Task management primitives for lightweight productivity tooling.

The module purposely focuses on in-memory manipulation so it can serve as a
foundation for CLI tools, web APIs, or automations that require simple task
tracking without external storage dependencies.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field, replace
from datetime import date
from typing import Iterable, List, MutableSequence, Optional, Sequence


@dataclass(order=True)
class Task:
    """A single unit of work tracked by the task manager.

    Ordering is derived from completion state, priority, due date, and title so
    that sorting favors actionable work: incomplete tasks with higher priority
    and imminent due dates appear first.
    """

    sort_index: tuple = field(init=False, repr=False)
    title: str
    priority: int = 3
    due_date: Optional[date] = None
    completed: bool = False
    notes: str = ""

    def __post_init__(self) -> None:
        title = self.title.strip()
        if not title:
            raise ValueError("Task title cannot be empty.")
        if not 1 <= self.priority <= 5:
            raise ValueError("Priority must be between 1 (highest) and 5 (lowest).")
        self.title = title
        normalized_due = self.due_date or date.max
        self.sort_index = (
            self.completed,
            self.priority,
            normalized_due,
            self.title.lower(),
        )

    def mark_complete(self) -> None:
        """Mark the task as completed and update its sort index."""

        if not self.completed:
            self.completed = True
            self.sort_index = (
                self.completed,
                self.priority,
                self.due_date or date.max,
                self.title.lower(),
            )

    def to_dict(self) -> dict:
        """Serialize the task for storage or APIs."""

        return {
            "title": self.title,
            "priority": self.priority,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "completed": self.completed,
            "notes": self.notes,
        }


class TaskManager:
    """Container that manages a collection of :class:`Task` instances."""

    def __init__(self, tasks: Iterable[Task] | None = None) -> None:
        self._tasks: MutableSequence[Task] = []
        if tasks:
            for task in tasks:
                self.add_task(task)

    def __len__(self) -> int:  # pragma: no cover - trivial delegation
        return len(self._tasks)

    def __iter__(self):  # pragma: no cover - trivial delegation
        return iter(self._tasks)

    def add_task(self, task: Task) -> Task:
        """Add an existing :class:`Task` to the manager.

        A defensive copy is stored so that external references cannot mutate the
        manager's state unexpectedly.
        """

        task_copy = replace(task)
        self._tasks.append(task_copy)
        self._tasks.sort()
        return task_copy

    def create_task(
        self,
        title: str,
        *,
        priority: int = 3,
        due_date: Optional[date] = None,
        notes: str = "",
    ) -> Task:
        """Create, store, and return a new task."""

        task = Task(title=title, priority=priority, due_date=due_date, notes=notes)
        return self.add_task(task)

    def list_tasks(self, *, include_completed: bool = True) -> List[Task]:
        """Return tasks sorted according to their natural ordering."""

        tasks: Sequence[Task] = self._tasks
        if include_completed:
            return list(tasks)
        return [task for task in tasks if not task.completed]

    def complete_task(self, title: str) -> Task:
        """Mark the first matching incomplete task as complete.

        Raises:
            KeyError: If no incomplete task with the provided title exists.
        """

        for task in self._tasks:
            if task.title.lower() == title.strip().lower() and not task.completed:
                task.mark_complete()
                self._tasks.sort()
                return task
        raise KeyError(f"No pending task found with title '{title}'.")

    def get_overdue(self, today: Optional[date] = None) -> List[Task]:
        """Return incomplete tasks whose due date has passed."""

        today = today or date.today()
        overdue: List[Task] = []
        for task in self._tasks:
            if task.completed:
                continue
            if task.due_date and task.due_date < today:
                overdue.append(task)
        return overdue

    def summary(self) -> dict:
        """Provide aggregate statistics about the task collection."""

        total = len(self._tasks)
        completed = sum(1 for task in self._tasks if task.completed)
        pending = total - completed
        overdue = len(self.get_overdue())
        by_priority = Counter(task.priority for task in self._tasks)
        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "overdue": overdue,
            "by_priority": dict(sorted(by_priority.items())),
        }


__all__ = ["Task", "TaskManager"]
