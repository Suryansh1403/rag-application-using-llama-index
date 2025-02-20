from llama_index.core import VectorStoreIndex
from llama_index.core import Settings
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding

from QAWithPDF.data_ingestion import load_data
from QAWithPDF.model_api import load_model
import os
import sys
from exception import customexception
from logger import logging

def download_gemini_embedding(model,document):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Returns:
    - VectorStoreIndex: An index of vector embeddings for efficient similarity queries.
    """
    try:
        persistent_dir = "storage"
        if(os.path.exists(persistent_dir)):
            logging.info("loading model from persistent dir")
            storage_context = StorageContext.from_defaults(persist_dir=persistent_dir)
            index = load_index_from_storage(storage_context)
            query_engine = index.as_query_engine()
            logging.info("model loading from persistent dir completed")
            return query_engine
        else:
            logging.info("creating embedding")
            gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001")
            Settings.llm = model
            Settings.embed_model = gemini_embed_model
            Settings.chunk_size=800
            Settings.chunk_overlap=20
            logging.info("")
            index = VectorStoreIndex.from_documents(document,embed_model = gemini_embed_model)
            index.storage_context.persist()
            
            logging.info("")
            query_engine = index.as_query_engine()
            return query_engine
    except Exception as e:
        raise customexception(e,sys)