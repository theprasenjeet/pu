import pickle
import streamlit as st
import numpy as np

# Load the model
with open('phishing_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the Streamlit app
def app():
    st.set_page_config(page_title="Phishing Website Detector", page_icon=":guardsman:", layout="centered")

    st.title("Phishing Website Detector")

    url = st.text_input("Enter the website URL:")

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
