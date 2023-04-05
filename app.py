import streamlit as st
import pickle
import pandas as pd
import re

# Load the pre-trained model from phishing.pkl
with open('phishing.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the Streamlit app
st.title('Phishing Detector')
st.write('Enter a URL to check if it is a phishing website or not.')

# Define the input field for the user to enter a URL
input_url = st.text_input('URL')

# Define a function to preprocess the input URL
def preprocess_url(url):
    # Remove any unnecessary parts of the URL
    url = re.sub(r'https?://', '', url)
    url = re.sub(r'www\.', '', url)
    url = re.sub(r'\/.*', '', url)
    
    # Tokenize the URL
    tokens = re.findall(r'\w+', url)
    
    # Stem the tokens
    stemmed_tokens = [token.lower() for token in tokens]
    
    # Convert the tokens to a string
    token_str = ' '.join(stemmed_tokens)
    
    # Convert the tokens to a pandas DataFrame
    data = {'text_tokenized': [tokens], 'text_stemmed': [stemmed_tokens], 'text_sent': [[]]}
    df = pd.DataFrame(data)
    
    return df

# Perform phishing detection when the user clicks the button
if st.button('Check'):
    # Preprocess the input URL
    input_df = preprocess_url(input_url)
    
    # Use the pre-trained model to predict if the URL is a phishing website or not
    result = model.predict(input_df)[0]
    
    # Display the phishing detection result to the user
    if result == 1:
        st.write('The URL is a phishing website.')
    else:
        st.write('The URL is not a phishing website.')
