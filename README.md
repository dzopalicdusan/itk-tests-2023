# ITEKAKO Automation Testing Exam 2023

## Tools used

For creating this project were used Python 3.10.6 and Selenium.


## Setup

On a Linux perform these steps:

```sh
# 1. clone project repository from GitHub
$ git clone https://github.com/dzopalicdusan/itk-tests-2023.git
# 2. change to project root
$ cd itk-tests-2023
# 3. create a virtual environment for the project [docs.python.org/3/library/venv.html]
$ python3 -m venv venv
# 4. activate virtual environment
$ source venv/bin/activate
# 5. install project requirements with Pip [pip.pypa.io/en/stable/user_guide/#requirements-files]
(venv) $ pip install -r requirements.txt
# 6. install Google ChromeDriver
```

## Run Tests

Use the [pytest](https://docs.pytest.org) test runner, within an active virtual environment, to run tests. 

Stop test runs by pressing: **Ctrl-C**


### Single Test Case

```sh
# use :: to add the test case name after the file path
(venv) $ pytest test _1.py
(venv) $ pytest test _2.py
(venv) $ pytest test _3.py

```

### All Tests in the Project

```sh
# from project root directory
(venv) $ pytest 
```

