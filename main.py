import streamlit as st
import os
from logger import logging
from QAWithPDF.data_ingestion import load_data
from QAWithPDF.embedding import download_gemini_embedding
from QAWithPDF.model_api import load_model
def main():
    st.title("Document Query App with LlamaIndex")
    

    uploaded_files = st.file_uploader(
        "Upload your documents (PDF, TXT, DOCX)", 
        type=["pdf", "txt", "docx"], 
        accept_multiple_files=True
    )

    if uploaded_files:
        temp_dir = "Data"
        os.makedirs(temp_dir, exist_ok=True)  
        logging.info("moving user data to DATA folder")
        for uploaded_file in uploaded_files:
            file_path = os.path.join(temp_dir, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
        logging.info("user data moved successfully")
        st.success(f"Uploaded {len(uploaded_files)} file(s) successfully!")


    user_question= st.text_input("Ask your question")

    if st.button("submit & process"):
        with st.spinner("Processing..."):
            document=load_data()
            model=load_model()
            query_engine=download_gemini_embedding(model,document)
                
            response = query_engine.query(user_question)
                
            st.write(response.response)

if __name__=="__main__":
    main()

