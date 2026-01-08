from flask import Flask, request, jsonify
import tensorflow as tf
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

print("Loading AI Model...")
# 1. Load the trained Deep Learning model
model = tf.keras.models.load_model('deep_mess_model.keras')

# 2. Load the Scaler (Crucial for Neural Networks!)
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
print("AI Loaded and Ready!")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # A. Get data sent from your Backend
        data = request.get_json()
        poll_count = data.get('poll_count')
        is_rainy = data.get('is_rainy')

        # B. Prepare input exactly how the model was trained
        # We use a DataFrame because the scaler expects column names
        input_df = pd.DataFrame([[poll_count, is_rainy]], columns=['Poll_Count', 'Is_Rainy'])
        
        # C. Scale the input
        scaled_input = scaler.transform(input_df)

        # D. Predict
        prediction = model.predict(scaled_input)
        
        # E. Send result back as JSON
        result = int(prediction[0][0])
        return jsonify({
            'status': 'success',
            'plates_needed': result,
            'message': f"Prediction: {result} plates."
        })

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    # Run on port 5000
    app.run(debug=True, port=5000)