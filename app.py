import streamlit as st
import joblib
model = joblib.load('Sentiment-Analysis')
st.title('Sentiment Analysis using Machine Learning Algorithms')
ip = st.text_input('Enter your message')
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
