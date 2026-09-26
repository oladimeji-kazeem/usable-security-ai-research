import os
import re
import json

TEXTS_DIR = r"C:\Users\oladi\.gemini\antigravity-ide\brain\f32186c3-d5d3-4508-a451-07c97b6872f1\scratch\texts"
OUTPUT_FILE = r"C:\Users\oladi\.gemini\antigravity-ide\brain\f32186c3-d5d3-4508-a451-07c97b6872f1\scratch\papers_parsed_sections.json"

files = sorted([f for f in os.listdir(TEXTS_DIR) if f.endswith('.txt')])

papers = []

for f in files:
    doc_name = f.replace('.txt', '')
    path = os.path.join(TEXTS_DIR, f)
    with open(path, "r", encoding="utf-8", errors="replace") as file:
        content = file.read()
    
    pages = content.split("=== PAGE ")
    # First 3 pages text
    first_pages = ""
    for p in pages[1:4]:
        first_pages += p + "\n"
        
    # Last 3 pages text
    last_pages = ""
    for p in pages[-3:]:
        last_pages += p + "\n"
        
    papers.append({
        "doc_name": doc_name,
        "first_page_head": pages[1][:1500] if len(pages) > 1 else content[:1500],
        "first_3_pages": first_pages[:4000],
        "last_3_pages": last_pages[-4000:] if last_pages else "",
        "total_pages": len(pages) - 1,
        "total_chars": len(content)
    })

with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    json.dump(papers, out, indent=2, ensure_ascii=False)

print(f"Parsed overview for {len(papers)} papers.")
