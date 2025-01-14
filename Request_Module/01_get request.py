import requests
r=requests.get("https://mazespin.live/")
# print(r.text)
with open("index.html",'w') as f:
    f.write(r.text)
