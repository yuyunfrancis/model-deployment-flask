from flask import Flask
from app import app
from user.models import User

@app.route('/signup', methods=['POST'])
def signup():
    user = User()
    return user.signup()

@app.route('/login', methods=['POST'])
def login():
    user = User()
    return user.login()