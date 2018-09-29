from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from database_setup import Family, Base

app = Flask(__name__)

APPLICATION_NAME = "AMAVI"

# Database session setup
engine = create_engine('sqlite:///amavi.db')
Base.metadata.bind = engine
DBSession = scoped_session(sessionmaker(bind=engine))
session = DBSession()

# Show main page: show all 
@app.route('/')
def main():
    return showAll('family')

# Show all families sorted by some option
@app.route('/option/<the_option>')
def showAll(the_option):
    #return 'these are all families sorted by '+ the_option
    families = session.query(Family)
    return render_template('main_page.html', families=families, option=the_option)


# Show one family
@app.route('/family/<family>')
def showOne(family):
    #return 'this is '+ family
    return render_template('showOne.html')



# Login
@app.route('/login')
def login():
    #return 'login or signup redirect is here'
    return render_template('login.html')

# Signup
@app.route('/signup')
def signup():
    #return 'Signup'
    return render_template('signup.html')

# My page
@app.route('/veni')
@app.route('/my')
def my():
    #return 'This is my page. I can edit all the stuff here.'
    return render_template('my.html')

# List all users present
@app.route('/vidi')
def listFamilies():
    #return 'These is list of all families sorted alphabetically'
    return render_template('vidi.html')



if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)



