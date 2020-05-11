import requests

response = requests.get("http://www.google.com")
print(response.content)
print(response.text)
print(response.status_code)
