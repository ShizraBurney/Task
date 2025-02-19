from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
     return " HELLO MY NAME IS SHIZRA"

if __name__ == '__main__':
    app.run()