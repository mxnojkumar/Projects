import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=500)
    
with col2:
    st.title("Manoj Kumar")
    content = """
    Hello, I’m Manoj Kumar V, currently in my final year of BE in Mechatronics Engineering 
    at KCT and working as a virtual intern at Soliton Technologies. Throughout my academic 
    journey, I have developed a solid foundation in engineering principles and honed my 
    technical skills in various domains such as programming, robotics, and system analysis. 
    I’m highly adaptable and versatile, always eager to learn and expand my knowledge, 
    which allows me to embrace new challenges with confidence.
    I’m recognized for my problem-solving abilities, technical expertise, innovative 
    thinking and passionate about addressing complex challenges.
    """
    st.info(content)

message = """
Below you can find some of the apps that I am going to build using Python. Feeling very 
excited and curious to do more of these projects!
""" 
st.write(message)

df = pd.read_csv("data.csv", sep=";")
col3, space, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[::2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Code link]({row['url']})")
        

with col4:
    for index, row in df[1::2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Code link]({row['url']})")
