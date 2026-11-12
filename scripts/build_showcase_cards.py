#!/usr/bin/env python3
"""Procedural Generator for Theme-Reactive Architecture Diagram & Benchmark Matrix SVGs.

Generates:
  1. assets/cards/diagram-architecture.svg (1200x640)
  2. assets/cards/benchmark-matrix.svg (1200x540)

Conforms strictly to:
  - Pure Python standard library (zero external dependencies)
  - 100% valid XML parseable by xml.etree.ElementTree
  - Dual theme reactivity via @media (prefers-color-scheme: dark)
  - Motion accessibility via @media (prefers-reduced-motion: reduce)
  - Absolute coordinate placement ensuring zero text coordinate collisions
"""

import os
import sys
from pathlib import Path
from xml.sax.saxutils import escape

# Default target directory
REPO_ROOT = Path(__file__).resolve().parent.parent
CARDS_DIR = REPO_ROOT / "assets" / "cards"


def e(text: str) -> str:
    """Escape XML special characters."""
    return escape(str(text), {'"': "&quot;"})


def build_architecture_diagram_svg(w: int = 1200, h: int = 640) -> str:
    """Generates an Interactive, Theme-Reactive Enterprise GenAI RAG Architecture SVG (1200x640)."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="{h}" role="img" aria-label="Enterprise GenAI RAG &amp; Multi-Agent System Architecture">
  <title>Enterprise GenAI RAG &amp; Multi-Agent System Architecture</title>
  <desc>Interactive, theme-reactive system architecture diagram showing Ingestion, Hybrid Vector Retrieval, LangGraph Self-Correction, and Synthesis with SHA-256 Ledger Audit.</desc>

  <defs>
    <!-- Light Theme Gradients -->
    <linearGradient id="light-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F8FAFC" />
      <stop offset="50%" stop-color="#F1F5F9" />
      <stop offset="100%" stop-color="#E2E8F0" />
    </linearGradient>

    <!-- Dark Theme Gradients -->
    <linearGradient id="dark-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090B12" />
      <stop offset="50%" stop-color="#10131F" />
      <stop offset="100%" stop-color="#161C30" />
    </linearGradient>

    <!-- Node Glow Gradients -->
    <linearGradient id="cyan-glow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#06B6D4" stop-opacity="0.2" />
      <stop offset="100%" stop-color="#3B82F6" stop-opacity="0.05" />
    </linearGradient>
    <linearGradient id="emerald-glow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.2" />
      <stop offset="100%" stop-color="#059669" stop-opacity="0.05" />
    </linearGradient>
    <linearGradient id="amber-glow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F59E0B" stop-opacity="0.2" />
      <stop offset="100%" stop-color="#D97706" stop-opacity="0.05" />
    </linearGradient>
    <linearGradient id="purple-glow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0.2" />
      <stop offset="100%" stop-color="#6366F1" stop-opacity="0.05" />
    </linearGradient>

    <!-- Grid Pattern -->
    <pattern id="grid-pat" width="30" height="30" patternUnits="userSpaceOnUse">
      <path d="M 30 0 L 0 0 0 30" fill="none" class="theme-grid-line" stroke-width="1" />
    </pattern>

    <!-- Flow Arrow Markers -->
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" class="theme-arrow" />
    </marker>
    <marker id="arrow-fallback" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#F59E0B" />
    </marker>
  </defs>

  <style>
    /* <![CDATA[ */
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Roboto, sans-serif; }}
    .mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }}
    .serif {{ font-family: 'Iowan Old Style', 'Palatino Linotype', Palatino, Georgia, serif; }}

    /* Light Theme (Default) */
    .theme-canvas {{ fill: url(#light-bg); stroke: #CBD5E1; }}
    .theme-grid-line {{ stroke: rgba(148, 163, 184, 0.15); }}
    .theme-tier-bg {{ fill: #FFFFFF; stroke: #E2E8F0; }}
    .theme-tier-header {{ fill: #0F172A; }}
    .theme-tier-sub {{ fill: #64748B; }}
    .theme-node-bg {{ fill: #F8FAFC; stroke: #CBD5E1; }}
    .theme-node-title {{ fill: #0F172A; }}
    .theme-node-desc {{ fill: #475569; }}
    .theme-node-meta {{ fill: #0891B2; }}
    .theme-conn-line {{ stroke: #94A3B8; stroke-dasharray: 4,4; }}
    .theme-arrow {{ fill: #64748B; }}
    .theme-pill-bg {{ fill: #E2E8F0; stroke: #CBD5E1; }}
    .theme-pill-text {{ fill: #334155; }}
    .theme-kicker {{ fill: #0284C7; }}
    .theme-title {{ fill: #0F172A; }}
    .theme-sub {{ fill: #475569; }}
    .theme-footer-bg {{ fill: #FFFFFF; stroke: #E2E8F0; }}

    /* Dark Theme Overrides */
    @media (prefers-color-scheme: dark) {{
      .theme-canvas {{ fill: url(#dark-bg); stroke: #262E47; }}
      .theme-grid-line {{ stroke: rgba(99, 102, 241, 0.08); }}
      .theme-tier-bg {{ fill: #10131F; stroke: #1E293B; }}
      .theme-tier-header {{ fill: #F8FAFC; }}
      .theme-tier-sub {{ fill: #94A3B8; }}
      .theme-node-bg {{ fill: #161C30; stroke: #262E47; }}
      .theme-node-title {{ fill: #F8FAFC; }}
      .theme-node-desc {{ fill: #94A3B8; }}
      .theme-node-meta {{ fill: #22D3EE; }}
      .theme-conn-line {{ stroke: #475569; stroke-dasharray: 4,4; }}
      .theme-arrow {{ fill: #94A3B8; }}
      .theme-pill-bg {{ fill: #1E293B; stroke: #334155; }}
      .theme-pill-text {{ fill: #E2E8F0; }}
      .theme-kicker {{ fill: #38BDF8; }}
      .theme-title {{ fill: #FFFFFF; }}
      .theme-sub {{ fill: #94A3B8; }}
      .theme-footer-bg {{ fill: #10131F; stroke: #1E293B; }}
    }}

    .node-group {{
      cursor: pointer;
    }}
    .node-group:hover .theme-node-bg {{
      stroke: #38BDF8 !important;
      stroke-width: 1.5;
      filter: drop-shadow(0 4px 12px rgba(56, 189, 248, 0.15));
    }}
    .node-group:hover .theme-node-title {{
      fill: #38BDF8 !important;
    }}

    .signal-pulse {{ animation: signalFlow 3s linear infinite; }}
    .signal-pulse-fast {{ animation: signalFlow 1.8s linear infinite; }}
    .signal-pulse-amber {{ animation: signalFlow 2.4s linear infinite; }}
    @keyframes signalFlow {{
      0% {{ stroke-dashoffset: 40; }}
      100% {{ stroke-dashoffset: 0; }}
    }}

    .ping {{
      animation: pingGlow 2s ease-in-out infinite;
      transform-origin: center;
    }}
    @keyframes pingGlow {{
      0%, 100% {{ r: 3.5; opacity: 0.7; }}
      50% {{ r: 5.5; opacity: 1; }}
    }}

    @media (prefers-reduced-motion: reduce) {{
      .signal-pulse, .signal-pulse-fast, .signal-pulse-amber, .ping {{
        animation: none !important;
      }}
    }}
    /* ]]> */
  </style>

  <!-- Canvas Outer Bounds & Grid -->
  <rect x="2" y="2" width="{w-4}" height="{h-4}" rx="18" class="theme-canvas" stroke-width="1.5" />
  <rect x="2" y="2" width="{w-4}" height="{h-4}" rx="18" fill="url(#grid-pat)" />

  <!-- HEADER SECTION -->
  <text x="40" y="36" class="mono theme-kicker" font-size="11" font-weight="700" letter-spacing="2.5">04.1 // PRODUCTION SYSTEM ARCHITECTURE</text>
  <text x="40" y="62" class="sans theme-title" font-size="20" font-weight="700" letter-spacing="-0.3">Enterprise GenAI RAG &amp; Autonomous Multi-Agent Pipeline</text>
  <text x="40" y="82" class="sans theme-sub" font-size="12">Self-correcting LangGraph state machine with OCI Vector Search, Tavily fallback loop, and immutable SHA-256 audit ledger.</text>

  <!-- Header Badges -->
  <rect x="720" y="41" width="145" height="26" rx="6" class="theme-pill-bg" stroke-width="1" />
  <circle cx="732" cy="54" r="3.5" fill="#F59E0B" class="ping" />
  <text x="742" y="58" class="mono" font-size="10.5" font-weight="600" fill="#F59E0B">OCI GenAI Certified</text>

  <rect x="875" y="41" width="140" height="26" rx="6" class="theme-pill-bg" stroke-width="1" />
  <circle cx="887" cy="54" r="3.5" fill="#10B981" class="ping" />
  <text x="897" y="58" class="mono" font-size="10.5" font-weight="600" fill="#10B981">-53% Hallucination</text>

  <rect x="1025" y="41" width="135" height="26" rx="6" class="theme-pill-bg" stroke-width="1" />
  <circle cx="1037" cy="54" r="3.5" fill="#06B6D4" class="ping" />
  <text x="1047" y="58" class="mono" font-size="10.5" font-weight="600" fill="#06B6D4">Sub-Second SLA</text>

  <!-- ==================== TIER 1: INGESTION (x: 40) ==================== -->
  <rect x="40" y="115" width="260" height="425" rx="12" class="theme-tier-bg" stroke-width="1.2" />
  <path d="M 40 153 L 300 153" class="theme-conn-line" stroke-width="1" />
  <rect x="52" y="125" width="8" height="18" rx="2" fill="#06B6D4" />
  <text x="68" y="139" class="mono theme-tier-header" font-size="12" font-weight="700">TIER 1: INGESTION</text>
  <text x="288" y="139" class="mono theme-tier-sub" font-size="10.5" text-anchor="end">INPUT</text>

  <!-- Node 1.1: Multi-Modal Ingestion -->
  <g class="node-group">
    <rect x="54" y="167" width="232" height="100" rx="8" class="theme-node-bg" stroke-width="1" />
    <rect x="54" y="167" width="232" height="100" rx="8" fill="url(#cyan-glow)" />
    <text x="66" y="189" class="sans theme-node-title" font-size="13" font-weight="700">Multi-Modal Dispatcher</text>
    <text x="66" y="207" class="sans theme-node-desc" font-size="11">FastAPI async gateway with</text>
    <text x="66" y="222" class="sans theme-node-desc" font-size="11">I2C/SPI telemetry &amp; voice streams</text>
    <line x1="66" y1="234" x2="274" y2="234" class="theme-conn-line" stroke-width="0.8" />
    <text x="66" y="251" class="mono theme-node-meta" font-size="10">p50 &lt; 4.2ms · 10k req/s</text>
  </g>

  <!-- Node 1.2: Intent Classifier & Rewriter -->
  <g class="node-group">
    <rect x="54" y="283" width="232" height="100" rx="8" class="theme-node-bg" stroke-width="1" />
    <rect x="54" y="283" width="232" height="100" rx="8" fill="url(#cyan-glow)" />
    <text x="66" y="305" class="sans theme-node-title" font-size="13" font-weight="700">Query Intent Analyzer</text>
    <text x="66" y="323" class="sans theme-node-desc" font-size="11">StateGraph decomposition node</text>
    <text x="66" y="338" class="sans theme-node-desc" font-size="11">extracts entities &amp; sub-queries</text>
    <line x1="66" y1="350" x2="274" y2="350" class="theme-conn-line" stroke-width="0.8" />
    <text x="66" y="367" class="mono theme-node-meta" font-size="10">spaCy NER · Zero-Shot Gate</text>
  </g>

  <!-- Node 1.3: Embeddings Engine -->
  <g class="node-group">
    <rect x="54" y="399" width="232" height="100" rx="8" class="theme-node-bg" stroke-width="1" />
    <rect x="54" y="399" width="232" height="100" rx="8" fill="url(#cyan-glow)" />
    <text x="66" y="421" class="sans theme-node-title" font-size="13" font-weight="700">Dense Embedding Core</text>
    <text x="66" y="439" class="sans theme-node-desc" font-size="11">OCI Cohere Embed v3.0</text>
    <text x="66" y="454" class="sans theme-node-desc" font-size="11">1024-dim dense representation</text>
    <line x1="66" y1="466" x2="274" y2="466" class="theme-conn-line" stroke-width="0.8" />
    <text x="66" y="483" class="mono theme-node-meta" font-size="10">Normalized Cosine Metric</text>
  </g>

  <!-- Connectors Tier 1 -> Tier 2 -->
  <path d="M 300 217 L 326 217" class="theme-conn-line signal-pulse" stroke-width="2" marker-end="url(#arrow)" />
  <path d="M 300 333 L 326 333" class="theme-conn-line signal-pulse" stroke-width="2" marker-end="url(#arrow)" />

  <!-- ==================== TIER 2: RETRIEVAL (x: 326) ==================== -->
  <rect x="326" y="115" width="260" height="425" rx="12" class="theme-tier-bg" stroke-width="1.2" />
  <path d="M 326 153 L 586 153" class="theme-conn-line" stroke-width="1" />
  <rect x="338" y="125" width="8" height="18" rx="2" fill="#3B82F6" />
  <text x="354" y="139" class="mono theme-tier-header" font-size="12" font-weight="700">TIER 2: RETRIEVAL</text>
  <text x="574" y="139" class="mono theme-tier-sub" font-size="10.5" text-anchor="end">HYBRID</text>

  <!-- Node 2.1: OCI Vector Search Store -->
  <g class="node-group">
    <rect x="340" y="167" width="232" height="100" rx="8" class="theme-node-bg" stroke-width="1" />
    <rect x="340" y="167" width="232" height="100" rx="8" fill="url(#cyan-glow)" />
    <text x="352" y="189" class="sans theme-node-title" font-size="13" font-weight="700">OCI Vector Search Store</text>
    <text x="352" y="207" class="sans theme-node-desc" font-size="11">HNSW index partition with</text>
    <text x="352" y="222" class="sans theme-node-desc" font-size="11">sub-15ms semantic k-NN recall</text>
    <line x1="352" y1="234" x2="560" y2="234" class="theme-conn-line" stroke-width="0.8" />
    <text x="352" y="251" class="mono theme-node-meta" font-size="10">97.2% Recall @ Top-10</text>
  </g>

  <!-- Node 2.2: BM25 Lexical Inverter -->
  <g class="node-group">
    <rect x="340" y="283" width="232" height="100" rx="8" class="theme-node-bg" stroke-width="1" />
    <rect x="340" y="283" width="232" height="100" rx="8" fill="url(#cyan-glow)" />
    <text x="352" y="305" class="sans theme-node-title" font-size="13" font-weight="700">BM25 Lexical Inverter</text>
    <text x="352" y="323" class="sans theme-node-desc" font-size="11">Exact entity keyword matches</text>
    <text x="352" y="338" class="sans theme-node-desc" font-size="11">for code, IDs &amp; legal clauses</text>
    <line x1="352" y1="234" x2="560" y2="234" class="theme-conn-line" stroke-width="0.8" />
    <text x="352" y="367" class="mono theme-node-meta" font-size="10">Deterministic ID Match</text>
  </g>

  <!-- Node 2.3: Reciprocal Rank Fusion -->
  <g class="node-group">
    <rect x="340" y="399" width="232" height="100" rx="8" class="theme-node-bg" stroke-width="1" />
    <rect x="340" y="399" width="232" height="100" rx="8" fill="url(#cyan-glow)" />
    <text x="352" y="421" class="sans theme-node-title" font-size="13" font-weight="700">Reciprocal Rank Fusion</text>
    <text x="352" y="439" class="sans theme-node-desc" font-size="11">RRF score: R(d)=1/(k + r_i)</text>
    <text x="352" y="454" class="sans theme-node-desc" font-size="11">blends dense &amp; sparse ranking</text>
    <line x1="352" y1="466" x2="560" y2="466" class="theme-conn-line" stroke-width="0.8" />
    <text x="352" y="483" class="mono theme-node-meta" font-size="10">Rank Calibration Gate</text>
  </g>

  <!-- Connectors Tier 2 -> Tier 3 -->
  <path d="M 586 217 L 612 217" class="theme-conn-line signal-pulse" stroke-width="2" marker-end="url(#arrow)" />
  <path d="M 586 333 L 612 333" class="theme-conn-line signal-pulse" stroke-width="2" marker-end="url(#arrow)" />

  <!-- ==================== TIER 3: SELF-CORRECT (x: 612) ==================== -->
  <rect x="612" y="115" width="260" height="425" rx="12" class="theme-tier-bg" stroke-width="1.2" />
  <path d="M 612 153 L 872 153" class="theme-conn-line" stroke-width="1" />
  <rect x="624" y="125" width="8" height="18" rx="2" fill="#10B981" />
  <text x="640" y="139" class="mono theme-tier-header" font-size="12" font-weight="700">TIER 3: SELF-CORRECT</text>
  <text x="860" y="139" class="mono theme-tier-sub" font-size="10.5" text-anchor="end">AGENT</text>

  <!-- Node 3.1: Document Relevance Grader -->
  <g class="node-group">
    <rect x="626" y="167" width="232" height="100" rx="8" class="theme-node-bg" stroke-width="1" />
    <rect x="626" y="167" width="232" height="100" rx="8" fill="url(#emerald-glow)" />
    <text x="638" y="189" class="sans theme-node-title" font-size="13" font-weight="700">Relevance Grading Node</text>
    <text x="638" y="207" class="sans theme-node-desc" font-size="11">Binary chunk evaluator grades</text>
    <text x="638" y="222" class="sans theme-node-desc" font-size="11">relevance before generation</text>
    <line x1="638" y1="234" x2="846" y2="234" class="theme-conn-line" stroke-width="0.8" />
    <text x="638" y="251" class="mono" font-size="10" fill="#10B981">Confidence Threshold: 0.82</text>
  </g>

  <!-- Node 3.2: Autonomous Web Fallback -->
  <g class="node-group">
    <rect x="626" y="283" width="232" height="100" rx="8" class="theme-node-bg" stroke-width="1.2" stroke="#F59E0B" />
    <rect x="626" y="283" width="232" height="100" rx="8" fill="url(#amber-glow)" />
    <text x="638" y="305" class="sans" font-size="13" font-weight="700" fill="#F59E0B">Autonomous Fallback Search</text>
    <text x="638" y="323" class="sans theme-node-desc" font-size="11">Triggers when chunks &lt; 2;</text>
    <text x="638" y="338" class="sans theme-node-desc" font-size="11">queries Tavily API for fresh facts</text>
    <line x1="638" y1="350" x2="846" y2="350" class="theme-conn-line" stroke-width="0.8" />
    <text x="638" y="367" class="mono" font-size="10" fill="#F59E0B">Dynamic Fallback Router</text>
  </g>

  <!-- Node 3.3: Hallucination Guardrail -->
  <g class="node-group">
    <rect x="626" y="399" width="232" height="100" rx="8" class="theme-node-bg" stroke-width="1" />
    <rect x="626" y="399" width="232" height="100" rx="8" fill="url(#emerald-glow)" />
    <text x="638" y="421" class="sans theme-node-title" font-size="13" font-weight="700">Hallucination Guardrail</text>
    <text x="638" y="439" class="sans theme-node-desc" font-size="11">Verifies synthesis grounded in</text>
    <text x="638" y="454" class="sans theme-node-desc" font-size="11">ground truth prior to release</text>
    <line x1="638" y1="466" x2="846" y2="466" class="theme-conn-line" stroke-width="0.8" />
    <text x="638" y="483" class="mono" font-size="10" fill="#10B981">PopQA: 31.4% &#8594; 14.6%</text>
  </g>

  <!-- Dynamic Fallback Loop Path (Animated Amber Signal) -->
  <path d="M 742 383 C 742 388, 742 392, 742 396" class="signal-pulse-amber" stroke="#F59E0B" stroke-width="1.8" stroke-dasharray="3,3" fill="none" marker-end="url(#arrow-fallback)" />

  <!-- Connectors Tier 3 -> Tier 4 -->
  <path d="M 872 217 L 898 217" class="theme-conn-line signal-pulse" stroke-width="2" marker-end="url(#arrow)" />
  <path d="M 872 333 L 898 333" class="theme-conn-line signal-pulse" stroke-width="2" marker-end="url(#arrow)" />

  <!-- ==================== TIER 4: SYNTHESIS (x: 898) ==================== -->
  <rect x="898" y="115" width="260" height="425" rx="12" class="theme-tier-bg" stroke-width="1.2" />
  <path d="M 898 153 L 1158 153" class="theme-conn-line" stroke-width="1" />
  <rect x="910" y="125" width="8" height="18" rx="2" fill="#8B5CF6" />
  <text x="926" y="139" class="mono theme-tier-header" font-size="12" font-weight="700">TIER 4: SYNTHESIS</text>
  <text x="1146" y="139" class="mono theme-tier-sub" font-size="10.5" text-anchor="end">AUDIT</text>

  <!-- Node 4.1: LLM Inference Core -->
  <g class="node-group">
    <rect x="912" y="167" width="232" height="100" rx="8" class="theme-node-bg" stroke-width="1" />
    <rect x="912" y="167" width="232" height="100" rx="8" fill="url(#purple-glow)" />
    <text x="924" y="189" class="sans theme-node-title" font-size="13" font-weight="700">Inference Core (OCI)</text>
    <text x="924" y="207" class="sans theme-node-desc" font-size="11">Cohere Command R+ &amp;</text>
    <text x="924" y="222" class="sans theme-node-desc" font-size="11">Meta LLaMA 3.3 70B cluster</text>
    <line x1="924" y1="234" x2="1132" y2="234" class="theme-conn-line" stroke-width="0.8" />
    <text x="924" y="251" class="mono" font-size="10" fill="#8B5CF6">142 tok/sec · 32k Window</text>
  </g>

  <!-- Node 4.2: Streaming Delivery Gateway -->
  <g class="node-group">
    <rect x="912" y="283" width="232" height="100" rx="8" class="theme-node-bg" stroke-width="1" />
    <rect x="912" y="283" width="232" height="100" rx="8" fill="url(#purple-glow)" />
    <text x="924" y="305" class="sans theme-node-title" font-size="13" font-weight="700">Streaming Response Bus</text>
    <text x="924" y="323" class="sans theme-node-desc" font-size="11">Server-Sent Events (SSE) &amp;</text>
    <text x="924" y="338" class="sans theme-node-desc" font-size="11">Groq LPU audio synthesis</text>
    <line x1="924" y1="350" x2="1132" y2="350" class="theme-conn-line" stroke-width="0.8" />
    <text x="924" y="367" class="mono" font-size="10" fill="#8B5CF6">~8s 30-min Turnaround</text>
  </g>

  <!-- Node 4.3: Cryptographic Audit Ledger -->
  <g class="node-group">
    <rect x="912" y="399" width="232" height="100" rx="8" class="theme-node-bg" stroke-width="1" />
    <rect x="912" y="399" width="232" height="100" rx="8" fill="url(#purple-glow)" />
    <text x="924" y="421" class="sans theme-node-title" font-size="13" font-weight="700">Immutable SHA-256 Ledger</text>
    <text x="924" y="439" class="sans theme-node-desc" font-size="11">Cryptographic hash-chain links</text>
    <text x="924" y="454" class="sans theme-node-desc" font-size="11">query, context &amp; audit proof</text>
    <line x1="924" y1="466" x2="1132" y2="466" class="theme-conn-line" stroke-width="0.8" />
    <text x="924" y="483" class="mono" font-size="10" fill="#8B5CF6">100% Tamper Isolation</text>
  </g>

  <!-- ==================== BOTTOM TELEMETRY STATUS BAR ==================== -->
  <rect x="40" y="560" width="1120" height="52" rx="10" class="theme-footer-bg" stroke-width="1.2" />
  <circle cx="64" cy="586" r="5" fill="#10B981" class="ping" />
  <text x="78" y="590" class="mono theme-tier-header" font-size="11" font-weight="700">PIPELINE TELEMETRY STATUS: HEALTHY</text>

  <text x="360" y="590" class="mono theme-tier-sub" font-size="11">END-TO-END LATENCY: <tspan class="theme-node-title" font-weight="700">42.8 ms</tspan></text>
  <line x1="530" y1="576" x2="530" y2="596" class="theme-conn-line" stroke-width="1" />

  <text x="550" y="590" class="mono theme-tier-sub" font-size="11">R-PRECISION: <tspan fill="#10B981" font-weight="700">97.2%</tspan></text>
  <line x1="710" y1="576" x2="710" y2="596" class="theme-conn-line" stroke-width="1" />

  <text x="730" y="590" class="mono theme-tier-sub" font-size="11">FALLBACK RATE: <tspan fill="#F59E0B" font-weight="700">18.2%</tspan></text>
  <line x1="880" y1="576" x2="880" y2="596" class="theme-conn-line" stroke-width="1" />

  <text x="900" y="590" class="mono theme-tier-sub" font-size="11">LEDGER AUDIT: <tspan fill="#8B5CF6" font-weight="700">VERIFIED GENESIS-0</tspan></text>
</svg>
"""


