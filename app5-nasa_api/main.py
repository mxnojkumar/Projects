import requests
import streamlit as st


url = "https://api.nasa.gov/planetary/apod?"\
    "api_key=AaqldXzJCuwivy6GcWflUUwBZjuhScyYdZfLi3tf"
    
request1 = requests.get(url)
content = request1.json()

title = content["title"]
image = content["hdurl"]
description = content["explanation"]

image_path = "app5-nasa_api/img.jpg"
request2 = requests.get(image)
with open(image_path, "wb") as img:
    img.write(request2.content)

st.title(title)
st.image(image_path)
st.write(description)