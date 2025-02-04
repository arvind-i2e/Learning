# import requests
# from bs4 import BeautifulSoup
# from flask import Flask, jsonify

# app = Flask(__name__)

# def scrape_wikipedia_kol(name):
#     url = f"https://en.wikipedia.org/wiki/{name.replace(' ', '_')}"
#     response = requests.get(url)

#     if response.status_code != 200:
#         return {"error": "Page not found or request failed"}

#     soup = BeautifulSoup(response.text, "html.parser")

#     infobox = soup.find("table", {"class": "infobox"})
#     details = {"name": name, "url": url, "sections": {}}

#     if infobox:
#         for row in infobox.find_all("tr"):
#             header = row.find("th")
#             value = row.find("td")
#             if header and value:
#                 details[header.text.strip()] = value.text.strip()

#     content_sections = soup.find_all("h2")
#     for section in content_sections:
#         section_title = section.text.replace("[edit]", "").strip()
#         paragraphs = []
#         for sibling in section.find_next_siblings():
#             if sibling.name == "h2":
#                 break
#             if sibling.name == "p":
#                 paragraphs.append(sibling.text.strip())
#         if paragraphs:
#             details["sections"][section_title] = " ".join(paragraphs)

#     return details

# @app.route('/scrape/kol/<name>', methods=['GET'])
# def get_scraped_kol_details(name):
#     return jsonify(scrape_wikipedia_kol(name))

# if __name__ == '__main__':
#     app.run(debug=True)

##### with api key
# def get_google_scholar_author_id(name):
#     url = f"https://serpapi.com/search.json?engine=google_scholar&q={name}&api_key={SERPAPI_KEY}"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         if "organic_results" in data:
#             for result in data["organic_results"]:
#                 if "author_id" in result:
#                     return result["author_id"]
#     return None

# def fetch_google_scholar(name):
#     author_id = get_google_scholar_author_id(name)
#     if not author_id:
#         return {"error": "Google Scholar profile not found."}

#     url = f"https://serpapi.com/search.json?engine=google_scholar_author&author_id={author_id}&api_key={SERPAPI_KEY}"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         return {
#             "name": data.get("author", {}).get("name", "N/A"),
#             "affiliations": data.get("author", {}).get("affiliations", "N/A"),
#             "h_index": data.get("cited_by", {}).get("table", [])[0].get("value", "N/A") if "cited_by" in data else "N/A",
#             "i10_index": data.get("cited_by", {}).get("table", [])[1].get("value", "N/A") if "cited_by" in data else "N/A",
#             "citations": data.get("cited_by", {}).get("table", [])[2].get("value", "N/A") if "cited_by" in data else "N/A",
#         }
#     return {"error": "Google Scholar data not available"}


# import requests
# from bs4 import BeautifulSoup
# from flask import Flask, jsonify
# from scholarly import scholarly
# import os

# app = Flask(__name__)

# SERPAPI_KEY = "your_key"
# TWITTER_BEARER_TOKEN = "your token"

# def scrape_wikipedia_kol(name):
#     url = f"https://en.wikipedia.org/wiki/{name}"
#     response = requests.get(url)

#     if response.status_code != 200:
#         return {"error": "Page not found or request failed"}

#     soup = BeautifulSoup(response.text, "html.parser")

#     infobox = soup.find("table", {"class": "infobox"})
#     details = {"name": name, "url": url, "sections": {}}

#     if infobox:
#         for row in infobox.find_all("tr"):
#             header = row.find("th")
#             value = row.find("td")
#             if header and value:
#                 details[header.text.strip()] = value.text.strip()

#     content_sections = soup.find_all("h2")
#     for section in content_sections:
#         section_title = section.text.replace("[edit]", "").strip()
#         paragraphs = []
#         for sibling in section.find_next_siblings():
#             if sibling.name == "h2":
#                 break
#             if sibling.name == "p":
#                 paragraphs.append(sibling.text.strip())
#         if paragraphs:
#             details["sections"][section_title] = " ".join(paragraphs)

#     return details

# def fetch_pubmed_data(kol_name):
#     base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
#     params = {
#         "db": "pubmed",
#         "term": f"{kol_name}[Author]",
#         "retmode": "json",
#         "retmax": 5  # Limit results to 5
#     }
#     try:
#         response = requests.get(base_url, params=params)
#         response.raise_for_status()
#         data = response.json()
#         pubmed_ids = data.get("esearchresult", {}).get("idlist", [])

#         if not pubmed_ids:
#             return "No publications found on PubMed."

