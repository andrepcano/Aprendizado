import requests

url = "https://www.fiap.com.br/"

a = requests.get(url)
b = a.json()
print(b)