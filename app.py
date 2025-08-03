from flask import Flask, render_template, request
import joblib
import os


app = Flask(__name__)

# Load model and encoder
model = joblib.load('model.pkl')
location_encoder = joblib.load('location_encoder.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            bedrooms = int(request.form['bedrooms'])
            bathrooms = int(request.form['bathrooms'])
            size = float(request.form['size_sqft'])
            age = int(request.form['age'])
            garage = int(request.form['garage'])
            location = request.form['location']

            location_encoded = location_encoder.transform([location])[0]

            features = [[bedrooms, bathrooms, size, age, garage, location_encoded]]
            price = model.predict(features)[0]
            prediction = f"${price:,.2f}"

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
