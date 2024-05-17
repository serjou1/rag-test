from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from modules.llm.services.get_prompt import get_prompt
from modules.llm.services.vector_store_loader import initialize_vector_store_retriever

OLLAMA_URL = "http://localhost:11434"
MODEL = "llama3"


class SpHelper:
    def __init__(self):
        self.chain = None
        self.model = Ollama(model=MODEL)

    def initialize(self):
        print('Initializing vector store')
        retriever = initialize_vector_store_retriever()
        print('Vector store initialized')
        prompt = get_prompt()

        self.chain = (
                {"context": retriever, "question": RunnablePassthrough()}
                | prompt
                | self.model
                | StrOutputParser()
        )

    def ask(self, question: str):
        return self.chain.invoke(question)

    def find_episode(self, description: str):
        pass
