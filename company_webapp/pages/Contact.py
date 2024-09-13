import streamlit as st
from send_mails import send_mail

st.header("Contact us")

with st.form(key="email_form"):
    user_mail = st.text_input("Your email address")
    message = st.text_area("Message")
    message = message + "\n" + user_mail
    button = st.form_submit_button("Submit")
    
    if button:
        send_mail(message)