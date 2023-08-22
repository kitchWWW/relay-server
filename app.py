from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

allData = {}

@app.route('/post_message/<uuid>', methods=['POST'])
def post_message(uuid):
    print(uuid)
    allData[uuid] = request.json
    return jsonify({"success":True})

@app.route('/append_message/<uuid>', methods=['POST'])
def append_message(uuid):
    print(uuid)
    if(uuid not in allData):
        allData[uuid] = []    
    allData[uuid].append(request.json)
    return jsonify({"success":True})

@app.route('/get_message/<uuid>', methods=['GET'])
def get_message(uuid):
    print(uuid)
    if(uuid in allData):
        return jsonify(allData[uuid])
    else:
        return jsonify({})

if __name__ == '__main__':
    app.run(host="localhost", port=3005, debug=True)