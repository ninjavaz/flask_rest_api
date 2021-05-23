import requests

BASE = "http://127.0.0.1:5000/"
video_id = "1"

response = requests.put(BASE + "video/"+video_id, {'name':'szybcy i wcsielki','likes': 10, 'views': 100})
print(response.json())

input()
response = requests.get(BASE + "video/"+video_id)
print(response.json())



# 36 minuta