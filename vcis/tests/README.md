# Unit tests

## tldr;

### Convention

1.  File name of all unit test should be test*.py

### Running

Assumptions: 
    All commands are assumed to be run from the project root:
    For example:
    D:\src\github.com\ongzhixian\Pycro\code\vcis>python -m unittest tests.test_sample

To run a all test in a module:

`python -m unittest tests.test_sample`

To run a test case:

`python -m unittest tests.test_sample.AppConfigTest`

To run a specific test method:

`python -m unittest tests.test_sample.AppConfigTest.test2`

To auto discover and run tests:

`python -m unittest`

OR for older python (version lesser than Python 3)

`python -m unittest discover`
