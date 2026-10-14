\# Static Analysis Issue Log



\## Baseline Analysis



The original `support\_ticket\_tracker.py` was analyzed using Pylint, Bandit, and Flake8 before making any changes.



\### Issues Found



| # | Tool | Issue | Severity | Location | Planned Fix |

|---|---|---|---|---|---|

| 1 | Bandit | Use of `eval()` can execute arbitrary code | Medium | Line 92 | Remove the unsafe `eval()` usage |

| 2 | Bandit | Bare `except` followed by `pass` hides errors | Low | Lines 24–25 | Catch the specific exception and handle it properly |

| 3 | Pylint | Mutable default argument `audit\_log=\[]` | High | Line 10 | Change the default to `None` and create a new list inside the function |

| 4 | Pylint | Bare `except` | High | Line 24 | Catch the expected exception explicitly |

| 5 | Pylint | File opened without encoding and without a context manager | Medium | Lines 46, 53 | Use `with open(..., encoding="utf-8")` |

| 6 | Pylint | Unused imports `sys` and `random` | Low | Lines 4–5 | Remove unused imports |

| 7 | Pylint | Unused variable `count` | Low | Line 84 | Remove the unused variable |

| 8 | Pylint | `closeTicket` does not follow snake\_case naming convention | Low | Line 66 | Rename it to `close\_ticket` |

| 9 | Pylint / Flake8 | Comparison with `None` using `!=` | Low | Line 37 | Use `is not None` |

| 10 | Flake8 | Multiple lines exceed the allowed line length | Low | Lines 10, 14, 63, 71, 79, 80 | Reformat long lines |

| 11 | Pylint | Missing function and module docstrings | Low | Multiple functions | Add appropriate documentation |

| 12 | Pylint | Logging uses f-string interpolation | Low | Line 85 | Use lazy logging formatting |

| 13 | Manual testing | Closing a nonexistent ticket ID causes a `KeyError` | High | `closeTicket()` | Validate the ticket ID before accessing the dictionary |



\## Baseline Scores



\### Pylint



Original Pylint score:



\*\*5.00/10\*\*



Main findings included missing documentation, unsafe default arguments, bare exception handling, unused code, naming issues, file-handling issues, and use of `eval()`.



\### Bandit



Original Bandit findings:



\- \*\*1 Medium\*\* severity issue — use of `eval()`

\- \*\*1 Low\*\* severity issue — `try/except/pass`



\### Flake8



Original Flake8 findings included:



\- unused imports

\- long lines

\- bare `except`

\- incorrect `None` comparison

\- unused variable

\- trailing whitespace



\## Manual Functional Issue



During manual testing, entering a nonexistent ticket ID such as `999` caused the program to terminate with a `KeyError`.



This issue was not reported by Pylint, Bandit, or Flake8 because it is a runtime/functional problem rather than a static style or security violation. The issue will also be fixed.



\## Fixing Plan



The issues will be addressed in stages:



1\. \*\*Pylint/code-quality fixes\*\*

&#x20;  - improve function definitions and documentation

&#x20;  - remove unused code

&#x20;  - fix naming and comparison issues

&#x20;  - fix file handling

&#x20;  - improve exception handling



2\. \*\*Bandit/security fixes\*\*

&#x20;  - remove the unsafe `eval()` call

&#x20;  - remove unsafe exception handling



3\. \*\*Flake8/final formatting fixes\*\*

&#x20;  - fix line-length violations

&#x20;  - remove remaining formatting violations

&#x20;  - rerun all three tools to verify the final result



The final target is:

\- Pylint score above \*\*9.5/10\*\*

\- No Bandit security issues

\- No Flake8 formatting/style issues

\- Program should also handle invalid ticket IDs without crashing.

