import urllib.request
import urllib.parse
import json

queries = [
    ("berant2013", "Semantic parsing on Freebase from question-answer pairs Berant 2013"),
    ("reddy2014", "Large-scale semantic parsing without question-answer pairs Reddy 2014"),
    ("bast2015", "More accurate question answering on Freebase Bast 2015"),
    ("yih2015", "Semantic parsing via staged query graph generation Yih 2015"),
    ("miller2016", "Key-value memory networks for directly reading documents Miller 2016"),
    ("xu2019", "Enhancing key-value memory neural networks for knowledge based question answering Xu 2019"),
    ("zhang2018", "Variational reasoning for question answering with knowledge graph Zhang 2018"),
    ("han2021", "Knowledge Graph-augmented Language Models Han 2021"),
    ("saxena2020", "Improving multi-hop question answering over knowledge graphs using knowledge base embeddings Saxena 2020"),
    ("han2020", "Han 2020 Question Answering Knowledge Graph text"),
    ("wang2023c", "Plan-and-Solve Prompting Wang 2023"),
    ("he2021decomp", "Measuring and narrowing the compositionality gap in language models He 2021"),
    ("wang2024b", "Self-Consistency Improves Chain of Thought Reasoning in Language Models Wang 2022"),
    ("yu2022", "Yu 2022 Language Models reasoning tasks"),
    ("hoffman2024", "Hoffman 2024 reasoning tasks large language models"),
    ("yao2022react", "ReAct: Synergizing Reasoning and Acting in Language Models Yao 2022"),
    ("sun2024tog", "Think-on-Graph: Deep and Responsible Reasoning of Large Language Model with Knowledge Graph Sun 2024"),
    ("wang2023b", "Knowledge-Driven Chain-of-Thought Wang 2023"),
    ("he2022rr", "RR: Faithful Reasoning on Knowledge Graphs He 2022"),
    ("mavromatis2024gnnrag", "GNN-RAG Graph Neural Networks for Retrieval Augmented Generation Mavromatis Karypis 2024"),
    ("luo2025gfmrag", "GFM-RAG Graph Foundation Models Retrieval Augmented Generation Luo 2025"),
    ("zhuang2024structlm", "StructLM Towards Building Generalist Models for Structured Knowledge Grounding Zhuang 2024"),
    ("markowitz2024", "Tree-of-Traversals Markowitz 2024"),
    ("jin2024graphcot", "Graph Chain-of-Thought Jin 2024")
]

with open("references_additions.bib", "a") as f:
    for key, query in queries:
        url = "https://api.crossref.org/works?query=" + urllib.parse.quote(query) + "&select=DOI&rows=1"
        req = urllib.request.Request(url, headers={'User-Agent': 'mailto:test@example.com'})
        try:
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read())
                if data['message']['items']:
                    doi = data['message']['items'][0]['DOI']
                    bib_url = "https://api.crossref.org/works/" + urllib.parse.quote(doi) + "/transform/application/x-bibtex"
                    bib_req = urllib.request.Request(bib_url, headers={'User-Agent': 'mailto:test@example.com'})
                    with urllib.request.urlopen(bib_req) as bib_res:
                        bibtex = bib_res.read().decode('utf-8')
                        
                        # Replace the bib key
                        # The crossref format is @type{original_key, ...
                        lines = bibtex.split('\n')
                        if len(lines) > 0 and lines[0].startswith('@'):
                            first_brace = lines[0].find('{')
                            lines[0] = lines[0][:first_brace+1] + key + ","
                            bibtex = '\n'.join(lines)
                        
                        f.write(bibtex + "\n\n")
                        print("Fetched", key)
                else:
                    print("No results for", key)
        except Exception as e:
            print("Failed for", key, e)
