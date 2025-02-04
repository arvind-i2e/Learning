import requests
from flask import Flask, jsonify
import wikipediaapi
from scholarly import scholarly

app = Flask(__name__)

# Initialize Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia(user_agent='MyFlaskApp/1.0',language='en')

# Function to fetch details from Wikipedia API
def fetch_wikipedia_data(kol_name):
    page = wiki_wiki.page(kol_name)

    if not page.exists():
        return {}

    details = {
        "First Name": "",
        "Last Name": kol_name,
        "Gender": "",
        "Qualification": "",
        "Country": "",
        "Awards": [],
        "Social Media": {"Twitter": "", "Facebook": "", "Instagram": ""}
    }

    # Extract summary (which may contain education details)
    summary = page.summary
    if "born" in summary.lower():
        born_section = summary.split("born")[1].split(".")[0]
        details["Country"] = born_section.split(",")[-1].strip()  # Extract country from birthplace

    # Extract awards from Wikipedia sections
    for section in page.sections:
        if "awards" in section.title.lower():
            details["Awards"] = [award.title for award in section.sections]

    # # Extract social media links from the page references
    # for link in page.references:
    #     if "twitter.com" in link:
    #         details["Social Media"]["Twitter"] = link
    #     elif "facebook.com" in link:
    #         details["Social Media"]["Facebook"] = link
    #     elif "instagram.com" in link:
    #         details["Social Media"]["Instagram"] = link

    return details

# Function to fetch Google Scholar Data
def fetch_google_scholar_data(kol_name):
    try:
        search_query = scholarly.search_author(kol_name)
        author = next(search_query)
        
        author_profile = {
            "Primary Affiliation": author.get("affiliation"),
            "Areas of Interest": author.get("interests"),
            "Cited By": author.get("citedby"),
            "Publications": [
                {"Title": pub.get("bib", {}).get("title"), "Year": pub.get("bib", {}).get("pub_year")}
                for pub in scholarly.fill(author)["publications"][:5]  # First 5 publications
            ]
        }
        
        return author_profile
    except StopIteration:
        return {}
    except Exception as e:
        return {"Error": f"Error fetching Google Scholar data: {str(e)}"}

# Function to fetch affiliation from PubMed E-utilities
def fetch_pubmed_affiliation(kol_name):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {"db": "pubmed", "term": f"{kol_name}[Author]", "retmode": "json", "retmax": 5}
    response = requests.get(base_url, params=params)
    data = response.json()
    pubmed_ids = data.get("esearchresult", {}).get("idlist", [])

    if not pubmed_ids:
        return None

    fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    params = {"db": "pubmed", "id": ",".join(pubmed_ids), "retmode": "json"}
    response = requests.get(fetch_url, params=params)
    data = response.json()

    affiliation = None
    for article in data.get("result", {}).values():
        if isinstance(article, dict) and "source" in article:
            affiliation = article.get("source")
            break

    return affiliation

# Function to predict gender using Genderize API
def predict_gender(first_name):
    if not first_name:
        return ""

    url = f"https://api.genderize.io/?name={first_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("gender", "")
    return ""

@app.route('/kol_metadata/<string:kol_name>', methods=['GET'])
def get_kol_metadata(kol_name):
    if not kol_name:
        return jsonify({"error": "KOL name is required"}), 400

    # Step 1: Fetch metadata from Wikipedia API
    wikipedia_data = fetch_wikipedia_data(kol_name)

    # Step 2: Fetch primary affiliation from PubMed E-utilities
    affiliation = fetch_pubmed_affiliation(kol_name)

    # Step 3: Fetch details from Google Scholar
    google_scholar_data = fetch_google_scholar_data(kol_name)

    # Step 4: Predict gender using first name from Wikipedia (if available)
    first_name = wikipedia_data.get("First Name", "")
    gender = predict_gender(first_name)

    # Fill final metadata structure
    kol_metadata = {
        "KOL Name": kol_name,
        "Salutation": "",
        "First Name": first_name,
        "Middle Name": "",
        "Last Name": wikipedia_data.get("Last Name", kol_name),
        "Gender": gender,
        "Qualification": wikipedia_data.get("Qualification", ""),
        "Primary Affiliation": affiliation if affiliation else google_scholar_data.get("Primary Affiliation", ""),
        "Department": "",
        "Title": "",
        "Address": "",
        "City": "",
        "State": "",
        "Country": wikipedia_data.get("Country", ""),
        "Last Engaged": "",
        "Phone": "",
        "Fax": "",
        "Email": "",
        "Languages": "",
        "Twitter": wikipedia_data["Social Media"].get("Twitter", ""),
        "Facebook": wikipedia_data["Social Media"].get("Facebook", ""),
        "Instagram": wikipedia_data["Social Media"].get("Instagram", ""),
        "Professional Summary": "",
        "Education": "",
        "Professional History": "",
        "Likes": "",
        "Conferences": "",
        "Awards": wikipedia_data.get("Awards", []),
        "Areas of Interests": google_scholar_data.get("Areas of Interest", []),
        "Shown Interest": "",
        "Career Status": "",
        "Speciality": ""
    }

    return jsonify(kol_metadata)

if __name__ == '__main__':
    app.run(debug=True, port=9000)
