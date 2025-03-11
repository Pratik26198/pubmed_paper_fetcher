import pytest
from pubmed_paper_fetcher.fetch_papers import fetch_pubmed_ids, is_non_academic

def test_fetch_pubmed_ids():
    query = "cancer treatment"
    pubmed_ids = fetch_pubmed_ids(query, max_results=2)
    assert isinstance(pubmed_ids, list)
    assert len(pubmed_ids) > 0

def test_is_non_academic():
    assert is_non_academic("XYZ Pharma Inc.") == True
    assert is_non_academic("Harvard University") == False
