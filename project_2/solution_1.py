# Import necessary modules
from langchain.document_loaders import ReadTheDocsLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import tiktoken
import json

# Initialize a loader for reading documents
loader = ReadTheDocsLoader('rtdocs')

# Load documents and calculate the number of documents
docs = loader.load()
print(f"Loaded {len(docs)} documents")  # Display the number of loaded documents

# Set up the tokenizer with a specific encoding
tokenizer = tiktoken.get_encoding('cl100k_base')

# Define a function to calculate the length in tokens of a given text
def tiktoken_len(text):
    # Encode the text into tokens and count the number of tokens
    tokens = tokenizer.encode(text, disallowed_special=())
    return len(tokens)

# Configure a text splitter that breaks up text into manageable chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,  # Max number of tokens in one chunk
    chunk_overlap=20,  # Number of tokens for chunks to overlap
    length_function=tiktoken_len,  # Function to use for calculating token count
    separators=['\n\n', '\n', ' ', '']  # Separators for splitting the text
)

# Save the documents into a JSONL file
output_file = '/Users/pabloelgueta/Downloads/train_1.jsonl'
with open(output_file, 'w') as f:
    for doc in docs:  # Iterate through each document
        # Convert the document into a JSON string and write to the file with a newline
        f.write(json.dumps(doc) + '\n')

# Confirm completion
print(f"Documents have been saved in {output_file}")
