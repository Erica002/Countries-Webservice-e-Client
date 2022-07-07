from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1

@app.route("/countries",methods=['GET'])
def get_countries():
    return jsonify(countries)

@app.route("/countries",methods=['POST'])
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415

@app.route("/countries/<int:id>", methods=['GET'])        
def get_country(id):
    for country in  countries:
        if country['id'] == id:
            return jsonify(country), 200
    return jsonify('error: id not founded'), 404

@app.route("/countries/<int:id>", methods=['PUT'])
def put(id):
    for country in  countries:
        if country['id'] == id:
            country["name"] = request.json["name"]
            country["capital"] = request.json["capital"]
            country["area"] = request.json["area"]
            return jsonify(country), 200
    return jsonify('error: id not founded'), 404

@app.route("/countries/<int:id>", methods=['DELETE'])
def delete(id):
    for country in  countries:
        if country['id'] == id:
            countries.remove(country)
            return jsonify({}), 200
    return jsonify('error: id not founded'), 404

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=8090)