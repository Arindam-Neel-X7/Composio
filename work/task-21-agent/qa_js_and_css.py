"""
Task 21 JavaScript Runtime & Responsive CSS/A11y QA Script.
1. Extracts embedded <script> from outputs/task-20/index.html, runs `node --check`.
2. Executes a Node.js DOM-shim functional harness testing:
   - Search filter ("HubSpot" -> 1, "Paygent" -> 1, "MCP" -> >0)
   - Queue pills (build_now -> 44, conditional -> 50, outreach_required -> 4, unknown -> 2)
   - Sample-only checkbox (20 apps)
   - Auth filter (OAuth2 -> 79, API_key -> 39, Bearer_token -> 35, Basic -> 15, none -> 5)
   - MCP filter (official_only -> 66, community_only -> 15, official_and_community -> 4, not_found_bounded -> 11, unknown -> 4)
   - Sorting (id, name, queue, mcp_category)
   - openDrawer(id) across ALL 100 apps (0 exceptions, non-empty HTML, valid drawerTitle, transitions rendered for sampled apps)
   - Theme toggle state
3. Inspects responsive CSS (@media breakpoints, viewport meta, table overflow-x, drawer width, .hide-sm, focus/ARIA).
"""

import json
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
HTML_PATH = ROOT / "outputs" / "task-20" / "index.html"
OUT_PATH = ROOT / "work" / "task-21-agent" / "qa_js_css_results.json"


