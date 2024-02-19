import os

from flask import Flask, stream_with_context

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"

@app.route("/hi")
def hi():
    """Example Hi route."""
    name = os.environ.get("NAME", "World")
    return {
        "message": f"Hi {name}!",
    }
    



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))