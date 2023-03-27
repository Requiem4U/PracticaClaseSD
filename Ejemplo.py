from flask import Flask
from flask import request
from flask import jsonify
import json, os

app=Flask(__name__)

allUser = []

if(os.path.exists("data.json")):
    with open("data.json") as file:
        allUser = json.load(file)
else:
    allUser= [{"id":0, "nombre" : "damian"},{"id":1, "nombre" : "pepe"}]

@app.route('/app/v1/users/<id>', methods=["GET"])
def users_action(id):
    return jsonify(allUser[int(id)])

@app.route('/app/v1/users', methods=["POST", "GET"])
def users_action2():
    if(request.method == "GET"):
        return jsonify(allUser)
    else:
        user = {
            "id": request.args.get("id"), 
            "nombre": request.args.get("nombre")
        }
        allUser.append(user)
        with open('data.json', 'w') as file:
            json.dump(allUser,file, indent=4)
        return jsonify(allUser)

app.run(debug=True, port="5000")