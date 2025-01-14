# import requests
# url="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=science[journal]+AND+breast+cancer+AND+2008[pdat]"
# r=requests.get(url)
# with open("Article.txt",'w') as f:
#     f.write(r.text)

# import requests
# import json

# baseurl = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?"
# params={
#     'db': 'pubmed',
#     # 'term': 'science[journal]'
#      'id':'39787246,39787245',
#     'retmode':'json',
#     # 'retmax':'5',
#     'sort': 'relevance'
    
# }

# r = requests.get(baseurl,params)

# if r.status_code == 200:

#     data = r.json()

#     with open("journal.json", 'w') as f:
#         json.dump(data,f,indent=4)
# else:
#     print(f"Error retrieving data: {r.status_code}")
# import requests
# import json

# search_baseurl = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
# search_params = {
#     'db': 'pubmed',
#     'term': 'science[journal]',
#     'retmode': 'json',
#     'retmax': '5',
#     'sort': 'relevance'
# }

# search_response = requests.get(search_baseurl, params=search_params)

# if search_response.status_code == 200:
#     search_data = search_response.json()
#     id_list = search_data.get('esearchresult', {}).get('idlist', [])
    
#     if id_list:
#         print(f"Found {len(id_list)} article IDs: {id_list}")
        
    
#         summary_baseurl = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
#         summary_params = {
#             'db': 'pubmed',
#             'id': ','.join(id_list),  
#             'retmode': 'json'
#         }
        
#         summary_response = requests.get(summary_baseurl, params=summary_params)

#         if summary_response.status_code == 200:
#             summary_data = summary_response.json()
            
            
#             with open("journal_summary.json", 'w') as f:
#                 json.dump(summary_data, f, indent=4)
#             print("Summaries saved to journal_summary.json")
#         else:
#             print(f"Error retrieving summaries: {summary_response.status_code}")
#     else:
#         print("No article IDs found.")
# else:
#     print(f"Error retrieving search data: {search_response.status_code}")

import requests
import json
search_baseurl = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
search_params = {
    'db': 'pubmed',
    'term': 'science[journal]', 
    'retmode': 'json',
    'retmax': '5',  
    'sort': 'relevance'
}

search_response = requests.get(search_baseurl, params=search_params)

if search_response.status_code == 200:
    search_data = search_response.json()
    id_list = search_data.get('esearchresult', {}).get('idlist', [])
    
    if id_list:
        print(f"Found {len(id_list)} article IDs: {id_list}")
       
        summary_baseurl = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
        summary_params = {
            'db': 'pubmed',
            'id': ','.join(id_list),
            'retmode': 'json'
        }
        
        summary_response = requests.get(summary_baseurl, params=summary_params)

        if summary_response.status_code == 200:
            summary_data = summary_response.json()
            articles = []

            
            for article_id, details in summary_data.get('result', {}).items():
                if article_id == 'uids':  
                    continue
                
                article_metadata = {
                    "article_id": article_id,
                    "article_title": details.get('title', ''),
                    "article_text": "",  
                    "web_article_url":f"https://pubmed.ncbi.nlm.nih.gov/{article_id}/",
                    "authors": [author.get('name') for author in details.get('authors', [])],
                    "article_summary": details.get('title', ''),  
                    "article_category": "",  
                    "article_type": details.get('pubtype', [''])[0],
                    "time_date": details.get('pubdate', '')
                }
                articles.append(article_metadata)
            with open("articles_metadata.json", 'w') as f:
                json.dump(articles, f, indent=4)
            print("Article metadata saved to articles_metadata.json")
        else:
            print(f"Error retrieving summaries: {summary_response.status_code}")
    else:
        print("No article IDs found.")
else:
    print(f"Error retrieving search data: {search_response.status_code}")



