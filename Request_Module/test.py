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

# import requests
# import json
# from datetime import datetime
# search_baseurl = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
# current_year = datetime.now().year
# start_year = current_year - 5
# search_params = {
#     'db': 'pubmed',
#     'term': f'science[journal] AND {start_year}/01/01:{current_year}/01/01[dp]', #retrieving last 5 year data through this filter
#     'retmode': 'json',
#     'usehistory': 'y',
#     'retmax': '10',  
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
#             articles = []

            
#             for article_id, details in summary_data.get('result', {}).items():
#                 if article_id == 'uids':  
#                     continue
                
#                 article_metadata = {
#                     "article_id": article_id,
#                     "article_title": details.get('title', ''),
#                     "article_text": "",  
#                     "web_article_url":f"https://pubmed.ncbi.nlm.nih.gov/{article_id}/",
#                     "authors": [author.get('name') for author in details.get('authors', [])],
#                     "article_summary": details.get('title', ''),  
#                     "article_category": "", 
#                     "article_type": details.get('pubtype', [''])[0],
#                     "time_date": details.get('pubdate', '')
#                 }
#                 articles.append(article_metadata)
#             with open("articles_metadata.json", 'w') as f:
#                 json.dump(articles, f, indent=4)
#             print("Article metadata saved to articles_metadata.json")
#         else:
#             print(f"Error retrieving summaries: {summary_response.status_code}")
#     else:
#         print("No article IDs found.")
# else:
#     print(f"Error retrieving search data: {search_response.status_code}")





import requests
from scholarly import scholarly

# Function to fetch publication data from PubMed
def fetch_pubmed_data(kol_name):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": f"{kol_name}[Author]",
        "retmode": "json",
        "retmax": 5  # Limit results to 5
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        pubmed_ids = data.get("esearchresult", {}).get("idlist", [])

        if not pubmed_ids:
            return "No publications found on PubMed."

        # Fetch publication details for the IDs
        details_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
        details_params = {
            "db": "pubmed",
            "id": ",".join(pubmed_ids),
            "retmode": "json"
        }
        details_response = requests.get(details_url, params=details_params)
        details_response.raise_for_status()
        details = details_response.json()

        # Extract and return publication titles, publication dates, and affiliations
        publications = []
        for pub_id in pubmed_ids:
            pub_data = details.get("result", {}).get(pub_id, {})
            publications.append({
                "title": pub_data.get("title"),
                "pub_date": pub_data.get("pubdate"),
                "affiliation": pub_data.get("source")  # Affiliation information
            })

        return publications

    except requests.exceptions.RequestException as e:
        return f"Error fetching PubMed data: {str(e)}"

# Function to fetch data from Wikipedia
def fetch_wikipedia_data(kol_name):
    wiki_base_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "prop": "extracts",
        "format": "json",
        "titles": kol_name.replace(" ", "_")
    }
    try:
        response = requests.get(wiki_base_url, params=params)
        response.raise_for_status()
        data = response.json()
        pages = data.get("query", {}).get("pages", {})

        for page_id, content in pages.items():
            if page_id != "-1":
                return content.get("extract", "No details found.")
        return "No Wikipedia page found."

    except requests.exceptions.RequestException as e:
        return f"Error fetching Wikipedia data: {str(e)}"

# Function to fetch data from Google Scholar
def fetch_google_scholar_data(kol_name):
    try:
        search_query = scholarly.search_author(kol_name)
        author = next(search_query)
        author_profile = {
            "name": author.get("name"),
            "affiliation": author.get("affiliation"),
            "interests": author.get("interests"),
            "cited_by": author.get("citedby"),
            "publications": [
                {"title": pub.get("bib", {}).get("title"), "year": pub.get("bib", {}).get("pub_year")}
                for pub in scholarly.fill(author)["publications"][:5]
            ]  # Fetch only the first 5 publications
        }
        return author_profile
    except StopIteration:
        return "No Google Scholar profile found."
    except Exception as e:
        return f"Error fetching Google Scholar data: {str(e)}"
    
def fetch_clinical_trials_data(kol_name):
    base_url = "https://clinicaltrials.gov/api/v2/studies"
    params = {
        "query": kol_name,
        "fields": "BriefTitle,LeadSponsorName,Condition,Phase,EnrollmentCount",
        "format": "json"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        if not data.get("studies"):
            return "No clinical trials found."

        trials = []
        for trial in data["studies"]:
            trials.append({
                "title": trial.get("BriefTitle"),
                "sponsor": trial.get("LeadSponsorName"),
                "condition": trial.get("Condition"),
                "phase": trial.get("Phase"),
                "enrollment": trial.get("EnrollmentCount")
            })

        return trials
    except requests.exceptions.RequestException as e:
        return f"Error fetching clinical trials data: {str(e)}"    

# Main function to fetch and save data
def get_kol_data(kol_name):
    if not kol_name:
        return "KOL name is required"

    # Fetch data from sources
    pubmed_data = fetch_pubmed_data(kol_name)
    wikipedia_data = fetch_wikipedia_data(kol_name)
    google_scholar_data = fetch_google_scholar_data(kol_name)
    clinical_trials_data = fetch_clinical_trials_data(kol_name)

    # Combine results
    kol_data = {
        "KOL Name": kol_name,
        "PubMed Data": pubmed_data,
        "Wikipedia Data": wikipedia_data,
        "Google Scholar Data": google_scholar_data,
        "Clinical Trials Data": clinical_trials_data
    }

    # Write data to a file
    with open(f"{kol_name.replace(' ', '_')}_data.txt", "w", encoding="utf-8") as file:
        for key, value in kol_data.items():
            file.write(f"{key}:\n")
            if isinstance(value, list):
                for item in value:
                    file.write(f"  - {item}\n")
            else:
                file.write(f"{value}\n")
            file.write("\n")

    return f"Data for {kol_name} has been written to {kol_name.replace(' ', '_')}_data.txt"


kol_name = "Dr. Shubham Jain"  
print(get_kol_data(kol_name))



