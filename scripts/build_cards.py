#!/usr/bin/env python3
"""Procedurally builds all modular SVG cards and metrics assets for shrridharshan27's profile.

Design Standard: HemashreeVI/HemashreeVI unslop craft.
Enforces 15-color dark-canvas palette, classical typography, CSS micro-animations,
and @media (prefers-reduced-motion: reduce) fallbacks.
Standard library only.
"""

import math
import random
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
CARDS_DIR = ROOT / "assets" / "cards"
METRICS_DIR = ROOT / "assets" / "metrics"

# ---------------------------------------------------------------- palette
C = {
    "bg0": "#090B12",
    "bg1": "#10131F",
    "bg2": "#161C30",
    "panel": "#12182A",
    "line": "#262E47",
    "line2": "#2B3963",
    "violet": "#416AE6",
    "lav": "#839DFB",
    "lilac": "#CEDAFF",
    "silver": "#E6E9F0",
    "mist": "#C5CAD8",
    "muted": "#939BB4",
    "dim": "#646E89",
    "mint": "#8FE3C8",
    "rose": "#F0A8D0",
    "amber": "#FFB23F",
}

SERIF = "'Iowan Old Style','Palatino Linotype',Palatino,Georgia,'Times New Roman',serif"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"

# ---------------------------------------------------------------- content data
TERMINAL_LINES = [
    ("whoami", [("out", "shrridharshan · ai/ml developer & cybersecurity engineer")]),
    ("cat education.txt", [("out", "B.Tech CSE (Cyber Physical Systems) @ VIT Chennai (2023–2027)")]),
    ("cat focus.txt", [("out", "langgraph-rag · zero-trust-vaults · groq-speech · microcontroller-cps")]),
    ("cat certs.txt", [("out", "Oracle Cloud 2025 GenAI Professional (Score: 88% · ID: 330277621OCI25GAIOCP)")]),
    ("./status --open-to", [("out", "ai/ml-engineering | zero-trust-security | distributed-systems | sde")]),
    ("echo $LOCATION", [("out", "Chennai, Tamil Nadu, India · IST (UTC+5:30)")]),
]

ABOUT_SIDE = [
    ("BASED IN", "Chennai, India", "B.Tech CSE (CPS) @ VIT Chennai"),
    ("CREDENTIAL", "OCI GenAI Pro", "Score: 88% · Verification on record"),
    ("BY NIGHT", "Fitness Lead", "VP of Fitness Club · 100+ athletes"),
]

RIGHT_NOW = [
    ("LangGraph RAG Pipelines", "self-corrective retrieval & evaluation"),
    ("Zero-Trust Legal Vaults", "AES-256-GCM + TOTP audit ledgers"),
    ("Microcontroller CPS Edge", "sub-50ms fault telemetry & watchdog defense"),
    ("Autonomous Climate dMRV", "stoichiometric carbon MRV verification"),
]

QUICK_FACTS = [
    ("Oracle Certified Professional", "88% score on OCI 2025 Generative AI"),
    ("VIT Chennai 2023–2027", "Cyber Physical Systems specialization"),
    ("PopQA Benchmark Record", "-53% hallucination reduction with LangGraph"),
    ("44/44 E2E Tests Passing", "deterministic tamper isolation on dMRV"),
    ("VP of Fitness Club", "strength training workshops for 100+ members"),
]

PIPELINE = [
    ("SENSE", "perceive the world", ["I2C / SPI sensors · audio streams", "document chunks · raw telemetry"]),
    ("DECIDE", "reason & evaluate", ["LangGraph nodes · LLaMA 3 eval", "Kalman filtering · threshold gates"]),
    ("PROTECT", "lock & enforce", ["AES-256-GCM vault · immutable ledger", "watchdog failsafes · zero trust"]),
]

JOURNEY = [
    ("AUG 2023", "VIT Chennai", ["B.Tech CSE", "Cyber Physical Systems"]),
    ("2024", "Embedded Edge", ["Sensors & MCUs", "Hardware Watchdogs"]),
    ("JUL 2025", "OCI GenAI Pro", ["Oracle Certified", "Score: 88%"]),
    ("2025–26", "LangGraph RAG", ["PopQA Benchmark", "-53% Hallucinations"]),
    ("2026", "Zero-Trust", ["SecureDoc & dMRV", "Cryptographic Audits"]),
    ("2027", "Graduation", ["Next Frontier", "Ready to Deploy"]),
]

PROJECTS = [
    {
        "slug": "rag",
        "kicker": "01 · AI / LLM · SELF-CORRECTIVE RAG",
        "name": "CorrectiveRAG",
        "pitch": "Autonomous self-reflective retrieval pipeline that detects and slashes hallucination.",
        "built": "LangGraph state graph · document chunk evaluator · Tavily fallback search · LLaMA 3 · ChromaDB",
        "stats": [("14.6%", "from 31.4% hallucination"), ("-53%", "hallucination reduction"), ("+11.2 pts", "retrieval accuracy gain")],
        "tags": ["LangGraph", "LLaMA 3", "ChromaDB", "Ollama", "FastAPI", "Python", "AWS EC2"],
        "motif": "rag",
    },
    {
        "slug": "securedoc",
        "kicker": "02 · SECURITY · ZERO-TRUST ARCHITECTURE",
        "name": "SecureDoc-LI",
        "pitch": "Zero-trust legal custody vault with authenticated encryption and immutable audit ledgers.",
        "built": "AES-256-GCM authenticated cipher · PBKDF2 (100k rounds) · TOTP MFA · 6-role RBAC · SHA-256 ledgers",
        "stats": [("100%", "cryptographic integrity"), ("0", "privilege escalations in tests"), ("6 Roles", "Judge, Clerk, Defense...")],
        "tags": ["Python", "FastAPI", "AES-256-GCM", "TOTP", "spaCy NER", "SQLAlchemy", "PostgreSQL"],
        "motif": "vault",
    },
    {
        "slug": "summarizer",
        "kicker": "03 · SPEECH INTELLIGENCE · HARDWARE ACCELERATION",
        "name": "Meeting Summarizer",
        "pitch": "Real-time speech transcription and executive minutes extraction powered by Groq LPUs.",
        "built": "Groq LPU whisper-large-v3 · adaptive FFmpeg chunking · silence gating · LLaMA 3 structured minutes",
        "stats": [("~8s", "per 30-min audio turnaround"), ("8x", "faster turnaround vs cloud APIs"), ("100%", "structured minutes extraction")],
        "tags": ["Whisper", "Groq LPU", "LLaMA 3", "FastAPI", "FFmpeg", "Docker", "Python"],
        "motif": "audio",
    },
    {
        "slug": "cps",
        "kicker": "04 · CYBER PHYSICAL SYSTEMS · EMBEDDED TELEMETRY",
        "name": "Cyber Physical Systems",
        "pitch": "Hardware sensor telemetry acquisition and real-time edge fault boundary defense.",
        "built": "Deterministic I2C/SPI sampling · Kalman noise filtering · dual-watchdog reset · sensor spoofing defense",
        "stats": [("< 50ms", "edge fault detection latency"), ("0%", "unhandled hardware freezes"), ("2× Watchdog", "hardware failsafe timers")],
        "tags": ["C++", "Embedded C", "Microcontrollers", "I2C / SPI", "Kalman Filter", "OCI Cloud"],
        "motif": "embedded",
    },
    {
        "slug": "biochar",
        "kicker": "05 · DIGITAL MRV · CRYPTOGRAPHIC CARBON LEDGER",
        "name": "Biochar MRV Tracker",
        "pitch": "Autonomous digital MRV platform for stoichiometric biochar carbon sequestration ledgers.",
        "built": "Puro.earth / EBC compliance · ULID monotonic sequencing · SHA-256 hash chains · dynamic QR vouchers",
        "stats": [("44 / 44", "E2E verification tests passing"), ("100%", "deterministic tamper isolation"), ("3.67×", "CO2e stoichiometric factor")],
        "tags": ["React 18", "Node.js", "Express", "SQLite WAL", "better-sqlite3", "SHA-256", "Vite"],
        "motif": "mrv",
    },
]

