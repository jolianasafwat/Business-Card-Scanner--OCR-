import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from model.preprocess import preprocess_image
from model.predict import extract_business_card_info

st.set_page_config(page_title="Business Card Scanner", page_icon=":card_index:", layout="centered")

st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(135deg, #020617 0%, #111827 45%, #1f2937 100%);
        }
        .hero-card {
            background: rgba(15, 23, 42, 0.9);
            border: 1px solid #334155;
            border-radius: 20px;
            padding: 1.4rem 1.6rem;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.35);
            margin-bottom: 1rem;
        }
        .hero-title {
            font-size: 2.2rem;
            font-weight: 800;
            color: #f8fafc;
            margin-bottom: 0.3rem;
        }
        .hero-subtitle {
            font-size: 1rem;
            color: #cbd5e1;
            line-height: 1.5;
        }
        .upload-box {
            background: linear-gradient(90deg, #111827 0%, #1f2937 100%);
            border: 2px dashed #8b5cf6;
            border-radius: 16px;
            padding: 0.8rem;
            margin-top: 0.8rem;
        }
        .result-card {
            background: #111827;
            color: #f8fafc;
            border-radius: 16px;
            padding: 1rem 1.1rem;
            border: 1px solid #334155;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.25);
            margin-top: 0.7rem;
        }
        .stSubheader, .stSuccess, .stError, .stSpinner, .stFileUploader label, .stTextInput label {
            color: #f8fafc !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-card">
        <div class="hero-title">✨ Business Card Scanner</div>
        <div class="hero-subtitle">Upload a card image and let the app pull out the key details in a colorful, polished view.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

uploaded_file = st.file_uploader("Choose a business card image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = uploaded_file.read()
    original_img, processed_thresh = preprocess_image(file_bytes)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="upload-box">', unsafe_allow_html=True)
        st.subheader('Uploaded Image')
        st.image(original_img, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="upload-box">', unsafe_allow_html=True)
        st.subheader('Processed Image')
        st.image(processed_thresh, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()
    st.subheader("Extracted Information")

    if processed_thresh is not None:
        with st.spinner("Extracting text via Tesseract OCR..."):
            result = extract_business_card_info(processed_thresh)

            st.success("Extraction Complete!")
            st.markdown(f"<div class='result-card'><strong>Name:</strong> {result['name']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='result-card'><strong>Company:</strong> {result['company']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='result-card'><strong>Email:</strong> {', '.join(result['emails'])}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='result-card'><strong>Phone:</strong> {', '.join(result['phones'])}</div>", unsafe_allow_html=True)

    else:
        st.error("Error processing the image. Please make sure the uploaded file is a valid image.")