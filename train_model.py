import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Sample dataset (replace later with real data)
data = pd.DataFrame({
    'temperature': [25, 30, 20, 35, 28],
    'rainfall': [200, 150, 300, 100, 180],
    'humidity': [80, 60, 90, 50, 70],
    'soil_type': [1, 2, 1, 3, 2],
    'nitrogen': [40, 60, 30, 70, 50],
    'phosphorus': [20, 30, 25, 35, 28],
    'potassium': [30, 40, 35, 45, 38],
    'crop': ['Rice', 'Wheat', 'Rice', 'Maize', 'Wheat']
})

X = data.drop('crop', axis=1)
y = data['crop']

model = RandomForestClassifier()
model.fit(X, y)

# Save model
pickle.dump(model, open('model.pkl', 'wb'))

print("✅ Model trained and saved as model.pkl")