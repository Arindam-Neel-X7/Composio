"""Task 12 supplemental sources (capture-002): Clay developer docs found after capture-001."""
import json
from pathlib import Path
from make_sources import SOURCES, s, PP

CLAY = ["index.md", "quickstart.md", "public-api/authentication.md", "public-api/rate-limits.md", "tables.md",
        "audiences.md", "searches.md", "routines/index.md", "routines/api.md", "concepts/cli-basics.md",
        "use-cases/agent-workflows.md", "recipes/agent-function-access.md", "signals.md", "public-api/webhooks.md"]
MORE = [s(60, "https://developers.clay.com/" + p) for p in CLAY] + [s(60, "https://developers.clay.com/llms.txt")]
ALL = SOURCES + MORE

if __name__ == "__main__":
    out = Path(__file__).parent / "sources-002.json"
    out.write_text(json.dumps({"sources": ALL}, indent=2) + "\n", encoding="utf-8")
    print(len(ALL), "->", out)
