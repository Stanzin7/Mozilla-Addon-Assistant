from langchain.chains import RetrievalQA
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI    
import os
import sys

os.environ["OPENAI_API_KEY"] = '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'

persist_directory = "./data"

embedding = OpenAIEmbeddings()

vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)

llm = ChatOpenAI( model_name="gpt-3.5-turbo", temperature=0.0, max_tokens=250)  # Modify model_name if you have access to GPT-4

retriever = vectordb.as_retriever(search_kwargs={'k': 5})
qa_chain = RetrievalQA.from_chain_type (llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=False )

question="are there any extensions that allow you to change the browser text size"
prompt=f"You are an expert at question answering. Please answer the following question using only the context provided. If you do not know the answer to the question do not guess, reply with I don't know:\n\n{question}"

llm_response = qa_chain(prompt)

print( llm_response["result"] )


