import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "NLP")
print(response.json())

response = requests.get(BASE + "NFI")
print(response.json())

response = requests.get(BASE + "SFU")
print(response.json())