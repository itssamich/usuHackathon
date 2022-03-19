from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/<list_name>/<dimentions>")
def json_response(list_name, dimentions):
    response = jsonify(
        list_name="Test",
        dimensions=2,
        number_of_points= 10,
        points= [[0,1], [1,2], [8, 3.8], [6.2, 6.1], [0.1, 0], [0.2, 0], [0.3, 0], [-4, -2.895784], [-4, 4], [3.98, -6.75]],
        labels= ["[0,1]", "[1,2]", "[8, 3.8]", "[6.2, 6.1]", "[0.1, 0]", "[0.2, 0]", "[0.3, 0]", "[-4, -2.895784]", "[-4, 4]", "[3.98, -6.75]"]
        )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    