import requests
import json
r = requests.get('https://api.github.com/events')
print(r.status_code)

print(r.headers['content-type'])

print(r.encoding)