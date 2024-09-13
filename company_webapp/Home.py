import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("The Best Company")
content1 = """
The best software company is one that combines cutting-edge technology with a customer-centric 
approach, delivering innovative solutions that drive growth and efficiency. It fosters a 
culture of continuous learning, collaboration, and creativity, empowering its employees to push 
boundaries and achieve excellence. With a commitment to quality, the company consistently 
exceeds client expectations, shaping the future of the tech industry.
"""
st.write(content1)
st.subheader("Our team!")

col1,col2,col3 = st.columns([1,1,1])

df = pd.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(row["first name"].capitalize() + " "+ row["last name"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"])
        
with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(row["first name"].capitalize() + " "+ row["last name"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"])
        
with col3:
    for index, row in df[8:].iterrows():
        st.subheader(row["first name"].capitalize() + " "+ row["last name"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"])