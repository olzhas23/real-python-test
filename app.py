
from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/hello")

def helloworld():
    return ("Hello world")
if __name__=="__main__":
    app.run()

