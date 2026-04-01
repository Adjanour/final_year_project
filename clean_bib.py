import re

with open('references.bib', 'r') as f:
    content = f.read()

seen = set()
out = []
for block in re.split(r'\n@', '\n' + content)[1:]:
    if not block.strip():
        continue
    match = re.search(r'^[a-zA-Z]+\{([^,]+),', block)
    if match:
        key = match.group(1).strip()
        if key not in seen:
            seen.add(key)
            out.append('@' + block)
    else:
        out.append('@' + block)

with open('references.bib', 'w') as f:
    f.write('\n'.join(out))
