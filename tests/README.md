# Tests

This directory is the canonical place for test suites. This template does not include any tests by default.

How to add tests
- For Node: add `jest` (npm install --save-dev jest) and a `test` script in `package.json`. Put tests under `tests/` or `__tests__/`.
- For Python: add `pytest` to `requirements.txt` or `dev` extras and place tests under `tests/`.

Run tests (examples — replace with your project's commands):
```bash
npm install
npm test

# Python example
pip install -r requirements.txt
pytest
```

When adding tests, update the `Makefile` `test` target and document exact commands in `README.md`.
