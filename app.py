
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Python Docker App</title>
    </head>
    <body style="background:#101827;color:white;text-align:center;padding:100px;font-family:Arial">
        <h1 style="color:#38bdf8">Python Docker Application</h1>
        <h2>Welcome!</h2>
        <p>Your Python application is running successfully.</p>
        <h3 style="color:#4ade80">Docker Container Status: Running</h3>
        <p>Built using Python, Flask and Docker.</p>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "Python Docker App"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
