import streamlit as st
from apis.ocr import ocr_api
from PIL import Image

st.title("OCR")
st.write("This is an OCR application")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Processing..."):
        status, output_image = ocr_api(uploaded_file)

    st.write(f"Status: {status}")
    if output_image is not None:
        st.image(output_image, caption="Output Image", use_container_width=True)
    else:
        st.write("No output image to display.")