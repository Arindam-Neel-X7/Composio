# Composio 100-App Integration & MCP Research Repository

Evidence-grounded, reproducible research evaluating **100 SaaS, developer, commerce, finance, and AI applications** for Composio integration readiness, authentication patterns, credential/sandbox gating, API breadth, and callable Model Context Protocol (MCP) server availability.

- **Live Hosted Case Study**: [**https://arindam-neel-x7.github.io/Composio/**](https://arindam-neel-x7.github.io/Composio/) (deployed via GitHub Pages from `gh-pages` branch; zero external assets).
- **Local Interactive Case Study**: Open [`index.html`](index.html) directly in any browser (100% offline-capable; identical copy at [`outputs/task-20/index.html`](outputs/task-20/index.html)).
- **Master Synthesis & Prioritization**: [`outputs/task-19/patterns-and-priorities.md`](outputs/task-19/patterns-and-priorities.md), [`outputs/task-19/build-queues.md`](outputs/task-19/build-queues.md), and [`outputs/task-19/coverage-matrix.md`](outputs/task-19/coverage-matrix.md).
- **QA, Publication & Deployment Records**: [`outputs/task-21/qa-report.md`](outputs/task-21/qa-report.md), [`outputs/task-22/publication-record.md`](outputs/task-22/publication-record.md), and [`outputs/task-23/deployment-record.md`](outputs/task-23/deployment-record.md).

---

## Key Verified Findings (N = 100 Applications)

All percentages carry explicit denominators derived from `outputs/task-19/aggregates.json` and `outputs/task-19/build-queues.json` (merged authoritative dataset: 80 first-pass apps + 20 Task 18 human-rechecked apps):

| Metric | Count / Denominator | Share |
| --- | --- | --- |
| **Build Now** (self-serve API/MCP & credentials) | `44 / 100` | `44.00%` |
| **Conditional** (admin consent, cloud/quota, vendor review, paid plan, or partner gate) | `50 / 100` | `50.00%` |
| **Outreach Required** (sales/enterprise/partner gating) | `4 / 100` | `4.00%` |
| **Unknown** (blocked or unverified product/API surface) | `2 / 100` | `2.00%` |
| **Official MCP Server Observed** (`official_only` 66 + `official_and_community` 4) | `70 / 100` | `70.00%` |
| **Community MCP Only** | `15 / 100` | `15.00%` |
| **No MCP Found (Bounded Search)** | `11 / 100` | `11.00%` |
| **MCP Unknown** | `4 / 100` | `4.00%` |

### Human Verification & Paired Remeasurement (Frozen Sample `composio-20app-sample-v1`)

- **Sampling Method**: Deterministic stratified SHA-256 sample (`2` apps per category across `10` categories = `20` apps, frozen in [`outputs/task-06/sampling-manifest.json`](outputs/task-06/sampling-manifest.json) before batch research began).
- **Task 17 Human Baseline** (`ARINDAM KARMAKAR`, 2026-11-24, `N = 327` fixed eligible claims, 100% review coverage): **84.71%** (`277` correct, `50` unsupported, `0` incorrect, `0` unresolved; observed `95.52%`, inferred `0.00%`). See [`outputs/task-17/human-baseline-report.md`](outputs/task-17/human-baseline-report.md).
- **Task 18 Human Recheck** (`ARINDAM KARMAKAR`, 2026-11-23, same fixed `N = 327` denominator after immutable child corrections): **100.00%** (`327 / 327` correct; observed `100.00%`, inferred `100.00%`). See [`outputs/task-18/remeasurement-report.md`](outputs/task-18/remeasurement-report.md).
- **Disclosure**: Task 18 rechecks the same 20-app sample after targeted correction (sample reuse is explicitly disclosed). The remaining 80 apps underwent independent AI review and schema/grounding validation, not human scoring. No live authenticated API or MCP operational tool calls were executed (`operational_check = not_researched`).

---

## Repository Structure

```text
.
├── index.html                        # Self-contained interactive case study (0 external assets)
├── research_pipeline.py              # Pipeline v0.2.0 CLI (collect, packet, ingest, extract, validate, review, metrics, sample)
├── data/apps.json                    # Authoritative 100-app roster & identities
├── schemas/record.json               # Draft 2020-12 JSON Schema (Contract v1.1)
├── docs/
│   ├── evidence-rules.md             # Claim provenance, citation, unknown & accuracy rules
│   └── pipeline-usage.md             # Full CLI reference and operational boundaries
├── tests/
│   └── test_research_pipeline.py     # 23 offline unit & integration tests
├── tools/                            # Human review intake & paired metrics scripts
├── outputs/
│   ├── execution-plan.json           # 24-task ledger and acceptance records
│   ├── task-05/                      # 5-app pilot independent AI verification
│   ├── task-06/                      # Frozen 20-app sampling manifest & rubric
│   ├── task-07/ .. task-16/          # 10 batch outputs & independent AI review reports
│   ├── task-17/                      # Human baseline judgments, metrics & report
│   ├── task-18/                      # Human recheck judgments, paired metrics & correction log
│   ├── task-19/                      # 100-app aggregates, build queues & synthesis
│   ├── task-20/                      # Generated case study HTML
│   ├── task-21/                      # Reproduction & presentation QA report
│   ├── task-22/                      # Repository publication record
│   └── task-23/                      # Live deployment verification record
└── work/
    ├── research-runs/                # Immutable, SHA-256 sealed runs (captures, snapshots, records, reviews)
    ├── task-04-runs/                 # Preserved original 5-app pilot & Task 05 review runs
    └── task-*-agent/                 # Deterministic generators, QA scripts, and audit artifacts
```

---

## Quickstart & Offline Reproduction

### 1. Prerequisites

- **Python 3.10+**
- **`jsonschema` (Draft 2020-12)** — installed via `requirements.txt` (or PowerShell 7 `Test-Json` as fallback). No API keys, cloud accounts, or network access are required for offline validation and replay.

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 2. Run the Offline Unit Test Suite (23 Tests)

```powershell
.venv\Scripts\python.exe -B -m unittest discover -s tests -v
```

### 3. Perform a Fresh Zero-Network Offline Replay

Create a new immutable child run from any sealed parent without making network requests, then validate it against Contract v1.1:

```powershell
.venv\Scripts\python.exe -B research_pipeline.py --store work/research-runs collect --run-id local-replay-demo --parent task07-first-pass-003 --replay
.venv\Scripts\python.exe -B research_pipeline.py --store work/research-runs validate --run-id local-replay-demo
```

### 4. Recompute Paired Human Review Metrics

```powershell
.venv\Scripts\python.exe -B research_pipeline.py --store work/research-runs metrics --run-id task18-human-recheck-07 --target task18-corrections-07
```

### 5. Regenerate & Verify Aggregates, Case Study, and QA Seals

```powershell
.venv\Scripts\python.exe -B work/task-19-agent/generate_task19_outputs.py
.venv\Scripts\python.exe -B work/task-20-agent/generate_case_study.py
.venv\Scripts\python.exe -B work/task-20-agent/verify_case_study.py
.venv\Scripts\python.exe -B work/task-21-agent/qa_audit.py
```

---

## Live-Research Prerequisites

To collect **new live vendor documentation** (beyond replaying sealed runs):

1. **Network Access**: Outbound HTTPS to public, credential-free vendor documentation URLs (userinfo and credential-like query parameters are rejected by `research_pipeline.py`).
2. **Explicit Source Manifest**: Supply a JSON file (`{"sources": [...]}`) declaring `app_id`, `url`, `kind`, `scope`, `environments`, `attribution_basis`, and `attribution_by`. See [`docs/pipeline-usage.md`](docs/pipeline-usage.md) for the exact format and collector limits (`--timeout`, `--retries`, `--max-bytes`).
3. **Extraction & Independent Review**: No model backend is embedded in `research_pipeline.py`. Provide researcher-authored records via `ingest` or an explicit trusted adapter via `extract --extractor-command-json`. Independent reviews require a distinct `--reviewer-id`; `--reviewer-type human --actual-human-attestation` may only be used when an identified person personally verifies primary sources.

---

## Known Limitations & Boundaries

- **Documentary Scope Only**: All findings are grounded in captured public vendor documentation and official/community repositories; no authenticated API calls, paid account signups, or live MCP server executions were performed (`operational_check = not_researched`).
- **Sample Reuse**: Task 18 remeasurement (`84.71% → 100.00%`) reuses the frozen 20-app sample from Task 17 (`N = 327`) rather than a fresh held-out sample.
- **Immutability Model**: Run seals (`seal.json`) are unsigned SHA-256 integrity checksums for accidental drift/tamper detection, not cryptographic signatures.
- **Static Capture Limits**: Static HTTP capture cannot execute JS-only SPAs or bypass HTTP 403 bot walls (documented explicitly as `unknown` where applicable, e.g., App 90 PitchBook).