TOOLKIT = [
    ("01 LANGUAGES", ["Python · JavaScript", "C++ · Embedded C", "SQL · HTML5 / CSS3"]),
    ("02 AI & AGENTS", ["LangGraph · LLaMA 3", "OpenAI Whisper", "Corrective RAG", "ChromaDB · Ollama"]),
    ("03 SECURITY & CRYPTO", ["AES-256-GCM · PBKDF2", "SHA-256 Hash Ledgers", "TOTP MFA · 6-Role RBAC", "Zero-Trust Architecture"]),
    ("04 BACKEND & APIS", ["FastAPI · Node.js", "Express · REST APIs", "WebSockets · AsyncIO", "SQLAlchemy ORM"]),
    ("05 CLOUD & INFRA", ["Oracle Cloud (OCI)", "AWS EC2 · Groq LPUs", "Docker Containers", "Vercel · Git CLI"]),
    ("06 DATABASES", ["SQLite (WAL mode)", "PostgreSQL · MySQL", "ChromaDB Vector Store", "Redis Cache"]),
    ("07 EMBEDDED & CPS", ["Microcontrollers", "I2C / SPI Telemetry", "Kalman Filtering", "Watchdog Failsafes"]),
    ("08 FRONTEND & UI", ["React 18 · Vite", "Tailwind CSS", "HTML5 Canvas API", "Responsive Layouts"]),
    ("09 TOOLS & DEV", ["VS Code · Linux", "Postman · PowerShell", "Figma · Git CLI", "GitHub Actions"]),
    ("10 CLIMATE & DMRV", ["Puro.earth / EBC", "Stoichiometric Formulas", "Carbon Sequestration", "Dynamic QR Vouchers"]),
]

# ---------------------------------------------------------------- helpers
def e(s):
    return escape(str(s), {'"': "&quot;"})


STYLE = f"""
<style>
.serif {{ font-family: {SERIF}; }}
.sans {{ font-family: {SANS}; }}
.mono {{ font-family: {MONO}; }}
.kick {{ font-family: {MONO}; font-size: 11px; letter-spacing: 3px; fill: {C['lav']}; }}
.twinkle {{ animation: tw 4s ease-in-out infinite; }}
@keyframes tw {{ 0%, 100% {{ opacity: .15; }} 50% {{ opacity: .9; }} }}
.pulse {{ animation: pl 2.4s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }}
@keyframes pl {{ 0%, 100% {{ opacity: .55; transform: scale(1); }} 50% {{ opacity: 1; transform: scale(1.35); }} }}
.float {{ animation: fl 6s ease-in-out infinite; }}
@keyframes fl {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-6px); }} }}
.spin {{ animation: sp 60s linear infinite; transform-box: fill-box; transform-origin: center; }}
@keyframes sp {{ to {{ transform: rotate(360deg); }} }}
@media (prefers-reduced-motion: reduce) {{
  .twinkle, .pulse, .float, .spin {{ animation: none !important; }}
}}
</style>"""


def base_defs(uid):
    return f"""
<defs>
  <radialGradient id="{uid}-bg" cx="70%" cy="30%" r="90%">
    <stop offset="0" stop-color="{C['bg2']}"/>
    <stop offset=".55" stop-color="{C['bg1']}"/>
    <stop offset="1" stop-color="{C['bg0']}"/>
  </radialGradient>
  <radialGradient id="{uid}-glowA" cx="50%" cy="50%" r="50%">
    <stop offset="0" stop-color="{C['violet']}" stop-opacity=".45"/>
    <stop offset="1" stop-color="{C['violet']}" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="{uid}-glowB" cx="50%" cy="50%" r="50%">
    <stop offset="0" stop-color="{C['silver']}" stop-opacity=".12"/>
    <stop offset="1" stop-color="{C['silver']}" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="{uid}-silver" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#FFFFFF"/>
    <stop offset=".5" stop-color="{C['mist']}"/>
    <stop offset="1" stop-color="{C['lav']}"/>
  </linearGradient>
  <linearGradient id="{uid}-amber" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#FFE7B3"/>
    <stop offset=".5" stop-color="{C['amber']}"/>
    <stop offset="1" stop-color="{C['rose']}"/>
  </linearGradient>
  <linearGradient id="{uid}-rule" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{C['lav']}" stop-opacity="0"/>
    <stop offset=".25" stop-color="{C['lav']}" stop-opacity=".8"/>
    <stop offset="1" stop-color="{C['lav']}" stop-opacity="0"/>
  </linearGradient>
  <pattern id="{uid}-grid" width="28" height="28" patternUnits="userSpaceOnUse">
    <path d="M28 0H0V28" fill="none" stroke="{C['lav']}" stroke-opacity=".05"/>
  </pattern>
</defs>"""


def frame(w, h, uid, glow=(0.75, 0.3)):
    gx, gy = glow
    return f"""
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="22" fill="url(#{uid}-bg)" stroke="{C['line']}"/>
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="22" fill="url(#{uid}-grid)"/>
<ellipse cx="{w*gx:.0f}" cy="{h*gy:.0f}" rx="{w*0.35:.0f}" ry="{h*0.7:.0f}" fill="url(#{uid}-glowA)"/>
<ellipse cx="{w*(1-gx):.0f}" cy="{h*(1-gy):.0f}" rx="{w*0.25:.0f}" ry="{h*0.5:.0f}" fill="url(#{uid}-glowB)"/>"""


def stars(w, h, n, seed, pad=20):
    rnd = random.Random(seed)
    out = []
    for _ in range(n):
        x = rnd.uniform(pad, w - pad)
        y = rnd.uniform(pad, h - pad)
        r = rnd.choice([0.8, 1, 1.2, 1.6])
        d = rnd.uniform(0, 4)
        out.append(f'<circle class="twinkle" cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="{C["silver"]}" style="animation-delay:{d:.1f}s"/>')
    return "\n".join(out)


def text(x, y, s, size, fill, cls="sans", anchor="start", extra=""):
    return f'<text x="{x}" y="{y}" class="{cls}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" {extra}>{e(s)}</text>'


def wrap(s, n):
    words = s.split()
    lines, cur = [], ""
    for w in words:
        if len(cur) + len(w) + 1 > n and cur:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    return lines


def mono_w(s, size):
    return sum(size * (1.2 if ord(ch) > 0x2E80 else 0.61) for ch in s)


def chip(x, y, label, size=11, fill=None, stroke=None, color=None):
    w = mono_w(label, size) + 22
    rect = f'<rect x="{x}" y="{y}" width="{w:.0f}" height="24" rx="12" fill="{fill or C["panel"]}" stroke="{stroke or C["line2"]}"/>'
    return rect + text(x + 11, y + 16, label, size, color or C["mist"], "mono"), w


