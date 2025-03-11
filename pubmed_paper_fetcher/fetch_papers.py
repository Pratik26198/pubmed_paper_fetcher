import requests
from bs4 import BeautifulSoup
import time

# PubMed API URLs
ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def fetch_pubmed_ids(query, max_results=10):
    """ Fetch PubMed IDs based on query """
    params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": max_results}
    
    try:
        response = requests.get(ESEARCH_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("esearchresult", {}).get("idlist", [])
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching PubMed IDs: {e}")
        return []

def fetch_article_details(pubmed_ids):
    """ Fetch article details using PubMed IDs """
    if not pubmed_ids:
        return []

    params = {"db": "pubmed", "id": ",".join(pubmed_ids), "retmode": "xml"}
    
    try:
        response = requests.get(EFETCH_URL, params=params)
        response.raise_for_status()
        return response.text  # Return raw XML
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching article details: {e}")
        return ""

def parse_pubmed_xml(xml_data):
    """ Parse XML response to extract relevant details """
    soup = BeautifulSoup(xml_data, "xml")
    papers = []

    for article in soup.find_all("PubmedArticle"):
        paper_data = {}

        # Extract PubMed ID
        paper_data["PubmedID"] = article.PubmedData.ArticleIdList.find("ArticleId", {"IdType": "pubmed"}).text if article.PubmedData else "N/A"

        # Extract Title
        paper_data["Title"] = article.find("ArticleTitle").text if article.find("ArticleTitle") else "N/A"

        # Extract Publication Date
        pub_date = article.find("PubDate")
        if pub_date:
            year = pub_date.find("Year")
            month = pub_date.find("Month")
            day = pub_date.find("Day")
            paper_data["Publication Date"] = f"{year.text}-{month.text}-{day.text}" if year and month and day else "N/A"
        else:
            paper_data["Publication Date"] = "N/A"

        # Extract Author & Affiliations
        authors = []
        company_affiliations = []
        corresponding_email = "N/A"

        for author in article.find_all("Author"):
            name = f"{author.find('ForeName').text} {author.find('LastName').text}" if author.find("ForeName") and author.find("LastName") else "N/A"
            affiliation = author.find_next_sibling("AffiliationInfo")
            email = author.find("ElectronicAddress")
            
            if affiliation:
                affiliation_text = affiliation.Affiliation.text
                if is_non_academic(affiliation_text):  
                    company_affiliations.append(affiliation_text)

            if email:
                corresponding_email = email.text  # Store corresponding author email

            authors.append(name)

        paper_data["Authors"] = ", ".join(authors)
        paper_data["Company Affiliations"] = ", ".join(company_affiliations) if company_affiliations else "None"
        paper_data["Corresponding Author Email"] = corresponding_email

        papers.append(paper_data)

    return papers

def is_non_academic(affiliation):
    """ Check if an affiliation belongs to a non-academic institution """
    non_academic_keywords = ["Pharma", "Biotech", "Inc.", "Ltd.", "Corporation", "Laboratories"]
    return any(keyword in affiliation for keyword in non_academic_keywords)

if __name__ == "__main__":
    query = "cancer treatment"
    pubmed_ids = fetch_pubmed_ids(query)
    if pubmed_ids:
        xml_data = fetch_article_details(pubmed_ids)
        parsed_data = parse_pubmed_xml(xml_data)
        
        for paper in parsed_data:
            print(paper)  # Print structured metadata
