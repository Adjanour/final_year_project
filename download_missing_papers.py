import re
import os
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
import json

def get_arxiv_data(title):
    query = urllib.parse.quote(f'ti:"{title}"')
    url = f'http://export.arxiv.org/api/query?search_query={query}&start=0&max_results=1'
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            xml_data = response.read()
            root = ET.fromstring(xml_data)
            entry = root.find('{http://www.w3.org/2005/Atom}entry')
            if entry is not None:
                title_elem = entry.find('{http://www.w3.org/2005/Atom}title')
                summary_elem = entry.find('{http://www.w3.org/2005/Atom}summary')
                
                found_title = title_elem.text.replace('\n', ' ').strip().lower()
                clean_title = title.lower().replace('\n', ' ').strip()
                if clean_title[:20] in found_title or found_title[:20] in clean_title:
                    pdf_link = None
                    for link in entry.findall('{http://www.w3.org/2005/Atom}link'):
                        if link.attrib.get('title') == 'pdf':
                            pdf_link = link.attrib.get('href')
                            break
                    if not pdf_link:
                        for link in entry.findall('{http://www.w3.org/2005/Atom}link'):
                            if link.attrib.get('type') == 'application/pdf':
                                pdf_link = link.attrib.get('href')
                                break
                    if pdf_link:
                        pdf_link = pdf_link.replace('http://', 'https://')
                        if not pdf_link.endswith('.pdf'):
                            pdf_link += '.pdf'
                        return pdf_link, summary_elem.text.replace('\n', ' ').strip()
    except Exception as e:
        pass
    return None, None

def process_paper(k, v):
    title = v['title']
    print(f"Processing: {title[:50]}...")
    
    pdf_link, summary = get_arxiv_data(title)
    
    filename = f"{k}.pdf"
    filepath = os.path.join('papers', filename)
    file_prop = "null"
    
    if pdf_link:
        try:
            req = urllib.request.Request(pdf_link, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                with open(filepath, 'wb') as out_f:
                    out_f.write(response.read())
            file_prop = f'"{filename}"'
            print(f" -> OK {filename}")
        except Exception as e:
            summary = "Metadata only. PDF download failed."
            print(f" -> FAIL {filename}")
    else:
        summary = "Metadata only. PDF not found on ArXiv."
        print(f" -> NO MATCH {filename}")
        
    if not summary:
        summary = "Metadata only."

    esc_title = title.replace('"', '\\"')
    esc_cit = v['citation'].replace('"', '\\"')
    esc_sum = summary.replace('"', '\\"').replace('\n', ' ')
    topic = "Other"
    tags = "[\"auto-imported\"]"
    
    return f'''
        {{
          title: "{esc_title}",
          citation: "{esc_cit}",
          summary: "{esc_sum}",
          topic: "{topic}",
          tags: {tags},
          file: {file_prop}
        }}'''

def main():
    with open('references.bib', 'r') as f:
        bib_content = f.read()

    entries = {}
    for match in re.finditer(r'@(\w+)\{([^,]+),', bib_content):
        entry_type = match.group(1).strip()
        key = match.group(2).strip()
        
        start = match.end()
        next_match = re.search(r'\n@\w+\{', bib_content[start:])
        end = start + next_match.start() if next_match else len(bib_content)
        body = bib_content[start:end]
        
        title_m = re.search(r'title\s*=\s*[\{"](.+?)[\}"]', body, re.IGNORECASE | re.DOTALL)
        if title_m:
            title = title_m.group(1).replace('\n', ' ').strip()
            title = re.sub(r'\s+', ' ', title).replace('{', '').replace('}', '')
            
            author = "Unknown"
            author_m = re.search(r'author\s*=\s*[\{"](.+?)[\}"]', body, re.IGNORECASE | re.DOTALL)
            if author_m:
                author = author_m.group(1).replace('\n', ' ').strip()
                author = re.sub(r'\s+', ' ', author)
                
            year = ""
            year_m = re.search(r'year\s*=\s*[\{"](\d+)[\}"]', body, re.IGNORECASE)
            if year_m:
                year = f" - {year_m.group(1)}"
                
            entries[key] = {
                'title': title,
                'citation': f"{author}{year}",
                'body': body
            }

    with open('papers/index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    papers_str_m = re.search(r'const papers = \[(.*?)\n      \];', html_content, re.DOTALL)
    if not papers_str_m:
        print("Error: Could not find papers array in index.html")
        return
        
    existing_titles = set()
    for t_m in re.finditer(r'title:\s*"(.*?)"', papers_str_m.group(1)):
        existing_titles.add(t_m.group(1).lower().strip())

    missing = {k: v for k, v in entries.items() if v['title'].lower().strip() not in existing_titles}
    print(f"Found {len(missing)} missing papers to process.")

    new_entries_js = []
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(lambda item: process_paper(item[0], item[1]), missing.items())
        new_entries_js = list(results)

    if new_entries_js:
        insert_pos = papers_str_m.end(1)
        new_content = html_content[:insert_pos]
        if not html_content[insert_pos-1].isspace() and html_content[insert_pos-2:insert_pos] != ',\n':
            new_content += ","
            
        new_content += "," + ",".join(new_entries_js)
        new_content += html_content[insert_pos:]
        
        with open('papers/index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Done! index.html updated.")

if __name__ == "__main__":
    main()
