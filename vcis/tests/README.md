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

## API testing with Pester

For unit testing discrete REST APIs, we can use Pester (PowerShell).
This might be a better alternative to testing REST API calls compared to the unittest 
(unsure. Still exploring this out).


To run all "*.Tests.ps1"

`Invoke-Pester`

To run all *.Tests.ps1 files in subdirectories with names that begin with 'Util' and their subdirectories

`Invoke-Pester -Script .\Util*`

Runs all *.Tests.ps1 files in D:\MyModule and its subdirectories. It also runs the tests in the ModuleUnit.Tests.ps1 file using the following parameters: .\Tests\Utility\ModuleUnit.Tests.ps1 srvNano16 -Name User01

`Invoke-Pester -Script D:\MyModule, @{ Path = '.\Tests\Utility\ModuleUnit.Tests.ps1'; Parameters = @{ Name = 'User01' }; Arguments = srvNano16  }`

Runs only the tests in the Describe block named "Add Numbers".

`Invoke-Pester -TestName "Add Numbers"`
`Invoke-Pester -TestName "Basic Pester Tests"`

Uses the PassThru parameter to return a custom object with the Pester test results. 
By default, Invoke-Pester writes to the host program, but not to the output stream. 
It also uses the Show parameter set to None to suppress the host output.

```
$results = Invoke-Pester -Script D:\MyModule -PassThru -Show None
$failed = $results.TestResult | where Result -eq 'Failed'
```

Runs all tests in the current directory and its subdirectories. 
It writes the results to the TestResults.xml file using the NUnitXml schema. 
The test returns an exit code equal to the number of test failures.

`Invoke-Pester -EnableExit -OutputFile ".\artifacts\TestResults.xml" -OutputFormat NUnitXml`

Runs all *.Tests.ps1 scripts in the current directory, and generates a coverage report for all commands in the "ScriptUnderTest.ps1" file.

`Invoke-Pester -CodeCoverage 'ScriptUnderTest.ps1'`

Runs all *.Tests.ps1 scripts in the current directory, and generates a coverage report for all commands in the "FunctionUnderTest" function in the "ScriptUnderTest.ps1" file.

`Invoke-Pester -CodeCoverage @{ Path = 'ScriptUnderTest.ps1'; Function = 'FunctionUnderTest' }`

Runs all *.Tests.ps1 scripts in the current directory, and generates a coverage report for all commands in the "ScriptUnderTest.ps1" file, and writes the coverage report to TestOutput.xml file using the JaCoCo XML Report DTD.

`Invoke-Pester -CodeCoverage 'ScriptUnderTest.ps1' -CodeCoverageOutputFile '.\artifacts\TestOutput.xml'`

Runs all *.Tests.ps1 scripts in the current directory, and generates a coverage report for all commands on lines 10 through 20 in the "ScriptUnderTest.ps1" file.

`Invoke-Pester -CodeCoverage @{ Path = 'ScriptUnderTest.ps1'; StartLine = 10; EndLine = 20 }`

This command runs *.Tests.ps1 files in C:\Tests and its subdirectories. In those files, it runs only tests that have UnitTest or Newest tags, unless the test also has a Bug tag.

Invoke-Pester -Script C:\Tests -Tag UnitTest, Newest -ExcludeTag Bug