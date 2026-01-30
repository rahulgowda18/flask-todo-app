from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
import uuid
import hashlib
import json

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client.todo_db
collection = db.items

# Home page
@app.route("/")
def home():
    return render_template("todo.html")

# API route (JSON file)
@app.route("/api", methods=["GET"])
def api():
    with open("data.json", "r") as file:
        data = json.load(file)
    return jsonify(data)

# Submit ToDo item
@app.route("/submittodoitem", methods=["POST"])
def submit_todo():
    item_id = request.form.get("itemId")
    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")

    item_uuid = str(uuid.uuid4())
    item_hash = hashlib.sha256(item_name.encode()).hexdigest()

    todo_item = {
        "itemId": item_id,
        "itemName": item_name,
        "itemDescription": item_description,
        "itemUUID": item_uuid,
        "itemHash": item_hash
    }

    collection.insert_one(todo_item)

    return jsonify({
        "message": "ToDo item stored successfully",
        "data": todo_item
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
