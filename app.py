from flask import Flask, url_for, redirect, render_template, request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform-login',methods=['POST'])
def perform_login():
    response = request.form.to_dict()
    return response

@app.route('/perform-registration',methods=['POST'])
def perform_registration():
    response = request.form.to_dict()
    return response

if __name__ == "__main__":
    app.run(port= 8080,
            debug= True)