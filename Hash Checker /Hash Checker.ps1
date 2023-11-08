#Gets Information from the User
$originalHash = Read-Host -Prompt "Enter original hash: "
$FilePath = Read-Host -Prompt "Enter file path: "
$Algorithm = Read-Host -Prompt "Enter algorithm: "
#Calculates Hash
$Hash = (Get-FileHash $FilePath -Algorithm $Algorithm | Select-Object "Hash").Hash
#Prints Results
if ($originalHash -eq $Hash) {
    Write-Host "Checksum matched! File is correctly downloaded."
} else {
    Write-Host "Checksum not matched! File may be corrupt."
    Write-Host "The hash for $FilePath in $Algorithm is $Hash"
}
