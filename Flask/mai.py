## put and delete
##woprking with api


from flask import flask, jsonify,request

app = Flask(__name__)

##initial data in my to do list

items = [

    {'id':1, "name" : "Item 1" , "description": "This is item 1"},
    {'id':1 ,"name" : "Item 1" , "description": "This is item 1"}
  
]   

@app.route('/')

def home():
    return "Welcome To the sample TODO List App"

#get : retrive  all the items

@app.route('/items', methods =['GET'])

def get_items():