from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

allData = {}

@app.route('/post_message/<uuid>', methods=['POST'])
def post_message(uuid):
    print("post_message")
    print(uuid)
    allData[uuid] = request.json
    return jsonify({"success":True})


@app.route('/post_message/<uuid>/<uuid2>', methods=['POST'])
def post_message_in_set(uuid,uuid2):
    print("post_message2")
    print(uuid,uuid2)
    if(uuid not in allData):
        allData[uuid] = {}
    allData[uuid][uuid2] = request.json
    return jsonify({"success":True})

@app.route('/append_message/<uuid>', methods=['POST'])
def append_message(uuid):
    print("append_message")
    print(uuid)
    if(uuid not in allData):
        allData[uuid] = []    
    allData[uuid].append(request.json)
    return jsonify({"success":True})

@app.route('/clear_message/<uuid>', methods=['POST'])
def clear_message(uuid):
    print("clear_message")
    print(uuid)
    if(uuid in allData):
        del allData[uuid]
    return jsonify({"success":True})

@app.route('/get_message/<uuid>', methods=['GET'])
def get_message(uuid):
    print("get_message")
    print(uuid)
    if(uuid in allData):
        return jsonify(allData[uuid])
    else:
        return jsonify({})

if __name__ == '__main__':
    app.run(host="localhost", port=3005, debug=True)