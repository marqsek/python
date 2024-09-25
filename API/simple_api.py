import requests

response = requests.get("https://randomfox.ca/floof")
#print(response.json()) #formating response text to JSON
fox = response.json()
print(fox['image'])