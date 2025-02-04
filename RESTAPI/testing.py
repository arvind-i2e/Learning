import requests

def format_kol_name(kol_name):
    # Split the full name into parts
    name_parts = kol_name.strip().split()
    
    # If there are two parts (first and last name)
    if len(name_parts) == 2:
        return f"{name_parts[1]} {name_parts[0][0]}"  # Surname Initial

    # If there are more than two parts (first, middle, last name)
    elif len(name_parts) > 2:
        return f"{name_parts[2]} {name_parts[0][0]} {name_parts[1][0]}"  # Last Name Initials for first and middle names

    return kol_name  # In case of an unexpected format

def fetch_pubmed_articles(kol_name):
    # Format the name for PubMed search
    formatted_name = format_kol_name(kol_name)
    
    # Format the E-utilities search URL for PubMed
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": formatted_name,
        "retmode": "json",
        "retmax": 5
    }
    
    # Make the API request
    response = requests.get(base_url, params=params)
    data = response.json()
    
    # Extract the PubMed IDs from the response
    pubmed_ids = data.get("esearchresult", {}).get("idlist", [])
    if pubmed_ids:
        pubmed_id = pubmed_ids[0]
        print(f"Found PubMed ID: {pubmed_id}")
        
        # Use efetch to retrieve article details
        fetch_articles(pubmed_id)
    else:
        print("No PubMed results found.")

def fetch_articles(pubmed_id):
    # Use the efetch endpoint to retrieve details about the articles for the given PubMed ID
    efetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": pubmed_id,
        "retmode": "xml"  # We can use XML to get more structured results
    }
    
    response = requests.get(efetch_url, params=params)
    
    if response.status_code == 200:
        # Parse the XML data to extract relevant details
        print("Article details fetched successfully.")
        
        # Here, you can parse the XML to get article titles, authors, dates, etc.
        # For example, you can extract the titles and authors:
        from xml.etree import ElementTree
        tree = ElementTree.fromstring(response.content)
        
        # Loop through the XML to get article details
        for docsum in tree.findall(".//DocSum"):
            title = docsum.find(".//Item[@Name='Title']").text
            authors = docsum.find(".//Item[@Name='AuthorList']").text
            source = docsum.find(".//Item[@Name='Source']").text
            pub_date = docsum.find(".//Item[@Name='PubDate']").text
            
            print(f"Title: {title}")
            print(f"Authors: {authors}")
            print(f"Source: {source}")
            print(f"Publication Date: {pub_date}")
    else:
        print(f"Failed to fetch articles for PubMed ID: {pubmed_id}")

# Example usage
kol_name = "Jitendra Kumar Singh"
fetch_pubmed_articles(kol_name)
