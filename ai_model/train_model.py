import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
data = pd.read_csv('ai_model/storage_data.csv')
X = data[['current_usage', 'days_active']]
y = data['predicted_growth']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open('ai_model/model.pkl', 'wb') as f:
    pickle.dump(model, f)