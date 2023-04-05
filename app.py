import streamlit as st
import requests

# Define the Streamlit app
st.title('Phishing Detector')
st.write('Enter a URL to check if it is a phishing website or not.')

# Define the input field for the user to enter a URL
input_url = st.text_input('URL')

# Define the API endpoint to call
api_url = 'https://api.phishstats.info/v1/url/check'

# Perform phishing detection when the user clicks the button
if st.button('Check'):
    # Call the API to check if the URL is a phishing website or not
    response = requests.post(api_url, json={'url': input_url})
    data = response.json()
    
    # Display the phishing detection result to the user
    if data['in_database'] and data['verified']:
        st.write('The URL is a phishing website.')
    else:
        st.write('The URL is not a phishing website.')
