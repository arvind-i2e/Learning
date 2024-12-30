import requests
import json
response=requests.get("http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")#Fetching questions from stack over flow through it's API
for data in response.json()['items']:
    if data['answer_count']==0:
        print(data['title'])
        print(data['link'])
    else:
        print("Skipped")   
    print()     