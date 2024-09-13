import streamlit as st
import sys
sys.path.append('A:\python\projects\company_webapp')
from send_mails import send_mail
import pandas as pd

st.header("Contact us")

df = pd.read_csv("A:/python/projects/company_webapp/topics.csv")

with st.form(key="email_form"):
    user_mail = st.text_input("Your email address", key="user_id")
    option = st.selectbox("What topic do you want to discuss?", df["topic"])
    message = st.text_area("Text")
    full_message = f"""\
Subject: New email from {user_mail}\n
From: {user_mail} \nTopic {option}\n{message}
"""
    button = st.form_submit_button("Submit")
    
    if button:
        send_mail(full_message)
        st.info("Your mail has been sent successfully!")