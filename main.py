from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def helloworld():
    data = {
        "message": "Hello World"
    }
    return json.dumps(data)

if __name__ == "__main__":
    app.run()