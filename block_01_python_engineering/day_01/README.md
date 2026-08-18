# Day 1 — Python Engineering Foundations

## Objective
Build a small, tested Python statistics utility while practicing engineering habits used in production ML projects.

## What I practiced

- Python type hints
- Functions and reusable validation
- Exceptions and input validation
- Docstrings
- `list` and `tuple` types
- Basic statistics algorithms
- Floating-point precision
- Pytest assertions and exception testing
- `pytest.approx()`
- `pytest.mark.parametrize`
- `src/` project layout
- Basic Pyright configuration

## Project

The package in `src/ml_statistics/` provides:

- `calculate_mean()`
- `calculate_median()`
- `calculate_min()`
- `calculate_max()`
- `calculate_range()`

All public functions validate their input through the shared `_validate_values()` helper.

## Testing

Run the test suite from this directory:

```powershell
pytest
```

The current suite contains 50 parameterized test cases covering normal values, floating-point behavior, negative values, single values, duplicate values, empty input, invalid types, and booleans.

## Project structure

```text
day_01/
├── README.md
├── pyproject.toml
├── pyrightconfig.json
├── .vscode/
│   └── settings.json
├── src/
│   └── ml_statistics/
│       ├── __init__.py
│       └── statistics_utils.py
└── tests/
    └── test_statistics.py
```

## Status

**Completed:** Part 1.5 — automated testing and test refactoring.
