import streamlit as st
from model.preprocess import preprocess_image
from model.predict import extract_business_card_info

st.set_page_config(page_title="Business Card Scanner", page_icon=":card_index:", layout="centered")
st.title("Business Card Scanner :card_index:")
st.write("Upload an image of a business card, and the app will extract the text, email addresses, and phone numbers from it.")

uploaded_file = st.file_uploader("Choose a business card image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = uploaded_file.read()
    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Uploaded Image')
        st.image(uploaded_file, use_column_width=True)

    original_img, processed_thresh = preprocess_image(file_bytes)

    if processed_thresh is not None:
        result = extract_business_card_info(processed_thresh)

        with col2:
            st.subheader('Processed Image')
            st.image(processed_thresh, use_column_width=True)

    else: 
        st.error("Error processing the image. Please make sure the uploaded file is a valid image.")        