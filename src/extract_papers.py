import os
import json
import glob
from pypdf import PdfReader

PAPERS_DIR = r"c:\Users\oladi\OneDrive\Financial Performance\research papers"
OUTPUT_DIR = r"C:\Users\oladi\.gemini\antigravity-ide\brain\f32186c3-d5d3-4508-a451-07c97b6872f1\scratch"
os.makedirs(OUTPUT_DIR, exist_ok=True)

files = sorted([f for f in os.listdir(PAPERS_DIR) if f.lower().endswith('.pdf')])

results = []

for filename in files:
    filepath = os.path.join(PAPERS_DIR, filename)
    try:
        reader = PdfReader(filepath)
        num_pages = len(reader.pages)
        meta = reader.metadata or {}
        
        # Extract first 3 pages
        first_pages_text = ""
        for i in range(min(3, num_pages)):
            txt = reader.pages[i].extract_text() or ""
            first_pages_text += f"\n--- PAGE {i+1} ---\n" + txt
            
        # Extract last 3 pages
        last_pages_text = ""
        start_last = max(3, num_pages - 3)
        for i in range(start_last, num_pages):
            txt = reader.pages[i].extract_text() or ""
            last_pages_text += f"\n--- PAGE {i+1} ---\n" + txt

        # Also full text search for specific headings: "conclusion", "future", "objective", "research question", "methodology", "model"
        full_text_snippets = []
        for i, page in enumerate(reader.pages):
            t = page.extract_text() or ""
            lower_t = t.lower()
            found_keys = [k for k in ["conclusion", "future work", "future research", "methodology", "empirical model", "research question"] if k in lower_t]
            if found_keys:
                full_text_snippets.append({
                    "page": i + 1,
                    "keys": found_keys,
                    "text_preview": t[:1000]
                })

        info = {
            "filename": filename,
            "num_pages": num_pages,
            "meta_title": str(meta.get("/Title", "")),
            "meta_author": str(meta.get("/Author", "")),
            "meta_creation_date": str(meta.get("/CreationDate", "")),
            "first_pages_sample": first_pages_text[:4000],
            "last_pages_sample": last_pages_text[-4000:] if last_pages_text else "",
            "snippets": full_text_snippets
        }
        results.append(info)
        print(f"Processed {filename}: {num_pages} pages")
    except Exception as e:
        print(f"Error {filename}: {e}")
        results.append({
            "filename": filename,
            "error": str(e)
        })

with open(os.path.join(OUTPUT_DIR, "papers_initial_extracted.json"), "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"Done processing {len(results)} files.")
