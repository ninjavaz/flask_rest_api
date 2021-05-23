import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "video/2", {'name':'szybcy i wcsielki','likes': 10, 'views': 100})
print(response.json())

input()

