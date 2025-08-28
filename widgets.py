import streamlit as st
import pandas as pd

st.title('Application form')

name = st.text_input('Enter your name: ')
surname = st.text_input('Enter your surname: ')

age = st.slider('Select your age: ',0,100,20)    #20 means minimum age is 20.
options = ['Python','Java','C++','Javascript']
choice = st.selectbox('Choose your favorite language: ',options)

if name and surname:
    st.write(f'Hello {name} {surname}!!')
st.write(f'You age is: {age}')
st.write(f'You choose: {choice} as your favorite language')

#create and show any dataframe:
data = {
    'Name' : ['Ganesh','brad','pitt','sany'],
    'Age' : [33,28,31,33],
    'City' : ['Bangalore','Nashik','Pune','Nashik']
}

df = pd.DataFrame(data)
df.to_csv('sampledata.csv')
st.write(df)

#upload button:
uploaded_file = st.file_uploader('Upload a csv file:',type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
