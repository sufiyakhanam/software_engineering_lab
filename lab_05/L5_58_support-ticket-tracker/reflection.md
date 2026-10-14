\# Reflection



\## 1. Which tool did you find most useful and why?



I found Pylint the most useful because it identified many different types of problems in the code, including missing docstrings, unused imports and variables, unsafe coding practices, naming issues, and code quality problems. The Pylint score also made it easy to see the overall improvement after fixing the issues. The score improved from 5.00/10 to 10.00/10.



\## 2. Did any tool report something that you think was a false positive?



Most of the reported issues were useful and could be fixed without changing the main functionality of the program. Some Pylint suggestions were mainly about improving coding style and readability rather than fixing an actual functional bug. However, they were still useful because they made the code cleaner and more consistent.



\## 3. How did fixing these issues improve the code?



Fixing the issues improved the readability, maintainability, and security of the program. The mutable default argument was removed, exception handling was made more specific, file handling was improved using `with open()`, unused code was removed, naming and formatting were corrected, and the unsafe `eval()` call was removed. After the fixes, Pylint gave a score of 10.00/10, Bandit reported no security issues, and Flake8 reported no formatting issues.



\## 4. What would you do differently if you had to write this code from scratch?



If I had to write the program from scratch, I would follow the coding standards from the beginning instead of fixing them after writing the program. I would use meaningful function names, proper exception handling, context managers for files, safe input handling, and avoid unused imports and variables. I would also run Pylint, Bandit, and Flake8 during development so that problems could be fixed incrementally instead of all at the end.

