import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

# Load the dataset
data = pd.read_csv("your_file_path.csv")  # Replace with the correct file path
data = data[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

# Use 'Close' as the label to predict
label = data.pop('Close')

# Convert to numpy arrays
features_np = data.values
label_np = label.values

# Reshape features for the model
features_np = np.reshape(features_np, (features_np.shape[0], features_np.shape[1], 1))

# Create the sequential model
model = models.Sequential([
    layers.LSTM(64, activation='relu', input_shape=(features_np.shape[1], 1)),
    layers.Dense(1)
])

# Compile the model
model.compile(optimizer=tf.keras.optimizers.Adam(),
              loss='mean_squared_error')

# Fit the model
history = model.fit(features_np, label_np, epochs=10, verbose=0)

# Print model summary
print("Model Summary:")
model.summary()

# Print history
print("History:")
print(history.history)
