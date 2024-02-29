import requests

# Define sensor data
sensor_data = {'sensor_data': [80]}

# Send POST request to Flask application
response = requests.post('http://localhost:5000/predict', json=sensor_data)

# Print the prediction received from the Flask application
print(response.json())
