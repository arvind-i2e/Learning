from flask import Flask, jsonify
import requests
from scholarly import scholarly

app = Flask(__name__)

# Function to fetch affiliation from PubMed
def fetch_pubmed_affiliation(kol_name):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {"db": "pubmed", "term": f"{kol_name}[Author]", "retmode": "json", "retmax": 1}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        pubmed_ids = data.get("esearchresult", {}).get("idlist", [])
        if pubmed_ids:
            pubmed_id = pubmed_ids[0]
            return fetch_pubmed_publication_details(pubmed_id)
    return {"affiliation": "Not Available"}

def fetch_pubmed_publication_details(pubmed_id):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    params = {"db": "pubmed", "id": pubmed_id, "retmode": "json"}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        docsum = data.get("result", {}).get(pubmed_id, {})
        affiliation = docsum.get("author", [])
        return {"affiliation": affiliation if affiliation else "Not Available"}
    return {"affiliation": "Not Available"}

# Function to fetch data from Google Scholar
def fetch_google_scholar_data(kol_name, affiliation):
    try:
        search_query = scholarly.search_author(kol_name)
        author = next(search_query)
        
        # Handling if 'affiliation' is a list or string
        author_affiliation = author.get("affiliation", "")
        if isinstance(author_affiliation, list):
            # If affiliation is a list, check if any of the list items match the provided affiliation
            if any(affil.lower() in affiliation.lower() for affil in author_affiliation):
                author_profile = {
                    "name": author.get("name"),
                    "first_name": author.get("name").split()[0],
                    "last_name": author.get("name").split()[-1],
                    "middle_name": author.get("name").split()[1] if len(author.get("name").split()) > 2 else "",
                    "affiliation": author_affiliation,
                    "interests": author.get("interests"),
                    "cited_by": author.get("citedby"),
                    "publications": [
                        {"title": pub.get("bib", {}).get("title"), "year": pub.get("bib", {}).get("pub_year")}
                        for pub in scholarly.fill(author)["publications"][:5]  # Limit to first 5 publications
                    ]
                }
                # Adding additional fields for gender, salutation, specialty if possible
                author_profile["salutation"] = "Not Available"
                author_profile["gender"] = "Not Available"
                author_profile["specialty"] = "Not Available"  # Could be extracted from "interests"
                return author_profile
        elif isinstance(author_affiliation, str):
            # If affiliation is a string, check if it matches
            if affiliation.lower() in author_affiliation.lower():
                author_profile = {
                    "name": author.get("name"),
                    "first_name": author.get("name").split()[0],
                    "last_name": author.get("name").split()[-1],
                    "middle_name": author.get("name").split()[1] if len(author.get("name").split()) > 2 else "",
                    "affiliation": author_affiliation,
                    "interests": author.get("interests"),
                    "cited_by": author.get("citedby"),
                    "publications": [
                        {"title": pub.get("bib", {}).get("title"), "year": pub.get("bib", {}).get("pub_year")}
                        for pub in scholarly.fill(author)["publications"][:5]  # Limit to first 5 publications
                    ]
                }
                # Adding additional fields for gender, salutation, specialty if possible
                author_profile["salutation"] = "Not Available"
                author_profile["gender"] = "Not Available"
                author_profile["specialty"] = "Not Available"  # Could be extracted from "interests"
                return author_profile
        return {"error": "Affiliation does not match"}
    except StopIteration:
        return {"error": "No Google Scholar profile found."}
    except Exception as e:
        return {"error": f"Error fetching Google Scholar data: {str(e)}"}

@app.route('/kol/<name>', methods=['GET'])
def get_kol_details(name):
    # Step 1: Fetch affiliation from PubMed
    pubmed_affiliation = fetch_pubmed_affiliation(name)
    
    # Step 2: Fetch KOL metadata from Google Scholar using the PubMed affiliation
    if pubmed_affiliation.get("affiliation") != "Not Available":
        scholar_data = fetch_google_scholar_data(name, pubmed_affiliation["affiliation"])
        # Combine PubMed affiliation with Google Scholar data
        scholar_data.update(pubmed_affiliation)
        return jsonify(scholar_data)
    else:
        return jsonify({"error": "Affiliation not found in PubMed or Google Scholar data unavailable."})

if __name__ == '__main__':
    app.run(debug=True, port=4000)
