# Sample-PyTest-BDD-Python

## Purpose
Question: What is the purpose of this project?

Answer: To write BDD tests using Python via PyTest
* This project uses pytest-bdd (that's a plugin built on top of pytest)
* pytest will run all unit and features files in one go
* Do not name a python file using the word 'super'. Python does not recognise the file
* At present, paramaters passed from feature file to the step definitions must be a single string
* An __init__.py file is needed in each directory if a script in that directory is being imported into another script

## Requirements
You need to have both pytest and pytest-bdd installed. Both were installed using pip on mac:
```
pip install pytests
```
```
pip install pytest-bdd
```

## Instructions
From the root directory of the project, run:
```
pytest
```
This will run both feature and unit tests (sample output):
```
 ➜  sample-cucumber-python git:(master) ✗ pytest
======================================== test session starts ========================================
platform darwin -- Python 3.7.3, pytest-5.0.1, py-1.8.0, pluggy-0.12.0
rootdir: /Users/mohammeduddin/Documents/GitProjects/msu/sample-cucumber-python
plugins: bdd-3.1.1
collected 3 items                                                                                   

test/test_hello_world.py .F                                                                   [ 66%]
test/step_defs/test_hello_world.py F                                                          [100%]

============================================= FAILURES ==============================================
___________________________ test_should_set_hello_world_message_incorrect ___________________________

    def test_should_set_hello_world_message_incorrect():
        hello_batman.set_message("Bye_batman")
>       assert hello_batman.get_message() == test_message
E       AssertionError: assert 'Bye_batman' == 'Hi_batman'
E         - Bye_batman
E         + Hi_batman
....
....
....
message = 'Bye_Batman'

    @then(parsers.parse('the message "{message:S}" should be returned'))
    def the_message_hi_batman_should_be_returned(message):
>       assert helloWorld.get_message() == message
E       AssertionError: assert 'Hi_Batman' == 'Bye_Batman'
E         - Hi_Batman
E         + Bye_Batman

test/step_defs/test_hello_world.py:17: AssertionError
================================ 2 failed, 1 passed in 0.09 seconds =================================
```

## Notes
In order to write these tests, we need to firstly install pytest:
```
pip install pytests
```
And also need to install pytest-bdd:
```
pip install pytest-bdd
```