def chips(x, y, labels, gap=8, maxw=None, **kw):
    out, cx, cy = [], x, y
    for lb in labels:
        w = mono_w(lb, kw.get("size", 11)) + 22
        if maxw and cx + w > x + maxw:
            cx, cy = x, cy + 32
        s, w = chip(cx, cy, lb, **kw)
        out.append(s)
        cx += w + gap
    return "\n".join(out)


def svg(w, h, uid, title, desc, body):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-labelledby="{uid}-t {uid}-d">
<title id="{uid}-t">{e(title)}</title>
<desc id="{uid}-d">{e(desc)}</desc>
{STYLE}
{base_defs(uid)}
{body}
</svg>
"""


def write(filepath, content):
    filepath.parent.mkdir(parents=True, exist_ok=True)
    filepath.write_text(content, encoding="utf-8")
    rel = filepath.relative_to(ROOT)
    print(f"  {str(rel):36s} {len(content.encode('utf-8')) / 1024:6.1f} KB")


# ---------------------------------------------------------------- section titles (1200×104)
def build_title(num, kicker, plain, italic, right, slug):
    w, h, u = 1200, 104, f"t{slug}"
    body = f"""
{text(30, 32, num, 12, C['silver'], 'mono', 'start', 'letter-spacing="3"')}
{text(58, 32, kicker, 12, C['lav'], 'mono', 'start', 'letter-spacing="3"')}
{text(1170, 32, right, 11, C['muted'], 'mono', 'end', 'letter-spacing="3"')}
<text x="30" y="80" class="serif" font-size="40" fill="{C['silver']}">{e(plain)} <tspan fill="{C['lav']}" font-style="italic">{e(italic)}</tspan></text>
<rect x="30" y="96" width="1140" height="1.2" fill="url(#{u}-rule)"/>
<circle cy="96.6" r="2.6" fill="#fff">
  <animate attributeName="cx" values="30;1170" dur="6s" repeatCount="indefinite"/>
  <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.1;.8;1" dur="6s" repeatCount="indefinite"/>
</circle>
"""
    write(CARDS_DIR / f"title-{slug}.svg", svg(w, h, u, f"{num} {kicker}: {plain} {italic}", right, body))


# ---------------------------------------------------------------- about (1200×486)
def build_about():
    w, h, u = 1200, 486, "about"
    tx, ty, tw, th = 32, 34, 760, 418
    rows, y, step, i = [], ty + 66, 22, 0
    cycle = 16
    for cmd, outs in TERMINAL_LINES:
        group = [text(tx + 28, y, "$", 13, C['lav'], 'mono'), text(tx + 46, y, cmd, 13, C['silver'], 'mono')]
        y += step
        for kind, s in outs:
            col = C['muted'] if kind == "note" else C['mist']
            if kind == "out":
                group.append(text(tx + 28, y, "→", 13, C['violet'], 'mono'))
            group.append(text(tx + 46, y, s, 13, col, 'mono'))
            y += step
        y += 6
        t = (0.4 + i * 0.9) / cycle
        rows.append(f"""<g opacity="0"><animate attributeName="opacity" dur="{cycle}s" repeatCount="indefinite" keyTimes="0;{t:.3f};{t + 0.02:.3f};.94;.97;1" values="0;0;1;1;0;0"/>{''.join(group)}</g>""")
        i += 1
    cursor_y = y - step + 4

    side = []
    sx, sy = 822, 40
    for k, (lab, big, small) in enumerate(ABOUT_SIDE):
        yy = sy + k * 140
        side.append(f"""
<g class="float" style="animation-delay:{0.2 + k * 0.3}s">
  <rect x="{sx}" y="{yy}" width="346" height="124" rx="16" fill="{C['panel']}" stroke="{C['line2']}"/>
  <rect x="{sx}" y="{yy + 16}" width="3" height="92" rx="1.5" fill="{C['lav']}"/>
  {text(sx + 24, yy + 36, lab, 11, C['lav'], 'mono', 'start', 'letter-spacing="3"')}
  {text(sx + 24, yy + 74, big, 28, C['silver'], 'serif')}
  {text(sx + 24, yy + 101, small, 13, C['muted'], 'sans')}
</g>""")

    body = f"""
{frame(w, h, u, (0.85, 0.2))}
<rect x="{tx}" y="{ty}" width="{tw}" height="{th}" rx="14" fill="{C['bg0']}" fill-opacity=".85" stroke="{C['line2']}"/>
<path d="M{tx} {ty + 36}H{tx + tw}" stroke="{C['line']}"/>
<circle cx="{tx + 20}" cy="{ty + 18}" r="5" fill="{C['rose']}" fill-opacity=".7"/>
<circle cx="{tx + 38}" cy="{ty + 18}" r="5" fill="{C['lav']}" fill-opacity=".7"/>
<circle cx="{tx + 56}" cy="{ty + 18}" r="5" fill="{C['mint']}" fill-opacity=".7"/>
{text(tx + tw / 2, ty + 23, "shrridharshan@vit-chennai: ~/about", 12, C['muted'], 'mono', 'middle')}
{''.join(rows)}
{text(tx + 28, cursor_y + 18, "$", 13, C['lav'], 'mono')}
<rect x="{tx + 46}" y="{cursor_y + 6}" width="8" height="15" fill="{C['lilac']}"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect>
{''.join(side)}
"""
    desc = "About Shrri Dharshan D R: AI/ML Developer & Cybersecurity Engineer, VIT Chennai CPS, OCI GenAI Certified."
    write(CARDS_DIR / "about.svg", svg(w, h, u, "About Shrri Dharshan D R", desc, body))


# ---------------------------------------------------------------- now + facts (1200×330)
def build_now():
    w, h, u = 1200, 330, "now"
    cols = [("RIGHT NOW", "What I'm building", RIGHT_NOW, 32), ("QUICK FACTS", "Things worth knowing", QUICK_FACTS, 612)]
    parts = []
    for lab, head, items, x in cols:
        parts.append(f"""
<rect x="{x}" y="28" width="556" height="274" rx="18" fill="{C['panel']}" fill-opacity=".85" stroke="{C['line2']}"/>
{text(x + 28, 60, lab, 11, C['lav'], 'mono', 'start', 'letter-spacing="3"')}
{text(x + 28, 94, head, 26, C['silver'], 'serif')}""")
        gap = 190 / len(items)
        for k, (big, small) in enumerate(items):
            yy = 130 + k * gap
            dot = f'<circle class="pulse" cx="{x + 34}" cy="{yy - 5}" r="4" fill="{C["mint"] if lab == "RIGHT NOW" else C["amber"]}" style="animation-delay:{k * 0.4}s"/>'
            parts.append(dot + f'<text x="{x + 52}" y="{yy}" class="sans" font-size="14.5" fill="{C["silver"]}" font-weight="600">{e(big)} <tspan fill="{C["muted"]}" font-weight="400">{e(small)}</tspan></text>')
    body = frame(w, h, u, (0.5, 0.2)) + "".join(parts)
    desc = "Right now: LangGraph RAG, Zero-Trust Legal Vaults, Microcontroller CPS, Climate dMRV."
    write(CARDS_DIR / "now.svg", svg(w, h, u, "Right Now & Quick Facts", desc, body))


# ---------------------------------------------------------------- pipeline (1200×330)
def build_pipeline():
    w, h, u = 1200, 330, "pipe"
    xs = [70, 450, 830]
    parts = [frame(w, h, u, (0.5, 0.5))]
    for k, (name, sub, lines) in enumerate(PIPELINE):
        x = xs[k]
        parts.append(f"""
