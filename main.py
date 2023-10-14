from langchain.chains import RetrievalQA
from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import sys

os.environ["OPENAI_API_KEY"] = 'ENTER API KEY HERE'

embedding = OpenAIEmbeddings()

persist_directory = "./data"

loader = CSVLoader( file_path="firefox-extensions.csv" )
documents = []
documents.extend(loader.load())

text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=20, separators=[" ", ",", "\n"])
texts = text_splitter.split_documents(documents)

vectordb = Chroma.from_documents(documents=texts, embedding=embedding, persist_directory=persist_directory)        

print("Saving database..")
vectordb.persist()
vectordb=None
