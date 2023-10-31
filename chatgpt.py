import os
import sys
import openai
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma
from settings import APIKEY


# Declare global variables
chain = None
chat_history = []
def init_chatbot():
    global chain, chat_history

    api_key = APIKEY
    if not api_key:
        raise ValueError("API key environment variable not set.")

    os.environ["OPENAI_API_KEY"] = api_key

    PERSIST = False
    if PERSIST and os.path.exists("persist"):
        print("Reusing index...\n")
        vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
        index = VectorStoreIndexWrapper(vectorstore=vectorstore)
    else:
      
        loader = TextLoader("data/data.txt") # Uncomment to load from data.txt only
        if PERSIST:
            index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory":"persist"}).from_loaders([loader])
        else:
            index = VectorstoreIndexCreator().from_loaders([loader])

    chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model="gpt-3.5-turbo"),
        retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
    )

    chat_history = []

def get_response(user_input):
    global chain, chat_history
    
    # Parse and handle context (this is a placeholder, you might need NLP or regex-based extraction methods)
    context = "Mozilla extensions"
    
    # Build the refined query
    refined_input = f"In the context of {context}, {user_input}"
    
    # Query the model
    result = chain({"question": refined_input, "chat_history": chat_history})
    
    # Ensure a valid answer is returned
    answer = result.get('answer', "I don't have access to that information")
    
    if not answer.strip():
        answer = "I don't have access to that information"
    
    # Update chat history
    chat_history.append((user_input, answer))
    
    return answer

if __name__ == "__main__":
    init_chatbot()
    while True:
        user_input = input("Prompt: ")
        if user_input in ['quit', 'q', 'exit']:
            break
        print(get_response(user_input))