from typing import List
import requests

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

def search_pubmed(query: str) -> List[str]:
    resp = requests.get(f"{BASE_URL}/esearch.fcgi", params={
        "db": "pubmed", "term": query, "retmode": "json", "retmax": 20
    })
    resp.raise_for_status()
    return resp.json()["esearchresult"]["idlist"]

def fetch_details(pubmed_ids: List[str]) -> str:
    if not pubmed_ids:
        return ""
    resp = requests.get(f"{BASE_URL}/efetch.fcgi", params={
        "db": "pubmed", "id": ",".join(pubmed_ids), "retmode": "xml"
    })
    resp.raise_for_status()
    return resp.text
