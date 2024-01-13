from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route('/')
def login():
    return 'Hello World'




if __name__ == "__main__":
    app.run(port= 8080,
            debug= True)