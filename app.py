import pickle
from flask import Flask, request, jsonify

api = Flask(__name__)

# Load the model
try:
    with open('ai.pkl', 'rb') as f:
        ai = pickle.load(f)
except Exception as e:
    raise RuntimeError(f"Failed to load model: {e}")

@api.route('/')
def home():
    return "API Server Running"

@api.route('/predict', methods=['GET'])
def predict():
    try:
        T = float(request.args.get('T', ''))
        P = float(request.args.get('P', ''))
        ECG = float(request.args.get('ECG', ''))
    except ValueError:
        return jsonify({"error": "Invalid input parameters. Ensure T, P, and ECG are numeric."}), 400

    try:
        data = [[T, P, ECG]]
        prediction = ai.predict(data)[0]
        return jsonify({"prediction": str(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    api.run(host='0.0.0.0', port=2000)
