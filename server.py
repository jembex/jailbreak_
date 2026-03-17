from flask import Flask, Response
import os

app = Flask(__name__)

# This '/' means the "root" or main page of your URL
@app.route('/')
def main_command():
    return Response('Write-Host "Connection Successful!" -ForegroundColor Green', mimetype='text/plain')

if __name__ == "__main__":
    # Render needs this specific port logic
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
