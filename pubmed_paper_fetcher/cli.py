import argparse
import pandas as pd
from fetch_papers import fetch_pubmed_ids, fetch_article_details, parse_pubmed_xml

def save_to_csv(data, filename):
    """ Save extracted paper data to a CSV file. """
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Results saved to {filename}")

def main():
    """ Command-line interface for fetching PubMed research papers. """
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", help="Search query for PubMed")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("-f", "--file", help="Save results to CSV file")

    args = parser.parse_args()

    if args.debug:
        print(f"Debug Mode: Fetching papers for query '{args.query}'")

    # Fetch PubMed IDs
    pubmed_ids = fetch_pubmed_ids(args.query)
    if not pubmed_ids:
        print("No results found.")
        return

    # Fetch and parse article details
    xml_data = fetch_article_details(pubmed_ids)
    papers = parse_pubmed_xml(xml_data)

    if args.file:
        save_to_csv(papers, args.file)
    else:
        for paper in papers:
            print(paper)  # Print result to console

if __name__ == "__main__":
    main()
