import streamlit as st
import pickle
import pandas as pd

# Load the pre-trained model from phishing.pkl
with open('phishing.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the Streamlit app
st.title('Phishing Detector')
st.write('Enter a URL to check if it is a phishing website or not.')

# Define the input field for the user to enter a URL
input_url = st.text_input('URL')

# Perform phishing detection when the user clicks the button
if st.button('Check'):
    # Preprocess the input URL
    text_tokenized = input_url.split()
    text_stemmed = [word.lower() for word in text_tokenized]
    text_sent = [' '.join(text_stemmed)]
    input_df = pd.DataFrame({'URL': [input_url], 'Label': ['unknown'], 'text_tokenized': [text_tokenized], 'text_stemmed': [text_stemmed], 'text_sent': text_sent})
    
    # Use the pre-trained model to predict if the URL is a phishing website or not
    prediction = model.predict(input_df)[0]
    
    # Map the prediction to a label
    label = 'good' if prediction == 0 else 'bad'
    
    # Display the phishing detection result to the user
    if prediction == 1:
        st.write('The URL is a phishing website.')
    else:
        st.write('The URL is not a phishing website.')
