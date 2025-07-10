def is_non_academic(affiliation: str) -> bool:
    affiliation = affiliation.lower()
    academic = ["university", "institute", "college", "school", "hospital", "clinic", "centre", "center"]
    company = [
                "pharma", "biotech", "gmbh", "inc", "corp", "ltd", "llc", "company",
                "pfizer", "moderna", "astrazeneca", "biontech", "gsk", "novartis", "roche",
                "sanofi", "abbvie", "merck", "lilly", "bayer", "takeda", "teva", "biogen"
            ]
    return any(word in affiliation for word in company) and not any(word in affiliation for word in academic)
