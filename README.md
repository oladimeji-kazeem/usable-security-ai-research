# Usable Cybersecurity, Privacy & AI Governance Research Synthesis

A comprehensive research intelligence repository synthesizing **42 academic research papers** spanning usable security, biometric authentication, vulnerable & neurodivergent populations, privacy governance (GDPR/CCPA), dark patterns, and emerging generative AI threats.

---

## 📁 Repository Structure

```tree
├── src/                                  # Data extraction, NLP & generation scripts
│   ├── extract_papers.py                 # PDF metadata and text extractor
│   ├── dump_texts.py                     # High-fidelity multi-page plain text dumper
│   ├── parse_sections.py                 # Regex and heuristic section boundary parser
│   ├── extract_digest.py                 # Abstract, RQ, methodology & conclusion extractor
│   ├── analyze_all.py                    # Multi-pass structural analyzer
│   ├── compile_db.py                     # Master database compiler (all 10 fields)
│   ├── generate_md_artifact.py           # Markdown summary table and profiles generator
│   └── generate_html_table.py            # Interactive web dashboard generator
├── data/                                 # Machine-readable datasets
│   ├── all_papers_analyzed.json          # Master JSON database of all 42 papers (10 fields)
│   ├── heuristic_summary.json            # Parsed structural paper summaries
│   ├── papers_digest.json                # Compact abstracts, RQs, and methodologies
│   └── papers_parsed_sections.json       # Granular section splits
├── research_papers_summary_table.csv     # Complete 10-field spreadsheet database (Excel/Sheets)
├── research_papers_summary_table.md      # Full 10-column master table and in-depth profiles
├── interactive_papers_table.html         # Interactive web dashboard (search, sort, filter, export)
├── phd_ai_research_proposals.md          # 5 foundational PhD AI research proposals
├── phd_ai_big_data_models_proposals.md   # 5 big-data & foundation model PhD research proposals
├── phd_ai_global_control_das_proposals.md# 5 elite PhD AI research proposals for Dr. Sanchari Das (GMU)
└── README.md                             # Repository documentation
```

---

## 📊 Synthesized Fields (All 42 Papers)

Every document in this collection has been analyzed across 10 standardized academic fields:
1. **Document Name** (e.g., `0632.pdf`, `2512.15945v1.pdf`, `ssrn-4173372.pdf`)
2. **Title**
3. **Published Year** (ranging 2018–2026)
4. **Aim**
5. **Objectives**
6. **Research Questions**
7. **Methodology** (empirical lab studies, ethnographic observation, NLP scraping, web scans, user surveys)
8. **Model Used** (TAM, P3F, UTAUT2, GOMS, SHAP/XAI, Structural Equation Modeling, etc.)
9. **Conclusion**
10. **Further Areas of Research**

---

## 🚀 Key Research Outputs

### 1. Interactive Web Dashboard (`interactive_papers_table.html`)
A standalone, zero-dependency browser application featuring:
- **Instant Search:** Filter papers by author, keyword, methodology, or model in real-time.
- **Multi-Column Sorting:** Sort by publication year, title, or filename.
- **Category Filter Badges:** Quickly isolate papers by domain (Authentication, Vulnerable Groups, Privacy Governance, AI Threats, IoT & Smart Home).
- **One-Click Export:** Download custom-filtered views directly to CSV.

*To view: Double click `interactive_papers_table.html` or open in any web browser.*

### 2. Master Table & Extended Profiles (`research_papers_summary_table.md`)
Over 160 KB of detailed academic analysis featuring both the 10-column master comparison matrix and dedicated narrative profiles for each individual paper.

### 3. Master CSV Database (`research_papers_summary_table.csv`)
UTF-8 encoded spreadsheet ready for import into Microsoft Excel, Google Sheets, Pandas, or R.

---

## 🎓 PhD AI Research Proposals

Based on the explicit gaps and future research areas identified across the 42 papers, 15 structured PhD AI proposals were generated across three targeted portfolios:

### Portfolio A: Human-Centered Usable AI ([phd_ai_research_proposals.md](./phd_ai_research_proposals.md))
1. **Adaptive Neuro-Inclusive Cyber Defense:** Dynamic RL-driven cognitive-state adaptation for ADHD/Autistic users.
2. **Multimodal Defense Against Generative Social Engineering:** Cross-modal speech & linguistic deepfake detection.
3. **Autonomous Client-Side Privacy Agents:** VLM-based agentic dark pattern evasion & machine-negotiated consent.
4. **Calibrated & Interactive XAI for SOC Analysts:** Conformal prediction & counterfactual causal inference in threat triage.
5. **Edge-Native Foundation Models for Contextual DLP:** Sub-1B quantized SLMs with mechanistic interpretability for prompt privacy.

### Portfolio B: Big Data & Foundation Models ([phd_ai_big_data_models_proposals.md](./phd_ai_big_data_models_proposals.md))
1. **Web-Scale Automated Vulnerability Synthesis:** 70B Code LLMs + SMT solvers trained across 50M+ GitHub repos.
2. **Predictive Multi-Agent DeFi Intelligence:** Spatio-temporal graph transformers on petabyte-scale on-chain DAGs and social sentiment.
3. **Continuous Multimodal Zero-Trust Biometrics:** Masked Sensor Transformers (SensorMAE) trained over 100+ TB time-series telemetry.
4. **Spatial Foundation Models for Metaverse Privacy:** Real-time 3D Gaussian Splatting and generative diffusion anonymizers.
5. **Internet-Scale Empirical Legal-Tech AI:** 70B Vision-Language Models auditing 2M+ Android/iOS app binaries for dark patterns.

### Portfolio C: Elite Proposals for Dr. Sanchari Das / GMU ([phd_ai_global_control_das_proposals.md](./phd_ai_global_control_das_proposals.md))
*Authored from the perspective of Global AI Control, AI Systems Architecture, and Engineering:*
1. **Autonomous AI Agent Governance & Sandboxed Control:** Neuro-symbolic formal verification gatekeepers for tool-using LLMs.
2. **AI ReadyCheck & Algorithmic Dark Pattern Auditing:** Dynamic red-teaming multi-agent swarms auditing generative consumer interfaces.
3. **Zero-Trust Continuous Biometrics with Epistemic Uncertainty:** Bayesian sensor transformers resolving the P3F trade-off.
4. **Global AI Control Architecture for Autonomous Cyber Weapons:** Decentralized POMDPs containing rogue AI agents at machine speed.
5. **Privacy-Preserving Ambient Spatial AI for In-Home Care:** Neuromorphic event cameras & zk-SNARKs protecting vulnerable aging adults.

---

## 🛠️ Usage & Reproduction

To re-run the extraction and generation pipeline:

```bash
# Extract raw texts from all PDF documents
python src/dump_texts.py

# Parse structural sections and heuristics
python src/parse_sections.py

# Compile master 10-field database
python src/compile_db.py

# Generate markdown table artifact
python src/generate_md_artifact.py

# Generate interactive web table
python src/generate_html_table.py
```

---

## 📄 License & Attribution
Curated and synthesized from academic literature under fair-use scholarly research guidelines.
Authors: Dr. Sanchari Das, InSpirit Lab, SPICE Lab (George Mason University), and collaborating researchers.
Repository maintained by **ubasify** (`oladimeji@ubasify.com`).
