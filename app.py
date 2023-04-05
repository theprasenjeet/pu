import streamlit as st
import requests
import os

# Get the FraudGuard API username and password from environment variables
API_USERNAME = os.environ.get("6hklAl7a1g4TLdCE")
API_PASSWORD = os.environ.get("X8C9Ifk1DWTdh1oX")

# Define the API endpoint URL and parameters
API_URL = "https://api.fraudguard.io/v1/scan"
API_PARAMS = {"url": None}

st.title("Phishing Website Detector")

# Get the user input URL
url = st.text_input("Enter a website URL:")

# Check if the user has entered a URL
if url:
    # Update the API parameters with the user input URL
    API_PARAMS["url"] = url
    
    # Call the FraudGuard API and get the response
    response = requests.post(API_URL, data=API_PARAMS, auth=(API_USERNAME, API_PASSWORD))
    
    # Check if the API call was successful
    if response.ok:
        # Parse the JSON response and get the result
        result = response.json()
        
        # Check if the URL is a phishing website or not
        if result["status"] == "malicious":
            st.error("The URL is a phishing website.")
        else:
            st.success("The URL is not a phishing website.")
    else:
        st.error("An error occurred while connecting to the FraudGuard API.")
