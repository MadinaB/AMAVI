from flask import Flask, render_template, request, redirect, jsonify, url_for, flash

app = Flask(__name__)

# Show main page: show all 
@app.route('/')
def main():
    return showAll('family')

# Show all families sorted by some option
@app.route('/option/<option>')
def showAll(option):
    return 'these are all families sorted by '+ option

# Show one family
@app.route('/family/<family>')
def showOne(family):
    return 'this is '+ family


# Login
@app.route('/veni/login')
def login():
    return 'login or signup redirect is here'

# Signup
@app.route('/veni/signup')
def signup():
    return 'Signup'

# My page
@app.route('/veni')
def my():
    return 'This is my page. I can edit all the stuff here.'

# List all users present
@app.route('/vidi')
def listFamilies():
    return 'These is list of all families sorted alphabetically'



if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)