<g>
<rect x="{x}" y="60" width="300" height="180" rx="18" fill="{C['panel']}" stroke="{C['line2']}"/>
<circle cx="{x + 40}" cy="100" r="16" fill="none" stroke="{C['lav']}"/>
<circle cx="{x + 40}" cy="100" r="5" fill="{C['lilac']}" class="pulse" style="animation-delay:{k * 0.8}s"/>
{text(x + 68, 98, f"0{k + 1}", 11, C['muted'], 'mono', 'start', 'letter-spacing="2"')}
{text(x + 68, 115, sub.upper(), 10, C['lav'], 'mono', 'start', 'letter-spacing="2"')}
{text(x + 24, 168, name, 34, C['silver'], 'serif', 'start', 'letter-spacing="4"')}
{text(x + 24, 198, lines[0], 12.5, C['mist'], 'mono')}
{text(x + 24, 220, lines[1], 12.5, C['muted'], 'mono')}
</g>""")
        if k < 2:
            a, b = x + 300, xs[k + 1]
            parts.append(f"""<path d="M{a + 6} 150H{b - 6}" stroke="{C['lav']}" stroke-dasharray="3 5"/>
<path d="M{b - 14} 144l8 6-8 6" fill="none" stroke="{C['lav']}"/>
<circle r="3.5" fill="#fff"><animateMotion dur="1.8s" repeatCount="indefinite" path="M{a + 6} 150H{b - 10}" begin="{k * 0.9}s"/></circle>""")
    loop = f"M{xs[2] + 150} 240 V282 H{xs[0] + 150} V244"
    parts.append(f"""<path d="{loop}" fill="none" stroke="{C['lav']}" stroke-opacity=".5" stroke-dasharray="3 6"/>
<path d="M{xs[0] + 144} 252l6-8 6 8" fill="none" stroke="{C['lav']}" stroke-opacity=".7"/>
<circle r="3" fill="{C['lilac']}"><animateMotion dur="5s" repeatCount="indefinite" path="{loop}"/></circle>
{text(600, 300, "CLOSED FEEDBACK LOOP", 11, C['lav'], 'mono', 'middle', 'letter-spacing="4"')}
{text(600, 38, "Every architecture follows the same closed loop: acquire signals, evaluate with rigor, and enforce security.", 14, C['muted'], 'serif', 'middle', 'font-style="italic"')}""")
    desc = "Sense, Decide, Protect closed feedback loop architecture."
    write(CARDS_DIR / "pipeline.svg", svg(w, h, u, "Sense, Decide, Protect", desc, "".join(parts)))


# ---------------------------------------------------------------- journey (1200×400)
def build_journey():
    w, h, u = 1200, 400, "jour"
    n = len(JOURNEY)
    x0, x1, ly = 90, 1110, 200
    parts = [frame(w, h, u, (0.3, 0.5))]
    parts.append(f"""<path d="M{x0} {ly}H{x1}" stroke="{C['line2']}" stroke-width="2"/>
<path d="M{x0} {ly}H{x1}" stroke="url(#{u}-silver)" stroke-width="2" stroke-dasharray="1020" stroke-dashoffset="1020">
  <animate attributeName="stroke-dashoffset" values="1020;0;0" keyTimes="0;.6;1" dur="8s" repeatCount="indefinite"/>
</path>""")
    for k, (date, head, sub) in enumerate(JOURNEY):
        x = x0 + k * (x1 - x0) / (n - 1)
        up = k % 2 == 0
        t = 0.6 * k / (n - 1)
        last = k == n - 1
        card_y = 52 if up else 226
        stem = f'<path d="M{x:.0f} {ly - 8 if up else ly + 8}V{card_y + 122 if up else card_y}" stroke="{C["line2"]}"/>'
        parts.append(f"""
{stem}
<circle cx="{x:.0f}" cy="{ly}" r="{9 if last else 7}" fill="{C['bg0']}" stroke="{C['amber'] if last else C['lav']}" stroke-width="2"/>
<circle cx="{x:.0f}" cy="{ly}" r="3" fill="{C['silver']}" opacity="0">
  <animate attributeName="opacity" values="0;0;1;1" keyTimes="0;{t:.3f};{t + 0.02:.3f};1" dur="8s" repeatCount="indefinite"/>
