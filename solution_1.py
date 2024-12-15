# Import necessary modules
from langchain_community.document_loaders import ReadTheDocsLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import tiktoken
import json

# Initialize a loader for reading documents
path = 'C:/repos/liveProjects/documentation/apidocs/api.python.langchain.com/en/latest'
# path = "C:/repos/liveProjects/docagents/agents"

loader = ReadTheDocsLoader(path)

# Load documents and calculate the number of documents
try:
    docs = loader.load()
except Exception as e:
    print(f"An error occurred while loading documents: {e}")
    quit()  # Exit the program if an error occurs


print(f"Loaded {len(docs)} documents")  # Display the number of loaded documents

# Set up the tokenizer with a specific encoding
tokenizer = tiktoken.get_encoding('cl100k_base')

# Define a function to calculate the length in tokens of a given text
def tiktoken_len(text):
    # Encode the text into tokens and count the number of tokens
    tokens = tokenizer.encode(text, disallowed_special=())
    return len(tokens)

print("Splitting text into chunks...")

# Configure a text splitter that breaks up text into manageable chunks

chunk_size = 300  # Max number of tokens in one chunk
chunk_overlap = 200  # Number of tokens for chunks to overlap

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,  # Max number of tokens in one chunk
    chunk_overlap=chunk_overlap,  # Number of tokens for chunks to overlap
    length_function=tiktoken_len,  # Function to use for calculating token count
    separators=['/n/n', '/n', ' ', '']  # Separators for splitting the text
)

print("Saving documents...")

# Save the documents into a JSONL file
output_file = f'C:/repos/liveProjects/output/train_chunks_{chunk_size}_{chunk_overlap}_all.jsonl'
# output_file = f'C:/repos/liveProjects/output/train_agents_docs.jsonl'
nid = 1  # Initialize a document ID
with open(output_file, 'w') as f:
    for doc in docs:  # Iterate through each document
        # Convert the document into a JSON string and write to the file with a newline

        splittedText = text_splitter.split_text(doc.page_content)

        for text in splittedText:
            try:            
                # replace the character \u2192 with '->'
                text = text.replace('\u2192', '->')
                # read the metadata of the document that is a json string and get the source field
                text_json = { "id": nid, "url": doc.metadata.get('source'), "text": text }                
                
                f.write(json.dumps(text_json) + '\n')
                nid += 1
            except Exception as e:
                print(f"-----------------------------------------------------")
                print(f"An error occurred while saving document: {e}")
                print(f"BELOW DOC")
                # print(f"{doc}")
                # show the structure of the document
                print(f"{doc.metadata.keys()}")

        if False:
            try:            
                json = doc.model_dump_json()
                # replace the character \u2192 with '->'
                json = json.replace('\u2192', '->')
                f.write(json + '/n')
            except Exception as e:
                print(f"-----------------------------------------------------")
                print(f"An error occurred while saving document: {e}")
                print(f"BELOW DOC")
                print(f"{doc}")

# Confirm completion
print(f"Documents have been saved in {output_file}")
