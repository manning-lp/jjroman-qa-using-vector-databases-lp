from langchain.document_loaders import ReadTheDocsLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import tiktoken
import json
import os  # Make sure you've imported the necessary modules

# TODO: Step 1 - Load Documents from your directory
# HINT: Create an instance of ReadTheDocsLoader with an argument the represents your directory and call the load method on it.

# TODO: Step 2 - Initialize Tokenizer
# HINT: Use tiktoken.get_encoding('cl100k_base') to get the tokenizer.

def calculate_token_length(text):
    """
    Calculate the number of tokens in a given text using the initialized tokenizer.

    :param text: str - Text to tokenize
    :return: int - Number of tokens
    """
    # TODO: Step 3 - Encode Text and Calculate Number of Tokens
    # HINT: Use the tokenizer's encode method for the text. Disallow special tokens. Then, use len() on the result.
    pass  # Remove 'pass' and write your code here

# TODO: Step 4 - Configure Text Splitter
# HINT: Initialize RecursiveCharacterTextSplitter with appropriate parameters. Use calculate_token_length as the length function.

# TODO: Step 5 - Prepare JSON Lines File for Writing
# HINT: Use a with statement to open a file in write mode. 

    # Inside the with statement:
    
    # TODO: Step 6 - Iterate Through Documents and Write to File
    # HINT: For each document in your loaded documents, convert it to JSON and write it to the file with a newline.
    # IMPORTANT: Make sure 'documents' is correctly defined or replaced with the variable holding your documents.

