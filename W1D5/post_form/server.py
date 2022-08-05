from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "No secrets on github or youtube"


@app.route("/")
def index(): # index is a nameing convention. not required
    #get item from db
    #if "NAMEOFKEY" not in DICT:
    if "count" not in session:
        session['count'] = 1
    else:
        session['count'] +=1
    return render_template("index.html")


@app.route("/submit", methods=["POST"]) #ACTION ROUTE do not render on action routes
def submit():
    print(request.form)
    session['name'] = request.form['name']
    session['age'] = request.form['age']

    # if request.form['secret'] != "secret_value":
    #     return "HEY QUIT MISSING WITH MY HIDDEN VALUES"
    # session['secret'] = request.form['secret']

    return redirect('/display')

@app.route('/display') #DISPLAY
def display():
    name = session['name']
    return render_template('display.html', name=name,age=session['age'])

@app.route('/restart')
def restart():
    #session.clear() ##clears session entirely
    # popped_val = session.pop('count')
    del session['count']

    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)