from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import VectorStoreRetriever
import config

model = ChatOllama(
    model=config.LLM_MODEL,
    temperature=0.1
)

template = """
You are an expert in answering questions.Answer the question using ONLY the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

prompt = ChatPromptTemplate.from_template(template)


def answer(question:str, retriever:VectorStoreRetriever):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    chain = prompt | model

    # to return the full response at once
    # return chain.invoke({
    #     "context": context,
    #     "question": question
    # })

    return chain.stream({
        "context": context,
        "question": question
    })