from flask import Flask, jsonify, render_template, request
import json

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('ui/index.html')

@application.route('/register')
def renderForm():
    return render_template('ui/auth/registerForm.html')

@application.route('/registration', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return render_template('ui/auth/registration.html', password=request.form['password'])
    elif request.method == 'GET':
        return('A unsupported GET request was made')
    else:
        return('Not a valid request method for this route')
    
if '__name__' == '__main__':
    application.run()