import urllib.request
import json

def search_scholar(query):
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,abstract,url,year"
    req = urllib.request.Request(url, headers={"User-Agent": "ResearchScript/1.0"})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            for d in data.get("data", []):
                print(f"Title: {d.get('title')}")
                print(f"Abstract: {d.get('abstract', 'N/A')}")
                print("-" * 50)
    except Exception as e:
        print("Error:", e)

search_scholar("graph-constrained+reasoning+hallucination")
q = "agrawal+retrieval+augmented+generation+hallucination"
search_scholar(q)
