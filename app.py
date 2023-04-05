import pickle
import streamlit as st
import numpy as np
# Load the model
with open('phishing_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Create the Streamlit app
st.write('# Phishing Website Prediction')

url = st.text_input('Enter a website URL')

if st.button("Predict"):
        # Reshape the input data to have shape (1, )
        input_data = np.array([url]).reshape(1, )

        # Make the prediction
        prediction = model.predict(input_data)[0]

        # Show the prediction
        if prediction == 'good':
            st.success("This website is safe!")
        else:
            st.warning("This website is a phishing website!")
