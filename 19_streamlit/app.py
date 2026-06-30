import streamlit as st
import pandas as pd
import numpy as np

#title of app
st.title("Hello soham this is  streamlit")

#display a simple text
st.write("this is the simple text ")

#create and display dataframe
df=pd.DataFrame(
    {
        'first column':[1,2,3,4],
        'second column':[10,20,30,40]
    }
)

st.write("here is a dataframe")
st.write(df)


#create a line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']    
)
st.line_chart(chart_data)
