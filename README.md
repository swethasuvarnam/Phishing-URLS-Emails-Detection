
# Phishing URL & Email Detector
This project provides a robust solution for detecting malicious URLs and identifying spam emails. Leveraging machine learning models and comprehensive feature engineering, it offers a proactive defense against prevalent cyber threats. The application is built with a user-friendly web interface using Flask, making it accessible for real-time analysis.

## 🚀 Features
### Dual-Threat Detection: 
Identifies both phishing URLs and spam emails within a single application.
### Machine Learning Powered: 
Utilizes trained models (Gradient Boosting Classifier for URLs and Multinomial Naive Bayes for emails) for accurate threat assessment.
### Extensive URL Feature Extraction: 
Employs a sophisticated FeatureExtraction module to analyze various URL characteristics (e.g., IP address presence, URL length, use of symbols, redirection, domain registration length, HTTPS status, favicon, non-standard ports, and more) to determine legitimacy.
### Email Spam Classification: 
Processes email content using a CountVectorizer and a trained model to classify emails as "Ham" (safe) or "Spam".
### Intuitive Web Interface: 
A Flask-based web application provides a simple and interactive platform for users to input URLs or email content and receive instant predictions.
### Confidence Scores: 
For URL detections, the application provides a confidence score, indicating the probability of a website being safe or a phishing attempt.
### Clear Visual Feedback: 
Displays distinct messages and interactive buttons  based on the detection result, enhancing user experience and awareness.
## 💻 Technologies Used

* **Python:** Core programming language.
* **Flask:** Web framework for the application.
* **Scikit-learn:** For machine learning model training and prediction (Gradient Boosting Classifier, Multinomial Naive Bayes, CountVectorizer).
* **Numpy:** Numerical operations.
* **Pandas:** Data manipulation and analysis (used in Jupyter notebooks for dataset handling).
* **Requests:** HTTP library for making web requests.
* **Whois:** For domain information retrieval in URL feature extraction.
* **Matplotlib & Seaborn:** For data visualization (used in Jupyter notebooks).
* **HTML/CSS:** For the front-end web interface.
## ⚙️ How It Works

### URL Phishing Detection

The URL detection module analyzes various features extracted from a given URL to classify it as legitimate or phishing. The `FeatureExtraction` class meticulously extracts over 20 features, including:

* Presence of IP address in the URL
* Length of the URL
* Usage of URL shortening services
* Presence of `@` symbol in the URL
* Redirection count
* Prefix/Suffix in the domain
* Number of subdomains
* HTTPS usage and certificate validity
* Domain registration length
* Favicon characteristics
* Non-standard port usage
* Request URL, Anchor URL, and Links in Script Tags analysis
* Server Form Handler and Information Email presence
* Abnormal URL characteristics
* Website forwarding behavior
* Status bar customization and disabling right-click
* Pop-up window usage and iframe redirection
* Age of domain and DNS recording
* Website traffic, PageRank, and Google Index status
* Links pointing to the page and statistical reports

These features are fed into a pre-trained Gradient Boosting Classifier model (`url_detection.pkl`), which outputs a prediction and confidence score. The `url_phishing.ipynb` notebook details the training and evaluation process for this model using the `phishing.csv` dataset.

### Email Spam Detection

The email spam detection component processes the text content of an email. It uses a `CountVectorizer` (`vectorizer.pkl`) to transform the text into numerical features, which are then input into a pre-trained Multinomial Naive Bayes model (`email_detection.pkl`). This model classifies the email as either "Ham" (safe) or "Spam." The `email_phishing.ipynb` notebook outlines the data preprocessing, model training (including handling class imbalance with SMOTE), and evaluation for this spam detection model using the `emails.csv` dataset.

## 🛠️ Setup and Installation

To set up and run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/swethasuvarnam/Phishing-URLS-Emails-Detection.git](https://github.com/swethasuvarnam/Phishing-URLS-Emails-Detection.git)
    cd Phishing-URLS-Emails-Detection
    ```

2.  **Create a virtual environment (recommended):**
    This isolates your project's dependencies from your system-wide Python packages.
    ```bash
    python -m venv venv
    ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
    * **On Windows:**
        ```bash
        venv\Scripts\activate
        ```

3.  **Install the required libraries:**
    The project dependencies are listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ensure models and vectorizer are available:**
    * The `app.py` script requires pre-trained machine learning models (`url_detection.pkl`, `email_detection.pkl`) and the `CountVectorizer` object (`vectorizer.pkl`) to  function.
    * These `.pkl` files are generated when you run the Jupyter notebooks (`url_phishing.ipynb` and `email_phishing.ipynb`).
    * **Run these notebooks fully** in your local environment to train the models and save these necessary `.pkl` files into your project directory.

6.  **Run the Flask application:**
    ```bash
    python app.py
    ```
    The application will typically start on https://ai-based-phishing-detector.onrender.com/. Open this URL in your web browser to access the Phishing URL & Spam Email Detector.


## 📂 Project Structure
* `app.py`: The main Flask application file that handles web requests and integrates the detection models.
* `feature_extraction.py`: Contains the `FeatureExtraction` class with methods to extract various features from URLs.
* `email_phishing.ipynb`: Jupyter notebook for training and evaluating the email spam detection model.
* `url_phishing.ipynb`: Jupyter notebook for training and evaluating the URL phishing detection model.
* `emails.csv`: Dataset used for training the email spam detection model.
* `phishing.csv`: Dataset used for training the URL phishing detection model.
* `requirements.txt`: Lists all necessary Python dependencies.
* `templates/index.html`: HTML template for the web interface.
* `static/style.css`: CSS file for styling the web interface.
 `*.pkl`: Pickled machine learning models and vectorizer (generated after running notebooks).

## 📈 Model Performance 

### Email Spam Detection

* **Accuracy:** Achieved high accuracy (e.g., 98.7% on training, 97.4% on testing for a Multinomial Naive Bayes model after SMOTE).
* **Classification Report:**
    * **Precision (Spam):** 95%
    * **Recall (Spam):** 96%
    * **F1-Score (Spam):** 95%
    * **Precision (Ham):** 98%
    * **Recall (Ham):** 98%
    * **F1-Score (Ham):** 98%

### URL Phishing Detection

* **Accuracy:** Models like Gradient Boosting Classifier showed high performance (e.g., 97% accuracy).
* **Confusion Matrix:** Provides detailed insight into true positives, true negatives, false positives, and false negatives.
