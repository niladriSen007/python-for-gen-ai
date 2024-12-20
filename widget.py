import streamlit as st
import pandas as pd
st.title('My first app')

name=st.text_input('Enter your name')
if name:
    st.write(f'Hello {name}')
age  = st.slider('Enter your age',1,100,24)
if age:
    st.write(f'Your age is {age}')

st.selectbox('Select your course',['Python','Java','C++','C#'])


data ={
  "Name":['John','Doe','Smith'],
  "Age":[23,24,25],
  "Course":['Python','Java','C++']}
st.write(pd.DataFrame(data))

st.file_uploader('Upload file',type=['csv','xlsx'])

st.button('Click me')
