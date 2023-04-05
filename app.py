import streamlit as st
import requests
import re

# Define the Streamlit app
st.title('Phishing Detector')
st.write('Enter a URL to check if it is a phishing website or not.')

# Define the input field for the user to enter a URL
input_url = st.text_input('URL')

# Define a function to check if a URL is a phishing website
def is_phishing(url):
    response = requests.get(url)
    if response.status_code != 200:
        return False

    html_content = response.content.decode('utf-8')
    if 'content="text/html' not in html_content:
        return False

    # check if the url contains an IP address
    if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url):
        return True

    # check for common phishing keywords in the url
    keywords = ['login', 'signin', 'bank', 'paypal', 'ebay', 'amazon']
    for keyword in keywords:
        if keyword in url:
            return True

    # check for redirection to a different domain
    if response.history:
        last_url = response.history[-1].url
        if last_url != url:
            return True

    return False

# Perform phishing detection when the user clicks the button
if st.button('Check'):
    # Check if the input URL is a phishing website
    result = is_phishing(input_url)
    
    # Display the phishing detection result to the user
    if result:
        st.write('The URL is a phishing website.')
    else:
        st.write('The URL is not a phishing website.')
