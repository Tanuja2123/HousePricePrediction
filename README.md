# 🏠 Bengaluru House Price Predictor

A web-based application built using Flask that predicts house prices in Bengaluru based on user input such as location, number of bedrooms (BHK), bathrooms, and total square footage. It uses a trained machine learning regression model and serves predictions in real-time.

## 🚀 Features

- 📍 Location selection using a dynamic dropdown
- 🛏️ Input fields for BHK, bathrooms, and total area
- 📈 Real-time house price prediction
- 🎨 Clean and responsive frontend using Bootstrap and Jinja2 templates
- 🔄 AJAX request for smoother user experience (without page reload)

## 🛠️ Tech Stack

- **Backend**: Flask (Python), Scikit-learn (ML Model)
- **Frontend**: HTML5, CSS3, Bootstrap 5, Jinja2
- **ML**: Pre-trained regression model with feature engineering and label encoding
- **Web**: AJAX (Vanilla JS and XMLHttpRequest)

## 📂 Project Structure

project/

│

├── app.py # Flask backend with routing and prediction logic

├── model/ # Folder containing the trained ML model (e.g., model.pkl)

├── templates/

│ └── index.html # Main HTML file with Bootstrap and dynamic Jinja2 rendering

├── static/ # Static files (CSS/JS) if used separately

└── requirements.txt # List of Python dependencies

🔍 Prediction Logic
Accepts POST request from the form via AJAX

Parses user inputs (location, BHK, bath, sqft)

Processes input and passes it to the loaded regression model

Returns the predicted price and displays it dynamically on the webpage
