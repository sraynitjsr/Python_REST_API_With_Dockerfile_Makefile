from flask import Flask

app = Flask(__name__)

@app.route('/helloWorld', methods=['GET'])
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run('0.0.0.0',port=8080)
