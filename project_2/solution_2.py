# Importing required libraries and modules
import json
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from tqdm import tqdm
import os

# List to store loaded documents
documents = []

# Load documents from a JSON lines file
with open('/Users/pabloelgueta/Downloads/train_1.jsonl', 'r') as file:
    for line in file:
        # Parse each line as a JSON object and append to the 'documents' list
        documents.append(json.loads(line))

# Retrieve the OpenAI API key from the environment variable
api_key = os.getenv('OPENAI_API_KEY') 
# Specify the model name to be used for embeddings
model_name = 'text-embedding-ada-002'

# Initialize the OpenAI embeddings using the specified model and API key
embeddings = OpenAIEmbeddings(
    model=model_name,
    openai_api_key=api_key
)

# Initialize a Chroma vector store with the specified collection name and embedding function
# The data is persisted in the specified directory
vectorstore = Chroma(
    collection_name="langchain_store",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)

# Iterating over the documents and adding them to the vector store
# 'tqdm' is used for showing the progress bar during the operation
for doc in tqdm(documents):
    # The texts are added as embeddings into the vector store
    vectorstore.add_texts(texts=[str(doc)])

# Constructing a query for similarity search
query = "What is the best way to implement retrieval?"

# Performing a similarity search in the vector store using the query
# It retrieves documents that are semantically similar to the query
docs = vectorstore.similarity_search(query)

# Print the most similar document from the search result
print(docs[0])
