# PubMed Fetcher CLI

A command-line Python program that fetches PubMed research papers based on a user-specified query and returns papers that include **at least one author affiliated with a pharmaceutical or biotech company**. Results can be printed to the console or saved to a CSV file.

---

## 📝 Task Description

The goal of this tool is to search PubMed using a flexible query, identify papers with **non-academic authors**, and extract relevant metadata into a structured format.

---

## 📚 Problem Details

### 1. Source of Papers
- Fetch papers using the official **[PubMed API (E-Utilities)](https://www.ncbi.nlm.nih.gov/books/NBK25500/)**.
- Supports **full PubMed query syntax**.

### 2. Output Requirements

The tool returns the following columns:

| Column                     | Description                                               |
|---------------------------|-----------------------------------------------------------|
| `PubmedID`                | Unique identifier for the paper                           |
| `Title`                   | Title of the paper                                        |
| `Publication Date`        | Date the paper was published                              |
| `Non-academic Author(s)`  | Authors affiliated with non-academic institutions         |
| `Company Affiliation(s)`  | Names of pharma/biotech companies in the affiliations      |
| `Corresponding Author Email` | Email of the corresponding author (if available)      |

---

## 💻 Command-Line Interface Features

```bash
poetry run get-papers-list "<query>" [OPTIONS]
```

### Required:
- `query` (string): A PubMed-compatible search term.

### Options:
| Flag                     | Description                                  |
|--------------------------|----------------------------------------------|
| `-h`, `--help`           | Show help and usage instructions             |
| `-d`, `--debug`          | Print debug logs during execution            |
| `-f`, `--file <filename>`| Save results to the specified CSV file       |

### Example Usages

```bash
# Basic search (output to console)
poetry run get-papers-list "CRISPR cancer therapy"

# Save output to CSV
poetry run get-papers-list "COVID-19 vaccine" -f results.csv

# Enable debug logging
poetry run get-papers-list "mRNA vaccine" --debug
```

---

## 🧱 Code Organization & Environment

### 🔗 Version Control
- Managed via **Git** and hosted on **GitHub**.

### 📦 Dependency Management
- All dependencies managed using **[Poetry](https://python-poetry.org/)**.
- To install dependencies:

```bash
poetry install
```

### ⚙️ Execution
- A CLI command `get-papers-list` is exposed via Poetry:

```toml
[tool.poetry.scripts]
get-papers-list = "cli:main"
```

---

## 🧩 Code Structure

```bash
pubmed-fetcher/
├── cli.py                  # Entry-point CLI using Typer
├── papers/
│   ├── __init__.py
│   ├── client.py           # Handles PubMed API requests
│   ├── parser.py           # Parses XML and extracts required fields
│   └── utils.py            # Heuristics to identify non-academic authors
├── pyproject.toml          # Poetry config
├── README.md
```

---

## 🔍 Identification Heuristics

To detect non-academic authors:
- Affiliations are scanned for **pharma/biotech company terms** like:
  - `pharma`, `biotech`, `inc`, `corp`, `gmbh`, `llc`, `company`, etc.
- Academic affiliations are filtered out using terms like:
  - `university`, `institute`, `college`, `hospital`, `clinic`, `center`, etc.
- Email patterns (e.g., missing `.edu` or `.ac`) are also considered.

---

## 🔧 Tools & Libraries Used

- [Poetry](https://python-poetry.org/) — dependency management and packaging
- [Typer](https://typer.tiangolo.com/) — CLI framework
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) — XML parsing
- [Requests](https://docs.python-requests.org/) — HTTP client
- [PubMed API](https://www.ncbi.nlm.nih.gov/books/NBK25500/) — data source

---

## ✅ Evaluation Criteria

### Functional:
- Fetches papers via PubMed API
- Filters authors with company affiliations
- Outputs correct CSV format

### Non-Functional:
- Fully typed Python code using `mypy`-friendly annotations
- Efficient API usage and XML parsing
- Readable and modular code with docstrings
- Handles invalid queries, missing data, and HTTP errors gracefully

---

## 👤 Author

Made by **Siddhant Dixit**  
For queries or collaboration, feel free to reach out.