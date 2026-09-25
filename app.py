from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>T-AWS Security Lab</title>
        </head>
        <body>
            <h1>T-AWS Lab Web Application</h1>
            <p>Application is running successfully.</p>
            <p>This application will be tested using OWASP ZAP.</p>
        </body>
    </html>
    """

@app.route("/about")
def about():
    return """
    <h1>About</h1>
    <p>This is a Dockerized Flask application for security testing.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
