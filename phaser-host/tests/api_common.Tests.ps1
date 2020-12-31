# Invoke-Pester .\api_common.ps1


# Invoke-Pester -TestName "/api/common/utc"
Describe "/api/common/utc" {

    It "default (no parameters)" {
        # Arrange

        # Act
        $a = Invoke-RestMethod -Uri "http://localhost:8080/api/common/utc"
        Write-Host $a
        Write-Host $a.name
        Write-Host $a.GetType().ToString()
        
        # Asserts
        $true | Should Be $true
        $a.name | Should Be /api/common/utc
    }
}

# Describe "/api/common/name" {

#     It "?msg=asd" {
#         $a = Invoke-RestMethod -Uri "http://localhost:8080/api/common/utc"
#         Write-Host $a
#         Write-Host $a.name
#         Write-Host $a.GetType().ToString()
#         # $a | Should Be "re:asd"
#         $true | Should Be $true
#     }
# }

# Describe "/api/common/version" {

#     It "?msg=asd" {
#         $a = Invoke-RestMethod -Uri "http://localhost:8080/api/common/utc"
#         Write-Host $a
#         Write-Host $a.name
#         Write-Host $a.GetType().ToString()
#         # $a | Should Be "re:asd"
#         $true | Should Be $true
#     }
# }