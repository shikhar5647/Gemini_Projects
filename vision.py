from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        return "Please provide an input."    
    return response.text

st.set_page_config(page_title="Gemini image demo")
st.header("Gemini App by Shikhar Dave")
input=st.text_input("Input: ",key="input")

uploaded_file=st.file_uploader("Choose an image :",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)

if st.button("Tell me about the image:"):
    response = get_gemini_response(input, image)
    st.subheader("The response is:")
    st.write(response)



