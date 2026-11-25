import streamlit as st
from pypdf import PdfReader

st.set_page_config(
    page_title="IntelliAssist AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 IntelliAssist AI")
st.subheader("Your Smart Document Assistant")

st.write(
    "Upload your PDF documents and explore their contents."
)

uploaded_file = st.file_uploader(
    "Upload your PDF document",
    type=["pdf"]
)

if uploaded_file is not None:
    try:
        reader = PdfReader(uploaded_file)

        document_text = ""

        for page in reader.pages:
            document_text += page.extract_text() or ""

        st.success("PDF uploaded successfully!")

        st.write(f"Total pages: {len(reader.pages)}")

        with st.expander("View extracted document text"):
            st.text(document_text[:10000])

        question = st.text_input(
            "Ask something about your document:"
        )

        if st.button("Search Document"):
            if question.strip():
                words = [
                    sentence.strip()
                    for sentence in document_text.split(".")
                    if question.lower() in sentence.lower()
                ]

                if words:
                    st.subheader("Search Results")
                    for result in words[:5]:
                        st.write("📄", result)
                else:
                    st.info(
                        "No exact keyword match found. "
                        "Try another keyword."
                    )
            else:
                st.warning("Please enter a keyword.")

    except Exception as error:
        st.error(f"Unable to read PDF: {error}")
else:
    st.info("Upload a PDF to get started.")