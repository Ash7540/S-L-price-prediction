import streamlit as st
import os
from PIL import Image


st.title(" SmartPhone and Laptop Prediction :sunglasses:")
st.snow()
image = Image.open('a.jpg')

st.image(image, caption='Proud to Be Data Scientist')
st.header("Ash Smartphone & Laptops")
st.text('Want to predict price of smartphone and laptop then visit us')

st.subheader("Let's Connect:-")
st.text("LinkedIn:- ")
if st.button(' Click Here to Connect with me'):
    st.write('https://www.linkedin.com/in/ashwinachavan1902/')
    st.balloons()

st.text("GitHub:- ")
if st.button(' Click Here to Connect'):
    st.write('https://github.com/Ash7540')
    st.balloons()
