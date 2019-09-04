from flask import Flask

app = Flask(__name__)


@app.route('/')
def func():
    # returning hello text
    return "hello"


# calling main method to run
app.run()
