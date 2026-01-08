import pandas as pd
import numpy as np
import pickle
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import StandardScaler

# --- PART 1: Generating Data (Same as before) ---
print("Generating synthetic data....")
data = []
for i in range(500): # Increased to 500 rows so the Neural Net learns better
    poll_count = np.random.randint(300, 600)
    is_rainy = 1 if np.random.rand() < 0.2 else 0
    actual_eaten = poll_count
    if is_rainy == 1:
        actual_eaten += (poll_count * 0.1)
    actual_eaten += np.random.randint(-5, 5)
    data.append([poll_count, is_rainy, int(actual_eaten)])

df = pd.DataFrame(data, columns=['Poll_Count', 'Is_Rainy', 'Actual_Eaten'])

# --- PART 2: Preprocessing (CRITICAL for Neural Networks) ---
# Neural Networks fail if inputs are vastly different sizes (e.g., 600 vs 1).
# We must "Scale" the data to be between -1 and 1.

X = df[['Poll_Count', 'Is_Rainy']]
y = df['Actual_Eaten']

# Create a scaler for Inputs (X)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# --- PART 3: Building the "Brain" (The Neural Network) ---
print("\nBuilding the Neural Network....")

model = Sequential()

# Layer 1: Input Layer + 64 Neurons (The "Thinking" layer)
# 'relu' is the activation function that allows it to learn complex patterns
model.add(Dense(64, input_dim=2, activation='relu'))

# Layer 2: Hidden Layer (32 Neurons) - Deepening the learning
model.add(Dense(32, activation='relu'))

# Layer 3: Output Layer (1 Neuron) - The final number prediction
model.add(Dense(1, activation='linear')) 

# Compile: Tell the AI how to learn (Optimizer='adam' is standard)
model.compile(loss='mean_squared_error', optimizer='adam')

# --- PART 4: Training ---
print("Training the Deep Learning Model (this may take a moment)...")
# Epochs = How many times the AI reviews the data. 
# Batch_size = How many rows it studies at once.
history = model.fit(X_scaled, y, epochs=100, batch_size=10, verbose=0)

print("✅ Model Trained Successfully!!!")
print(f"Final Error Rate (Loss): {history.history['loss'][-1]:.2f}")

# --- PART 5: Saving ---
# We must save BOTH the Model AND the Scaler
model.save('deep_mess_model.keras') # Keras format
with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

print("✅ Saved model to 'deep_mess_model.keras' and scaler to 'scaler.pkl'")

# --- PART 6: TEST PREDICTION ---
print("\n--- TEST PREDICTION ---")
test_poll = 500
test_rain = 1 

# 1. Prepare input
raw_input = pd.DataFrame([[test_poll, test_rain]], columns=['Poll_Count', 'Is_Rainy'])

# 2. SCALE the input (The AI only understands scaled numbers now!)
scaled_input = scaler.transform(raw_input)

# 3. Predict
prediction = model.predict(scaled_input)

print(f"Input: Poll={test_poll}, Rain={test_rain}")
print(f"Neural Network Prediction: {int(prediction[0][0])} plates needed")