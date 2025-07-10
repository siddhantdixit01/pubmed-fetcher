import typer
from papers.client import search_pubmed, fetch_details
from papers.parser import parse_papers
import csv

app = typer.Typer()

@app.command()
def get_papers_list(
    query: str,
    file: str = typer.Option(None, "-f", "--file", help="CSV output file name"),
    debug: bool = typer.Option(False, "-d", "--debug", help="Print debug logs"),
):
    if debug:
        print(f"Searching PubMed for: {query}")
    ids = search_pubmed(query)
    if debug:
        print(f"Found {len(ids)} papers. Fetching details...")

    xml_data = fetch_details(ids)
    results = parse_papers(xml_data)

    if not results:
        print("No papers found with non-academic authors.")
        return

    if file:
        with open(file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
        print(f"Saved {len(results)} results to {file}")
    else:
        for r in results:
            print(r)


def main():
    app()

if __name__ == "__main__":
    main()
