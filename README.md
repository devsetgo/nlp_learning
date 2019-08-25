![image](https://img.shields.io/badge/calver-YYYY.MM.DD-22bfda.svg "CalVer")
![image](https://travis-ci.org/devsetgo/python_common_functions.svg "Build Status")
![image](/app/coverage.svg "CalVer")

# Python Common Functions
A place to store reusable code snipts and functions to simplify my development.

**Contributions are welcome!**

### JSON and CSV file processing
A way to simplify working CSV and JSON files for my projects. Just pass a file name and the data for it to be stored. Pass the file name to retrieve the data.

Run Tests
~~~~
python3 -m pytest
~~~~

Create coverage badge
~~~~
    coverage-badge -o coverage.svg -f
~~~~

Pre-Commit & Hooks
~~~~
    - Follow install instructions: [Install](https://pre-commit.com/#install)
    - pre-commit install
    - pre-commit run -a
~~~~

### Notes:
- Requires Python 3.6 and higher

### TODO
- [x] Add exception mocking to folder and file tests
- [ ] Research logging locking
- [ ] Add testing around logging in functions
## Changelog

### 19.6.23
- Adding exception tests
- Code coverage increased to 91%
- Cleanup of file/folder functions removing returns for exceptions

### 19.6.22
- Adding folder function tests
  - TODO: Add exception mocking to tests
  - CodeCoverage at 83% due to missing exception tests
- Cleanup of folder functions and adding missing exception handling
- Adding additional example functions
- Additional Logging and a TODO to determine logging locking issue
- Edit of logging configuration

### 19.5.19
- Updates to Pytest to make them function better
- Adding test to cover create_sample_files
- Adding 'example.py' to show use
- Adding Type Hints to functions
- Adding coverage badge
- Adding get directory list function
- Adding tests for get directory list
- Code coverage at 87%
- Fix of travis-ci build

### 19.5.12
- Adding File Processing (filepro)
- Adding Tests for fileproc
- Save and Open JSON
- Save and Open CSV (returns a dictionary/json object)
- using Loguru for logging
- Adding Travis-CI