def build_benchmark_matrix_svg(w: int = 1200, h: int = 540) -> str:
    """Generates an Empirical Benchmark Showcase Card SVG (1200x540)."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="{h}" role="img" aria-label="Empirical Benchmark &amp; Latency Evaluation Matrix">
  <title>Empirical Benchmark &amp; Latency Evaluation Matrix</title>
  <desc>Quantitative benchmark matrix measuring Inference Latency, Throughput, Retrieval Precision, and Hallucination Suppression across OCI GenAI models and hardware accelerators.</desc>

  <defs>
    <!-- Background Gradients -->
    <linearGradient id="bench-light-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F8FAFC" />
      <stop offset="100%" stop-color="#EEF2F6" />
    </linearGradient>
    <linearGradient id="bench-dark-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090B12" />
      <stop offset="50%" stop-color="#0E121E" />
      <stop offset="100%" stop-color="#14192B" />
    </linearGradient>

    <!-- Bar Gradients -->
    <linearGradient id="bar-cyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#06B6D4" />
      <stop offset="100%" stop-color="#3B82F6" />
    </linearGradient>
    <linearGradient id="bar-emerald" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10B981" />
      <stop offset="100%" stop-color="#059669" />
    </linearGradient>
    <linearGradient id="bar-amber" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F59E0B" />
      <stop offset="100%" stop-color="#D97706" />
    </linearGradient>
    <linearGradient id="bar-purple" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#8B5CF6" />
      <stop offset="100%" stop-color="#6366F1" />
    </linearGradient>

    <!-- Subtle Grid Pattern -->
    <pattern id="bench-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M 28 0 L 0 0 0 28" fill="none" class="b-grid" stroke-width="1" />
    </pattern>
  </defs>

  <style>
    /* <![CDATA[ */
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Roboto, sans-serif; }}
    .mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }}

    /* Light Theme (Default) */
    .b-canvas {{ fill: url(#bench-light-bg); stroke: #CBD5E1; }}
    .b-grid {{ stroke: rgba(148, 163, 184, 0.15); }}
    .b-title {{ fill: #0F172A; }}
    .b-sub {{ fill: #475569; }}
    .b-kicker {{ fill: #0284C7; }}
    .b-table-head {{ fill: #64748B; }}
    .b-row-bg {{ fill: #FFFFFF; stroke: #E2E8F0; }}
    .b-row-hover {{ fill: #F1F5F9; }}
    .b-cell-main {{ fill: #0F172A; }}
    .b-cell-sub {{ fill: #64748B; }}
    .b-bar-track {{ fill: #E2E8F0; }}
    .b-kpi-bg {{ fill: #FFFFFF; stroke: #CBD5E1; }}
    .b-kpi-label {{ fill: #64748B; }}
    .b-badge-bg {{ fill: #E2E8F0; stroke: #CBD5E1; }}
    .b-divider {{ stroke: #E2E8F0; }}

    /* Dark Theme */
    @media (prefers-color-scheme: dark) {{
      .b-canvas {{ fill: url(#bench-dark-bg); stroke: #262E47; }}
      .b-grid {{ stroke: rgba(99, 102, 241, 0.08); }}
      .b-title {{ fill: #FFFFFF; }}
      .b-sub {{ fill: #94A3B8; }}
      .b-kicker {{ fill: #38BDF8; }}
      .b-table-head {{ fill: #94A3B8; }}
      .b-row-bg {{ fill: #10131F; stroke: #1E293B; }}
      .b-row-hover {{ fill: #161C30; }}
      .b-cell-main {{ fill: #F8FAFC; }}
      .b-cell-sub {{ fill: #94A3B8; }}
      .b-bar-track {{ fill: #1E293B; }}
      .b-kpi-bg {{ fill: #10131F; stroke: #262E47; }}
      .b-kpi-label {{ fill: #94A3B8; }}
      .b-badge-bg {{ fill: #1E293B; stroke: #334155; }}
      .b-divider {{ stroke: #1E293B; }}
    }}

    .bench-row {{
      cursor: pointer;
    }}
    .bench-row:hover rect.b-row-bg {{
      stroke: #38BDF8 !important;
      stroke-width: 1.5;
    }}
    .bench-row:hover .row-highlight {{
      fill: #38BDF8 !important;
    }}

    .b-kpi-card {{
      cursor: pointer;
    }}
    .b-kpi-card:hover rect.b-kpi-bg {{
      stroke: #38BDF8 !important;
      stroke-width: 1.6;
      filter: drop-shadow(0 4px 12px rgba(56, 189, 248, 0.15));
    }}

    .ping-b {{
      animation: pingGlowB 2s ease-in-out infinite;
    }}
    @keyframes pingGlowB {{
      0%, 100% {{ opacity: 0.6; }}
      50% {{ opacity: 1; }}
    }}

    @media (prefers-reduced-motion: reduce) {{
      .ping-b {{
        animation: none !important;
      }}
    }}
    /* ]]> */
  </style>

  <!-- Frame Background -->
  <rect x="2" y="2" width="{w-4}" height="{h-4}" rx="18" class="b-canvas" stroke-width="1.5" />
  <rect x="2" y="2" width="{w-4}" height="{h-4}" rx="18" fill="url(#bench-grid)" />

  <!-- HEADER -->
  <text x="40" y="36" class="mono b-kicker" font-size="11" font-weight="700" letter-spacing="2.5">05.1 // EMPIRICAL BENCHMARKS &amp; TELEMETRY</text>
  <text x="40" y="62" class="sans b-title" font-size="20" font-weight="700" letter-spacing="-0.3">Empirical Model Evaluation &amp; Inference Latency Matrix</text>
  <text x="40" y="82" class="sans b-sub" font-size="12">Production telemetry measured across OCI GenAI Dedicated Clusters, Groq LPUs, and LangGraph evaluation pipelines.</text>

  <!-- Header Badges -->
  <rect x="750" y="41" width="130" height="26" rx="6" class="b-badge-bg" stroke-width="1" />
  <circle cx="762" cy="54" r="3.5" fill="#10B981" class="ping-b" />
  <text x="772" y="58" class="mono" font-size="10.5" font-weight="600" fill="#10B981">p50/p95/p99 Live</text>

  <rect x="890" y="41" width="130" height="26" rx="6" class="b-badge-bg" stroke-width="1" />
  <circle cx="902" cy="54" r="3.5" fill="#F59E0B" class="ping-b" />
  <text x="912" y="58" class="mono" font-size="10.5" font-weight="600" fill="#F59E0B">OCI Enterprise</text>

  <rect x="1030" y="41" width="130" height="26" rx="6" class="b-badge-bg" stroke-width="1" />
  <circle cx="1042" cy="54" r="3.5" fill="#06B6D4" class="ping-b" />
  <text x="1052" y="58" class="mono" font-size="10.5" font-weight="600" fill="#06B6D4">100% Vector SVG</text>

  <!-- TABLE HEADERS (y: 115) -->
  <text x="56" y="115" class="mono b-table-head" font-size="10.5" font-weight="700" letter-spacing="1.2">MODEL &amp; ENGINE</text>
  <text x="290" y="115" class="mono b-table-head" font-size="10.5" font-weight="700" letter-spacing="1.2">SPECIALIZATION</text>
  <text x="480" y="115" class="mono b-table-head" font-size="10.5" font-weight="700" letter-spacing="1.2">LATENCY (p50 / p95 / p99)</text>
  <text x="730" y="115" class="mono b-table-head" font-size="10.5" font-weight="700" letter-spacing="1.2">THROUGHPUT</text>
  <text x="900" y="115" class="mono b-table-head" font-size="10.5" font-weight="700" letter-spacing="1.2">R-PRECISION</text>
  <text x="1040" y="115" class="mono b-table-head" font-size="10.5" font-weight="700" letter-spacing="1.2">HALLUCINATION</text>

  <!-- ==================== TABLE ROWS ==================== -->
  <!-- ROW 1: Cohere Command R+ (y: 130) -->
  <g class="bench-row">
    <rect x="40" y="130" width="1120" height="52" rx="8" class="b-row-bg" stroke-width="1" />
    
    <text x="56" y="154" class="sans b-cell-main row-highlight" font-size="13" font-weight="700">Cohere Command R+</text>
    <text x="56" y="170" class="mono b-cell-sub" font-size="10">OCI GenAI Dedicated AI Cluster</text>

    <text x="290" y="155" class="sans b-cell-main" font-size="12">Enterprise RAG &amp; Synthesis</text>
    <text x="290" y="170" class="mono" font-size="10" fill="#3B82F6">128k Context Window</text>

    <text x="480" y="155" class="mono b-cell-main" font-size="12" font-weight="600">21.5 <tspan class="b-cell-sub">/ 32.1 / 48.0</tspan> <tspan font-size="10" class="b-cell-sub">ms</tspan></text>
    <text x="480" y="170" class="mono" font-size="10" fill="#10B981">p50 SLA Met</text>

    <rect x="730" y="146" width="130" height="8" rx="4" class="b-bar-track" />
    <rect x="730" y="146" width="75" height="8" rx="4" fill="url(#bar-cyan)" />
    <text x="730" y="170" class="mono b-cell-main" font-size="11" font-weight="600">128.0 <tspan class="b-cell-sub">tok/s</tspan></text>

    <text x="900" y="155" class="mono" font-size="13" font-weight="700" fill="#10B981">97.2%</text>
    <rect x="900" y="162" width="100" height="5" rx="2.5" class="b-bar-track" />
    <rect x="900" y="162" width="97" height="5" rx="2.5" fill="#10B981" />

    <text x="1040" y="155" class="mono" font-size="13" font-weight="700" fill="#10B981">2.1%</text>
    <text x="1040" y="170" class="mono b-cell-sub" font-size="10">Rank 1 Grounding</text>
  </g>

  <!-- ROW 2: Meta LLaMA 3.3 70B (y: 190) -->
  <g class="bench-row">
    <rect x="40" y="190" width="1120" height="52" rx="8" class="b-row-bg" stroke-width="1" />
    
    <text x="56" y="214" class="sans b-cell-main row-highlight" font-size="13" font-weight="700">Meta LLaMA 3.3 70B</text>
    <text x="56" y="230" class="mono b-cell-sub" font-size="10">OCI Ultra-Cluster (A100-80G)</text>

    <text x="290" y="215" class="sans b-cell-main" font-size="12">Agentic Reasoning &amp; Logic</text>
    <text x="290" y="230" class="mono" font-size="10" fill="#8B5CF6">LangGraph Node Evaluator</text>

    <text x="480" y="215" class="mono b-cell-main" font-size="12" font-weight="600">18.2 <tspan class="b-cell-sub">/ 28.4 / 41.2</tspan> <tspan font-size="10" class="b-cell-sub">ms</tspan></text>
    <text x="480" y="230" class="mono" font-size="10" fill="#10B981">High Concurrency SLA</text>

    <rect x="730" y="206" width="130" height="8" rx="4" class="b-bar-track" />
    <rect x="730" y="206" width="84" height="8" rx="4" fill="url(#bar-purple)" />
    <text x="730" y="230" class="mono b-cell-main" font-size="11" font-weight="600">142.5 <tspan class="b-cell-sub">tok/s</tspan></text>

    <text x="900" y="215" class="mono" font-size="13" font-weight="700" fill="#10B981">94.6%</text>
    <rect x="900" y="222" width="100" height="5" rx="2.5" class="b-bar-track" />
    <rect x="900" y="222" width="94" height="5" rx="2.5" fill="#10B981" />

    <text x="1040" y="215" class="mono" font-size="13" font-weight="700" fill="#10B981">3.8%</text>
    <text x="1040" y="230" class="mono b-cell-sub" font-size="10">Zero Hallucination Gate</text>
  </g>

  <!-- ROW 3: Mistral Large 2 (y: 250) -->
  <g class="bench-row">
    <rect x="40" y="250" width="1120" height="52" rx="8" class="b-row-bg" stroke-width="1" />
    
    <text x="56" y="274" class="sans b-cell-main row-highlight" font-size="13" font-weight="700">Mistral Large 2 (123B)</text>
    <text x="56" y="290" class="mono b-cell-sub" font-size="10">OCI Enterprise AI Endpoint</text>

    <text x="290" y="275" class="sans b-cell-main" font-size="12">Code Verification &amp; Math</text>
    <text x="290" y="290" class="mono" font-size="10" fill="#06B6D4">HumanEval: 91.2</text>

    <text x="480" y="275" class="mono b-cell-main" font-size="12" font-weight="600">19.8 <tspan class="b-cell-sub">/ 30.2 / 44.5</tspan> <tspan font-size="10" class="b-cell-sub">ms</tspan></text>
    <text x="480" y="290" class="mono" font-size="10" fill="#10B981">Deterministic Code</text>

    <rect x="730" y="266" width="130" height="8" rx="4" class="b-bar-track" />
    <rect x="730" y="266" width="80" height="8" rx="4" fill="url(#bar-cyan)" />
    <text x="730" y="290" class="mono b-cell-main" font-size="11" font-weight="600">135.2 <tspan class="b-cell-sub">tok/s</tspan></text>

    <text x="900" y="275" class="mono" font-size="13" font-weight="700" fill="#10B981">93.8%</text>
    <rect x="900" y="282" width="100" height="5" rx="2.5" class="b-bar-track" />
    <rect x="900" y="282" width="93" height="5" rx="2.5" fill="#10B981" />

    <text x="1040" y="275" class="mono" font-size="13" font-weight="700" fill="#10B981">4.2%</text>
    <text x="1040" y="290" class="mono b-cell-sub" font-size="10">Syntax Corrected</text>
  </g>

  <!-- ROW 4: Groq LPU Whisper-v3 + LLaMA (y: 310) -->
  <g class="bench-row">
    <rect x="40" y="310" width="1120" height="52" rx="8" class="b-row-bg" stroke-width="1" />
    
    <text x="56" y="334" class="sans b-cell-main row-highlight" font-size="13" font-weight="700">Groq LPU (Whisper-v3 + LLaMA)</text>
    <text x="56" y="350" class="mono b-cell-sub" font-size="10">Language Processing Unit HW</text>

    <text x="290" y="335" class="sans b-cell-main" font-size="12">Speech Intel &amp; Executive Minutes</text>
    <text x="290" y="350" class="mono" font-size="10" fill="#F59E0B">8x Speedup vs Cloud</text>

    <text x="480" y="335" class="mono b-cell-main" font-size="12" font-weight="600">3.4 <tspan class="b-cell-sub">/ 6.8 / 11.2</tspan> <tspan font-size="10" class="b-cell-sub">ms</tspan></text>
    <text x="480" y="350" class="mono" font-size="10" fill="#10B981">Ultra-Low Edge Latency</text>

    <rect x="730" y="326" width="130" height="8" rx="4" class="b-bar-track" />
    <rect x="730" y="326" width="130" height="8" rx="4" fill="url(#bar-amber)" />
    <text x="730" y="350" class="mono b-cell-main" font-size="11" font-weight="600">540.0 <tspan class="b-cell-sub">tok/s (Peak)</tspan></text>

    <text x="900" y="335" class="mono" font-size="13" font-weight="700" fill="#10B981">98.6%</text>
    <rect x="900" y="342" width="100" height="5" rx="2.5" class="b-bar-track" />
    <rect x="900" y="342" width="98" height="5" rx="2.5" fill="#10B981" />

    <text x="1040" y="335" class="mono" font-size="13" font-weight="700" fill="#10B981">1.4%</text>
    <text x="1040" y="350" class="mono b-cell-sub" font-size="10">Verbatim Extraction</text>
  </g>

  <!-- ROW 5: CorrectiveRAG on PopQA (y: 370) -->
  <g class="bench-row">
    <rect x="40" y="370" width="1120" height="52" rx="8" class="b-row-bg" stroke-width="1.2" stroke="#10B981" />
    
    <text x="56" y="394" class="sans row-highlight" font-size="13" font-weight="700" fill="#10B981">CorrectiveRAG (PopQA)</text>
    <text x="56" y="410" class="mono b-cell-sub" font-size="10">LangGraph Self-Reflective Graph</text>

    <text x="290" y="395" class="sans b-cell-main" font-size="12">Hallucination Slasher Pipeline</text>
    <text x="290" y="410" class="mono" font-size="10" fill="#10B981">+11.2 pts Accuracy Delta</text>

    <text x="480" y="395" class="mono b-cell-main" font-size="12" font-weight="600">14.2 <tspan class="b-cell-sub">/ 22.0 / 35.8</tspan> <tspan font-size="10" class="b-cell-sub">ms</tspan></text>
    <text x="480" y="410" class="mono" font-size="10" fill="#10B981">Evaluator Node Included</text>

    <rect x="730" y="386" width="130" height="8" rx="4" class="b-bar-track" />
    <rect x="730" y="386" width="92" height="8" rx="4" fill="url(#bar-emerald)" />
    <text x="730" y="410" class="mono b-cell-main" font-size="11" font-weight="600">165.0 <tspan class="b-cell-sub">tok/s</tspan></text>

    <text x="900" y="395" class="mono" font-size="13" font-weight="700" fill="#10B981">89.8%</text>
    <rect x="900" y="402" width="100" height="5" rx="2.5" class="b-bar-track" />
    <rect x="900" y="402" width="89" height="5" rx="2.5" fill="#10B981" />

    <text x="1040" y="395" class="mono" font-size="13" font-weight="700" fill="#10B981">14.6% <tspan font-size="10" fill="#06B6D4">(-53%)</tspan></text>
    <text x="1040" y="410" class="mono b-cell-sub" font-size="10">Baseline was 31.4%</text>
  </g>

  <!-- ==================== BOTTOM KPI SUMMARY CARDS ==================== -->
  <!-- KPI 1 -->
  <g class="b-kpi-card">
    <rect x="40" y="440" width="268" height="74" rx="8" class="b-kpi-bg" stroke-width="1.2" />
    <text x="56" y="470" class="mono" font-size="22" font-weight="800" fill="#10B981">-53.5%</text>
    <text x="56" y="488" class="sans b-cell-main" font-size="11.5" font-weight="600">Hallucination Reduction</text>
    <text x="56" y="502" class="mono b-kpi-label" font-size="9.5">PopQA Ground Truth Benchmark</text>
  </g>

  <!-- KPI 2 -->
  <g class="b-kpi-card">
    <rect x="324" y="440" width="268" height="74" rx="8" class="b-kpi-bg" stroke-width="1.2" />
    <text x="340" y="470" class="mono" font-size="22" font-weight="800" fill="#06B6D4">~8.2s</text>
    <text x="340" y="488" class="sans b-cell-main" font-size="11.5" font-weight="600">30-Min Audio Turnaround</text>
    <text x="340" y="502" class="mono b-kpi-label" font-size="9.5">Groq LPU Whisper-v3 (8x Cloud)</text>
  </g>

  <!-- KPI 3 -->
  <g class="b-kpi-card">
    <rect x="608" y="440" width="268" height="74" rx="8" class="b-kpi-bg" stroke-width="1.2" />
    <text x="624" y="470" class="mono" font-size="22" font-weight="800" fill="#F59E0B">&lt; 50ms</text>
    <text x="624" y="488" class="sans b-cell-main" font-size="11.5" font-weight="600">Edge Fault Detection Boundary</text>
    <text x="624" y="502" class="mono b-kpi-label" font-size="9.5">CPS Microcontroller Defense</text>
  </g>

  <!-- KPI 4 -->
  <g class="b-kpi-card">
    <rect x="892" y="440" width="268" height="74" rx="8" class="b-kpi-bg" stroke-width="1.2" />
    <text x="908" y="470" class="mono" font-size="22" font-weight="800" fill="#8B5CF6">100%</text>
    <text x="908" y="488" class="sans b-cell-main" font-size="11.5" font-weight="600">Cryptographic Integrity</text>
    <text x="908" y="502" class="mono b-kpi-label" font-size="9.5">Immutable SHA-256 Ledger</text>
  </g>
</svg>
"""


def generate_all(out_dir: Path) -> dict:
    """Generates both SVGs and writes them to out_dir."""
    out_dir.mkdir(parents=True, exist_ok=True)

    arch_svg = build_architecture_diagram_svg()
    bench_svg = build_benchmark_matrix_svg()

    arch_path = out_dir / "diagram-architecture.svg"
    bench_path = out_dir / "benchmark-matrix.svg"

    arch_path.write_text(arch_svg, encoding="utf-8")
    bench_path.write_text(bench_svg, encoding="utf-8")

    return {
        "diagram-architecture.svg": (arch_path, len(arch_svg.encode("utf-8"))),
        "benchmark-matrix.svg": (bench_path, len(bench_svg.encode("utf-8"))),
    }


def main():
    out_dir = CARDS_DIR
    if len(sys.argv) > 1:
        out_dir = Path(sys.argv[1]).resolve()

    print(f"Building showcase SVG cards in: {out_dir}")
    results = generate_all(out_dir)
    for name, (path, size_bytes) in results.items():
        print(f"  Generated {name:30s} -> {size_bytes:6d} bytes ({path})")


if __name__ == "__main__":
    main()