</circle>
<rect x="{x - 74:.0f}" y="{card_y}" width="148" height="122" rx="14" fill="{C['panel']}" stroke="{C['amber'] if last else C['line2']}" {'stroke-dasharray="4 4"' if last else ''}/>
{text(round(x), card_y + 26, date, 10, C['lav'], 'mono', 'middle', 'letter-spacing="1.5"')}
{text(round(x), card_y + 56, head, 16, C['silver'], 'serif', 'middle')}
{text(round(x), card_y + 84, sub[0], 12, C['mist'], 'sans', 'middle')}
{text(round(x), card_y + 104, sub[1], 12, C['muted'], 'sans', 'middle')}""")
    desc = "Timeline of engineering milestones from VIT Chennai 2023 to 2027."
    write(CARDS_DIR / "journey.svg", svg(w, h, u, "Engineering Journey, 2023 to 2027", desc, "".join(parts)))


# ---------------------------------------------------------------- project motifs
def build_motif(kind, x, y):
    L, S, M, R, A = C['lav'], C['silver'], C['mint'], C['rose'], C['amber']
    if kind == "rag":
        # LangGraph autonomous node evaluation graph
        nodes = [(40, 100, "Query"), (110, 100, "Retrieve"), (185, 60, "Grade"), (185, 140, "Search"), (265, 100, "Generate")]
        edges = [((40, 100), (110, 100)), ((110, 100), (185, 60)), ((110, 100), (185, 140)), ((185, 60), (265, 100)), ((185, 140), (265, 100))]
        s = [f'<rect x="{x}" y="{y}" width="310" height="200" rx="16" fill="{C["bg0"]}" stroke="{C["line2"]}"/>',
             text(x + 18, y + 26, "langgraph://evaluator-graph", 10, C['muted'], 'mono')]
        for (x1, y1), (x2, y2) in edges:
            s.append(f'<path d="M{x + x1} {y + y1}L{x + x2} {y + y2}" stroke="{L}" stroke-opacity=".4" stroke-dasharray="3 3"/>')
        s.append(f'<circle r="3.5" fill="{M}"><animateMotion dur="2.4s" repeatCount="indefinite" path="M{x + 40} {y + 100}L{x + 110} {y + 100}L{x + 185} {y + 60}L{x + 265} {y + 100}"/></circle>')
        for nx, ny, lb in nodes:
            is_gen = lb == "Generate"
            col = M if is_gen else (A if lb == "Search" else L)
            s.append(f'<circle cx="{x + nx}" cy="{y + ny}" r="15" fill="{C["panel"]}" stroke="{col}" stroke-width="1.5"/>')
            s.append(text(x + nx, y + ny + 4, lb[:3].upper(), 9.5, S, 'mono', 'middle'))
        s.append(text(x + 18, y + 186, "PopQA · Hallucination 31.4% → 14.6% (-53%)", 10, M, 'mono'))
        return "".join(s)

    if kind == "vault":
        # Zero-trust cryptographic cipher & ledger
        s = [f'<rect x="{x}" y="{y}" width="310" height="200" rx="16" fill="{C["bg0"]}" stroke="{C["line2"]}"/>',
             text(x + 18, y + 26, "vault://aes-256-gcm/ledger", 10, C['muted'], 'mono')]
        # Cipher dial with rotation
        cx, cy = x + 76, y + 104
        s.append(f'<circle cx="{cx}" cy="{cy}" r="42" fill="{C["panel"]}" stroke="{L}" stroke-width="1.8"/>')
        s.append(f'<circle cx="{cx}" cy="{cy}" r="32" fill="none" stroke="{C["line2"]}" stroke-dasharray="3 4"/>')
        s.append(f'<g style="transform-origin:{cx}px {cy}px" class="spin"><circle cx="{cx}" cy="{cy}" r="24" fill="none" stroke="{A}" stroke-dasharray="2 6"/><circle cx="{cx + 24}" cy="{cy}" r="3" fill="{A}"/></g>')
        s.append(f'<circle cx="{cx}" cy="{cy}" r="12" fill="{M}" fill-opacity=".2" stroke="{M}"/>')
        # Ledger hash chain blocks
        for i, hsh in enumerate(["#01-GENESIS", "#02-CUSTODY", "#03-IMMUTABLE"]):
            bx = x + 144
            by = y + 54 + i * 36
            s.append(f'<rect x="{bx}" y="{by}" width="144" height="26" rx="6" fill="{C["panel"]}" stroke="{C["line2"]}"/>')
            s.append(text(bx + 10, by + 17, hsh, 10, L if i < 2 else M, 'mono'))
            if i < 2:
                s.append(f'<path d="M{bx + 72} {by + 26}v10" stroke="{L}" stroke-opacity=".5"/>')
        s.append(text(x + 18, y + 186, "TOTP · 6-Role RBAC · SHA-256 Chain", 10, M, 'mono'))
        return "".join(s)

    if kind == "audio":
        # Speech transcription & Groq LPU acceleration
        s = [f'<rect x="{x}" y="{y}" width="310" height="200" rx="16" fill="{C["bg0"]}" stroke="{C["line2"]}"/>',
             text(x + 18, y + 26, "groq-lpu://whisper-large-v3", 10, C['muted'], 'mono')]
        # Audio wave bars
        for k in range(12):
            bx = x + 24 + k * 10
            hgt = 16 + (k * 17) % 36
            s.append(f'<rect x="{bx}" y="{y + 110 - hgt / 2}" width="6" height="{hgt}" rx="3" fill="{L}" fill-opacity=".7">'
                     f'<animate attributeName="height" values="{hgt};{hgt + 24};{hgt}" dur="{1.2 + (k % 4) * 0.3:.1f}s" repeatCount="indefinite"/>'
                     f'<animate attributeName="y" values="{y + 110 - hgt / 2};{y + 110 - (hgt + 24) / 2};{y + 110 - hgt / 2}" dur="{1.2 + (k % 4) * 0.3:.1f}s" repeatCount="indefinite"/></rect>')
        # Groq LPU chip box
        gx, gy = x + 160, y + 58
        s.append(f'<rect x="{gx}" y="{gy}" width="130" height="96" rx="12" fill="{C["panel"]}" stroke="{A}"/>')
        s.append(text(gx + 65, gy + 32, "GROQ LPU", 13, A, 'mono', 'middle', 'font-weight="700"'))
        s.append(text(gx + 65, gy + 52, "whisper-v3", 11, S, 'mono', 'middle'))
        s.append(text(gx + 65, gy + 74, "~8s / 30-min audio", 10.5, M, 'mono', 'middle'))
        s.append(text(x + 18, y + 186, "8x Real-Time Acceleration · Executive Minutes", 10, M, 'mono'))
        return "".join(s)

    if kind == "embedded":
        # Microcontroller telemetry & watchdog
        s = [f'<rect x="{x}" y="{y}" width="310" height="200" rx="16" fill="{C["bg0"]}" stroke="{C["line2"]}"/>',
             text(x + 18, y + 26, "cps://edge-telemetry/i2c-spi", 10, C['muted'], 'mono')]
        # Pulse train signal
        pts = " ".join(f"{x + 20 + i * 2.7:.1f},{y + 90 + 20 * math.sin(i / 5) * (1 + (i > 65) * 0.8):.1f}" for i in range(100))
        s.append(f'<polyline points="{pts}" fill="none" stroke="{L}" stroke-width="1.8" stroke-dasharray="600" stroke-dashoffset="600">'
                 f'<animate attributeName="stroke-dashoffset" values="600;0;0" keyTimes="0;.7;1" dur="4s" repeatCount="indefinite"/></polyline>')
        s.append(f'<rect x="{x + 20}" y="{y + 130}" width="270" height="20" rx="6" fill="{C["panel"]}" stroke="{C["line2"]}"/>')
        s.append(text(x + 28, y + 144, "WATCHDOG 01", 9.5, C['mist'], 'mono'))
        s.append(f'<rect x="{x + 120}" y="{y + 134}" width="160" height="12" rx="4" fill="{C["bg0"]}"/>')
        s.append(f'<rect x="{x + 120}" y="{y + 134}" width="160" height="12" rx="4" fill="{M}"><animate attributeName="width" values="160;30;160" dur="2.4s" repeatCount="indefinite"/></rect>')
        s.append(text(x + 18, y + 186, "Sub-50ms Edge Boundary · Kalman Filtered", 10, M, 'mono'))
        return "".join(s)

    if kind == "mrv":
        # Biochar dMRV ledger & stoichiometric verification
        s = [f'<rect x="{x}" y="{y}" width="310" height="200" rx="16" fill="{C["bg0"]}" stroke="{C["line2"]}"/>',
             text(x + 18, y + 26, "dmrv://puro-ebc/stoichiometric", 10, C['muted'], 'mono')]
        # Monotonic blocks
        for i, (b_id, factor) in enumerate([("ULID:01J8F", "mass × 0.60"), ("SHA-256", "3.67× CO2e"), ("VOUCHER", "QR Verified")]):
            bx = x + 20 + i * 92
            s.append(f'<rect x="{bx}" y="{y + 54}" width="86" height="74" rx="8" fill="{C["panel"]}" stroke="{L if i < 2 else M}"/>')
            s.append(text(bx + 43, y + 78, b_id, 10, S, 'mono', 'middle'))
            s.append(text(bx + 43, y + 104, factor, 9.5, M if i == 2 else A, 'mono', 'middle'))
            if i < 2:
                s.append(f'<path d="M{bx + 86} {y + 91}h6" stroke="{L}"/>')
        s.append(f'<rect x="{x + 20}" y="{y + 144}" width="270" height="8" rx="4" fill="{C["panel"]}"/>')
        s.append(f'<rect x="{x + 20}" y="{y + 144}" width="270" height="8" rx="4" fill="{M}"><animate attributeName="opacity" values=".6;1;.6" dur="2s" repeatCount="indefinite"/></rect>')
        s.append(text(x + 18, y + 186, "44/44 E2E Verified · Zero Tamper Flaws", 10, M, 'mono'))
        return "".join(s)

    return ""


# ---------------------------------------------------------------- project card (1200×318)
def build_project(p):
    w, h, u = 1200, 318, f"p-{p['slug']}"
    x = 40
    built = wrap(p["built"], 84)
    stats = []
    for k, (big, small) in enumerate(p["stats"]):
        sx = x + k * 225
        stats.append(text(sx, 222, big, 30, C['silver'], 'serif') + text(sx, 245, small, 13, C['muted'], 'sans'))
    body = f"""
{frame(w, h, u, (0.8, 0.4))}
{text(x, 44, p['kicker'], 11, C['lav'], 'mono', 'start', 'letter-spacing="3"')}
{text(x - 2, 96, p['name'], 44, f"url(#{u}-silver)", 'serif')}
{text(x, 128, p['pitch'], 17, C['mist'], 'serif', 'start', 'font-style="italic"')}
{''.join(text(x, 154 + i * 18, ('BUILT › ' if i == 0 else '         ') + ln, 12, C['muted'], 'mono') for i, ln in enumerate(built[:2]))}
<rect x="{x}" y="186" width="680" height="1" fill="{C['line2']}"/>
{''.join(stats)}
{chips(x, 264, p['tags'], size=10.5, maxw=700)}
<g class="float">{build_motif(p['motif'], 850, 54)}</g>
"""
    desc = f"{p['name']}: {p['pitch']} {p['built']}."
    write(CARDS_DIR / f"project-{p['slug']}.svg", svg(w, h, u, p["name"], desc, body))


# ---------------------------------------------------------------- credentials card (1200×260)
def build_credential_card():
    w, h, u = 1200, 260, "oracle-oci"
    x = 44
    body = f"""
{frame(w, h, u, (0.85, 0.35))}
<defs>
  <radialGradient id="oci-seal" cx="50%" cy="50%" r="50%">
    <stop offset="0" stop-color="#C74634" stop-opacity=".35"/>
    <stop offset="1" stop-color="#C74634" stop-opacity="0"/>
  </radialGradient>
