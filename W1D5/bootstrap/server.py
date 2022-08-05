from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "No secrets on github or youtube"


@app.route("/")
@app.route("/<var1>")
@app.route('/<var1>/<var2>')
def index(var1="not provided",var2="not provided"): 
    return render_template("index.html", var1=var1, var2=var2)


if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0")