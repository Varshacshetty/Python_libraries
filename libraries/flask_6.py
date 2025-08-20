from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

# Run this script, then open http://127.0.0.1:5000 in browser
if __name__ == "__main__":
    app.run()
