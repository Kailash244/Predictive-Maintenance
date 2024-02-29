# app.py
from flask import Flask, request, jsonify
from model import train_model, predict_failure

app = Flask(__name__)

# Dummy training data
X_train = [[80], [85], [75], [90], [95]]
y_train = [0, 1, 0, 1, 1]

# Train the model
model = train_model(X_train, y_train)

@app.route('/predict', methods=['POST'])
def predict():
    # Get sensor data from the request
    sensor_data = request.json.get('sensor_data')
    # Convert sensor data to numpy array
    sensor_data_np = np.array(sensor_data).reshape(1, -1)
    # Predict failure
    predictions = predict_failure(model, sensor_data_np)
    # Respond with the prediction
    return jsonify({'prediction': int(predictions[0])})

if __name__ == '__main__':
    app.run(debug=True)
