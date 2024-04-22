from flask import Flask
from flask_cors import CORS
import pymongo

app = Flask(__name__)
CORS(app) 

# Database
client = pymongo.MongoClient("mongodb+srv://fyuyun:vAkhv6wZBt9ghosN@aihealth.cmpfj6l.mongodb.net/?retryWrites=true&w=majority&appName=aihealth")
db = client.get_database('aihealth')

# Routes
from user import routes

@app.route('/')
def home():
    return {"Items" : ["item1", "item2", "item3", "item4", "item5"]}

if __name__ == '__main__':
    app.run(debug=True)