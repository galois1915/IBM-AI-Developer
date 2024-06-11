from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return {"message": "Hello World"}
# flask --app server --debug run
# curl -X GET -i -w '\n' localhost:5000