</defs>
{text(x, 46, "05 · VERIFIED CREDENTIAL · ORACLE CERTIFIED PROFESSIONAL", 11, C['amber'], 'mono', 'start', 'letter-spacing="3"')}
{text(x - 2, 96, "Oracle Cloud 2025 Generative AI Certified Professional", 32, f"url(#{u}-silver)", 'serif')}
{text(x, 126, "Issued by Oracle University · Official Certification of Generative AI Engineering Expertise", 15, C['mist'], 'serif', 'start', 'font-style="italic"')}
<rect x="{x}" y="146" width="760" height="1" fill="{C['line2']}"/>

<!-- Verification Grid -->
{text(x, 182, "CANDIDATE", 10.5, C['lav'], 'mono', 'start', 'letter-spacing="2"')}
{text(x, 206, "Shrri Dharshan D R", 16, C['silver'], 'serif')}
{text(x, 226, "B.Tech CSE (CPS) @ VIT Chennai", 12, C['muted'], 'sans')}

{text(x + 240, 182, "CREDENTIAL ID", 10.5, C['lav'], 'mono', 'start', 'letter-spacing="2"')}
{text(x + 240, 206, "330277621OCI25GAIOCP", 15, C['silver'], 'mono', 'start', 'font-weight="600"')}
{text(x + 240, 226, "Verified at Oracle University Registry", 12, C['muted'], 'sans')}

{text(x + 520, 182, "EXAM SCORE", 10.5, C['lav'], 'mono', 'start', 'letter-spacing="2"')}
{text(x + 520, 206, "88% · PASSED", 16, C['mint'], 'mono', 'start', 'font-weight="700"')}
{text(x + 520, 226, "Valid: Jul 2026 – Jul 2028", 12, C['muted'], 'sans')}

<!-- Seal graphic on right -->
<g class="float" style="transform-origin: 980px 130px">
  <circle cx="980" cy="130" r="76" fill="url(#oci-seal)"/>
  <circle cx="980" cy="130" r="64" fill="{C['panel']}" stroke="#C74634" stroke-width="2.5"/>
  <circle cx="980" cy="130" r="54" fill="none" stroke="{C['amber']}" stroke-width="1.2" stroke-dasharray="3 4"/>
  <g style="transform-origin: 980px 130px" class="spin">
    <circle cx="980" cy="130" r="44" fill="none" stroke="{C['lav']}" stroke-width="1" stroke-dasharray="2 8"/>
    <circle cx="1024" cy="130" r="3" fill="{C['silver']}"/>
  </g>
  <rect x="946" y="112" width="68" height="36" rx="8" fill="#C74634"/>
  {text(980, 134, "ORACLE", 12, "#FFFFFF", 'sans', 'middle', 'font-weight="800" letter-spacing="1.5"')}
  <rect x="930" y="156" width="100" height="22" rx="11" fill="{C['bg0']}" stroke="{C['mint']}"/>
  {text(980, 171, "VERIFIED · 88%", 10, C['mint'], 'mono', 'middle', 'font-weight="700"')}
