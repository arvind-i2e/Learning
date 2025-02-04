# import requests
# from xml.etree import ElementTree

# def fetch_kol_affiliation_and_achievements(kol_names, max_articles=10):
#     for kol_name in kol_names:
#         esearch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
#         esearch_params = {
#             "db": "pubmed",
#             "term": kol_name,
#             "retmax": max_articles,
#             "retmode": "json",
#         }
#         esearch_response = requests.get(esearch_url, params=esearch_params)
#         pmid_list = esearch_response.json().get("esearchresult", {}).get("idlist", [])
        
#         if not pmid_list:
#             print(f"No articles found for {kol_name}.")
#             continue
        
#         efetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
#         efetch_params = {
#             "db": "pubmed",
#             "id": ",".join(pmid_list),
#             "retmode": "xml",
#         }
#         efetch_response = requests.get(efetch_url, params=efetch_params)
        
#         filename = f"{kol_name.replace(' ', '_')}_details.txt"
#         root = ElementTree.fromstring(efetch_response.content)
#         with open(filename, "w", encoding="utf-8") as file:
#             for article in root.findall(".//PubmedArticle"):
#                 title = article.find(".//ArticleTitle").text
#                 affiliation = article.find(".//AffiliationInfo/Affiliation")
#                 affiliation_text = affiliation.text if affiliation is not None else "Affiliation not available"
#                 file.write(f"Title: {title}\n")
#                 file.write(f"Affiliation: {affiliation_text}\n")
#                 file.write("-" * 80 + "\n")
#         print(f"Data written to {filename}")

# kol_list = ["Odlander B", "Claesson HE", "Jakobsson PJ"]
# fetch_kol_affiliation_and_achievements(kol_list, max_articles=5)
# import requests
# from bs4 import BeautifulSoup

# def get_orcid_data(name, affiliation):
#     url = f"https://pub.orcid.org/v3.0/search?q={name}+{affiliation}"
#     headers = {"Accept": "application/json"}
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return response.json()
#     return {}

# def scrape_institution_website(name, affiliation, website_url):
#     response = requests.get(website_url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         profiles = []  # Extract relevant sections with BeautifulSoup
#         # Add parsing logic based on website structure
#         return profiles
#     return []

# def get_pubmed_data(name, affiliation):
#     esearch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
#     esearch_params = {"db": "pubmed", "term": f"{name} AND {affiliation}", "retmode": "json"}
#     response = requests.get(esearch_url, params=esearch_params)
#     if response.status_code == 200:
#         pmids = response.json().get("esearchresult", {}).get("idlist", [])
#         # Further fetch article details using efetch
#         return pmids
#     return []

# def fetch_kol_details(name, affiliation, website_url=None):
#     orcid_data = get_orcid_data(name, affiliation)
#     pubmed_data = get_pubmed_data(name, affiliation)
#     institution_data = scrape_institution_website(name, affiliation, website_url) if website_url else []

#     combined_data = {
#         "Name": name,
#         "Affiliation": affiliation,
#         "ORCID": orcid_data,
#         "Publications": pubmed_data,
#         "Institution Profiles": institution_data,
#     }

#     with open(f"{name.replace(' ', '_')}_career_details.json", "w", encoding="utf-8") as file:
#         import json
#         json.dump(combined_data, file, indent=4)

# # Example usage
# fetch_kol_details("Odlander B", "Karolinska Institute", "https://ki.se/en/staff-directory")
# import requests
# from bs4 import BeautifulSoup
# from xml.etree import ElementTree

# def get_degrees_from_orcid(name, affiliation):
#     """
#     Query ORCID API to fetch education details of a KOL.
#     """
#     url = f"https://pub.orcid.org/v3.0/search?q={name} {affiliation}"
#     headers = {"Accept": "application/json"}
#     response = requests.get(url, headers=headers)

#     if response.status_code == 200:
#         data = response.json()
#         if 'result' in data:
#             for result in data['result']:
#                 orcid_id = result['orcid-identifier']['path']
#                 edu_url = f"https://pub.orcid.org/v3.0/{orcid_id}/educations"
#                 edu_response = requests.get(edu_url, headers=headers)
#                 if edu_response.status_code == 200:
#                     educations = edu_response.json().get('education-summary', [])
#                     degrees = [
#                         f"{edu.get('role-title', 'Degree Unknown')} at {edu['organization']['name']}"
#                         for edu in educations
#                     ]
#                     return degrees
#     return ["No education details found in ORCID."]

