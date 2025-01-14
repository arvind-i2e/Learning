import requests
from PIL import Image
from io import BytesIO
r=requests.get("https://plus.unsplash.com/premium_photo-1664474619075-644dd191935f?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8aW1hZ2V8ZW58MHx8MHx8fDA%3D")
print(r.status_code)
i = Image.open(BytesIO(r.content))
fp=open("img.jpg","wb")
i.save(fp)
fp.close()