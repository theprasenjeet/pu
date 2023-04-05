import streamlit as st
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer

# Load the trained model from disk
with open('phishing_model.pkl', 'rb') as f:
    clf = pickle.load(f)

# Load the vectorizer from disk
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Define a function to make predictions
def predict(url):
    # Vectorize the URL using the pre-trained vectorizer
    url_vectorized = vectorizer.transform([url])
    
    # Make the prediction using the pre-trained classifier
    prediction = clf.predict(url_vectorized)[0]
    
    # Map the predicted label back to "good" or "bad"
    if prediction == 0:
        return "good"
    else:
        return "bad"

# Create the Streamlit app
st.title("Phishing Website Detector")

# Get input from the user
url = st.text_input("Enter a website URL to check")

# Make a prediction and display the result
if url:
    prediction = predict(url)
    st.write(f"The website {url} is {prediction}.")