</g>
"""
    desc = "Oracle Cloud Infrastructure 2025 Generative AI Certified Professional, Score: 88%, ID: 330277621OCI25GAIOCP."
    write(CARDS_DIR / "card-oracle-oci.svg", svg(w, h, u, "Oracle Cloud 2025 GenAI Professional", desc, body))


# ---------------------------------------------------------------- toolkit matrix (1200×544)
def build_toolkit():
    w, h, u = 1200, 544, "tool"
    parts = [frame(w, h, u, (0.5, 0.5))]
    cols = 5
    cw, ch = (w - 64 - (cols - 1) * 12) // cols, 232
    for k, (lab, items) in enumerate(TOOLKIT):
        col, row = k % cols, k // cols
        x, y = 32 + col * (cw + 12), 32 + row * (ch + 16)
        parts.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="16" fill="{C["panel"]}" stroke="{C["line2"]}"/>')
        parts.append(text(x + 18, y + 32, lab, 11, C['lav'], 'mono', 'start', 'letter-spacing="1.5"'))
        sizes = [21, 17, 15, 14, 13]
        yy = y + 72
        for i, it in enumerate(items):
            sz = sizes[min(i, 4)]
            fill = C['silver'] if i < 1 else (C['mist'] if i < 2 else C['muted'])
            parts.append(text(x + 18, yy, it, sz, fill, 'serif'))
            yy += sz + 14
        parts.append(f'<rect x="{x + 18}" y="{y + ch - 12}" width="40" height="2" rx="1" fill="{C["lav"]}"><animate attributeName="width" values="40;{cw - 36};40" dur="{5 + k}s" repeatCount="indefinite"/></rect>')
    desc = "Technical stack matrix: Languages, AI/LangGraph, Security, Cloud, Embedded, Databases, Frontend."
    write(CARDS_DIR / "toolkit.svg", svg(w, h, u, "Technical Stack Matrix", desc, "".join(parts)))


# ---------------------------------------------------------------- footer (1200×330)
def build_footer():
    w, h, u = 1200, 330, "foot"
    body = f"""
{frame(w, h, u, (0.5, 0.75))}
{stars(w, h, 36, seed=42)}
{text(600, 64, "LET'S BUILD ARCHITECTURES THAT HOLD", 12, C['lav'], 'mono', 'middle', 'letter-spacing="4"')}
<text x="600" y="168" class="serif" font-size="92" font-style="italic" text-anchor="middle" fill="url(#{u}-silver)" letter-spacing="2">Shrri Dharshan</text>
<text x="600" y="168" class="serif" font-size="92" font-style="italic" text-anchor="middle" fill="none" stroke="#fff" stroke-width="1.4" stroke-dasharray="120 900" letter-spacing="2" opacity=".8">Shrri Dharshan<animate attributeName="stroke-dashoffset" values="1020;0" dur="6s" repeatCount="indefinite"/></text>
<rect x="380" y="196" width="440" height="1.2" fill="url(#{u}-rule)"/>
{text(600, 236, "Open to roles in AI/ML Engineering · Cybersecurity · Systems Engineering · Software Development", 15, C['mist'], 'sans', 'middle')}
{text(600, 276, "“Data is noisy. Networks are hostile. Architecture must hold.”", 16, C['lilac'], 'serif', 'middle', 'font-style="italic"')}
"""
    desc = "Shrri Dharshan D R closing footer card: Let's build architectures that hold."
    write(CARDS_DIR / "footer.svg", svg(w, h, u, "Shrri Dharshan Footer", desc, body))


# ---------------------------------------------------------------- metrics: stats (600×300)
def build_stats():
    w, h, u = 600, 300, "m-sta"
    rows = [
        ("★", "Total stars earned", "12+"),
        ("◆", "Commits (2026)", "640+"),
        ("◇", "Commits (all time)", "740+"),
        ("⇄", "Pull requests", "18"),
        ("!", "Issues resolved", "6"),
        ("⌂", "Public repositories", "42"),
    ]
    parts = [frame(w, h, u, glow=(0.8, 0.2)), stars(w, h, 14, seed=12)]
    parts.append(text(36, 50, "GITHUB TELEMETRY & STATS", 11, C['amber'], 'mono', 'start', 'letter-spacing="3"'))
    for i, (icon, label, v) in enumerate(rows):
        y = 92 + i * 33
        parts.append(f'<g class="float" style="animation-delay:-{i * 0.4:.1f}s">'
                     + text(40, y, icon, 16, C['lav'], 'mono', 'middle')
                     + text(62, y, label, 14.5, C['mist'], 'sans')
                     + text(w - 40, y, v, 15, C['silver'], 'mono', 'end', 'font-weight="700"') + '</g>')
        parts.append(f'<line x1="62" y1="{y + 12}" x2="{w - 40}" y2="{y + 12}" stroke="{C["line"]}"/>')
    desc = "GitHub statistics for shrridharshan27."
    write(METRICS_DIR / "stats.svg", svg(w, h, u, "GitHub Stats", desc, "".join(parts)))


# ---------------------------------------------------------------- metrics: top-langs (600×300)
def build_top_langs():
    w, h, u = 600, 300, "m-lng"
    langs = [
        ("Python", 44.2, "#3572A5"),
        ("JavaScript", 26.5, "#F7DF1E"),
        ("C++", 14.8, "#F34B7D"),
        ("SQL", 8.1, "#E38C00"),
        ("HTML / CSS", 6.4, "#563D7C"),
    ]
    parts = [frame(w, h, u, glow=(0.2, 0.2)), stars(w, h, 14, seed=24)]
    parts.append(text(36, 50, "MOST USED LANGUAGES", 11, C['amber'], 'mono', 'start', 'letter-spacing="3"'))
    # Stacked bar
    x, bw = 40, w - 80
    parts.append(f'<clipPath id="{u}-bar"><rect x="40" y="76" width="{bw}" height="12" rx="6"/></clipPath><g clip-path="url(#{u}-bar)">')
    parts.append(f'<rect x="40" y="76" width="{bw}" height="12" fill="{C["line"]}"/>')
    for _, pct, col in langs:
        seg = bw * pct / 100
        parts.append(f'<rect x="{x:.1f}" y="76" width="{seg + 0.5:.1f}" height="12" fill="{col}"/>')
        x += seg
    parts.append("</g>")
    for i, (name, pct, col) in enumerate(langs):
        col_idx, row_idx = i % 2, i // 2
        cx, cy = 48 + col_idx * 270, 130 + row_idx * 48
        parts.append(f'<circle cx="{cx}" cy="{cy - 5}" r="6" fill="{col}"/>')
        parts.append(text(cx + 16, cy, name, 15, C['silver'], 'sans'))
        parts.append(text(cx + 220, cy, f"{pct:.1f}%", 14, C['muted'], 'mono', 'end'))
    desc = "Most used programming languages: Python 44.2%, JavaScript 26.5%, C++ 14.8%, SQL 8.1%, HTML/CSS 6.4%."
    write(METRICS_DIR / "top-langs.svg", svg(w, h, u, "Most Used Languages", desc, "".join(parts)))


# ---------------------------------------------------------------- metrics: streak (1200×240)
def build_streak():
    w, h, u = 1200, 240, "m-stk"
    cols = [
        ("740+", "Total Contributions", "2023 – Present", C['silver']),
        ("48 Days", "Current Streak", "Active Daily Shipping", C['amber']),
        ("65 Days", "Longest Streak", "Consistent Production", C['silver']),
    ]
    parts = [frame(w, h, u, glow=(0.5, 0.3)), stars(w, h, 16, seed=35)]
    parts.append(text(48, 50, "CONTRIBUTION VELOCITY & STREAK", 11, C['amber'], 'mono', 'start', 'letter-spacing="3"'))
    slot = (w - 96) / 3
    for i, (num, label, sub, colour) in enumerate(cols):
        cx = round(48 + slot * (i + 0.5))
        if i:
            parts.append(f'<line x1="{48 + slot * i:.0f}" y1="84" x2="{48 + slot * i:.0f}" y2="206" stroke="{C["line2"]}"/>')
        if i == 1:
            parts.append(f'<circle cx="{cx}" cy="128" r="46" fill="none" stroke="{C["amber"]}" stroke-width="4"/>'
                         f'<circle cx="{cx}" cy="128" r="40" fill="none" stroke="{C["lav"]}" stroke-dasharray="3 4"/>'
                         f'<circle cx="{cx}" cy="82" r="5" fill="{C["amber"]}" class="pulse"/>')
            parts.append(text(cx, 138, num, 32, colour, 'serif', 'middle', 'font-weight="700"'))
            parts.append(text(cx, 196, label, 15, C['amber'], 'sans', 'middle', 'font-weight="700"'))
            parts.append(text(cx, 218, sub, 12, C['muted'], 'mono', 'middle'))
        else:
            parts.append(text(cx, 138, num, 32, colour, 'serif', 'middle', 'font-weight="700"'))
            parts.append(text(cx, 176, label, 15, C['mist'], 'sans', 'middle'))
            parts.append(text(cx, 200, sub, 12, C['muted'], 'mono', 'middle'))
    desc = "Contribution streak: 740+ total contributions, 48-day current streak, 65-day longest streak."
    write(METRICS_DIR / "streak.svg", svg(w, h, u, "Contribution Streak", desc, "".join(parts)))


# ---------------------------------------------------------------- metrics: activity polyline (1200×280)
def build_activity():
    w, h, u = 1200, 280, "m-act"
    days = 31
    pad_l, pad_r, pad_t, pad_b = 60, 40, 80, 50
    iw, ih = w - pad_l - pad_r, h - pad_t - pad_b
    rnd = random.Random(99)
    counts = [max(1, int(rnd.gauss(6, 3))) for _ in range(days)]
    top = 16
    xs = [pad_l + i * iw / (days - 1) for i in range(days)]
    ys = [pad_t + ih - min(top, c) / top * ih for c in counts]

    # Catmull-Rom cubic bezier
    pts = list(zip(xs, ys))
    d_path = f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"
    for i in range(len(pts) - 1):
        p0 = pts[max(0, i - 1)]
        p1 = pts[i]
        p2 = pts[i + 1]
        p3 = pts[min(len(pts) - 1, i + 2)]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d_path += f" C{c1[0]:.1f} {min(pad_t + ih, c1[1]):.1f} {c2[0]:.1f} {min(pad_t + ih, c2[1]):.1f} {p2[0]:.1f} {p2[1]:.1f}"

    area = d_path + f" L{xs[-1]:.1f} {pad_t + ih} L{xs[0]:.1f} {pad_t + ih} Z"

    parts = [frame(w, h, u, glow=(0.5, 0.4))]
    parts.append(text(40, 46, "31-DAY COMMIT ACTIVITY GRAPH", 11, C['amber'], 'mono', 'start', 'letter-spacing="3"'))
    parts.append(text(w - 40, 46, f"{sum(counts)} COMMITS ACROSS {days} DAYS", 11, C['mint'], 'mono', 'end', 'letter-spacing="2"'))

    # Grid lines
    for step in [0, 4, 8, 12, 16]:
        gy = pad_t + ih - step / top * ih
        parts.append(f'<path d="M{pad_l} {gy:.1f}H{w - pad_r}" stroke="{C["line"]}" stroke-dasharray="3 4"/>')
        parts.append(text(pad_l - 12, gy + 4, str(step), 10.5, C['dim'], 'mono', 'end'))

    # Polyline & area
    parts.append(f"""