#         # Fetch publication details for the IDs
#         details_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
#         details_params = {
#             "db": "pubmed",
#             "id": ",".join(pubmed_ids),
#             "retmode": "json"
#         }
#         details_response = requests.get(details_url, params=details_params)
#         details_response.raise_for_status()
#         details = details_response.json()

#         # Extract and return publication titles, publication dates, and affiliations
#         publications = []
#         for pub_id in pubmed_ids:
#             pub_data = details.get("result", {}).get(pub_id, {})
#             publications.append({
#                 "title": pub_data.get("title"),
#                 "pub_date": pub_data.get("pubdate"),
#                 "affiliation": pub_data.get("source")  # Affiliation information
#             })

#         return publications

#     except requests.exceptions.RequestException as e:
#         return f"Error fetching PubMed data: {str(e)}"
# def fetch_google_scholar_data(kol_name):
#     try:
#         search_query = scholarly.search_author(kol_name)
#         author = next(search_query)
#         author_profile = {
#             "name": author.get("name"),
#             "affiliation": author.get("affiliation"),
#             "interests": author.get("interests"),
#             "cited_by": author.get("citedby"),
#             "publications": [
#                 {"title": pub.get("bib", {}).get("title"), "year": pub.get("bib", {}).get("pub_year")}
#                 for pub in scholarly.fill(author)["publications"][:5]
#             ]  # Fetch only the first 5 publications
#         }
#         return author_profile
#     except StopIteration:
#         return "No Google Scholar profile found."
#     except Exception as e:
#         return f"Error fetching Google Scholar data: {str(e)}"
    
# def fetch_twitter_profile(kol_name, timeout=5):
#     """Fetch professional details of a KOL from Twitter using username lookup."""
#     headers = {"Authorization": f"Bearer {TWITTER_BEARER_TOKEN}"}
#     twitter_username = kol_name.replace(" ", "")

#     search_url = f"https://api.twitter.com/2/users/by/username/{twitter_username}?user.fields=description,location,public_metrics,verified"

#     try:
#         response = requests.get(search_url, headers=headers, timeout=timeout)  # Set timeout
#         response.raise_for_status()
#         data = response.json()

#         if "data" in data:
#             profile = data["data"]  # Corrected JSON parsing

#             twitter_url = f"https://twitter.com/{profile.get('username')}"
#             return {
#                 "name": profile.get("name"),
#                 "username": {
#                     "handle": profile.get("username"),
#                     "link": twitter_url  # Clickable link to the Twitter profile
#                 },
#                 "bio": profile.get("description"),
#                 "location": profile.get("location"),
#                 "followers": profile.get("public_metrics", {}).get("followers_count"),
#                 "following": profile.get("public_metrics", {}).get("following_count"),
#                 "tweets": profile.get("public_metrics", {}).get("tweet_count"),
#                 "verified": profile.get("verified"),
#             }
#         else:
#             return {"error": "Twitter profile not found."}

#     except requests.exceptions.Timeout:
#         return {"error": "Error: Twitter API request timed out."}
#     except requests.exceptions.RequestException as e:
#         return {"error": f"Error fetching Twitter data: {str(e)}"}    

# @app.route('/kol/<name>', methods=['GET'])
# def get_kol_details(name):
#     wiki_data = scrape_wikipedia_kol(name)
#     pubmed_data = fetch_pubmed_data(name)
#     scholar_data = fetch_google_scholar_data(name)
#     twitter_data=fetch_twitter_profile(name)

#     return jsonify({
#         "Wikipedia": wiki_data,
#         "PubMed": pubmed_data,
#         "Google_Scholar": scholar_data,
#         "twitter":twitter_data
#     })

# if __name__ == '__main__':
#     app.run(debug=True)



import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from scholarly import scholarly
import os
TWITTER_BEARER_TOKEN = "your_token"

