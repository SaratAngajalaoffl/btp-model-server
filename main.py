from flask import Flask,jsonify,request

from services import get_bullying_prediction, handle_train
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/train-model', methods=['GET'])
def train_model():
	return jsonify({"status":handle_train()})


@app.route('/check-bullying', methods=['POST'])
def check_bullying():
	data = request.json
	return jsonify({"result":get_bullying_prediction(data["data"])})

if __name__ == '__main__':
    app.run(host='192.168.1.10', port=8080)