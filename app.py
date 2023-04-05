import streamlit as st
import pickle

# Load the pickled model and vectorizer
with open('phishing_model.pkl', 'rb') as f:
    clf = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Define a function to predict whether a URL is phishing or not
def predict_phishing(url):
    # Vectorize the URL using the pickled vectorizer
    url_vectorized = vectorizer.transform([url])

    # Use the pickled model to make a prediction
    prediction = clf.predict(url_vectorized)[0]
    if prediction == 1:
        return "Phishing"
    else:
        return "Not phishing"

# Set up the Streamlit app
st.title("Phishing Website Detector")

url = st.text_input("Enter a URL to check")
if st.button("Check"):
    result = predict_phishing(url)
    st.write(result)