def scrape_wikipedia_kol(name):
    url = f"https://en.wikipedia.org/wiki/{name.replace(' ', '_')}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Page not found or request failed"}

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Initialize the details dictionary with basic info
    details = {"name": name, "url": url, "achievements": []}
    
    # Scrape infobox details
    infobox = soup.find("table", {"class": "infobox"})
    if infobox:
        for row in infobox.find_all("tr"):
            header = row.find("th")
            value = row.find("td")
            if header and value:
                details[header.text.strip()] = value.text.strip()
    
    # Scrape content sections (e.g., 'Career', 'Personal Life', etc.)
    content_sections = soup.find_all("h2")
    sections_data = {}
    
    for section in content_sections:
        section_title = section.text.replace("[edit]", "").strip()
        paragraphs = []
        
        for sibling in section.find_next_siblings():
            if sibling.name in ["h2", "h3"]:  # Stop at the next major heading
                break
            if sibling.name == "p":
                paragraphs.append(sibling.text.strip())
        
        if paragraphs:
            sections_data[section_title] = " ".join(paragraphs)
    
    # Add sections to details only if they contain data
    if sections_data:
        details["sections"] = sections_data
    
    # Scrape Achievements if present in a specific section (e.g., 'Achievements')
    achievements_section = None
    
    for header in soup.find_all(["h2", "h3"]):
        if "Achievements" in header.get_text():
            achievements_section = header
            break
    
    if achievements_section:
        achievements = []
        ul = achievements_section.find_next_sibling("ul")
        
        if ul:
            for li in ul.find_all("li"):
                achievements.append(li.get_text(strip=True))
        
        if not achievements:
            paragraphs = []
            for sibling in achievements_section.find_next_siblings():
                if sibling.name in ["h2", "h3"]:
                    break
                if sibling.name == "p":
                    paragraphs.append(sibling.get_text(strip=True))
            achievements = paragraphs if paragraphs else ["No achievements listed"]
        
        details["achievements"] = achievements
    
    return details

def fetch_pubmed_data(kol_name):
    """ Fetches KOL publications and their URLs from PubMed """
    # Step 1: Search PubMed for publications by the KOL
    base_url_search = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {"db": "pubmed", "term": f"{kol_name}[Author]", "retmode": "json", "retmax": 5}
    response_search = requests.get(base_url_search, params=params)
    data_search = response_search.json()

    # Get the list of PubMed IDs
    pubmed_ids = data_search.get("esearchresult", {}).get("idlist", [])
    if not pubmed_ids:
        return {}

    # Step 2: Fetch detailed publication data using the PubMed IDs
    base_url_fetch = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    pubmed_urls = []
    for pubmed_id in pubmed_ids:
        params_fetch = {
            "db": "pubmed",
            "id": pubmed_id,
            "retmode": "xml",  # we will get XML response
            "rettype": "abstract"
        }
        response_fetch = requests.get(base_url_fetch, params=params_fetch)
        if response_fetch.status_code == 200:
            # Parse XML response to extract the publication URL (PMID link)
            soup = BeautifulSoup(response_fetch.text, 'xml')
            # Extract the URL of the publication
            article_url = f"https://pubmed.ncbi.nlm.nih.gov/{pubmed_id}/"
            pubmed_urls.append(article_url)
    
    return {"Publications": pubmed_urls}

def fetch_google_scholar_data(kol_name):
    try:
        # Search for the author in Google Scholar
        search_query = scholarly.search_author(kol_name)
        author = next(search_query)
        
        # Construct the author profile with relevant fields
        author_profile = {
            "Primary Affiliation": author.get("affiliation"),
            "Areas of Interest": author.get("interests"),
            "Cited By": author.get("citedby")
        }
        
        return author_profile
    except StopIteration:
        return {"Error": "No Google Scholar profile found."}
    except Exception as e:
        return {"Error": f"Error fetching Google Scholar data: {str(e)}"}
def fetch_twitter_profile(kol_name, timeout=5):
    headers = {"Authorization": f"Bearer {os.getenv(TWITTER_BEARER_TOKEN)}"}
    search_url = f"https://api.twitter.com/2/users/by/username/{kol_name}?user.fields=description,location,public_metrics,verified"
    try:
        response = requests.get(search_url, headers=headers, timeout=timeout)
        data = response.json()
        if "data" in data:
            profile = data["data"]
            twitter_url = f"https://twitter.com/{profile.get('username')}"
            return {"Twitter": twitter_url, "Followers": profile.get("public_metrics", {}).get("followers_count"), "Following": profile.get("public_metrics", {}).get("following_count"), "Tweets": profile.get("public_metrics", {}).get("tweet_count"), "Verified": profile.get("verified")}
        else:
            return {}
    except requests.exceptions.Timeout:
        return {}
    except Exception:
        return {}

app = Flask(__name__)
@app.route('/kol/<name>', methods=['GET'])
def get_kol_details(name):
    data = {}
    data.update(scrape_wikipedia_kol(name))
    data.update(fetch_pubmed_data(name))
    data.update(fetch_google_scholar_data(name))
    data.update(fetch_twitter_profile(name))
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True,port=7000)
