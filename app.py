import streamlit as st
import numpy as np
import pandas as pd

### Title of the application:-
st.title('Streamlit Application')

### Display a simple text:-
st.write('This is simple text for streamlit application!')

### Create a simple Dataframe:--
df = pd.DataFrame({
    'first Column' : [1,2,3,4],
    'second column' : [10,20,30,40]
})

### Display the dataframe:-
st.write('Displayin the dataframe:')
st.write(df)

### Create a line chart:-
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['A','B','C']
)
st.line_chart(chart_data)