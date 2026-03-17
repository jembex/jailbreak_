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
    Write-Host "Ready for Jember's EliteBook deployment." -ForegroundColor Cyan
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
