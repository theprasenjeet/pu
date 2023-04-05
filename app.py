import pickle
import streamlit as st

# Load the model
with open('phishing_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Create the Streamlit app
st.write('# Phishing Website Prediction')

url = st.text_input('Enter a website URL')

if st.button('Predict'):
    # Make a prediction
    prediction = model.predict([url])[0]

    # Show the prediction
    if prediction == 'good':
        st.write('This website is safe')
    else:
        st.write('This website is a phishing website')
