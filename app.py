#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importing required libraries
from flask import Flask, request, render_template
import numpy as np
import pickle
import warnings
from feature_extraction import FeatureExtraction
from sklearn.feature_extraction.text import CountVectorizer

# Ignore warnings
warnings.filterwarnings('ignore')

# Load the trained models
try:
    with open("url_detection.pkl", "rb") as file:
        gbc = pickle.load(file)  # URL detection model
except FileNotFoundError:
    print("Error: Model file 'url_detection.pkl' not found. Ensure it's in the correct directory.")
    exit()

try:
    with open("email_detection.pkl", "rb") as file:
        model = pickle.load(file)  # Email spam detection model
except FileNotFoundError:
    print("Error: Model file 'email_detection.pkl' not found. Ensure it's in the correct directory.")
    exit()

# Load the trained vectorizer
try:
    with open("vectorizer.pkl", "rb") as file:
        vectorizer = pickle.load(file)
except FileNotFoundError:
    print("Error: vectorizer.pkl not found. Run the Jupyter Notebook to generate it.")
    exit()

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    """Handles requests to the home page and processes user input."""
    result = None
    message_type = None
    url_link = None  # Ensure it's defined

    if request.method == "POST":
        input_text = request.form.get("input_text")  # Get user input
        choice = request.form.get("choice")  # Detect whether it's a URL or Email

        try:
            if choice == "url":
                # URL feature extraction
                obj = FeatureExtraction(input_text)
                x = np.array(obj.getFeaturesList()).reshape(1, -1)

                # URL prediction
                y_pred = gbc.predict(x)[0]
                y_pro_phishing = gbc.predict_proba(x)[0, 0]
                y_pro_non_phishing = gbc.predict_proba(x)[0, 1]

                # Define message based on prediction
                if y_pred == 1:
                    result = f"✅ Safe Website (Confidence: {y_pro_non_phishing * 100:.2f}%)"
                else:
                    result = f"⚠️ Phishing Website Detected (Confidence: {y_pro_phishing * 100:.2f}%)"
                
                message_type = "url"
                url_link = input_text  # Pass the entered URL to the template

            elif choice == "email":
                # Transform email input using vectorizer
                email_vector = vectorizer.transform([input_text])
                
                # Email prediction
                prediction = model.predict(email_vector)[0]
                result = "✅ Ham (Safe Email)" if prediction == 0 else "⚠️ Spam Email Detected"
                
                message_type = "email"

        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template("index.html", result=result, message_type=message_type, url_link=url_link)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)


# In[ ]:




