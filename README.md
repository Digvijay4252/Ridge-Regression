<!-- # Ridge-Regression

<img width="1907" height="915" alt="image" src="https://github.com/user-attachments/assets/638883c5-ea3f-401c-a37a-a5818ee9ae06" /> -->

## Ridge Regression – Final Grade Predictor

This project applies Ridge Regression, a regularized linear regression technique, to predict a student’s final grade (G3) based on academic and behavioral attributes. The solution includes a clean Flask web app where users input student data and receive an instant grade prediction.

---

## Project Structure

```
Ridge-Regression/
├── app.py                   # Flask backend
├── train_model.py           # Model training script using Ridge Regression
├── model.pkl                # Trained Ridge model
├── encoders.pkl             # Encoded values for categorical inputs
├── student_data.csv         # Training dataset
│
├── templates/
│   └── index.html           # Input form UI
└── static/
    └── style.css            # Optional CSS file

```

---

## Model Info

- Algorithm: Ridge() from sklearn.linear_model

- Loss Function: MSE + α \* (squared weights)

- Regularization strength: Tuned via alpha parameter

---

## Setup Instructions

1. **Clone the repository**

```
git clone https://github.com/Digvijay4252/Ridge-Regression.git
cd Ridge-Regression
```

Install dependencies

```
pip install -r requirements.txt
```

Run the application

```
python app.py
```

Open in browser

Visit: http://localhost:10000

# Sample Input
```
Sex: Male
Age: 17
StudyTime: 3
G1: 15, G2: 14
→ Prediction: 16.3
```
## Screenshots

### Step 1
<img width="1898" height="903" alt="image" src="https://github.com/user-attachments/assets/8c5e93ed-f5f6-44e4-a90d-852de9c7391e" />

### Step 2
<img width="1897" height="900" alt="image" src="https://github.com/user-attachments/assets/9c011dd1-d0aa-403f-a0a0-6e486a25fec4" />

### Step 4
<img width="1895" height="898" alt="image" src="https://github.com/user-attachments/assets/719f3af5-a2e7-4d11-8a1f-5c97c2cc67d0" />


## Future Improvements

Feature importance visualizations

Add prediction confidence/interval

Support batch predictions (CSV upload)

Deploy to Render/Heroku
