import requests
base_url="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi?db=pubmed" ## Getting DB statistics and search fields of pubmed
responses=requests.get(base_url)
if responses.status_code==200:
    with open ("Info.txt",'w') as f:
        f.write(responses.text)
    print("Successful")    
else:
    print("Check your url")    