import os
import re
import json

TEXTS_DIR = r"C:\Users\oladi\.gemini\antigravity-ide\brain\f32186c3-d5d3-4508-a451-07c97b6872f1\scratch\texts"
OUTPUT_FILE = r"C:\Users\oladi\.gemini\antigravity-ide\brain\f32186c3-d5d3-4508-a451-07c97b6872f1\scratch\papers_digest.json"

files = sorted([f for f in os.listdir(TEXTS_DIR) if f.endswith('.txt')])

digest = []

for f in files:
    doc_name = f[:-4] # remove .txt
    path = os.path.join(TEXTS_DIR, f)
    with open(path, "r", encoding="utf-8", errors="replace") as file:
        content = file.read()

    pages = content.split("=== PAGE ")
    p1 = pages[1] if len(pages) > 1 else ""
    p2 = pages[2] if len(pages) > 2 else ""
    p_last = pages[-1] if len(pages) > 1 else ""
    p_penult = pages[-2] if len(pages) > 2 else ""
    
    # Search for year: 19xx or 20xx
    # arXiv date e.g. arXiv:2101.07377v1 [cs.LG] 18 Jan 2021 or 2023 or 2024
    # SSRN date e.g. Electronic copy available at: ... or Posted: ... or 2020, 2021, etc.
    # ACM date e.g. 2018, 2019, 2022
    
    # Find headings and relevant paragraphs
    lines = content.splitlines()
    
    # look for conclusion
    conclusion_text = []
    future_text = []
    method_text = []
    
    for i, line in enumerate(lines):
        l_lower = line.strip().lower()
        if any(h in l_lower for h in ["conclusion", "concluding remarks", "conclusions and"]):
            if len(l_lower) < 60:
                conclusion_text.append("\n".join(lines[i:min(len(lines), i+35)]))
        if any(h in l_lower for h in ["future research", "future work", "further research", "limitations and future"]):
            if len(l_lower) < 60:
                future_text.append("\n".join(lines[i:min(len(lines), i+35)]))
        if any(h in l_lower for h in ["methodology", "empirical model", "research methodology", "data and methodology", "empirical methodology"]):
            if len(l_lower) < 60:
                method_text.append("\n".join(lines[i:min(len(lines), i+35)]))

    digest.append({
        "doc_name": doc_name,
        "total_pages": len(pages) - 1,
        "p1_head": p1[:2500],
        "p2_head": p2[:2000],
        "p_penult": p_penult[:2500],
        "p_last": p_last[:2500],
        "conclusion_snippets": conclusion_text[:3],
        "future_snippets": future_text[:3],
        "method_snippets": method_text[:3]
    })

with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    json.dump(digest, out, indent=2, ensure_ascii=False)

print(f"Generated digest for {len(digest)} papers.")
