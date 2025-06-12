import pickle
import json
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the model and columns
with open("price_prediction.pickle", "rb") as f:
    model = pickle.load(f)

with open("columns.json", "r") as f:
    columns = json.load(f)["data_columns"]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        location = data['location'].lower()
        total_sqft = float(data['total_sqft'])
        bath = float(data['bath'])
        bhk = int(data['bhk'])

        # Create input array
        x = np.zeros(len(columns))
        x[0] = total_sqft
        x[1] = bath
        x[2] = bhk

        # Set location index
        if location in columns:
            loc_index = columns.index(location)
            x[loc_index] = 1
        else:
            return jsonify({'error': 'Location not found in model columns'}), 400

        # Predict price
        prediction = model.predict([x])[0]
        return jsonify({'prediction': round(prediction, 2)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/locations', methods=['GET'])
def get_locations():
    return jsonify({'locations': columns[3:]})  # Skip total_sqft, bath, bhk

if __name__ == '__main__':
    app.run(debug=True, port=5000)