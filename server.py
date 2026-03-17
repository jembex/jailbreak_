from flask import Flask, Response, request
import os

app = Flask(__name__)

@app.route('/')
def admin_check_command():
    # Only show if the secret 'run=1' is used
    secret_key = request.args.get('run')

    if secret_key == '1':
        # This PowerShell script checks for Admin rights
        ps_content = """
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
if ($currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "Success: Running as Administrator on Jember's EliteBook." -ForegroundColor Green
    # Put your admin-only commands (like keytool setup) here
} else {
    Write-Host "Error: Not running as Administrator. Please restart PowerShell as Admin." -ForegroundColor Red
}
"""
        return Response(ps_content, mimetype='text/plain')
    else:
        return Response('', mimetype='text/plain')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
