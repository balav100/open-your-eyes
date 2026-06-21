import streamlit as st
import os

from modules.pdf_extractor import extract_text_from_pdf
from modules.text_cleaner import clean_text
from modules.braille_converter import text_to_braille
from modules.audio_generator import generate_audio
from modules.summarizer import summarize_text
from modules.readability import readability_score
from modules.language_detector import detect_language
from modules.ai_tutor import explain_chapter
from modules.utils import save_output
from modules.pdf_generator import save_braille_as_pdf

st.set_page_config(
    page_title="Open Your Eyes",
    layout="wide"
)

st.title("👁️ Open Your Eyes")
st.subheader("AI Powered Braille Accessibility Platform")

uploaded_file = st.file_uploader(
    "Upload PDF or TXT",
    type=["pdf", "txt"]
)

if uploaded_file:

    # Create folders if not exist
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    file_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully")

    # Extract text
    if uploaded_file.name.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    else:
        text = uploaded_file.read().decode("utf-8")

    # Clean text
    cleaned_text = clean_text(text)

    st.subheader("Extracted Text Preview")

    st.text_area(
        "Text",
        cleaned_text[:5000],
        height=250
    )

    # Language Detection
    language = detect_language(cleaned_text)

    st.subheader("Detected Language")
    st.write(language)

    # Braille Conversion
    braille_text = text_to_braille(cleaned_text)

    st.subheader("Braille Preview Panel")

    col1, col2 = st.columns(2)

    with col1:
        st.text_area(
            "Original Text",
            cleaned_text[:3000],
            height=400
        )

    with col2:
        st.text_area(
            "Braille Output",
            braille_text[:3000],
            height=400
        )

    # Accessibility Score
    score = readability_score(cleaned_text)

    st.subheader("Accessibility Score Meter")

    if score < 6:
        st.success(f"Easy Reading Level — Score: {score}")

    elif score < 12:
        st.warning(f"Medium Reading Level — Score: {score}")

    else:
        st.error(f"Advanced Reading Level — Score: {score}")

    # Summarization
    st.subheader("Smart Summary")

    summary = summarize_text(cleaned_text)

    st.write(summary)

    # Audio Narration
    st.subheader("Audio Narration")

    audio_path = generate_audio(cleaned_text)

    with open(audio_path, "rb") as audio_file:
        st.audio(audio_file.read())

    # AI Tutor
    st.subheader("AI Tutor — Braille Learning Assistant")

    user_question = st.text_input(
        "Ask questions about the uploaded book"
    )

    if user_question:

        explanation, braille_explanation = explain_chapter(
            cleaned_text[:4000],
            user_question
        )

        st.subheader("AI Tutor Explanation")

        st.write(explanation)

        st.subheader("Braille AI Explanation")

        st.text_area(
            "Braille Response",
            braille_explanation,
            height=300
        )

    # Save TXT Output
    output_path = save_output(braille_text)

    # Save PDF Output
    pdf_path = "outputs/braille_book.pdf"

    save_braille_as_pdf(
        braille_text,
        pdf_path
    )

    # Download Section
    st.subheader("📥 Download Braille Book")

    col1, col2 = st.columns(2)

    # TXT Download
    with col1:

        with open(output_path, "rb") as file:

            st.download_button(
                label="📄 Download as TXT",
                data=file,
                file_name="braille_book.txt",
                mime="text/plain"
            )

    # PDF Download
    with col2:

        with open(pdf_path, "rb") as pdf_file:

            st.download_button(
                label="📘 Download as PDF",
                data=pdf_file,
                file_name="braille_book.pdf",
                mime="application/pdf"
            )
