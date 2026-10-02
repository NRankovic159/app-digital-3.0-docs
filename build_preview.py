import os, re, json, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "_preview")

SECTIONS = [
    ("Home", "home"),
    ("Getting Started", "getting-started"),
    ("CX Guidelines", "cx-guidelines"),
    ("NPI Operations", "npi-operations"),
    ("Analytics", "analytics"),
    ("Theme Release", "theme-release"),
    ("Features & Functionality", "features-functionality"),
    ("Support", "support"),
    ("About Us", "about-us"),
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title} — APP Digital 3.0 Docs (Preview)</title>
<style>
  :root {{
    --border: #e3e2e0; --text: #1f2124; --muted: #6b7280;
    --accent: #2563eb; --sidebar-bg: #fbfbfa; --code-bg: #f3f3f1;
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin:0; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif; color:var(--text); background:#fff; }}
  .topbar {{ height:56px; border-bottom:1px solid var(--border); display:grid; grid-template-columns:1fr auto 1fr; align-items:center; padding:0 20px; position:sticky; top:0; background:#fff; z-index:10; }}
  .topbar .brand {{ font-weight:600; font-size:14px; white-space:nowrap; }}
  .search {{ justify-self:center; width:420px; position:relative; }}
  .search-input {{
    width:100%; background:var(--sidebar-bg); border:1px solid var(--border);
    border-radius:8px; padding:7px 12px; color:var(--text); font-size:13px; outline:none;
    text-align:center;
  }}
  .search-input:focus {{ border-color:var(--accent); text-align:left; }}
  .search-results {{
    position:absolute; top:calc(100% + 6px); left:0; right:0; background:#fff;
    border:1px solid var(--border); border-radius:10px; box-shadow:0 8px 24px rgba(0,0,0,.1);
    max-height:360px; overflow-y:auto; display:none; z-index:50; text-align:left;
  }}
  .search-results.open {{ display:block; }}
  .search-result {{ display:block; padding:10px 14px; text-decoration:none; color:var(--text); border-bottom:1px solid var(--border); }}
  .search-result:last-child {{ border-bottom:none; }}
  .search-result:hover, .search-result.highlighted {{ background:#f3f4f6; }}
  .search-result .srt {{ font-weight:600; font-size:13.5px; }}
  .search-result .srs {{ font-size:11.5px; color:var(--muted); margin-top:2px; }}
  .search-empty {{ padding:14px; font-size:13px; color:var(--muted); text-align:center; }}
  .layout {{ display:flex; min-height:calc(100vh - 56px); }}
  nav.sidebar {{ width:270px; flex-shrink:0; border-right:1px solid var(--border); background:var(--sidebar-bg); padding:14px 8px; overflow-y:auto; }}
  nav.sidebar .nav-group {{ margin-bottom: 14px; }}
  nav.sidebar .nav-title {{
    display:block; padding:6px 10px; border-radius:6px;
    font-size:13.5px; font-weight:700; color:var(--text); text-decoration:none;
  }}
  nav.sidebar .nav-title:hover {{ background:#eceae6; }}
  nav.sidebar .nav-title.active-section {{ color:var(--accent); }}
  nav.sidebar .nav-title.active {{ background:#e8edfc; color:var(--accent); }}
  nav.sidebar ul {{ list-style:none; margin:2px 0 0; padding:0; }}
  nav.sidebar li a {{ display:block; padding:5px 10px; border-radius:6px; color:#4b5563; font-weight:400; text-decoration:none; font-size:13px; }}
  nav.sidebar li a:hover {{ background:#eceae6; }}
  nav.sidebar li a.active {{ background:#e8edfc; color:var(--accent); font-weight:400; }}
  nav.sidebar li ul a {{ padding-left:20px; font-size:12.5px; color:var(--muted); }}
  main {{ flex:1; max-width:780px; margin:0 auto; padding:40px 32px 80px; }}
  main h1 {{ font-size:32px; margin-bottom:4px; }}
  main h2 {{ font-size:20px; margin-top:32px; border-top:1px solid var(--border); padding-top:20px; }}
  main p, main li {{ font-size:15px; line-height:1.6; color:#333; }}
  main blockquote {{ background:#fff8e6; border-left:3px solid #f0b429; margin:16px 0; padding:10px 16px; border-radius:4px; font-size:14px; }}
  main table {{ border-collapse:collapse; width:100%; margin:16px 0; font-size:14px; }}
  main th, main td {{ border:1px solid var(--border); padding:8px 10px; text-align:left; }}
  main code {{ background:var(--code-bg); padding:1px 5px; border-radius:4px; font-size:13px; }}
  main ul.task-list {{ list-style:none; padding-left:0; }}
  main ul.task-list li {{ margin-bottom:6px; }}
  main ul.task-list input[type="checkbox"] {{ margin-right:8px; }}
  .gb-hint {{ padding:12px 16px; border-radius:8px; margin:16px 0; font-size:14px; border-left:4px solid; }}
  .gb-hint p {{ margin:0; }}
  .gb-hint p + p {{ margin-top:8px; }}
  .gb-hint-info {{ background:#eff6ff; border-color:#3b82f6; }}
  .gb-hint-success {{ background:#f0fdf4; border-color:#22c55e; }}
  .gb-hint-warning {{ background:#fffbeb; border-color:#f59e0b; }}
  .gb-hint-danger {{ background:#fef2f2; border-color:#ef4444; }}
  .gb-tabs {{ margin:16px 0; border:1px solid var(--border); border-radius:10px; overflow:hidden; }}
  .gb-tab-buttons {{ display:flex; border-bottom:1px solid var(--border); background:var(--sidebar-bg); }}
  .gb-tab-btn {{ padding:10px 16px; background:none; border:none; cursor:pointer; font-size:13.5px; font-weight:600; color:var(--muted); border-bottom:2px solid transparent; }}
  .gb-tab-btn.gb-tab-active {{ color:var(--accent); border-bottom-color:var(--accent); }}
  .gb-tab-panel {{ padding:16px; }}
  .gb-tab-panel p:first-child {{ margin-top:0; }}
  table[data-view="cards"] {{
    border-collapse:separate; border-spacing:12px; width:calc(100% + 24px);
    margin:16px -12px 0; display:block;
  }}
  table[data-view="cards"] thead {{ display:none; }}
  table[data-view="cards"] tbody {{ display:grid; grid-template-columns:repeat(2, 1fr); gap:12px; }}
  table[data-view="cards"] tr {{
    display:block; border:1px solid var(--border); border-radius:10px; padding:14px 16px;
    transition:border-color .15s, box-shadow .15s; cursor:pointer;
  }}
  table[data-view="cards"] tr:hover {{ border-color:var(--accent); box-shadow:0 1px 4px rgba(0,0,0,.06); }}
  table[data-view="cards"] td {{ display:block; border:none; padding:0; }}
  table[data-view="cards"] td:first-child {{ font-weight:700; font-size:14px; margin-bottom:4px; }}
  table[data-view="cards"] td:nth-child(2) {{ font-size:13px; color:var(--muted); }}
  table[data-view="cards"] td:nth-child(3), table[data-view="cards"] td:nth-child(4) {{ display:none; }}
  .breadcrumb {{ font-size:12px; color:var(--muted); margin-bottom:10px; }}
  .brand {{ display:flex; align-items:center; gap:8px; }}
  .brand svg {{ flex-shrink:0; }}
  .announce-strip {{
    background:#eef2ff; border-bottom:1px solid var(--border);
    padding:10px 20px; display:flex; justify-content:center; position:relative;
  }}
  .announce-pill {{
    display:inline-flex; align-items:center; gap:8px; background:#fff;
    border:1px solid #c7d2fe; border-radius:999px; padding:5px 16px 5px 6px;
    cursor:pointer; font-size:13px; font-weight:600; color:var(--accent);
  }}
  .announce-pill:hover {{ border-color:var(--accent); }}
  .announce-badge {{
    background:var(--accent); color:#fff; font-size:11px; font-weight:700;
    border-radius:999px; width:20px; height:20px; display:flex;
    align-items:center; justify-content:center;
  }}
  .announce-panel {{
    position:absolute; top:calc(100% + 8px); left:50%; transform:translateX(-50%);
    width:440px; max-height:420px; overflow-y:auto; background:#fff;
    border:1px solid var(--border); border-radius:14px;
    box-shadow:0 12px 32px rgba(0,0,0,.12); z-index:60; display:none; text-align:left;
  }}
  .announce-panel.open {{ display:block; }}
  .announce-panel-header {{ font-weight:700; font-size:15px; padding:16px 18px; border-bottom:1px solid var(--border); }}
  .announce-item {{ display:block; padding:14px 18px; border-bottom:1px solid var(--border); text-decoration:none; color:inherit; }}
  .announce-item:last-child {{ border-bottom:none; }}
  .announce-item:hover {{ background:#f9fafb; }}
  .announce-item .ann-date {{ font-size:11px; letter-spacing:.04em; text-transform:uppercase; color:var(--muted); margin-bottom:4px; }}
  .announce-item .ann-title {{ font-weight:700; font-size:14.5px; color:var(--text); margin-bottom:3px; }}
  .announce-item .ann-desc {{ font-size:13px; color:var(--muted); line-height:1.5; }}
  main h2#recently-updated + ul {{
    list-style:none; margin:16px 0 0; padding:0;
    display:grid; grid-template-columns:repeat(2, 1fr); gap:12px;
  }}
  main h2#recently-updated + ul li {{
    border:1px solid var(--border); border-radius:10px; padding:14px 16px;
    transition:border-color .15s, box-shadow .15s;
  }}
  main h2#recently-updated + ul li:hover {{ border-color:var(--accent); box-shadow:0 1px 4px rgba(0,0,0,.06); }}
  main h2#recently-updated + ul li a {{
    font-weight:600; color:var(--text); text-decoration:none; font-size:14px;
  }}
  main h2#quick-start + table {{
    border-collapse:separate; border-spacing:12px; margin:16px -12px 0; width:calc(100% + 24px);
  }}
  main h2#quick-start + table td {{
    border:1px solid var(--border); border-radius:10px; padding:14px 16px;
    font-size:14px; font-weight:600; transition:border-color .15s, box-shadow .15s;
  }}
  main h2#quick-start + table td:hover {{ border-color:var(--accent); box-shadow:0 1px 4px rgba(0,0,0,.06); }}
  main h2#quick-start + table td a {{ color:var(--text); text-decoration:none; }}
  main h2#need-help + ul {{
    list-style:none; margin:16px 0 0; padding:0;
    display:grid; grid-template-columns:repeat(2, 1fr); gap:12px;
  }}
  main h2#need-help + ul li {{
    border:1px solid var(--border); border-radius:10px; padding:14px 16px;
    transition:border-color .15s, box-shadow .15s;
  }}
  main h2#need-help + ul li:hover {{ border-color:var(--accent); box-shadow:0 1px 4px rgba(0,0,0,.06); }}
  main h2#need-help + ul li a {{ font-weight:600; color:var(--text); text-decoration:none; font-size:14px; }}
  main h2#need-help + ul li em {{ display:block; margin-top:4px; font-style:normal; color:var(--muted); font-size:12.5px; }}
</style>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12.152 6.896c-.948 0-2.415-1.078-3.96-1.04-2.04.027-3.91 1.183-4.961 3.014-2.117 3.673-.546 9.104 1.519 12.09 1.013 1.454 2.208 3.09 3.792 3.039 1.52-.06 2.09-.985 3.935-.985 1.831 0 2.35.985 3.96.958 1.637-.026 2.717-1.48 3.73-2.93 1.098-1.596 1.549-3.135 1.573-3.202-.034-.014-3.017-1.16-3.05-4.596-.027-2.874 2.35-4.253 2.454-4.32-1.345-1.98-3.437-2.2-4.17-2.238-1.735-.14-3.19 1.208-4.822 1.21z'/%3E%3Cpath d='M15.53 3.83c.893-1.09 1.5-2.585 1.336-4.09-1.256.09-2.79.9-3.71 1.977-.83.943-1.548 2.463-1.36 3.928 1.436.11 2.85-.72 3.734-1.815z'/%3E%3C/svg%3E">
</head>
<body>
  <div class="topbar">
    <div class="brand">
      <svg width="19" height="22" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="#1f2124">
        <path d="M12.152 6.896c-.948 0-2.415-1.078-3.96-1.04-2.04.027-3.91 1.183-4.961 3.014-2.117 3.673-.546 9.104 1.519 12.09 1.013 1.454 2.208 3.09 3.792 3.039 1.52-.06 2.09-.985 3.935-.985 1.831 0 2.35.985 3.96.958 1.637-.026 2.717-1.48 3.73-2.93 1.098-1.596 1.549-3.135 1.573-3.202-.034-.014-3.017-1.16-3.05-4.596-.027-2.874 2.35-4.253 2.454-4.32-1.345-1.98-3.437-2.2-4.17-2.238-1.735-.14-3.19 1.208-4.822 1.21z"/>
        <path d="M15.53 3.83c.893-1.09 1.5-2.585 1.336-4.09-1.256.09-2.79.9-3.71 1.977-.83.943-1.548 2.463-1.36 3.928 1.436.11 2.85-.72 3.734-1.815z"/>
      </svg>
      <span>Premium Partner</span>
    </div>
    <div class="search">
      <input id="search-input" class="search-input" type="text" placeholder="🔍 Search" autocomplete="off">
      <div id="search-results" class="search-results"></div>
    </div>
  </div>
  <div class="announce-strip">
    <div class="announce-pill" id="announce-pill">
      <span class="announce-badge">4</span> Announcements
    </div>
    <div class="announce-panel" id="announce-panel">
      <div class="announce-panel-header">Announcements</div>
      <a class="announce-item" href="/features-functionality/index.html">
        <div class="ann-date">October 2026</div>
        <div class="ann-title">[3.0] Features and Functionality</div>
        <div class="ann-desc">Capability-area landing pages and change logs for all 15 Features &amp; Functionality topics are now live.</div>
      </a>
      <a class="announce-item" href="/home/new-features-3-0.html">
        <div class="ann-date">October 2026</div>
        <div class="ann-title">[3.0] New Features</div>
        <div class="ann-desc">Overview of net-new capabilities introduced in the 3.0 release.</div>
      </a>
      <a class="announce-item" href="/home/mobile-search-3-0.html">
        <div class="ann-date">September 2026</div>
        <div class="ann-title">[3.0] Mobile Search</div>
        <div class="ann-desc">Updated guidance on mobile search behavior for 3.0.</div>
      </a>
      <a class="announce-item" href="/home/energy-label-3-0.html">
        <div class="ann-date">September 2026</div>
        <div class="ann-title">[3.0] Energy Label</div>
        <div class="ann-desc">New compliance guidance for energy label requirements.</div>
      </a>
    </div>
  </div>
  <div class="layout">
    <nav class="sidebar">
      {sidebar}
    </nav>
    <main>
      <div class="breadcrumb">{breadcrumb}</div>
      {body}
    </main>
  </div>
  <script>
  (function() {{
    var input = document.getElementById('search-input');
    var results = document.getElementById('search-results');
    var index = null;
    var matches = [];
    var activeIndex = -1;

    fetch('/search-index.json').then(function(r) {{ return r.json(); }}).then(function(data) {{ index = data; }});

    function render(items) {{
      if (!items.length) {{
        results.innerHTML = '<div class="search-empty">No results</div>';
        results.classList.add('open');
        return;
      }}
      results.innerHTML = items.map(function(item) {{
        return '<a class="search-result" href="' + item.url + '">' +
          '<div class="srt">' + item.title + '</div>' +
          '<div class="srs">' + item.section + '</div>' +
          '</a>';
      }}).join('');
      results.classList.add('open');
    }}

    function runSearch(q) {{
      if (!index || !q) {{ results.classList.remove('open'); matches = []; return; }}
      var lower = q.toLowerCase();
      matches = index.filter(function(item) {{
        return item.title.toLowerCase().indexOf(lower) !== -1 || item.text.toLowerCase().indexOf(lower) !== -1;
      }}).slice(0, 8);
      activeIndex = -1;
      render(matches);
    }}

    function updateHighlight(links) {{
      for (var i = 0; i < links.length; i++) {{
        links[i].classList.toggle('highlighted', i === activeIndex);
      }}
    }}

    input.addEventListener('input', function() {{ runSearch(input.value.trim()); }});
    input.addEventListener('focus', function() {{ if (input.value.trim()) runSearch(input.value.trim()); }});
    document.addEventListener('click', function(e) {{
      if (!e.target.closest('.search')) results.classList.remove('open');
    }});
    input.addEventListener('keydown', function(e) {{
      var links = results.querySelectorAll('.search-result');
      if (e.key === 'ArrowDown') {{
        e.preventDefault();
        activeIndex = Math.min(activeIndex + 1, links.length - 1);
        updateHighlight(links);
      }} else if (e.key === 'ArrowUp') {{
        e.preventDefault();
        activeIndex = Math.max(activeIndex - 1, 0);
        updateHighlight(links);
      }} else if (e.key === 'Enter') {{
        e.preventDefault();
        if (activeIndex >= 0 && links[activeIndex]) {{
          window.location.href = links[activeIndex].getAttribute('href');
        }} else if (matches.length) {{
          window.location.href = matches[0].url;
        }}
      }} else if (e.key === 'Escape') {{
        results.classList.remove('open');
        input.blur();
      }}
    }});
  }})();
  (function() {{
    var pill = document.getElementById('announce-pill');
    var panel = document.getElementById('announce-panel');
    pill.addEventListener('click', function(e) {{
      e.stopPropagation();
      panel.classList.toggle('open');
    }});
    document.addEventListener('click', function(e) {{
      if (!e.target.closest('.announce-strip')) panel.classList.remove('open');
    }});
    document.addEventListener('keydown', function(e) {{
      if (e.key === 'Escape') panel.classList.remove('open');
    }});
  }})();
  (function() {{
    document.addEventListener('click', function(e) {{
      var btn = e.target.closest('.gb-tab-btn');
      if (!btn) return;
      var group = btn.closest('.gb-tabs');
      group.querySelectorAll('.gb-tab-btn').forEach(function(b) {{ b.classList.remove('gb-tab-active'); }});
      group.querySelectorAll('.gb-tab-panel').forEach(function(p) {{ p.style.display = 'none'; }});
      btn.classList.add('gb-tab-active');
      document.getElementById(btn.getAttribute('data-tab')).style.display = '';
    }});
    document.querySelectorAll('table[data-view="cards"] tbody tr').forEach(function(row) {{
      var link = row.children[2] && row.children[2].querySelector('a');
      if (link) {{
        row.addEventListener('click', function() {{ window.location.href = link.getAttribute('href'); }});
      }}
    }});
  }})();
  </script>
</body>
</html>
"""

def md_fragment_to_html(text):
    result = subprocess.run(["pandoc", "-f", "gfm", "-t", "html"], input=text, capture_output=True, text=True, check=True)
    return result.stdout

HINT_RE = re.compile(r'\{%\s*hint\s+style="(\w+)"[^%]*%\}\n(.*?)\n\{%\s*endhint\s*%\}', re.DOTALL)
TABS_RE = re.compile(r'\{%\s*tabs\s*%\}(.*?)\{%\s*endtabs\s*%\}', re.DOTALL)
TAB_RE = re.compile(r'\{%\s*tab\s+title="([^"]*)"[^%]*%\}\s*(.*?)\s*\{%\s*endtab\s*%\}', re.DOTALL)

def preprocess_gitbook_blocks(md_text):
    """Translate GitBook's Git Sync block syntax ({% hint %}, {% tabs %}) into
    raw HTML this preview's pandoc pass will preserve verbatim. Cards tables
    are already plain HTML and need no preprocessing."""

    def hint_repl(m):
        style = m.group(1)
        inner = md_fragment_to_html(m.group(2).strip())
        return f'\n\n<div class="gb-hint gb-hint-{style}">\n{inner}\n</div>\n\n'

    md_text = HINT_RE.sub(hint_repl, md_text)

    def tabs_repl(m):
        tabs = TAB_RE.findall(m.group(1))
        if not tabs:
            return m.group(0)
        uid = "tabs-" + str(abs(hash(m.group(1))) % 100000)
        buttons, panels = [], []
        for i, (title, content) in enumerate(tabs):
            active = " gb-tab-active" if i == 0 else ""
            buttons.append(f'<button class="gb-tab-btn{active}" data-tab="{uid}-{i}">{title}</button>')
            inner = md_fragment_to_html(content.strip())
            style = "" if i == 0 else ' style="display:none"'
            panels.append(f'<div class="gb-tab-panel" id="{uid}-{i}"{style}>{inner}</div>')
        return (
            f'\n\n<div class="gb-tabs" data-group="{uid}">'
            f'<div class="gb-tab-buttons">{"".join(buttons)}</div>'
            f'{"".join(panels)}</div>\n\n'
        )

    md_text = TABS_RE.sub(tabs_repl, md_text)
    return md_text

def md_to_html(md_path):
    with open(md_path) as f:
        raw = f.read()
    raw = preprocess_gitbook_blocks(raw)
    result = subprocess.run(["pandoc", "-f", "gfm", "-t", "html"], input=raw, capture_output=True, text=True, check=True)
    html = result.stdout
    html = fix_relative_links(html)
    return html

def fix_relative_links(html):
    """Rewrite hrefs pointing at sibling .md files (real Markdown link convention)
    to the .html filenames this preview builder actually generates."""
    def repl(m):
        path = m.group(1)
        if path.endswith("README.md"):
            path = path[: -len("README.md")] + "index.html"
        elif path.endswith(".md"):
            path = path[:-3] + ".html"
        return f'href="{path}"'
    return re.sub(r'href="([^"]+)"', repl, html)

link_re = re.compile(r"\[(.*?)\]\((.*?)\)")

def parse_space_summary(space_dir):
    """Returns list of (level, label, relative_md_link) for a space's SUMMARY.md"""
    path = os.path.join(ROOT, space_dir, "SUMMARY.md")
    if not os.path.exists(path):
        return [(0, "Overview", "README.md")]
    entries = []
    with open(path) as f:
        for line in f:
            stripped = line.rstrip("\n")
            if not stripped.strip().startswith("*"):
                continue
            indent = len(stripped) - len(stripped.lstrip(" "))
            level = 1 if indent >= 2 else 0
            m = link_re.search(stripped)
            if m:
                entries.append((level, m.group(1), m.group(2)))
    return entries

def to_html_rel(md_rel):
    if md_rel.endswith("README.md"):
        return md_rel[:-len("README.md")] + "index.html"
    return md_rel[:-3] + ".html"

# Build full page list per section, and overall url map
all_pages = []  # (section_path, level, label, page_html_rel_within_section)
for _, section_path in SECTIONS:
    for level, label, link in parse_space_summary(section_path):
        page_html_rel = to_html_rel(link)  # relative within section dir
        all_pages.append((section_path, level, label, page_html_rel, link))

def render_sidebar(current_section_path, current_page_rel):
    out = []
    for title, section_path in SECTIONS:
        pages = [p for p in all_pages if p[0] == section_path]
        is_active_section = section_path == current_section_path
        overview = next((p for p in pages if p[3] == "index.html"), None)
        rest = [p for p in pages if p is not overview]
        overview_href = f"/{section_path}/{overview[3]}" if overview else f"/{section_path}/"
        title_active = " active" if (is_active_section and current_page_rel == "index.html") else ""
        title_cls = " active-section" if is_active_section else ""
        out.append('<div class="nav-group">')
        out.append(f'  <a class="nav-title{title_cls}{title_active}" href="{overview_href}">{title}</a>')
        if rest:
            out.append('  <ul>')
            for _, level, label, page_rel, _ in rest:
                href = f"/{section_path}/{page_rel}"
                active = " active" if (is_active_section and page_rel == current_page_rel) else ""
                if level == 0:
                    out.append(f'    <li><a class="{active.strip()}" href="{href}">{label}</a></li>')
                else:
                    out.append(f'    <li><ul><li><a class="{active.strip()}" href="{href}">{label}</a></li></ul></li>')
            out.append('  </ul>')
        out.append('</div>')
    return "\n".join(out)

def extract_text(html):
    text = re.sub(r"<[^>]+>", " ", html)
    return re.sub(r"\s+", " ", text).strip()

count = 0
SEARCH_INDEX = []
for section_title, section_path in SECTIONS:
    for level, label, link in parse_space_summary(section_path):
        md_full = os.path.join(ROOT, section_path, link)
        page_rel = to_html_rel(link)
        out_full = os.path.join(OUT, section_path, page_rel)
        os.makedirs(os.path.dirname(out_full), exist_ok=True)

        body_html = md_to_html(md_full)
        sidebar_html = render_sidebar(section_path, page_rel)
        crumb = section_title if page_rel == "index.html" else f"{section_title} / {label}"
        page_title = section_title if page_rel == "index.html" else label

        page = TEMPLATE.format(title=page_title, sidebar=sidebar_html, body=body_html, breadcrumb=crumb)
        with open(out_full, "w") as f:
            f.write(page)
        count += 1
        SEARCH_INDEX.append({
            "title": label,
            "section": section_title,
            "url": f"/{section_path}/{page_rel}",
            "text": extract_text(body_html),
        })

print(f"Generated {count} preview pages in {OUT}")

# Orphan pages: real content, reachable by direct link, intentionally not listed
# in any space's SUMMARY.md (kept out of the left-nav tree).
ORPHAN_PAGES = [
    ("home", "new-features-3-0.md"),
    ("home", "mobile-search-3-0.md"),
    ("home", "energy-label-3-0.md"),
    ("theme-release", "release-notes-3-0.md"),
    ("theme-release", "release-notes-2-8.md"),
    ("theme-release", "release-notes-2-7.md"),
    ("theme-release", "release-notes-2-4.md"),
    ("theme-release", "migrating-to-3-0.md"),
    ("theme-release", "migrating-to-2-8.md"),
    ("theme-release", "migrating-to-2-7.md"),
    ("theme-release", "migrating-to-2-4.md"),
    ("theme-release", "deprecation-notices-3-0.md"),
    ("theme-release", "deprecation-notices-2-8.md"),
    ("theme-release", "deprecation-notices-2-7.md"),
    ("theme-release", "deprecation-notices-2-4.md"),
]
for section_path, link in ORPHAN_PAGES:
    md_full = os.path.join(ROOT, section_path, link)
    page_rel = to_html_rel(link)
    out_full = os.path.join(OUT, section_path, page_rel)
    os.makedirs(os.path.dirname(out_full), exist_ok=True)

    body_html = md_to_html(md_full)
    sidebar_html = render_sidebar(section_path, None)
    section_title = next(t for t, p in SECTIONS if p == section_path)
    with open(md_full) as f:
        first_line = f.readline().strip()
    label = first_line.lstrip("#").strip() if first_line.startswith("#") else link[:-3].replace("-", " ").title()
    crumb = f"{section_title} / {label}"

    page = TEMPLATE.format(title=label, sidebar=sidebar_html, body=body_html, breadcrumb=crumb)
    with open(out_full, "w") as f:
        f.write(page)
    count += 1
    SEARCH_INDEX.append({
        "title": label,
        "section": section_title,
        "url": f"/{section_path}/{page_rel}",
        "text": extract_text(body_html),
    })

with open(os.path.join(OUT, "search-index.json"), "w") as f:
    json.dump(SEARCH_INDEX, f)

print(f"Generated {count - len(ORPHAN_PAGES)} space pages + {len(ORPHAN_PAGES)} orphan pages in {OUT}")
print(f"Search index: {len(SEARCH_INDEX)} entries")
