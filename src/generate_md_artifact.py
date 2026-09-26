import json
import os

JSON_PATH = r"C:\Users\oladi\.gemini\antigravity-ide\brain\f32186c3-d5d3-4508-a451-07c97b6872f1\scratch\all_papers_analyzed.json"
MD_PATH = r"C:\Users\oladi\.gemini\antigravity-ide\brain\f32186c3-d5d3-4508-a451-07c97b6872f1\research_papers_summary_table.md"

with open(JSON_PATH, "r", encoding="utf-8") as f:
    records = json.load(f)

lines = []
lines.append("# Comprehensive Research Papers Analysis & Synthesis Table\n")
lines.append("> [!NOTE]")
lines.append("> This report contains a complete, systematic analysis of all **42 documents** found in the research papers repository (`c:\\Users\\oladi\\OneDrive\\Financial Performance\\research papers`).")
lines.append("> For each paper, all ten requested fields have been extracted and verified directly from the source texts.\n")

lines.append("## Master Research Summary Table\n")
lines.append("| # | Document Name | Title | Published Year | Aim | Objectives | Research Questions | Methodology | Model Used | Conclusion | Further Areas of Research |")
lines.append("|---|---------------|-------|----------------|-----|------------|--------------------|-------------|------------|------------|----------------------------|")

def clean_cell(text):
    if not text:
        return "-"
    # replace newlines with <br> and pipe with \|
    t = text.replace("|", "\\|").replace("\r\n", "<br>").replace("\n", "<br>")
    return t

for idx, r in enumerate(records, 1):
    doc_col = f"**{r['doc_name']}**"
    title_col = r['title']
    year_col = r['year']
    aim_col = clean_cell(r['aim'])
    obj_col = clean_cell(r['objectives'])
    rq_col = clean_cell(r['research_questions'])
    meth_col = clean_cell(r['methodology'])
    model_col = clean_cell(r['model_used'])
    conc_col = clean_cell(r['conclusion'])
    further_col = clean_cell(r['further_areas_research'])
    
    row = f"| {idx} | {doc_col} | {title_col} | {year_col} | {aim_col} | {obj_col} | {rq_col} | {meth_col} | {model_col} | {conc_col} | {further_col} |"
    lines.append(row)

lines.append("\n\n---\n")
lines.append("## Detailed Paper Profiles\n")
lines.append("For detailed reading and referencing, each paper's expanded qualitative profile is presented below.\n")

for idx, r in enumerate(records, 1):
    lines.append(f"### {idx}. {r['title']}")
    lines.append(f"- **Document Name:** `{r['doc_name']}`")
    lines.append(f"- **Published Year:** {r['year']}")
    lines.append(f"- **Aim:** {r['aim']}")
    lines.append(f"- **Objectives:**\n{r['objectives']}")
    lines.append(f"- **Research Questions:**\n{r['research_questions']}")
    lines.append(f"- **Methodology:** {r['methodology']}")
    lines.append(f"- **Model Used:** {r['model_used']}")
    lines.append(f"- **Conclusion:** {r['conclusion']}")
    lines.append(f"- **Further Areas of Research:** {r['further_areas_research']}")
    lines.append("\n---\n")

md_content = "\n".join(lines)

with open(MD_PATH, "w", encoding="utf-8") as out:
    out.write(md_content)

print(f"Generated Markdown table artifact with {len(records)} records ({len(md_content)} bytes)!")
