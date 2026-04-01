import re
import json

# Read references.bib
with open('references.bib', 'r') as f:
    bib_content = f.read()

# Extract bib entries (naive regex for title and arxiv id)
entries = {}
current_match = None
for match in re.finditer(r'@\w+\{([^,]+),', bib_content):
    key = match.group(1).strip()
    start = match.end()
    
    # find next @ or end of file
    next_match = re.search(r'\n@\w+\{', bib_content[start:])
    end = start + next_match.start() if next_match else len(bib_content)
    
    body = bib_content[start:end]
    
    title_m = re.search(r'title\s*=\s*[\{"](.+?)[\}"]', body, re.IGNORECASE | re.DOTALL)
    if title_m:
        title = title_m.group(1).replace('\n', ' ').strip()
        # simplified cleanup
        title = re.sub(r'\s+', ' ', title)
        entries[key] = {'title': title, 'body': body}

# Read index.html
with open('papers/index.html', 'r') as f:
    html_content = f.read()

# Try to extract the papers array
papers_str_m = re.search(r'const papers = (\[.*?\]);', html_content, re.DOTALL)
existing_titles = []
if papers_str_m:
    papers_str = papers_str_m.group(1)
    # just regex titles
    for t_m in re.finditer(r'title:\s*"(.*?)"', papers_str):
        existing_titles.append(t_m.group(1).lower())

missing = []
for k, v in entries.items():
    if v['title'].lower() not in existing_titles:
        missing.append((k, v['title'], v['body']))

print(f"Total bib entries: {len(entries)}")
print(f"Total existing in index.html: {len(existing_titles)}")
print(f"Missing: {len(missing)}")
for k, t, b in missing[:5]:
    print(f"- {k}: {t}")

