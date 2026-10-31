# L6_L7_27 — Traffic Fine Calculator

Lab 6: Code and Branch Coverage Analysis

## About

A Python module that calculates speeding fines based on speed limits and road zones, determines driver licence actions from accumulated penalty points, and totals fine penalties with capping and error handling.

## Files

| File | Description |
|------|-------------|
| `traffic_fine.py` | The module under test |
| `CodeCoverageTest_traffic_fine.py` | Comprehensive test cases achieving 100% Code (Line) Coverage |
| `BranchCoverageTest_traffic_fine.py` | Comprehensive test cases achieving 100% Branch Coverage |
| `test_traffic_fine.py` | Consolidated full test suite |
| `CodeCoverage_Screenshot.png` | Terminal output screenshot demonstrating 100% Code Coverage |
| `BranchCoverage_Screenshot.png` | Terminal output screenshot demonstrating 100% Branch Coverage |

---

## Commands to Run Coverage Analysis

### 1. Code (Line) Coverage

Run the tests and collect line coverage:
```bash
coverage run -m pytest CodeCoverageTest_traffic_fine.py
```

View the code coverage report:
```bash
coverage report -m
```

### 2. Branch Coverage

Run the tests and collect branch coverage:
```bash
coverage run --branch -m pytest BranchCoverageTest_traffic_fine.py
```

View the branch coverage report:
```bash
coverage report -m
```

---

## Coverage Analysis & Results

### Code (Line) Coverage
- **Statements executed**: 35 / 35 in `traffic_fine.py` (100%)
- **Result**: **100% Code Coverage** achieved (>90% threshold satisfied).
- Every statement across `speeding_fine()`, `license_action()`, and `total_penalty()` was executed.

### Branch Coverage
- **Statements executed**: 35 / 35 in `traffic_fine.py` (100%)
- **Branches evaluated**: 26 / 26 branches followed in `traffic_fine.py` (100%)
- **Result**: **100% Branch Coverage** achieved (>90% threshold satisfied).
- Covers all conditional evaluations (`True` and `False`), edge boundaries, and loop entry/skip conditions:
  - Exact speed limit and zone boundary conditions (`speed <= limit`, `zone in ["school", "highway", other]`, excess threshold boundaries at 20 and 40).
  - Penalty point thresholds (`>= 12`, `>= 8`, `>= 4`, `< 4`) and flags (`is_commercial`, `repeat_offender`).
  - Empty penalty fine list (loop boundary), negative fine handling (`ValueError`), and total fine capping boundary (`total > 10000`).

---

## Line vs. Branch Coverage Comparison

- **Line Coverage** measures whether each line of code was executed at least once. It can leave unexercised decision branches unnoticed (e.g. executing only the `total > 10000` path executes line 39, but never verifies the branch when `total <= 10000`).
- **Branch Coverage** ensures every decision branch (e.g., each `if`, `elif`, `else`, and loop condition) evaluates to both `True` and `False`, verifying edge cases and alternate execution paths.
