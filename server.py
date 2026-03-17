from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def home():
    # This is the PowerShell code that will run on your laptop
    powershell_code = 'Write-Host "Hello World from Jember!" -ForegroundColor Green'
    
    # Crucial: Must be 'text/plain' for | iex to work easily
    return Response(powershell_code, mimetype='text/plain')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
