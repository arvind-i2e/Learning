import requests
r = requests.post('https://httpbin.org/post?a=b', data={'Name': 'Elliot alderson'})
print(r.text)