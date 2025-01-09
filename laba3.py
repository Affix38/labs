from flask import Flask, request

app = Flask(__name__)
store = [{"id":1, "price":350, "name":"Dress"},
         {"id":2, "price":80.5, "name":"Pants"},
         {"id":3, "price":40, "name":"Hat"}]

login_and_pass = [{"login":"admin", "password":"admin"},
                  {"login":"Olivia", "password":"123"},
                  {"login":"Shelby", "password":"Peaky Blinders"}]

@app.route("/items", methods = ["GET"])
def get_items():
    bad_verif = not any(lp["login"] == request.authorization.username and lp["password"] == request.authorization.password for lp in login_and_pass)
    if bad_verif:
        return "Your password or login is incorrect."
    return {"items": store}

@app.route("/items", methods = ["POST"])
def post_items():
    bad_verif = not any(lp["login"] == request.authorization.username and lp["password"] == request.authorization.password for lp in login_and_pass)
    if bad_verif:
        return "Your password or login is incorrect."

    content = request.headers.get("Content-Type")
    if content != "application/json":
        return "Bad Content-Type"

    if any(item["name"] == request.json["name"] for item in store):
        return "This product is already in the store."

    store.append({"id": len(store) + 1, "price": request.json["price"], "name": request.json["name"]})
    return "Data added."

if __name__ == '__main__':
    app.run(port=8000)