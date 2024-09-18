import streamlit as st
import pandas as pd

st.header('Job details')
data = pd.read_csv('mentornow/bank.csv')
a = data['job'].unique()

option = st.selectbox('Select the job',(a))
df=data[data['job']==option]
st.write(df)
avr=df['age'].mean()
st.write(round(avr))
st.metric(label='Average Age',value='39',delta='10')