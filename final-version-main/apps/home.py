import streamlit as st
from PIL import Image

def app():
    st.title("Neural Style Transfer for Wedding Photo")
    image = Image.open('imgs/lake.jpeg')
    st.image(image, caption='Welcome to my webapp!', use_column_width=True)

   
