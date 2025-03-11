# PubMed Paper Fetcher

A Python CLI tool to fetch research papers from PubMed, filter results based on company affiliations, and export them to CSV.

## Features
✅ Fetches papers using PubMed API  
✅ Filters non-academic affiliations (Pharma/Biotech)  
✅ Saves results to a CSV file  
✅ Command-line interface with options  

## Installation

### Using Poetry:
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd pubmed_paper_fetcher
   ```
2. Install dependencies:
   ```bash
   poetry install
   ```
3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

## Usage

### Run the CLI:
```bash
poetry run get-papers-list "cancer treatment"
```

### Save to CSV:
```bash
poetry run get-papers-list "cancer treatment" -f results.csv
```

### Debug Mode:
```bash
poetry run get-papers-list "cancer treatment" -d
```

## Development

### Running Tests
```bash
poetry run pytest
```

## Contributing
1. Fork the repo.
2. Create a new branch.
3. Make changes and push.
4. Submit a Pull Request.

---