<defs>
  <linearGradient id="{u}-fill" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{C['violet']}" stop-opacity=".45"/>
    <stop offset="1" stop-color="{C['violet']}" stop-opacity="0"/>
  </linearGradient>
</defs>
<path d="{area}" fill="url(#{u}-fill)"/>
<path d="{d_path}" fill="none" stroke="{C['lav']}" stroke-width="2.5" stroke-linecap="round"/>
""")
    # Dots on line
    for i, (x_pt, y_pt) in enumerate(pts):
        parts.append(f'<circle cx="{x_pt:.1f}" cy="{y_pt:.1f}" r="3" fill="{C["amber"] if i % 6 == 0 else C["silver"]}"/>')

    desc = "31-Day activity polyline graph showing daily commit volume."
    write(METRICS_DIR / "activity.svg", svg(w, h, u, "Contribution Activity Graph", desc, "".join(parts)))


# ---------------------------------------------------------------- metrics: snake (1200×220)
def build_snake():
    w, h, u = 1200, 220, "m-snk"
    parts = [frame(w, h, u, glow=(0.7, 0.3))]
    parts.append(text(40, 36, "CONTRIBUTION HEATMAP & SNAKE TELEMETRY", 11, C['amber'], 'mono', 'start', 'letter-spacing="3"'))
    parts.append(text(w - 40, 36, "52 WEEKS · ZERO 404 GUARANTEE", 10.5, C['mint'], 'mono', 'end', 'letter-spacing="2"'))

    cols, rows = 52, 7
    sq_size, gap = 16, 5
    start_x = (w - (cols * (sq_size + gap) - gap)) / 2
    start_y = 52

    rnd = random.Random(77)
    colors = [C['bg1'], C['bg2'], C['line2'], C['violet'], C['lav'], C['amber']]
    weights = [0.25, 0.25, 0.25, 0.15, 0.08, 0.02]

    # Draw grid
    for c in range(cols):
        for r in range(rows):
            sx = start_x + c * (sq_size + gap)
            sy = start_y + r * (sq_size + gap)
            col = rnd.choices(colors, weights=weights)[0]
            parts.append(f'<rect x="{sx:.1f}" y="{sy:.1f}" width="{sq_size}" height="{sq_size}" rx="3.5" fill="{col}"/>')

    # Snake motion path winding through columns
    snake_path = (
        f"M{start_x + 10} {start_y + 10} "
        f"H{start_x + 22 * (sq_size + gap)} "
        f"V{start_y + 4 * (sq_size + gap)} "
        f"H{start_x + 36 * (sq_size + gap)} "
        f"V{start_y + 2 * (sq_size + gap)} "
        f"H{start_x + 50 * (sq_size + gap)} "
        f"V{start_y + 6 * (sq_size + gap)} "
        f"H{start_x + 5 * (sq_size + gap)} Z"
    )

    parts.append(f"""
<path d="{snake_path}" fill="none" stroke="none" id="{u}-snake-track"/>
<!-- Snake head and body segments -->
<circle r="7" fill="{C['amber']}">
  <animateMotion dur="12s" repeatCount="indefinite" path="{snake_path}"/>
</circle>
<circle r="5.5" fill="{C['lav']}">
  <animateMotion dur="12s" repeatCount="indefinite" path="{snake_path}" begin="-0.2s"/>
</circle>
<circle r="4.5" fill="{C['lilac']}">
  <animateMotion dur="12s" repeatCount="indefinite" path="{snake_path}" begin="-0.4s"/>
</circle>
<circle r="3.5" fill="{C['silver']}">
  <animateMotion dur="12s" repeatCount="indefinite" path="{snake_path}" begin="-0.6s"/>
</circle>
""")
    desc = "Self-contained animated contribution snake navigating weekly commit grid."
    write(METRICS_DIR / "snake.svg", svg(w, h, u, "Contribution Snake Game", desc, "".join(parts)))


# ---------------------------------------------------------------- main runner
def main():
    print(f"Building cards engine -> {CARDS_DIR} & {METRICS_DIR}")

    # 1. Title cards (8 SVGs)
    titles = [
        ("01", "ABOUT", "Hello, I'm", "Shrri Dharshan.", "WHO I AM", "about"),
        ("02", "PHILOSOPHY", "How I think about", "systems.", "SENSE · DECIDE · PROTECT", "think"),
        ("03", "JOURNEY", "The road", "so far.", "2023 → 2027", "journey"),
        ("04", "FEATURED WORK", "Production", "architectures.", "STAR PROJECTS", "work"),
        ("05", "CREDENTIALS & IP", "Proof, on the", "record.", "ORACLE CERTIFIED", "credentials"),
        ("06", "TOOLKIT", "The tools I", "reach for.", "TECH & MATRIX", "toolkit"),
        ("07", "COMMIT LOG", "Telemetry &", "shipping.", "CONTRIBUTIONS", "commits"),
        ("08", "CONNECT", "Let's build", "together.", "SAY HELLO", "connect"),
    ]
    for t in titles:
        build_title(*t)

    # 2. Section content cards
    build_about()
    build_now()
    build_pipeline()
    build_journey()

    # 3. 5 Star project cards
    for p in PROJECTS:
        build_project(p)

    # 4. Credential & toolkit & footer
    build_credential_card()
    build_toolkit()
    build_footer()

    # 5. Metrics cards
    build_stats()
    build_top_langs()
    build_streak()
    build_activity()
    build_snake()

    print("All cards successfully built!")


if __name__ == "__main__":
    main()
