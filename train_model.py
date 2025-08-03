import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
data = pd.read_csv('house_prices.csv')

# Encode categorical column
le_location = LabelEncoder()
data['Location'] = le_location.fit_transform(data['Location'])  # Urban=2, Suburban=1, Rural=0

# Features and target
X = data[['Bedrooms', 'Bathrooms', 'Size_sqft', 'Age', 'Garage', 'Location']]
y = data['Price']

# Train Ridge Regression model
model = Ridge(alpha=1.0)
model.fit(X, y)

# Save model and encoder
joblib.dump(model, 'model.pkl')
joblib.dump(le_location, 'location_encoder.pkl')

print("Ridge Regression model and encoder saved.")