# def fetch_degrees_from_pubmed(name, affiliation):
#     """
#     Use PubMed API to retrieve affiliation text which may include degree information.
#     """
#     esearch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
#     esearch_params = {
#         "db": "pubmed",
#         "term": f"{name} AND {affiliation}",
#         "retmode": "json",
#         "retmax": 10
#     }
#     esearch_response = requests.get(esearch_url, params=esearch_params)
#     if esearch_response.status_code == 200:
#         pmid_list = esearch_response.json().get("esearchresult", {}).get("idlist", [])
#         if pmid_list:
#             efetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
#             efetch_params = {
#                 "db": "pubmed",
#                 "id": ",".join(pmid_list),
#                 "retmode": "xml"
#             }
#             efetch_response = requests.get(efetch_url, params=efetch_params)
#             if efetch_response.status_code == 200:
#                 root = ElementTree.fromstring(efetch_response.content)
#                 degrees = []
#                 for article in root.findall(".//Author"):
#                     if name.lower() in article.find(".//LastName").text.lower():
#                         affiliation_elem = article.find(".//AffiliationInfo/Affiliation")
#                         if affiliation_elem is not None:
#                             affiliation_text = affiliation_elem.text
#                             if "PhD" in affiliation_text or "MD" in affiliation_text:
#                                 degrees.append(affiliation_text)
#                 return degrees if degrees else ["No degree details found in PubMed."]
#     return ["No degree details found in PubMed."]

# def scrape_degrees_from_institution(name, institution_url):
#     """
#     Scrape an institution's staff directory to retrieve degree details.
#     """
#     try:
#         response = requests.get(institution_url)
#         soup = BeautifulSoup(response.content, 'html.parser')
#         for profile in soup.find_all("div", class_="staff-profile"):
#             if name.lower() in profile.text.lower():
#                 return [profile.text]  # Look for degrees in text
#     except Exception as e:
#         return [f"Error while scraping: {e}"]
#     return ["No degree details found in institutional website."]

# def get_kol_degrees(name, affiliation, institution_url):
#     """
#     Consolidate degree details from multiple sources.
#     """
#     print(f"Fetching degrees for: {name} ({affiliation})")
#     degrees = {
#         "ORCID": get_degrees_from_orcid(name, affiliation),
#         "PubMed": fetch_degrees_from_pubmed(name, affiliation),
#         "Institution": scrape_degrees_from_institution(name, institution_url),
#     }
#     return degrees

# # Example usage
# kol_name = "Odlander B"
# kol_affiliation = "Karolinska Institute"
# institution_website = "https://example.edu/staff-directory"

# degrees_data = get_kol_degrees(kol_name, kol_affiliation, institution_website)

# # Save results to a file
# with open(f"{kol_name.replace(' ', '_')}_degrees.txt", "w", encoding="utf-8") as file:
#     for source, degrees in degrees_data.items():
#         file.write(f"{source} Degrees:\n")
#         for degree in degrees:
#             file.write(f"- {degree}\n")
#         file.write("\n")
# import requests
# from xml.etree import ElementTree

# def fetch_affiliations_from_pubmed(kol_name, max_articles=10):
#     """
#     Fetch affiliation details of a KOL from PubMed articles using their name.
#     """
#     esearch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
#     esearch_params = {
#         "db": "pubmed",
#         "term": kol_name,
#         "retmode": "json",
#         "retmax": max_articles,
#     }
#     esearch_response = requests.get(esearch_url, params=esearch_params)
#     pmid_list = esearch_response.json().get("esearchresult", {}).get("idlist", [])
    
#     if not pmid_list:
#         print(f"No articles found for {kol_name}.")
#         return []
    
#     efetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
#     efetch_params = {
#         "db": "pubmed",
#         "id": ",".join(pmid_list),
#         "retmode": "xml",
#     }
#     efetch_response = requests.get(efetch_url, params=efetch_params)
#     root = ElementTree.fromstring(efetch_response.content)
    
#     affiliations = []
#     for article in root.findall(".//Author"):
#         lastname_elem = article.find(".//LastName")
#         if lastname_elem is not None and kol_name.split()[0].lower() in lastname_elem.text.lower():
#             affiliation_elem = article.find(".//AffiliationInfo/Affiliation")
#             if affiliation_elem is not None:
#                 affiliations.append(affiliation_elem.text.strip())
    
#     return list(set(affiliations))  # Remove duplicates

# def enrich_with_career_details(name, affiliations):
#     """
#     Use affiliation data to infer or retrieve professional career details for the KOL.
#     """
#     career_details = {}
#     for affiliation in affiliations:
#         # Simulating a professional career data enrichment
#         # Replace with actual API calls to ORCID, institutional directories, etc., if available.
#         career_details[affiliation] = {
#             "Degrees": ["PhD", "MD"],  # Mocked degree data
#             "Position": "Senior Researcher",  # Mocked position
#             "Years Active": "1995-Present",  # Mocked career duration
#         }
#     return career_details

# def get_kol_career_details_from_pubmed(kol_name, max_articles=10):
#     """
#     Retrieve professional career details of a KOL using their name by combining PubMed data and enrichment logic.
#     """
#     print(f"Fetching affiliations for {kol_name}...")
#     affiliations = fetch_affiliations_from_pubmed(kol_name, max_articles=max_articles)
    
#     if not affiliations:
#         print(f"No affiliation data found for {kol_name}.")
#         return {}
    
#     print(f"Enriching career details for {kol_name}...")
#     career_details = enrich_with_career_details(kol_name, affiliations)
#     return career_details

