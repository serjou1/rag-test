from typing import List

# todo change AsyncChromiumLoader to AsyncHtmlLoader
from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import BeautifulSoupTransformer
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from modules.llm.constants.links import links


def get_chunks() -> List[Document]:
    loader = AsyncChromiumLoader(links)
    docs = loader.load()

    bs_transformer = BeautifulSoupTransformer()
    for doc in docs:
        doc.metadata['episode_name'] = bs_transformer.extract_tags(
            html_content=doc.page_content,
            tags=['title']
        ).replace(' Transcript at IMSDb.', '')

    docs = bs_transformer.transform_documents(documents=docs, tags_to_extract=["td"])

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=100)
    chunks = text_splitter.transform_documents(docs)

    return chunks
