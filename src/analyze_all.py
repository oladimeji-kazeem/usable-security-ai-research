import os
import re
import json

TEXTS_DIR = r"C:\Users\oladi\.gemini\antigravity-ide\brain\f32186c3-d5d3-4508-a451-07c97b6872f1\scratch\texts"

def analyze_all_papers():
    files = sorted([f for f in os.listdir(TEXTS_DIR) if f.endswith('.txt')])
    records = []
    
    for idx, f in enumerate(files):
        doc_name = f[:-4]
        with open(os.path.join(TEXTS_DIR, f), "r", encoding="utf-8", errors="replace") as fl:
            content = fl.read()

        pages = content.split("=== PAGE ")
        p1 = pages[1] if len(pages) > 1 else content[:3000]
        p2 = pages[2] if len(pages) > 2 else ""
        p3 = pages[3] if len(pages) > 3 else ""
        pend = pages[-1] if len(pages) > 1 else ""
        ppen = pages[-2] if len(pages) > 2 else ""
        
        # Look for research questions (RQ1, RQ2, etc. or questions with ?)
        rqs = re.findall(r'(RQ\s*\d+[:\.\-][^\.\n\?]+[\.\?]|Research Question\s*\d+[:\.\-][^\.\n\?]+[\.\?])', content, re.IGNORECASE)
        if not rqs:
            # find bullet points or numbered lists following "research question"
            m = re.search(r'research questions?[:\s]+((?:[0-9\-\*\•\–]\s*[^\n]+\n?){1,4})', content, re.IGNORECASE)
            if m:
                rqs = [m.group(0).strip()]
                
        # Look for aim / objective keywords in p1 and p2
        aim_matches = re.findall(r'([^.\n]*?(?:aims? to|aim of this|objective of this|purpose of this|in this paper, we|in this study, we|we propose|we explore|we investigate)[^.\n]*?\.)', p1 + "\n" + p2, re.IGNORECASE)

        # Look for future work
        future_matches = re.findall(r'([^.\n]*?(?:future work|future research|further research|in the future|future studies|limitations)[^.\n]*?\.)', content[-10000:], re.IGNORECASE)
        
        records.append({
            "idx": idx + 1,
            "doc_name": doc_name,
            "rqs": rqs[:4],
            "aim_matches": aim_matches[:4],
            "future_matches": future_matches[:4],
            "pages_count": len(pages) - 1
        })
        
    with open(r"C:\Users\oladi\.gemini\antigravity-ide\brain\f32186c3-d5d3-4508-a451-07c97b6872f1\scratch\heuristic_summary.json", "w", encoding="utf-8") as out:
        json.dump(records, out, indent=2, ensure_ascii=False)
    print("Heuristic summary written!")

if __name__ == "__main__":
    analyze_all_papers()
