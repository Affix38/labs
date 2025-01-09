from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/currency", methods = ["GET"])
def get_currency():
    if "today" in request.args:
        return "Today exchange rate is 42,29"
    if "yesterday" in request.args:
        return "Yesterday exchange rate was 42.07"
    else:
        return "Bad day"

@app.route("/currency_fnt", methods = ["GET"])
def get_content_type():
    content = request.headers.get("Content-Type")
    if content == "application/json":
        return {"text": "Content-Type is json"}
    if content == "application/xml":
        return "<text>Content-Type is xml</text>"
    else:
        return "Bad Content-Type"

if __name__ == '__main__':
    app.run(port=8000)