from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, world!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5016, debug=True)