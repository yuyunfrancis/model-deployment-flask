from flask import Flask, jsonify, request
import uuid
from passlib.hash import pbkdf2_sha256
from app import db

class User:
    
    def signup(self):
        
        data = request.get_json() 

        user = {
            "_id": uuid.uuid4().hex,
            "name": data.get('name'),
            "email": data.get('email'),
            "password": data.get('password'),
        }
        
        # encrypt password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])
        
        db.users.insert_one(user)
        
        return jsonify(user), 200
    
    def login(self):
        
        data = request.get_json()
        
        user = db.users.find_one({"email": data.get('email')})
        
        if user and pbkdf2_sha256.verify(data.get('password'), user['password']):
            return jsonify(user), 200
        else:
            return jsonify({"error": "Invalid email or password"}), 401
        
    
        
        