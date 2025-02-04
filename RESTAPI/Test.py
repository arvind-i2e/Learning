# import requests
# import json
# response=requests.get("http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")#Fetching questions from stack over flow through it's API
# for data in response.json()['items']:
#     if data['answer_count']==0:
#         print(data['title'])
#         print(data['link'])
#     else:
#         print("Skipped")   
#     print()     


##### Hitting by disease
import requests
from flask import Flask, jsonify
import xml.etree.ElementTree as ET

app = Flask(__name__)

def fetch_pubmed_articles(search_term, min_date, max_date):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        'db': 'pubmed',
        'term': f"{search_term}[MeSH Terms]",
        'mindate': min_date,
        'maxdate': max_date,
        'retmax': 10,
        'retmode': 'xml'
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.text
    else:
        return None

def fetch_article_summaries(pmid_list):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    params = {
        'db': 'pubmed',
        'id': ",".join(pmid_list),
        'retmode': 'xml'
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_esummary_response(xml_response):
    tree = ET.ElementTree(ET.fromstring(xml_response))
    root = tree.getroot()
    articles = []

    for docsum in root.findall("DocSum"):
        article = {}
        for item in docsum.findall("Item"):
            name = item.get("Name")
            if name == "Id":
                article["article_id"] = item.text
            elif name == "Title":
                article["article_title"] = item.text
            elif name == "Source":
                article["article_category"] = item.text
            elif name == "PubType":
                article["article_type"] = item.text
            elif name == "AuthorList":
                authors = [author.text for author in item.findall("Item")]
                article["authors"] = authors
            elif name == "PubDate":
                article["time_date"] = item.text
            elif name == "Item" and item.get("Name") == "Abstract":
                article["article_summary"] = item.text
            elif name == "Item" and item.get("Name") == "URL":
                article["web_article_url"] = item.text
        
        articles.append(article)
    
    return articles

@app.route('/fetch_articles/<search_term>', methods=['GET'])
def get_articles(search_term):
    min_date = '2018'
    max_date = '2023'

    esearch_response = fetch_pubmed_articles(search_term, min_date, max_date)
    
    if not esearch_response:
        return jsonify({"status": "error", "message": "Failed to fetch articles from PubMed"}), 500

    tree = ET.ElementTree(ET.fromstring(esearch_response))
    root = tree.getroot()

    pmid_list = [id.text for id in root.findall(".//Id")]
    
    if not pmid_list:
        return jsonify({"status": "error", "message": "No articles found"}), 404

    esummary_response = fetch_article_summaries(pmid_list)
    
    if not esummary_response:
        return jsonify({"status": "error", "message": "Failed to fetch article summaries"}), 500

    articles = parse_esummary_response(esummary_response)

    return jsonify({"status": "success", "articles": articles}), 200

if __name__ == '__main__':
    app.run(debug=True)
