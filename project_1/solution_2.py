import os

os.environ['API_KEY'] = 'YOUR_OPENAI_API_KEY'

import openai

def calculate_embeddings_for_dict(chunks_dict):
    """
    Calculate embeddings for a dictionary where each key is a file path and the corresponding value is a list of text chunks.
    
    Parameters:
    - chunks_dict (dict): Dictionary with file paths as keys and lists of text chunks as values.
    
    Returns:
    - Dictionary with file paths as keys and lists of embeddings as values.
    """
    EMBEDDING_MODEL = "text-embedding-ada-002"
    BATCH_SIZE = 1000
    
    embeddings_dict = {}
    
    for file_path, chunks in chunks_dict.items():
        embeddings = []
        
        for batch_start in range(0, len(chunks), BATCH_SIZE):
            batch_end = batch_start + BATCH_SIZE
            batch = chunks[batch_start:batch_end]
            print(f"Processing embeddings for {file_path}, batch {batch_start} to {batch_end-1}")
            response = openai.Embedding.create(model=EMBEDDING_MODEL, input=batch, api_key=os.getenv("API_KEY") )
            for i, be in enumerate(response["data"]):
                assert i == be["index"]
            batch_embeddings = [e["embedding"] for e in response["data"]]
            embeddings.extend(batch_embeddings)
        
        embeddings_dict[file_path] = embeddings
    
    return embeddings_dict

embeddings = calculate_embeddings_for_dict(results)

import openai

def get_embeddings_for_chunks(chunks):
    """
    Calculate embeddings for a list of text chunks.
    
    Parameters:
    - chunks (list): List of text chunks.
    
    Returns:
    - List of embeddings for each chunk.
    """
    EMBEDDING_MODEL = "text-embedding-ada-002"
    BATCH_SIZE = 1000
    
    embeddings = []
    
    for batch_start in range(0, len(chunks), BATCH_SIZE):
        batch_end = batch_start + BATCH_SIZE
        batch = chunks[batch_start:batch_end]
        print(f"Processing embeddings for batch {batch_start} to {batch_end-1}")
        response = openai.Embedding.create(model=EMBEDDING_MODEL, input=batch, api_key=api_key)
        for i, be in enumerate(response["data"]):
            assert i == be["index"]
        batch_embeddings = [e["embedding"] for e in response["data"]]
        embeddings.extend(batch_embeddings)
    
    return embeddings


import pandas as pd


def process_directory_and_get_embeddings(directory, max_tokens=4096):
    """
    Process all HTML files within a directory (and its subdirectories), extracting text, splitting based on token count, 
    and then calculating embeddings for each chunk.
    
    Parameters:
    - directory (str): The root directory to start the search for HTML files.
    - max_tokens (int): Maximum number of tokens per chunk.
    
    Returns:
    - DataFrame with file paths, text chunks, and their embeddings.
    """
    
    all_chunks = []
    file_paths = []
    
    # Extract and tokenize text from each HTML file
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.html'):
                file_path = os.path.join(dirpath, filename)
                text = extract_text_from_html(file_path)
                chunks = split_text_by_tokens(text, max_tokens)
                all_chunks.extend(chunks)
                file_paths.extend([file_path] * len(chunks))
    
    # Get embeddings for all chunks
    embeddings = get_embeddings_for_chunks(all_chunks)
    
    # Create a DataFrame with the file paths, chunks, and their embeddings
    df = pd.DataFrame({"file_path": file_paths, "text": all_chunks, "embedding": embeddings})
    
    return df