from langchain_community.embeddings import FastEmbedEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.vectorstores import VectorStoreRetriever

from modules.llm.services.chunks_loader import get_chunks


def initialize_vector_store_retriever() -> VectorStoreRetriever:
    chunks = get_chunks()

    vector_store = Chroma.from_documents(documents=chunks, embedding=FastEmbedEmbeddings())
    retriever = vector_store.as_retriever()

    return retriever
