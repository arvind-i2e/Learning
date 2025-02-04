from flask import Flask, request, jsonify
import requests
from scholarly import scholarly
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

app = Flask(__name__)

# PubMed API base URL
PUBMED_EUTILS_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

# General function for handling API requests
def fetch_api_data(url, params=None, headers=None):
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json() if response.status_code == 200 else None
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

# Function to fetch primary affiliation from PubMed using esearch and efetch
def fetch_pubmed_affiliation(kol_name):
    esearch_url = f"{PUBMED_EUTILS_BASE}esearch.fcgi?db=pubmed&term={kol_name}&retmode=json"
    esearch_response = fetch_api_data(esearch_url)
    
    if esearch_response and "esearchresult" in esearch_response and "idlist" in esearch_response["esearchresult"]:
        article_ids = esearch_response["esearchresult"]["idlist"]
        if article_ids:
            efetch_url = f"{PUBMED_EUTILS_BASE}efetch.fcgi?db=pubmed&id={article_ids[0]}&retmode=xml"
            efetch_response = requests.get(efetch_url).text
            root = ET.fromstring(efetch_response)
            affiliation = root.find(".//Affiliation")
            return affiliation.text if affiliation is not None else "Affiliation not found"
    
    return "Affiliation not found"

# Function to fetch KOL data from Google Knowledge Graph API
def fetch_google_kg(kol_name):
    GOOGLE_KG_API_KEY = "your_key"
    google_kg_url = f"https://kgsearch.googleapis.com/v1/entities:search?query={kol_name.replace(' ','%20')}&key={GOOGLE_KG_API_KEY}&limit=1&indent=True"
    response = fetch_api_data(google_kg_url)
    
    if response and "itemListElement" in response and len(response["itemListElement"]) > 0:
        entity = response["itemListElement"][0]["result"]
        return {
            "name": entity.get("name", kol_name),
            "Title": entity.get("description", "N/A"),
            "detailedDescription": entity.get("detailedDescription", {}).get("articleBody", "N/A"),
            "url": entity.get("url", "N/A")
        }
    
    return {"name": kol_name, "description": "N/A"}
def extract_name_parts(full_name):
    # List of common salutations
    salutations = ["Dr.", "Prof.", "Mr.", "Ms.", "Mrs.", "Mx.", "Rev."]
    
    # Split the full name into parts
    name_parts = full_name.strip().split()
    
    # Default to empty salutation, first name, and last name
    salutation = ""
    first_name = ""
    last_name = ""
    
    # Check if the first part is a salutation
    if name_parts[0] in salutations:
        salutation = name_parts[0]
        name_parts = name_parts[1:]  # Remove salutation from name parts
    
    # If the name has more than one part, split the first name and last name
    if len(name_parts) >= 2:
        first_name = name_parts[0]
        last_name = " ".join(name_parts[1:])
    elif len(name_parts) == 1:
        first_name = name_parts[0]
    
    return salutation, first_name, last_name
# Function to fetch Google Scholar profile
def fetch_google_scholar(kol_name):
    # Search for the author by name using scholarly
    search_query = scholarly.search_author(kol_name)
    author = next(search_query, None)  # Get the first result (if exists)
    
    if author:
        # Fetch full details of the author
        author_details = scholarly.fill(author)
        full_name = author_details.get("name", "N/A")
        salutation, first_name, last_name = extract_name_parts(full_name)
        email = author_details.get("email_domain", "N/A")
        # Extract available metadata (we'll filter what is available)
        metadata = {
            "name": full_name,
            "salutation": salutation,
            "first_name": first_name,
            "last_name": last_name,
            "primary_affiliation": author_details.get("affiliation", "N/A"),
            "citations": author_details.get("citedby", "N/A"),
            "h_index": author_details.get("hindex", "N/A"),
            "i10_index": author_details.get("i10index", "N/A"),
            "areas_of_interest": author_details.get("interests", "N/A"),
            "url": author_details.get("url", "N/A"),
            "email": email # Adding email to the metadata
        }

        return metadata
    
    return {
        "name": kol_name,
        "salutation": "N/A",
        "first_name": "N/A",
        "last_name": "N/A",
        "primary_affiliation": "N/A",
        "citations": "N/A",
        "h_index": "N/A",
        "i10_index": "N/A",
        "areas_of_interest": "N/A",
        "url": "N/A",
        "email": "N/A"
    }
# Function to fetch Wikipedia data (Updated to use provided API)
def fetch_wikipedia(kol_name):
    wikipedia_url = f"https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles={kol_name.replace(' ', '%20')}"
    response = fetch_api_data(wikipedia_url)
    if response and "query" in response and "pages" in response["query"]:
        pages = response["query"]["pages"]
        for page_id, page in pages.items():
            if "extract" in page:
                # Now, we will get the 'curid' (page id) and fetch detailed information by scraping the page
                curid = page_id
                wikipedia_page_url = f"https://en.wikipedia.org/?curid={curid}"
                page_response = requests.get(wikipedia_page_url)
                
                if page_response.status_code == 200:
                    soup = BeautifulSoup(page_response.text, 'html.parser')
                    infobox = soup.find('table', {'class': 'infobox'})

                    # Extract details from the infobox
                    born = occupation = awards = website = "N/A"
                    
                    if infobox:
                        rows = infobox.find_all('tr')
                        for row in rows:
                            header = row.find('th')
                            if header:
                                header_text = header.get_text().strip()
                                if header_text == "Born":
                                    born = row.find('td').get_text().strip()
                                elif header_text == "Occupation":
                                    occupation = row.find('td').get_text().strip()
                                elif header_text == "Awards":
                                    awards = row.find('td').get_text().strip()
                                elif header_text == "Website":
                                    website = row.find('td').get_text().strip()

                    return {
                        "summary": page["extract"],
                        "url": wikipedia_page_url,
                        "born": born,
                        "occupation": occupation,
                        "awards": awards,
                        "website": website
                    }

    return {"summary": "No Wikipedia page found", "url": "N/A", "born": "N/A", "occupation": "N/A", "awards": "N/A", "website": "N/A"}

@app.route('/kol', methods=['GET'])
def get_kol_metadata():
    kol_name = request.args.get('name')
    if not kol_name:
        return jsonify({"error": "KOL name is required"}), 400
    
    affiliation = fetch_pubmed_affiliation(kol_name)
    google_kg_data = fetch_google_kg(kol_name)
    scholar_data = fetch_google_scholar(kol_name)
    wikipedia_data = fetch_wikipedia(kol_name)
    
    # Combine metadata while ensuring no duplicates
    metadata = {
        "name": kol_name,
        "primary_affiliation": affiliation,
        "google_kg": google_kg_data,
        "google_scholar": scholar_data if scholar_data else {"error": "No data found"},
        "wikipedia": wikipedia_data
    }
    
    return jsonify(metadata)

if __name__ == '__main__':
    app.run(debug=True,port=12000)
