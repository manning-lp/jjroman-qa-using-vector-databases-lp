import requests

inputs = {"input": {"question": "how to use chroma?"}}
response = requests.post("http://localhost:8001/invoke", json=inputs)

print(response.json())