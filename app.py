from flask import Flask, render_template, request
from flask import redirect, url_for
from data import save_registration_details, verify_user


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
    email = response['email_id']
    password = response['password']
    
    # verify the user details
    result = verify_user(email= email,
                         password= password)
    
    if result:
        return redirect(url_for('welcome'))
    else:
        return render_template('login.html',error= 'Check Email/Password')
    
    
    
@app.route('/perform-registration',methods=['POST'])
def perform_registration():
    response = request.form.to_dict()
    email = response['email_id']
    username = response['username']
    password = response['password']
    # create the update dictionary 
    # * in format {email:{'user_name': username, 'password': password}
    update_dict = {email: {'username': username,
                           'password': password}}

    # use the dictionary to update the json file
    result = save_registration_details(details= update_dict)

    if result:
        message = 'Registration Successful'
        return render_template('login.html',message= message)
    else:
        message = "Already Registered, Proceed to Login"
        return render_template('register.html',message= message)
    
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/ner')
def ner():
    return render_template('ner.html')    

@app.route('/sentiment')
def sentiment():
    return render_template('sentiment.html')

@app.route('/abuse')
def abuse():
    return render_template('abuse.html')



if __name__ == "__main__":
    app.run(port= 8080,
            debug= True)