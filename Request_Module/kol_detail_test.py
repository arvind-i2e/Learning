import requests

def fetch_kol_details(kol_name, max_results=10, output_file="kol_details.txt"):
    # Step 1: Search for KOL's publications
    esearch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    esearch_params = {
        "db": "pubmed",
        "term": f"{kol_name}[Author]",
        "retmax": max_results,
        "retmode": "json",
    }
    esearch_response = requests.get(esearch_url, params=esearch_params)
    pmids = esearch_response.json().get("esearchresult", {}).get("idlist", [])

    if not pmids:
        return f"No publications found for {kol_name}."

    # Step 2: Fetch detailed publication summaries
    esummary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    esummary_params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "json",
    }
    esummary_response = requests.get(esummary_url, params=esummary_params)
    articles = esummary_response.json().get("result", {})

    # Prepare and write results to the output file
    with open(output_file, "w", encoding="utf-8") as file:
        for pmid in pmids:
            article = articles.get(pmid, {})
            title = article.get("title", "No title available")
            authors = ", ".join([author.get("name", "") for author in article.get("authors", [])])
            source = article.get("source", "Unknown Journal")
            pub_date = article.get("pubdate", "Unknown Date")

            file.write(f"PMID: {pmid}\n")
            file.write(f"Title: {title}\n")
            file.write(f"Authors: {authors}\n")
            file.write(f"Journal: {source}\n")
            file.write(f"Publication Date: {pub_date}\n")
            file.write("-" * 80 + "\n")
    
    print(f"KOL details saved to {output_file}.")

# Example usage
fetch_kol_details("Selleri L", max_results=5, output_file="kol_details.txt")
import requests

def fetch_kol_details(kol_name, max_results=10, output_file="kol_details.txt"):
    # Step 1: Search for KOL's publications
    esearch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    esearch_params = {
        "db": "pubmed",
        "term": f"{kol_name}[Author]",
        "retmax": max_results,
        "retmode": "json",
    }
    esearch_response = requests.get(esearch_url, params=esearch_params)
    pmids = esearch_response.json().get("esearchresult", {}).get("idlist", [])

    if not pmids:
        return f"No publications found for {kol_name}."

    # Step 2: Fetch detailed publication summaries
    esummary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    esummary_params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "json",
    }
    esummary_response = requests.get(esummary_url, params=esummary_params)
    articles = esummary_response.json().get("result", {})

    # Prepare results
    results = {
        "Publication History": [],
        "Affiliations": set(),
        "Collaboration Networks": {},
        "Research Impact": [],
        "Clinical Trials": []
    }

    # Prepare and write results to the output file
    with open(output_file, "w", encoding="utf-8") as file:
        for pmid in pmids:
            article = articles.get(pmid, {})
            title = article.get("title", "No title available")
            authors = [author.get("name", "") for author in article.get("authors", [])]
            source = article.get("source", "Unknown Journal")
            pub_date = article.get("pubdate", "Unknown Date")
            citations = article.get("citations", 0)  # This is a placeholder if available
            journal = article.get("source", "Unknown Journal")
            
            # Record publication history
            results["Publication History"].append(title)

            # Record affiliations
            affiliations = [aff.get("affiliation", "No affiliation") for aff in article.get("affiliation", [])]
            results["Affiliations"].update(affiliations)

            # Record collaboration networks (co-authors)
            for author in authors:
                if author != kol_name:  # Exclude the KOL name itself
                    results["Collaboration Networks"][author] = results["Collaboration Networks"].get(author, 0) + 1

            # Record research impact (journals and citations)
            results["Research Impact"].append({
                "Title": title,
                "Citations": citations,
                "Journal": journal,
                "Publication Date": pub_date
            })

            # Link clinical trials (if applicable)
            # Example: You would parse PubMed IDs and link them to clinicaltrials.gov if related.
            if "clinicaltrial" in title.lower():
                trial_link = f"https://clinicaltrials.gov/ct2/show/{pmid}"  # Example link
                results["Clinical Trials"].append(trial_link)

            # Write to file
            file.write(f"PMID: {pmid}\n")
            file.write(f"Title: {title}\n")
            file.write(f"Authors: {', '.join(authors)}\n")
            file.write(f"Journal: {journal}\n")
            file.write(f"Publication Date: {pub_date}\n")
            file.write(f"Citations: {citations}\n")
            file.write("-" * 80 + "\n")

    print(f"KOL details saved to {output_file}.")
    return results

# Example usage
kol_name = "Selleri L"
kol_data = fetch_kol_details(kol_name, max_results=5, output_file="kol_details.txt")

# For debugging purposes, print the inferred data (without file write)
print(kol_data)
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

        # Extract and return publication titles and publication dates only
        publications = []
        for pub_id in pubmed_ids:
            pub_data = details.get("result", {}).get(pub_id, {})
            publications.append({
                "title": pub_data.get("title"),
                "pub_date": pub_data.get("pubdate")
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


# Function to combine all results
def get_kol_data(kol_name):
    if not kol_name:
        return {"error": "KOL name is required"}

    # Fetch data from sources
    pubmed_data = fetch_pubmed_data(kol_name)
    wikipedia_data = fetch_wikipedia_data(kol_name)
    google_scholar_data = fetch_google_scholar_data(kol_name)

    # Combine results
    result = {
        "KOL Name": kol_name,
        "PubMed Data": pubmed_data,
        "Wikipedia Data": wikipedia_data,
        "Google Scholar Data": google_scholar_data
    }

    # Save the results to a file
    with open("kol_data.txt", "w", encoding="utf-8") as file:
        file.write(f"KOL Name: {kol_name}\n\n")
        file.write("PubMed Data:\n")
        file.write(f"{pubmed_data}\n\n")
        file.write("Wikipedia Data:\n")
        file.write(f"{wikipedia_data}\n\n")
        file.write("Google Scholar Data:\n")
        file.write(f"{google_scholar_data}\n\n")

    print("KOL data has been saved to kol_data.txt")
    return result


# Example usage
kol_name = "John LaMattina"
kol_details = get_kol_data(kol_name)
print(kol_details)


Flask-app
from flask import Flask, jsonify, request
import requests
from scholarly import scholarly
 
app = Flask(__name__)
 
# Function to fetch publication data from PubMed
def fetch_pubmed_data(kol_name):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": f"{kol_name}[Author]",
        "retmode": "json",
        "retmax": 5  # Limit results to 10
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
 
        # Extract and return publication titles and publication dates only
        publications = []
        for pub_id in pubmed_ids:
            pub_data = details.get("result", {}).get(pub_id, {})
            publications.append({
                "title": pub_data.get("title"),
                "pub_date": pub_data.get("pubdate")
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
 
# Flask API endpoint
@app.route('/get_kol_data', methods=['GET'])
def get_kol_data():
    # Get name and workplace from query parameters
    kol_name = request.args.get('name', None)
    if not kol_name:
        return jsonify({"error": "KOL name is required"}), 400
 
    # Fetch data from sources
    pubmed_data = fetch_pubmed_data(kol_name)
    wikipedia_data = fetch_wikipedia_data(kol_name)
    google_scholar_data = fetch_google_scholar_data(kol_name)
 
    # Combine results
    return jsonify({
        "KOL Name": kol_name,
        "PubMed Data": pubmed_data,
        "Wikipedia Data": wikipedia_data,
        "Google Scholar Data": google_scholar_data
    })
 
if __name__ == '__main__':
    app.run(debug=True)