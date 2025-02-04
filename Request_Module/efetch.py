import requests
import json
base_url="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
base_params={
    'db': 'pubmed',
    'id':'34822299',
    'retmode': 'xml'
}
efetch_response=requests.get(base_url,params=base_params)
# search_data=efetch_response.json()
if efetch_response.status_code==200:
    with open('details.xml','w',encoding="utf-8") as f:
        f.write(efetch_response.text)
    print("successfull done")
else:
    print("some error") 
    ####AIzaSyBFJjy2Fygh6FOcc35bn3anbRj5v479oU8