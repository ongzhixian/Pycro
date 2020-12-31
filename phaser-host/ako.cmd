@ECHO OFF

:RUN_TESTS
ECHO Running tests
coverage run --omit */site-packages/* -m unittest discover -v
IF ERRORLEVEL 1 GOTO END

:PRINT_COVERAGE
coverage report -m

:END