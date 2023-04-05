import streamlit as st
import requests

# Define the API endpoint URL and parameters
API_URL = "https://openphish.com/api/v1/"
API_ACTION = "search"
API_PARAMS = {"url": None}

st.title("Phishing Website Detector")

# Get the user input URL
url = st.text_input("Enter a website URL:")

# Check if the user has entered a URL
if url:
    # Update the API parameters with the user input URL
    API_PARAMS["url"] = url
    
    # Call the OpenPhish API and get the response
    response = requests.get(API_URL + API_ACTION, params=API_PARAMS)
    
    # Check if the API call was successful
    if response.ok:
        # Parse the JSON response and get the result
        result = response.json()["url"]
        
        # Check if the URL is a phishing website or not
        if result["in_database"]:
            st.error("The URL is a phishing website.")
        else:
            st.success("The URL is not a phishing website.")
    else:
        st.error("An error occurred while connecting to the OpenPhish API.")
