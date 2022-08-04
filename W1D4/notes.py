"""
ternary
_________ ? _____ : _____
 conditon   true    false
^ this is for js, not python

pip install pipenv (windows)
pip3 install pipenv (osx)
run this command ONCE EVER to globally install pipenv
pipenv is the software that lets us manage virtual envs

pipenv install flask 
python -m pipenv install flask
python3 -m pipenv install flask
run this command to set up virtual env / install flask to it

pipenv shell
enter the virtual environment

python server.py
python3 server.py
launches server once in environment


path variables
a way for us to get information from the client via the url requested

@app.route("/path/path/<variable>/<int:num_var>")

rendering templates:
import render_template from flask
must have "templates" folder same level as server
return render_template('template.html')
"""

"""
Afternoon notes:



"""