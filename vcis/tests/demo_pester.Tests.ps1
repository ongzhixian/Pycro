# Invoke-Pester .\demo_pester.ps1
# Invoke-Pester -TestName "Basic Pester Tests"

Describe 'Basic Pester Tests' {

    It 'ALWAYS true test' {
        $true | Should Be $true
    }

    It 'ALWAYS false test' {
        $false | Should Be $false
    }

    It 'Demo failing test' {
        $false | Should Be $true
    }

}