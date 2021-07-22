import streamlit as st
import pywhatkit
from PIL import Image
import time
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\nishant.mishra\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

st.title("Text to handwriting converter!")
st.sidebar.title("User Inputs:")
menu=["Text to writing","Picture to text"]
option=st.sidebar.selectbox("Select:",menu)



if option=="Text to writing":
    a=st.text_area("Enter here:")
    b=st.text_input("Enter file name:")

    if st.button("Convert"):

        if a=="" or b=="":
            st.warning("Please Fill required field")
        else:
            try:
                pywhatkit.text_to_handwriting(a,save_to=f'C:\\Users\\nishant.mishra\\Desktop\\yt-3\\images\\{b}.png')
                time.sleep(15)
                image=Image.open(f'C:\\Users\\nishant.mishra\\Desktop\\yt-3\\images\\{b}.png')
                st.image(image,use_column_width=True)
            except Warning:
                st.warning("Please press the enter button on file name input")

if option=="Picture to text":
    uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg'])
    if uploaded_file is not None:
        st.image(uploaded_file,use_column_width=True)
        if st.button("Convert"):
            text = pytesseract.image_to_string(Image.open(uploaded_file))
            st.write(text)
