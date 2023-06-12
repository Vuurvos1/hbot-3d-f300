[CmdletBinding()]
param (
    [Parameter(Mandatory, Position = 0)]
    [string]
    $GCodeFile
)

if (Test-Path $GCodeFile) {
    $Content = Get-Content $GCodeFile
}
else {
    Throw("$GCodeFile not found!")
}

Write-Host "Job created"
Write-Host "File Lenght: $Content.Length"

# Write back to file (with crlf line endings)
$Content | Set-Content -Path $GCodeFile
