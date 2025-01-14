import requests
url="https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-701.exe"
r=requests.get(url)
print(r.status_code)
fp=open("winraar.exe","wb")
fp.write(r.content)
fp.close()