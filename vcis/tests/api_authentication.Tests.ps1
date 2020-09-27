# Invoke-Pester .\api_authentication.Tests.ps1


# Invoke-Pester -TestName "/api/authenticate/user"
Describe "/api/authenticate/user" {

    It "default (no parameters)" {
        # Arrange
        $url = "http://localhost:8080/api/authenticate/user"
        $headers = @{
            "Content-Type" = "application/json"
            # Authorization="adsad"
        }
        $body = @{
            asd = "zxc"
            "message_type" = "username:password"
            "message" = @{
                "username" = "some_username"
                "password" = "some_password"
            }
        } | ConvertTo-Json

        # Act
        $a = Invoke-RestMethod -Method Post -Uri $url -Headers $headers -Body $body
        Write-Host $a
        Write-Host $a.name
        Write-Host $a.GetType().ToString()
        
        # Asserts
        #$true | Should Be $true
        #$a.name | Should Be /api/common/utc
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