from flask import Flask, render_template  # Import Flask to allow us to create our app


app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/success')
def success():
    return "success <h1>this is a h1</h1><script>alert('hello!')</script>"

@app.route('/hello/<name>/<int:times>')
def hello(name,times):
    return render_template("jinja.html", name=name, times=times)

@app.route('/template')
def template():
    student_info = [
       {'name' : 'Michael', 'age' : 35},
       {'name' : 'John', 'age' : 30 },
       {'name' : 'Mark', 'age' : 25},
       {'name' : 'KB', 'age' : 27}
    ]
    dict = {'test':9}
    return render_template("index.html",student_info=student_info, dict=dict)



@app.errorhandler(404)
def error_page(e):
    return "my custom error page"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.