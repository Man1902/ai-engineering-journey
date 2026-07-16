from document_loader import load_documents
from embedder import create_vectorstore, db_exists
from retriever import get_retriever
from rag import answer

if db_exists():
    print("Using existing vector database...")
else:
    print("Loading documents...")

    docs = load_documents()

    print("Creating vector database...")

    create_vectorstore(docs)

retriever = get_retriever()

while True:

    question = input("\nQuestion: ")

    if question.lower() == "exit":
        break

    response = answer(question, retriever)

    print("\nAnswer:\n")

    # print(response.content)
    for chunk in response:
        print(chunk.content, end="", flush=True)
