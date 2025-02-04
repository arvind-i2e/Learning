# import requests
# from bs4 import BeautifulSoup
# from scholarly import scholarly
# import urllib.parse

# # Function to fetch data from Google Scholar
# def fetch_google_scholar_data(kol_name):
#     try:
#         # Search for the author in Google Scholar
#         search_query = scholarly.search_author(kol_name)
#         author = next(search_query)
        
#         # Construct the author profile with relevant fields
#         author_profile = {
#             "Primary Affiliation": author.get("affiliation"),
#             "Areas of Interest": author.get("interests"),
#             "Cited By": author.get("citedby"),
#             "Publications": [
#                 {"Title": pub.get("bib", {}).get("title"), "Year": pub.get("bib", {}).get("pub_year")}
#                 for pub in scholarly.fill(author)["publications"][:5]  # Get the first 5 publications
#             ]
#         }
        
#         return author_profile
#     except StopIteration:
#         return {"Error": "No Google Scholar profile found."}
#     except Exception as e:
#         return {"Error": f"Error fetching Google Scholar data: {str(e)}"}

# # Function to scrape metadata from Wikipedia
# def scrape_wikipedia_kol(name):
#     """ Scrapes metadata from a KOL's Wikipedia page """
#     url_name = urllib.parse.quote(name.replace(' ', '_'))
#     url = f"https://en.wikipedia.org/wiki/{url_name}"
#     response = requests.get(url, allow_redirects=True)
    
#     if response.status_code != 200:
#         return {"Error": f"Failed to fetch Wikipedia page. Status code: {response.status_code}"}

#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Extract data from the infobox, if available
#     infobox = soup.find("table", {"class": "infobox"})
#     if not infobox:
#         return {"Error": "No infobox found on Wikipedia page."}

#     data = {}
#     # Example of scraping specific fields from the infobox
#     for row in infobox.find_all("tr"):
#         th = row.find("th")
#         td = row.find("td")
        
#         if th and td:
#             th_text = th.get_text(strip=True)
#             td_text = td.get_text(strip=True)
            
#             # Map these fields to your data structure
#             if "Born" in th_text:
#                 data["Date of Birth"] = td_text
#             elif "Nationality" in th_text:
#                 data["Nationality"] = td_text
#             elif "Occupation" in th_text:
#                 data["Occupation"] = td_text
#             elif "Alma mater" in th_text:
#                 data["Education"] = td_text
#             elif "Known for" in th_text:
#                 data["Known For"] = td_text
#             # Add more fields as needed based on the Wikipedia infobox

#     # Add Professional Summary from the Wikipedia page
#     summary = soup.find("div", {"class": "reflist"})
#     if summary:
#         data["Professional Summary"] = summary.get_text(strip=True)
#     else:
#         data["Professional Summary"] = "No summary available"

#     return data

# # Main function to get combined data from Google Scholar and Wikipedia
# def get_kol_details(kol_name):
#     google_scholar_data = fetch_google_scholar_data(kol_name)
#     wikipedia_data = scrape_wikipedia_kol(kol_name)

#     # Merge data from both sources
#     kol_data = {**wikipedia_data, **google_scholar_data}
#     return kol_data

# # Example Usage
# kol_name = "Jitendra Kumar Singh"  # Replace with any name you want to search
# kol_details = get_kol_details(kol_name)
# print(kol_details)


## flask app
import requests
from bs4 import BeautifulSoup
from scholarly import scholarly
import urllib.parse
from flask import Flask, jsonify

app = Flask(__name__)

# Function to fetch data from Google Scholar
def fetch_google_scholar_data(kol_name):
    try:
        # Search for the author in Google Scholar
        search_query = scholarly.search_author(kol_name)
        author = next(search_query)
        
        # Construct the author profile with relevant fields
        author_profile = {
            "Primary Affiliation": author.get("affiliation"),
            "Areas of Interest": author.get("interests"),
            "Cited By": author.get("citedby"),
            "Publications": [
                {"Title": pub.get("bib", {}).get("title"), "Year": pub.get("bib", {}).get("pub_year")}
                for pub in scholarly.fill(author)["publications"][:5]  # Get the first 5 publications
            ]
        }
        
        return author_profile
    except StopIteration:
        return {"Error": "No Google Scholar profile found."}
    except Exception as e:
        return {"Error": f"Error fetching Google Scholar data: {str(e)}"}

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

# Main function to get combined data from Google Scholar and Wikipedia
@app.route('/kol/<string:kol_name>', methods=['GET'])
def get_kol_details(kol_name):
    google_scholar_data = fetch_google_scholar_data(kol_name)
    wikipedia_data = scrape_wikipedia_kol(kol_name)

    # Merge data from both sources
    kol_data = {**wikipedia_data, **google_scholar_data}
    
    return jsonify(kol_data)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, port=6000)
