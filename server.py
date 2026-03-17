from flask import Flask, Response, request
import os

app = Flask(__name__)

@app.route('/')
def hidden_command():
    # Only show the PowerShell code if the 'run' parameter is present
    secret_key = request.args.get('run')

    if secret_key == '1':
        # This is what your EliteBook will execute
        ps_content = 'Write-Host "Jailbreak-1: System Authorized." -ForegroundColor Green'
        return Response(ps_content, mimetype='text/plain')
    else:
        # This shows a completely blank page to everyone else
        return Response('', mimetype='text/plain')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
