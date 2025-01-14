import requests
r=requests.put("https://httpbin.org/put",data={'a':1,'b':3})
print(r.text)
