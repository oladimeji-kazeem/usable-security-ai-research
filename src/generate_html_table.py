import json
import os
import html

JSON_PATH = r"C:\Users\oladi\.gemini\antigravity-ide\brain\f32186c3-d5d3-4508-a451-07c97b6872f1\scratch\all_papers_analyzed.json"
HTML_PATH = r"C:\Users\oladi\.gemini\antigravity-ide\brain\f32186c3-d5d3-4508-a451-07c97b6872f1\interactive_papers_table.html"

with open(JSON_PATH, "r", encoding="utf-8") as f:
    records = json.load(f)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Research Papers Analysis & Synthesis Directory (42 Documents)</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {{
  --bg-primary: #0f172a;
  --bg-secondary: #1e293b;
  --bg-tertiary: #334155;
  --accent: #38bdf8;
  --accent-hover: #0284c7;
  --text-main: #f8fafc;
  --text-muted: #94a3b8;
  --border: #334155;
  --badge-bg: rgba(56, 189, 248, 0.15);
  --badge-text: #38bdf8;
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  background-color: var(--bg-primary);
  color: var(--text-main);
  padding: 2rem 1.5rem;
  line-height: 1.6;
}}
.header {{
  max-width: 1600px;
  margin: 0 auto 2rem;
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  flex-wrap: wrap;
  gap: 1.5rem;
  border-bottom: 1px solid var(--border);
  padding-bottom: 1.5rem;
}}
.header h1 {{
  font-size: 1.85rem;
  font-weight: 700;
  color: #fff;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}}
.header h1 span.badge {{
  font-size: 0.85rem;
  padding: 0.25rem 0.75rem;
  background: var(--badge-bg);
  color: var(--badge-text);
  border-radius: 9999px;
  font-weight: 600;
  border: 1px solid rgba(56,189,248,0.3);
}}
.header p {{
  color: var(--text-muted);
  font-size: 0.95rem;
  margin-top: 0.35rem;
}}
.controls {{
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}}
.search-box {{
  position: relative;
  min-width: 320px;
}}
.search-box input {{
  width: 100%;
  padding: 0.65rem 1rem 0.65rem 2.4rem;
  border-radius: 8px;
  border: 1px solid var(--border);
  background: var(--bg-secondary);
  color: #fff;
  font-size: 0.9rem;
  outline: none;
  transition: all 0.2s;
}}
.search-box input:focus {{
  border-color: var(--accent);
  box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.2);
}}
.search-box svg {{
  position: absolute;
  left: 0.8rem;
  top: 50%;
  transform: translateY(-50%);
  width: 16px;
  height: 16px;
  fill: var(--text-muted);
}}
.btn {{
  background: var(--accent);
  color: #0f172a;
  border: none;
  padding: 0.65rem 1.25rem;
  border-radius: 8px;
  font-weight: 600;
  font-size: 0.9rem;
  cursor: pointer;
  transition: background 0.2s;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}}
.btn:hover {{ background: var(--accent-hover); color: #fff; }}
.table-container {{
  max-width: 1600px;
  margin: 0 auto;
  overflow-x: auto;
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  border-radius: 12px;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5);
}}
table {{
  width: 100%;
  border-collapse: collapse;
  text-align: left;
  font-size: 0.88rem;
}}
thead th {{
  background: #111c2e;
  padding: 1rem 0.85rem;
  font-weight: 600;
  color: #cbd5e1;
  border-bottom: 2px solid var(--border);
  white-space: nowrap;
  position: sticky;
  top: 0;
  cursor: pointer;
  user-select: none;
}}
thead th:hover {{ color: var(--accent); }}
thead th .sort-indicator {{
  font-size: 0.75rem;
  margin-left: 0.35rem;
}}
tbody tr {{
  border-bottom: 1px solid var(--border);
  transition: background 0.15s ease;
}}
tbody tr:hover {{
  background: rgba(51, 65, 85, 0.4);
}}
tbody td {{
  padding: 1rem 0.85rem;
  vertical-align: top;
}}
.doc-chip {{
  font-family: monospace;
  font-weight: 600;
  color: #38bdf8;
  background: rgba(56, 189, 248, 0.1);
  padding: 0.2rem 0.45rem;
  border-radius: 4px;
  white-space: nowrap;
}}
.year-pill {{
  display: inline-block;
  padding: 0.2rem 0.55rem;
  border-radius: 9999px;
  background: var(--bg-tertiary);
  color: #e2e8f0;
  font-weight: 600;
  font-size: 0.8rem;
  white-space: nowrap;
}}
.col-num {{ width: 40px; text-align: center; color: var(--text-muted); font-weight: 600; }}
.col-doc {{ min-width: 130px; }}
.col-title {{ min-width: 220px; font-weight: 600; color: #f1f5f9; }}
.col-year {{ width: 75px; text-align: center; }}
.col-aim {{ min-width: 240px; }}
.col-obj {{ min-width: 240px; font-size: 0.84rem; }}
.col-rq {{ min-width: 230px; font-size: 0.84rem; font-style: italic; color: #cbd5e1; }}
.col-meth {{ min-width: 240px; }}
.col-model {{ min-width: 190px; color: #93c5fd; font-size: 0.84rem; }}
.col-conc {{ min-width: 260px; }}
.col-further {{ min-width: 240px; color: #fca5a5; font-size: 0.84rem; }}
ol, ul {{ padding-left: 1.15rem; }}
li {{ margin-bottom: 0.25rem; }}
.stat-bar {{
  max-width: 1600px;
  margin: 0 auto 1.5rem;
  display: flex;
  gap: 1.5rem;
  font-size: 0.88rem;
  color: var(--text-muted);
}}
.stat-item {{
  background: var(--bg-secondary);
  border: 1px solid var(--border);
  padding: 0.6rem 1rem;
  border-radius: 8px;
}}
.stat-item strong {{ color: var(--accent); }}
</style>
</head>
<body>

<div class="header">
  <div>
    <h1>Research Papers Analysis & Synthesis Directory <span class="badge">42 Papers Fully Indexed</span></h1>
    <p>Systematic multi-dimensional extraction: Document Name, Title, Year, Aim, Objectives, Research Questions, Methodology, Models, Conclusions, and Future Research.</p>
  </div>
  <div class="controls">
    <div class="search-box">
      <svg viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
      <input type="text" id="searchInput" placeholder="Search papers, keywords, models, years..." onkeyup="filterTable()">
    </div>
    <button class="btn" onclick="exportCSV()">
      <svg style="width:16px;height:16px;fill:currentColor" viewBox="0 0 24 24"><path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"/></svg>
      Export CSV
    </button>
  </div>
</div>

<div class="stat-bar">
  <div class="stat-item">Total Analyzed: <strong>42 Documents</strong></div>
  <div class="stat-item">Year Range: <strong>2018 – 2026</strong></div>
  <div class="stat-item">Focus Areas: <strong>Cybersecurity, Authentication, Usability, Privacy, NLP, Vulnerability Audits</strong></div>
</div>

<div class="table-container">
  <table id="papersTable">
    <thead>
      <tr>
        <th class="col-num" onclick="sortTable(0)">#</th>
        <th class="col-doc" onclick="sortTable(1)">Document Name <span class="sort-indicator">↕</span></th>
        <th class="col-title" onclick="sortTable(2)">Title <span class="sort-indicator">↕</span></th>
        <th class="col-year" onclick="sortTable(3)">Year <span class="sort-indicator">↕</span></th>
        <th class="col-aim">Aim</th>
        <th class="col-obj">Objectives</th>
        <th class="col-rq">Research Questions</th>
        <th class="col-meth">Methodology</th>
        <th class="col-model">Model Used</th>
        <th class="col-conc">Conclusion</th>
        <th class="col-further">Further Areas of Research</th>
      </tr>
    </thead>
    <tbody>
"""

for idx, r in enumerate(records, 1):
    obj_html = "<br>".join(html.escape(line) for line in r['objectives'].splitlines() if line)
    rq_html = "<br>".join(html.escape(line) for line in r['research_questions'].splitlines() if line)
    
    html_content += f"""      <tr>
        <td class="col-num">{idx}</td>
        <td class="col-doc"><span class="doc-chip">{html.escape(r['doc_name'])}</span></td>
        <td class="col-title">{html.escape(r['title'])}</td>
        <td class="col-year"><span class="year-pill">{html.escape(r['year'])}</span></td>
        <td class="col-aim">{html.escape(r['aim'])}</td>
        <td class="col-obj">{obj_html}</td>
        <td class="col-rq">{rq_html}</td>
        <td class="col-meth">{html.escape(r['methodology'])}</td>
        <td class="col-model">{html.escape(r['model_used'])}</td>
        <td class="col-conc">{html.escape(r['conclusion'])}</td>
        <td class="col-further">{html.escape(r['further_areas_research'])}</td>
      </tr>\n"""

html_content += """    </tbody>
  </table>
</div>

<script>
function filterTable() {
  const query = document.getElementById('searchInput').value.toLowerCase();
  const rows = document.querySelectorAll('#papersTable tbody tr');
  rows.forEach(row => {
    const text = row.innerText.toLowerCase();
    row.style.display = text.includes(query) ? '' : 'none';
  });
}

function sortTable(n) {
  const table = document.getElementById("papersTable");
  let rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  switching = true;
  dir = "asc";
  while (switching) {
    switching = false;
    rows = table.rows;
    for (i = 1; i < (rows.length - 1); i++) {
      shouldSwitch = false;
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      let cmpX = x.innerText.toLowerCase();
      let cmpY = y.innerText.toLowerCase();
      if (n === 0 || n === 3) {
        cmpX = parseInt(cmpX) || 0;
        cmpY = parseInt(cmpY) || 0;
      }
      if (dir === "asc") {
        if (cmpX > cmpY) { shouldSwitch = true; break; }
      } else if (dir === "desc") {
        if (cmpX < cmpY) { shouldSwitch = true; break; }
      }
    }
    if (shouldSwitch) {
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      switchcount++;
    } else {
      if (switchcount === 0 && dir === "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}

function exportCSV() {
  const rows = document.querySelectorAll("#papersTable tr");
  let csv = [];
  rows.forEach(row => {
    let rowData = [];
    row.querySelectorAll("th, td").forEach(cell => {
      let text = cell.innerText.replace(/"/g, '""').replace(/\\n/g, ' ');
      rowData.push('"' + text + '"');
    });
    csv.push(rowData.join(","));
  });
  const blob = new Blob([csv.join("\\n")], { type: "text/csv;charset=utf-8;" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "research_papers_table.csv";
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
}
</script>
</body>
</html>
"""

with open(HTML_PATH, "w", encoding="utf-8") as out:
    out.write(html_content)

print(f"Generated Interactive HTML Table ({len(html_content)} bytes)!")
