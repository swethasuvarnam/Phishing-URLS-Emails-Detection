# Phishing-URLS-Emails-Detection
Phishing URL & Spam Email Detector
This project provides a robust solution for detecting malicious URLs and identifying spam emails. Leveraging machine learning models and comprehensive feature engineering, it offers a proactive defense against prevalent cyber threats. The application is built with a user-friendly web interface using Flask, making it accessible for real-time analysis.

#🚀 Features
Dual-Threat Detection: Identifies both phishing URLs and spam emails within a single application.
Machine Learning Powered: Utilizes trained models (Gradient Boosting Classifier for URLs and Multinomial Naive Bayes for emails) for accurate threat assessment.
Extensive URL Feature Extraction: Employs a sophisticated FeatureExtraction module to analyze various URL characteristics (e.g., IP address presence, URL length, use of symbols, redirection, domain registration length, HTTPS status, favicon, non-standard ports, and more) to determine legitimacy.
Email Spam Classification: Processes email content using a CountVectorizer and a trained model to classify emails as "Ham" (safe) or "Spam".
Intuitive Web Interface: A Flask-based web application provides a simple and interactive platform for users to input URLs or email content and receive instant predictions.
Confidence Scores: For URL detections, the application provides a confidence score, indicating the probability of a website being safe or a phishing attempt.
Clear Visual Feedback: Displays distinct messages and interactive buttons (e.g., "Visit Safe Website," "Still want to Continue?") based on the detection result, enhancing user experience and awareness.
