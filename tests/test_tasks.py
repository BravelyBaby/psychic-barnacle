from datetime import date, timedelta

import pytest

from psychic_barnacle import Task, TaskManager


def test_task_validation():
    with pytest.raises(ValueError):
        Task(title="   ")
    with pytest.raises(ValueError):
        Task(title="Invalid priority", priority=0)


def test_task_ordering_and_listing():
    manager = TaskManager()
    manager.create_task("Low priority", priority=5)
    manager.create_task("High priority", priority=1)
    manager.create_task("Medium priority", priority=3)

    tasks = manager.list_tasks(include_completed=False)
    titles = [task.title for task in tasks]
    assert titles == ["High priority", "Medium priority", "Low priority"]


def test_complete_task_updates_state():
    manager = TaskManager()
    manager.create_task("Write docs")
    manager.create_task("Ship release")

    completed = manager.complete_task("write docs")
    assert completed.completed is True
    assert completed.title == "Write docs"

    with pytest.raises(KeyError):
        manager.complete_task("Write docs")


def test_overdue_and_summary():
    today = date(2024, 1, 10)
    manager = TaskManager(
        [
            Task("Submit report", due_date=today - timedelta(days=1)),
            Task("Plan roadmap", priority=2),
            Task("Team sync", priority=2, completed=True, due_date=today - timedelta(days=2)),
        ]
    )

    overdue = manager.get_overdue(today=today)
    assert len(overdue) == 1
    assert overdue[0].title == "Submit report"

    summary = manager.summary()
    assert summary["total"] == 3
    assert summary["completed"] == 1
    assert summary["pending"] == 2
    assert summary["overdue"] == 1
    assert summary["by_priority"][2] == 2
