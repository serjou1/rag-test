import uvicorn
from langchain_community.document_loaders import TextLoader, AsyncHtmlLoader, AsyncChromiumLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from transcripts.links import links

from api import app

# todo change AsyncChromiumLoader to AsyncHtmlLoader


OLLAMA_URL = "http://localhost:11434"
MODEL = "llama3"


def run():
    model = Ollama(model=MODEL)

    prompt = get_prompt()

    loader = AsyncChromiumLoader(links)
    print('loading pages')
    scripts_html = loader.load()

    # text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    # documents = text_splitter.split_documents(scripts_html)

    embeddings = OllamaEmbeddings(model=MODEL)
    print('embedding')
    vectorstore = DocArrayInMemorySearch.from_documents(scripts_html, embeddings)

    parser = StrOutputParser()

    chain = (
            {"context": vectorstore.as_retriever(), "question": RunnablePassthrough()}
            | prompt
            | model
            | parser
    )
    print('asking question')
    print(chain.invoke("Why does Cartman hates rainbows?"))


def get_prompt():
    template = """
    Answer the question based on the context below. If you can't 
    answer the question, reply "I don't know".

    Context: {context}

    Question: {question}
    """

    prompt = PromptTemplate.from_template(template)
    return prompt


if __name__ == '__main__':
    uvicorn.run("main:app", port=4455, host="0.0.0.0", reload=True)
    # run()
