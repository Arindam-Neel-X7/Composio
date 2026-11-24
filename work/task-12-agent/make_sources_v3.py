"""Task 12 final source list (capture-003): adds SE Ranking openapi/seo-skills READMEs and Clay custom-functions/agent-plugins."""
import json
from pathlib import Path
from make_sources import s, OR
from make_sources_v2 import ALL

MORE = [
    s(52, "https://raw.githubusercontent.com/seranking/openapi/main/README.md", OR),
    s(52, "https://raw.githubusercontent.com/seranking/seo-skills/main/README.md", OR),
    s(60, "https://developers.clay.com/routines/custom-functions.md"),
    s(60, "https://github.com/clay-run/agent-plugins", OR),
    s(60, "https://raw.githubusercontent.com/clay-run/agent-plugins/main/README.md", OR),
]
FINAL = ALL + MORE

if __name__ == "__main__":
    out = Path(__file__).parent / "sources-003.json"
    out.write_text(json.dumps({"sources": FINAL}, indent=2) + "\n", encoding="utf-8")
    print(len(FINAL), "->", out)
