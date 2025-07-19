import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk

# Download stopwords if needed
nltk.download('stopwords')

# Load model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Text preprocessing function
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    words = text.split()
    words = [stemmer.stem(word) for word in words if word not in stop_words]
    return ' '.join(words)

# Streamlit app layout
st.title("🕵️‍♂️ Fake Review Detector")
st.subheader("Enter a product review and check if it's genuine or fake.")

# Input text
user_input = st.text_area("✍️ Enter your review here:")

if st.button("Check"):
    if user_input.strip() == "":
        st.warning("Please enter a review.")
    else:
        cleaned = preprocess(user_input)
        vect_text = vectorizer.transform([cleaned]).toarray()
        prediction = model.predict(vect_text)[0]

        if prediction == 0:
            st.success("✅ This review is **Genuine**.")
        else:
            st.error("⚠️ This review is **Fake**.")
