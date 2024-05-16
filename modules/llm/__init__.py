from langchain_community.llms import Ollama
# todo change AsyncChromiumLoader to AsyncHtmlLoader
from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.embeddings import OllamaEmbeddings

from links import links

OLLAMA_URL = "http://localhost:11434"
MODEL = "llama3"


def initialize():
    model = Ollama(model=MODEL)

    __initialize_vector_store()
    pass


def ask(question: str):
    pass


def find_episode(description: str):
    pass


def __initialize_vector_store():
    loader = AsyncChromiumLoader(links)
    scripts_html = loader.load()
    embeddings = OllamaEmbeddings(model=MODEL)
