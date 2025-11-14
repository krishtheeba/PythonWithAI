import streamlit as st

import pandas as pd

st.title("Welcome !")

model = st.text_input("Enter model name")

if model:
	st.success(f"Input Model name:{model}")

vector=st.slider('select vector range:',500,900)

if vector:
	st.success(f'selected vector range:{vector}')


st.slider("Select your age")
st.slider("select your port:",5000,5500,6000)

st.select_slider("Select your rate:",["Bad","Good","Excellent"])

st.selectbox("Select Your Model:", ["gpt4.0","gpt5.0","lamma","gemma:2b"])

st.multiselect("Select Your Model:", ["gpt4.0","gpt5.0","lamma","gemma:2b"])

file= st.file_uploader("Select your input file")

if file:
	st.success(f"Input file: {file.name} is loaded")

	df= pd.read_csv(file)

	st.write(df)


st.checkbox("yes")
st.checkbox("no")

st.radio("Select the interface", ["eth0","eth1","eth2"])

st.button("Click Me")




