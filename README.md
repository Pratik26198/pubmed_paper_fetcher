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

# **5.3 Add Version Control with GitHub**

## **1️⃣ Initialize a Git Repository**
If not already done:
```bash
git init
```

## **2️⃣ Add and Commit Changes**
```bash
git add .
git commit -m "Initial project structure and CLI implementation"
```

## **3️⃣ Create a GitHub Repository**
1. Go to GitHub.
2. Name the repository `pubmed_paper_fetcher`.
3. Copy the repo URL.

## **4️⃣ Link and Push to GitHub**
```bash
git remote add origin <your-repo-url>
git branch -M main
git push -u origin main
