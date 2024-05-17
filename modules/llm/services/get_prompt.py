from langchain_core.prompts import PromptTemplate


def get_prompt() -> PromptTemplate:
    template = """
        Answer the question based on the context below. If you can't 
        answer the question, reply with context.

        Context: {context}

        Question: {question}
        """

    prompt = PromptTemplate.from_template(template)
    return prompt
