from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello !</h1>"

@app.route('/greet')
def greet():
    return "Hello Nisha"

if __name__ == "__main__":
    app.run(debug=True)