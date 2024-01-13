from flask import Flask, url_for, redirect, render_template, request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/perform-login',methods=['POST'])
def perform_login():
    response = request.form.to_dict()
    return response

# TODO 1. Make a Registration page.
# TODO 2. Login and Registration page link

if __name__ == "__main__":
    app.run(port= 8080,
            debug= True)