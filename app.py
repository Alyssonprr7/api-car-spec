from flask import Flask, jsonify
import bson
import pprint
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId

client = MongoClient('mongodb+srv://car-match:car-match@cluster0-tnam3.mongodb.net/test?retryWrites=true&w=majority')
db = client.get_database("test")
collection = db.spec

app = Flask(__name__)


@app.route("/cars", methods=["GET"])
def get_all_cars():
    all_cars = collection.find()
    response = (dumps(all_cars))

    return response, 200


@app.route("/cars/<id>", methods=["GET"])
def get_car_by_id(id):
    try:
        car = collection.find_one({"id": id})
        response = dumps(car)
        return response, 200
    except bson.errors.InvalidId:
        return jsonify({"message": "Please, input an valid ID"}), 500


if __name__ == "__main__":
    app.run(debug=True)
