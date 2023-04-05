import streamlit as st
import pickle

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


# Load the pickled model and vectorizer
with open('phishing_model.pkl', 'rb') as f:
    clf = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Define a function to predict whether a URL is phishing or not
def predict_phishing(url):
    # Remove "http://" or "https://" if present
    if url.startswith("http://"):
        url = url[7:]
    elif url.startswith("https://"):
        url = url[8:]

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

        
# =========================================================================================
#                                           Footer
# =========================================================================================
st.markdown("---")
st.write("Follow me on social media:")
st.write("[Twitter](https://twitter.com/theprasenjeet)")
st.write("[LinkedIn](https://www.linkedin.com/in/theprasenjeet)")
st.write("[GitHub](https://github.com/theprasenjeet)")


footer="""<style>
a:link , a:visited{
color: white;
background-color: transparent;
text-decoration: underline;
}
a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: black;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://github.com/theprasenjeet" target="_blank">Prasen Jeet</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