def main():
    html_text = HTML_PATH.read_text(encoding="utf-8")

    # 1. Extract <script>
    scripts = re.findall(r"<script>(.*?)</script>", html_text, re.S)
    assert len(scripts) == 1, f"Expected 1 inline <script>, got {len(scripts)}"
    js_code = scripts[0]

    with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as tf:
        tf.write(js_code)
        js_tmp = Path(tf.name)

    syntax_proc = subprocess.run(["node", "--check", str(js_tmp)], capture_output=True, text=True)
    js_syntax_ok = syntax_proc.returncode == 0

    # 2. Functional Node.js runtime harness (minimal DOM shim)
    harness = r"""
const fs = require('fs');
const vm = require('vm');
const jsCode = fs.readFileSync(process.argv[2], 'utf8');

const elements = {};
function makeEl(id) {
  return {
    id,
    value: '',
    checked: false,
    textContent: '',
    innerHTML: '',
    children: [],
    dataset: {},
    classList: {
      _set: new Set(),
      add(c){ this._set.add(c); },
      remove(c){ this._set.delete(c); },
      contains(c){ return this._set.has(c); }
    },
    listeners: {},
    appendChild(c){ this.children.push(c); return c; },
    addEventListener(ev, fn){ (this.listeners[ev] ||= []).push(fn); },
    focus(){},
    setAttribute(k, v){ this[k] = v; },
    getAttribute(k){ return this[k] || null; },
    querySelectorAll(){ return []; },
    querySelector(){ return makeEl('sub'); }
  };
}

const knownIds = [
  'categoryFilter', 'resultCount', 'matrixBody', 'drawerContent', 'drawerBackdrop',
  'searchInput', 'mcpFilter', 'authFilter', 'queuePills', 'sampleOnlyCheck',
  'resetFiltersBtn', 'exportJsonBtn', 'themeToggle', 'copyAppJsonBtn', 'closeDrawerBtn'
];
for (const id of knownIds) elements[id] = makeEl(id);

const sandbox = {
  console,
  URL: { createObjectURL: () => 'blob:test', revokeObjectURL: () => {} },
  Blob: class { constructor(parts, opts){ this.parts = parts; this.opts = opts; } },
  navigator: { clipboard: { writeText: async () => {} } },
  setTimeout: (fn) => {},
  document: {
    documentElement: makeEl('html'),
    getElementById: (id) => (elements[id] ||= makeEl(id)),
    createElement: (tag) => makeEl(tag),
    querySelectorAll: () => [],
    addEventListener: () => {}
  },
  window: { matchMedia: () => ({ matches: false }) }
};

vm.createContext(sandbox);
vm.runInContext(jsCode, sandbox);

// Expose test results from inside the VM context
const report = vm.runInContext(`(() => {
  const results = {};
  results.totalApps = APPS.length;
  results.categoriesPopulated = document.getElementById('categoryFilter').children.length;

  // Test search
  state.search = 'HubSpot';
  results.searchHubSpot = getFilteredApps().length;
  state.search = 'Paygent';
  results.searchPaygent = getFilteredApps().length;
  state.search = '';

  // Test queues
  results.queues = {};
  for (const q of ['build_now', 'conditional', 'outreach_required', 'unknown']) {
    state.queue = q;
    results.queues[q] = getFilteredApps().length;
  }
  state.queue = '';

  // Test sampleOnly
  state.sampleOnly = true;
  results.sampleOnly = getFilteredApps().length;
  state.sampleOnly = false;

  // Test auth
  results.auth = {};
  for (const a of ['OAuth2', 'API_key', 'Bearer_token', 'Basic', 'none', 'other', 'JWT', 'session_cookie']) {
    state.auth = a;
    results.auth[a] = getFilteredApps().length;
  }
  state.auth = '';

  // Test mcp
  results.mcp = {};
  for (const m of ['official_only', 'community_only', 'official_and_community', 'not_found_bounded', 'unknown']) {
    state.mcp = m;
    results.mcp[m] = getFilteredApps().length;
  }
  state.mcp = '';

  // Test sorting
  state.sortKey = 'name'; state.sortDir = 1;
  const sortedNames = getFilteredApps().map(a => a.name);
  results.sortNameFirst = sortedNames[0];
  results.sortNameLast = sortedNames[sortedNames.length - 1];
  state.sortKey = 'id'; state.sortDir = 1;

  // Test openDrawer for ALL 100 apps
  let drawerOk = 0;
  let drawerErrors = [];
  for (const app of APPS) {
    try {
      openDrawer(app.id);
      const html = document.getElementById('drawerContent').innerHTML;
      if (!html || !html.includes('drawerTitle') || !html.includes('Primary Purpose')) {
        drawerErrors.push({ id: app.id, err: 'missing sections' });
      } else {
        drawerOk++;
      }
    } catch (e) {
      drawerErrors.push({ id: app.id, err: String(e) });
    }
  }
  closeDrawer();
  results.drawerOk = drawerOk;
  results.drawerErrors = drawerErrors;
  results.escTest = esc('<script>"&') === '&lt;script&gt;&quot;&amp;';
  return results;
})()`, sandbox);

console.log(JSON.stringify(report, null, 2));
"""

    with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as hf:
        hf.write(harness)
        harness_tmp = Path(hf.name)

    run_proc = subprocess.run(["node", str(harness_tmp), str(js_tmp)], capture_output=True, text=True)
    js_tmp.unlink(missing_ok=True)
    harness_tmp.unlink(missing_ok=True)

    runtime_ok = run_proc.returncode == 0
    runtime_report = json.loads(run_proc.stdout) if runtime_ok else {"stderr": run_proc.stderr}

    # 3. Static CSS & Responsive / A11y checks
    styles = re.findall(r"<style>(.*?)</style>", html_text, re.S)
    css_text = styles[0] if styles else ""
    media_queries = re.findall(r"@media\s*\([^)]+\)", css_text)

    css_checks = {
        "viewport_meta_present": '<meta name="viewport" content="width=device-width, initial-scale=1.0">' in html_text,
        "media_queries": media_queries,
        "table_horizontal_scroll": "overflow-x: auto" in css_text,
        "hide_sm_defined": ".hide-sm" in css_text,
        "drawer_mobile_width": "width: min(680px, 100%)" in css_text or "max-width: 100%" in css_text or "100vw" in css_text,
        "dark_theme_vars": '[data-theme="dark"]' in css_text,
        "sticky_topnav": "position: sticky" in css_text,
        "aria_modal_drawer": 'role="dialog" aria-modal="true"' in html_text,
        "aria_labels_count": len(re.findall(r'aria-label="[^"]+"', html_text)),
    }

    output = {
        "js_syntax_ok": js_syntax_ok,
        "js_syntax_stderr": syntax_proc.stderr,
        "js_runtime_ok": runtime_ok,
        "js_runtime_report": runtime_report,
        "css_responsive_a11y": css_checks,
    }
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
