from flask import Flask

app = Flask(__name__)



def bold(func):
    def inner():
        return




@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



if __name__ == "__main__":
    
    app.run()