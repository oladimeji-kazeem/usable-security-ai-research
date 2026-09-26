import os
from pypdf import PdfReader

PAPERS_DIR = r"c:\Users\oladi\OneDrive\Financial Performance\research papers"
OUTPUT_DIR = r"C:\Users\oladi\.gemini\antigravity-ide\brain\f32186c3-d5d3-4508-a451-07c97b6872f1\scratch\texts"
os.makedirs(OUTPUT_DIR, exist_ok=True)

files = sorted([f for f in os.listdir(PAPERS_DIR) if f.lower().endswith('.pdf')])

for filename in files:
    filepath = os.path.join(PAPERS_DIR, filename)
    txt_path = os.path.join(OUTPUT_DIR, filename + ".txt")
    if os.path.exists(txt_path) and os.path.getsize(txt_path) > 100:
        continue
    try:
        reader = PdfReader(filepath)
        all_text = []
        for i, page in enumerate(reader.pages):
            txt = page.extract_text() or ""
            all_text.append(f"=== PAGE {i+1} ===\n{txt}")
        full = "\n\n".join(all_text)
        with open(txt_path, "w", encoding="utf-8", errors="replace") as out:
            out.write(full)
        print(f"Dumped {filename} ({len(reader.pages)} pages, {len(full)} chars)")
    except Exception as e:
        print(f"Failed {filename}: {e}")

print("All dumped!")
