from langchain_community.document_loaders import BSHTMLLoader
import os

def process_directory(directory, max_tokens=400):
    """
    Process all HTML files within a directory (and its subdirectories), extracting text and splitting based on token count.
    
    Parameters:
    - directory (str): The root directory to start the search for HTML files.
    - max_tokens (int): Maximum number of tokens per chunk.
    
    Returns:
    - Dictionary with file paths as keys and lists of text chunks as values.
    """
    results = {}
    n = 0
        
    # Loop through the directory and its subdirectories
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.html'):
                file_path = os.path.join(dirpath, filename)
                loader = BSHTMLLoader(file_path)

                try:
                    data = loader.load()
                    results[file_path.replace("/", "-").replace("\\", "-")] = data
                    print(f"Loaded {file_path}")
                    n += 1
                except Exception as e:
                    print(f"Error loading {file_path}")
                    continue      
                
    print(f"{n} HTML files read")
    return results

import tiktoken

def get_tokens(documents):

    tokenizer = tiktoken.get_encoding('cl100k_base')

    for file_path, text in documents.items():
            ntokens = len(tokenizer.encode(text[0].page_content))
            print(f"Number of tokens: {file_path} - {ntokens}")
            print()

# C:/repos/liveProjects/jjroman-qa-using-vector-databases-lp/documentation/apidocs/api.python.langchain.com/en/latest

from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)

# 