# # Example usage
# kol_name = "Odlander B"
# career_data = get_kol_career_details_from_pubmed(kol_name, max_articles=10)

# # Save results to a file
# filename = f"{kol_name.replace(' ', '_')}_career_details.txt"
# with open(filename, "w", encoding="utf-8") as file:
#     for affiliation, details in career_data.items():
#         file.write(f"Affiliation: {affiliation}\n")
#         for key, value in details.items():
#             file.write(f"{key}: {value}\n")
#         file.write("\n")

# print(f"Career details saved to {filename}.")
# import requests
# from xml.etree import ElementTree

# def search_pubmed(kol_name, max_results=20):
#     """
#     Search PubMed for articles authored by the specified KOL.
#     """
#     esearch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
#     params = {
#         "db": "pubmed",
#         "term": kol_name,
#         "retmode": "json",
#         "retmax": max_results,
#     }
#     response = requests.get(esearch_url, params=params)
#     if response.status_code != 200:
#         print(f"Error: Unable to search PubMed (Status Code: {response.status_code})")
#         return []
#     data = response.json()
#     return data.get("esearchresult", {}).get("idlist", [])

# def fetch_article_details(pmid_list):
#     """
#     Fetch detailed information for articles from PubMed using PMIDs.
#     """
#     if not pmid_list:
#         return []
#     efetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
#     params = {
#         "db": "pubmed",
#         "id": ",".join(pmid_list),
#         "retmode": "xml",
#     }
#     response = requests.get(efetch_url, params=params)
#     if response.status_code != 200:
#         print(f"Error: Unable to fetch article details (Status Code: {response.status_code})")
#         return []
#     root = ElementTree.fromstring(response.content)
#     return root.findall(".//PubmedArticle")

# def extract_affiliations_and_collaborations(articles):
#     """
#     Extract affiliation information and identify co-authors from the articles.
#     """
#     affiliations = set()
#     co_authors = set()

#     for article in articles:
#         # Extract affiliations
#         for affiliation_elem in article.findall(".//AffiliationInfo/Affiliation"):
#             affiliations.add(affiliation_elem.text.strip())
        
#         # Extract co-authors
#         for author_elem in article.findall(".//Author"):
#             lastname = author_elem.find("LastName")
#             forename = author_elem.find("ForeName")
#             if lastname is not None and forename is not None:
#                 co_authors.add(f"{forename.text} {lastname.text}")
    
#     return list(affiliations), list(co_authors)

# def analyze_publication_history(articles):
#     """
#     Analyze publication history for topics and citations.
#     """
#     publication_data = []
#     for article in articles:
#         title_elem = article.find(".//ArticleTitle")
#         title = title_elem.text.strip() if title_elem is not None else "Title not available"

#         abstract_elem = article.find(".//Abstract/AbstractText")
#         abstract = abstract_elem.text.strip() if abstract_elem is not None else "Abstract not available"

#         publication_data.append({"Title": title, "Abstract": abstract})
    
#     return publication_data

# def save_results_to_file(kol_name, affiliations, co_authors, publication_data):
#     """
#     Save the extracted data to a text file.
#     """
#     filename = f"{kol_name.replace(' ', '_')}_pubmed_analysis.txt"
#     with open(filename, "w", encoding="utf-8") as file:
#         file.write(f"Key Opinion Leader: {kol_name}\n\n")
        
#         file.write("Affiliations:\n")
#         for affiliation in affiliations:
#             file.write(f"- {affiliation}\n")
#         file.write("\n")
        
#         file.write("Co-Authors:\n")
#         for co_author in co_authors:
#             file.write(f"- {co_author}\n")
#         file.write("\n")
        
#         file.write("Publication History:\n")
#         for pub in publication_data:
#             file.write(f"Title: {pub['Title']}\n")
#             file.write(f"Abstract: {pub['Abstract']}\n")
#             file.write("-" * 80 + "\n")
    
#     print(f"Results saved to {filename}")

# def analyze_kol_pubmed(kol_name, max_results=20):
#     """
#     Perform a complete analysis of a KOL using PubMed.
#     """
#     print(f"Searching PubMed for articles by {kol_name}...")
#     pmid_list = search_pubmed(kol_name, max_results=max_results)
#     if not pmid_list:
#         print(f"No articles found for {kol_name}.")
#         return
    
#     print(f"Fetching details for {len(pmid_list)} articles...")
#     articles = fetch_article_details(pmid_list)
#     if not articles:
#         print("No detailed articles found.")
#         return
    
#     print("Extracting affiliations and collaborations...")
#     affiliations, co_authors = extract_affiliations_and_collaborations(articles)
    
#     print("Analyzing publication history...")
#     publication_data = analyze_publication_history(articles)
    
#     print("Saving results to file...")
#     save_results_to_file(kol_name, affiliations, co_authors, publication_data)

# # Example usage
# kol_name = "Odlander B"
# analyze_kol_pubmed(kol_name, max_results=10)






