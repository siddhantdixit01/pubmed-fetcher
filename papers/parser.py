from typing import List, Tuple
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
from .utils import is_non_academic
import warnings

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
def parse_papers(xml_data: str) -> List[dict]:
    soup = BeautifulSoup(xml_data, "lxml")
    articles = soup.find_all("pubmedarticle")
    results = []

    for article in articles:
        pmid = article.pmid.text if article.pmid else ""
        title = article.articletitle.text if article.articletitle else ""
        pub_date = extract_pub_date(article)
        authors, companies, emails = extract_non_academic_authors(article)

        if not companies:
            continue

        results.append({
            "PubmedID": pmid,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": "; ".join(authors),
            "Company Affiliation(s)": "; ".join(companies),
            "Corresponding Author Email": "; ".join(emails),
        })
    return results

def extract_pub_date(article) -> str:
    try:
        date = article.find("pubdate")
        year = date.find("year").text if date.find("year") else ""
        month = date.find("month").text if date.find("month") else ""
        return f"{month} {year}".strip()
    except Exception:
        return ""

def extract_non_academic_authors(article) -> Tuple[List[str], List[str], List[str]]:
    authors, companies, emails = [], [], []
    for author in article.find_all("author"):
        aff = author.find("affiliation")
        if aff and is_non_academic(aff.text):
            name = f"{author.find('lastname').text if author.find('lastname') else ''} {author.find('firstname').text if author.find('firstname') else ''}".strip()
            authors.append(name)
            companies.append(aff.text)
            if "@" in aff.text:
                emails.append(aff.text.split()[-1])
    return authors, companies, emails
