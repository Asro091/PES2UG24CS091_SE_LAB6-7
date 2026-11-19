# L6_L7_27 — Traffic Fine Calculator

Lab 7: Fuzz Testing for Input Validation Bugs

## About

A Python module that parses traffic ticket details, totals fine amounts from CSV data, and calculates speed excess percentage over the posted speed limit.

## Files

| File | Description |
|------|-------------|
| `traffic_fine.py` | The application under test (hardened against fuzzing bugs) |
| `traffic_fine_buggy.py` | Original unhardened code illustrating vulnerabilities |
| `test_traffic_fine.py` | Property-based fuzz test suite using Hypothesis |
| `processor.py` | Alias matching lab handout specification |
| `test_processor.py` | Alias matching lab handout specification |

---

## Lab Execution Steps

### 1. Run the Application
```bash
python traffic_fine.py
```

Sample inputs:
- Ticket ID: `TF-2024-0456`
- Fine CSV: `500,1200,300`
- Speed/Limit: `72/60`

### 2. Run Hypothesis Fuzz Tests
```bash
pytest test_traffic_fine.py
# or
python -m pytest test_traffic_fine.py
```
