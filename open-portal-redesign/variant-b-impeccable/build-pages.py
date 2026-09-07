#!/usr/bin/env python3
"""
Build the Direction B portal pages.

index.html is the shell donor: head, tokens/CSS and behaviour script are lifted
from it verbatim, so a token can never drift between pages. Nav and footer are
generated here from one list and written back into index.html too, so all
twelve pages share one definition.

ponytail: no template engine, no build config. str.replace on four markers.
Run:  python3 build-pages.py
"""

import re
import sys
from pathlib import Path

import i18n
from i18n_zh_cn import ZH_CN
from i18n_zh_tw import ZH_TW

TABLES = {"zh-CN": ZH_CN, "zh-TW": ZH_TW}

HERE = Path(__file__).parent
INDEX = HERE / "index.html"

# ---------------------------------------------------------------- shell donor

SRC = INDEX.read_text(encoding="utf-8")


def cut(src, start, end):
    a = src.index(start)
    b = src.index(end, a)
    return src[a : b + len(end)]


HEAD_OPEN = SRC[: SRC.index("<title>")]
CSS = cut(SRC, "<style>", "</style>")
SYMBOL = cut(SRC, '<svg width="0" height="0"', "</symbol></svg>")
SCRIPT = cut(SRC, "<script>\n(function(){", "</script>")

# sanity: the donor must still look like the donor
for name, blob, need in (
    ("CSS", CSS, "--accent:#F97316"),
    ("SYMBOL", SYMBOL, 'id="fcg-logo"'),
    ("SCRIPT", SCRIPT, "IntersectionObserver"),
):
    assert need in blob, f"{name} block did not match index.html — check the markers"

# ---------------------------------------------------------------- nav + footer

# key, label, href
NAV = [
    ("home", "Home", "index.html"),
    ("apps", "App Management", "app-management.html"),
    ("docs", "API Docs", "api-docs-hotel.html"),
    ("sdk", "SDK", "sdk.html"),
    ("skills", "Skills", "skills.html"),
    ("ai", "AI Assistant", "ai-assistant.html"),
]

FOOTER_COLS = [
    (
        "Products",
        [
            ("G-Link Hotel API", "api-docs-hotel.html"),
            ("F-Link Flight API", "api-docs-flink.html"),
            ("TMC API", "index.html#products"),
            ("Product use cases", "index.html#use-cases"),
        ],
    ),
    (
        "Developers",
        [
            ("API Docs", "api-docs-hotel.html"),
            ("SDK", "sdk.html"),
            ("Skills", "skills.html"),
            ("Error code reference", "api-docs-errors.html"),
        ],
    ),
    (
        "Platform",
        [
            ("Home", "index.html"),
            ("App Management", "app-management.html"),
            ("AI Assistant", "ai-assistant.html"),
            ("Register", "register.html"),
        ],
    ),
]

LOGO = (
    '<svg viewBox="0 0 88 24" role="img" aria-label="FCG" '
    'style="height: {h}px; width: auto;"><use href="#fcg-logo"></use></svg>'
)

# code, output subdirectory, <html lang>, switcher label
LOCALES = [
    ("en", "", "en-GB", "ENG"),
    ("zh-CN", "zh-CN", "zh-Hans", "简体"),
    ("zh-TW", "zh-TW", "zh-Hant", "繁體"),
]


def lang_control(locale, slug):
    """Real cross-locale links. Every locale holds the same filenames, so the
    only thing that changes is the relative prefix."""
    here = next(d for c, d, _, _ in LOCALES if c == locale)
    out = []
    for code, subdir, _, label in LOCALES:
        if code == locale:
            out.append(f'<a href="{slug}.html" aria-current="page">{label}</a>')
            continue
        up = "../" if here else ""
        href = f"{up}{subdir + '/' if subdir else ''}{slug}.html"
        out.append(f'<a href="{href}">{label}</a>')
    inner = "\n        ".join(out)
    return f'''<div class="lang" role="group" aria-label="Language">
        {inner}
      </div>'''

ARROW = '<iconify-icon icon="solar:arrow-right-linear" aria-hidden="true"></iconify-icon>'


def header(active="", minimal=False, locale="en", slug="index"):
    """Full portal header, or the reduced brand-only header the auth pages use."""
    lang = lang_control(locale, slug)
    brand = (
        f'<a class="brand" href="index.html" aria-label="FCG Developer Platform — home">\n'
        f"      {LOGO.format(h=28)}\n"
        f'      <span class="brand-div" aria-hidden="true"></span>\n'
        f'      <span class="brand-sub">Developer Platform</span>\n'
        f"    </a>"
    )

    if minimal:
        return f"""<header class="hdr hdr--min" id="hdr">
  <div class="wrap hdr-in">
    {brand}
    <div class="nav-right">
      {lang}
      <a class="tlink" href="index.html">Back to platform {ARROW}</a>
    </div>
  </div>
</header>"""

    shell = "\n".join(
        f'      <a{" class=\"on\"" if k == active else ""} href="{h}">{lb}</a>'
        for k, lb, h in NAV
    )
    mob = "\n".join(f'        <li><a href="{h}">{lb}</a></li>' for _, lb, h in NAV)

    return f"""<header class="hdr" id="hdr">
  <div class="wrap hdr-in">
    {brand}

    <nav class="shell" aria-label="Primary">
{shell}
    </nav>

    <div class="nav-right">
      {lang}
      <a class="login" href="login.html">Login</a>
      <a class="btn btn--sm" href="register.html">Register {ARROW}</a>
      <button class="burger" type="button" id="burger" aria-expanded="false" aria-controls="mnav" aria-label="Open menu">
        <iconify-icon icon="solar:hamburger-menu-linear" aria-hidden="true"></iconify-icon>
      </button>
    </div>
  </div>

  <div class="mnav" id="mnav">
    <div class="wrap">
      <ul>
{mob}
      </ul>
      <div class="m-cta">
        <a class="btn btn--ghost" href="login.html">Login {ARROW}</a>
        {lang}
      </div>
    </div>
  </div>
</header>"""


def footer():
    cols = []
    for title, links in FOOTER_COLS:
        items = "\n".join(f'          <li><a href="{h}">{lb}</a></li>' for lb, h in links)
        fid = "ftr-" + title.lower()
        cols.append(
            f"""      <div class="ftr-col">
        <p class="ftr-h" id="{fid}">{title}</p>
        <nav aria-labelledby="{fid}">
        <ul>
{items}
        </ul>
        </nav>
      </div>"""
        )
    return f"""<footer class="ftr">
  <div class="wrap">
    <div class="ftr-top">
      <div class="ftr-brand">
        {LOGO.format(h=26)}
        <p>The FCG Developer Platform: standardised APIs and flexible SDKs for hotel, flight and travel management resources.</p>
      </div>
{chr(10).join(cols)}
    </div>
    <div class="ftr-bot">
      <span>© 2026 Fusion Connect Group Holdings Ltd (BVI). All rights reserved.</span>
      <span class="mono">ENG · 简体 · 繁體</span>
    </div>
  </div>
</footer>"""


# ------------------------------------------------------- CSS the pages add
# One shared block, appended to every page. Cheaper than per-page blocks and it
# keeps the additions auditable in one place.

PAGE_CSS = """<style>
/* ============================================================
   SUB-PAGE SHELL — page band, docs layout, tables, auth, chat
   Same tokens as index.html. Accent stays graphic only.
   ============================================================ */
.hdr--min .hdr-in{gap:16px}

/* ---------- page band (replaces the hero on inner pages) ---------- */
.band{position:relative;padding:74px 0 52px;border-bottom:1px solid var(--hair);overflow:hidden}
.band-grid{
  position:absolute;inset:0;z-index:0;pointer-events:none;
  background-image:
    linear-gradient(to right,rgba(15,17,20,.05) 1px,transparent 1px),
    linear-gradient(to bottom,rgba(15,17,20,.05) 1px,transparent 1px);
  background-size:40px 40px;
  -webkit-mask-image:linear-gradient(to bottom,#000 0%,transparent 92%);
  mask-image:linear-gradient(to bottom,#000 0%,transparent 92%);
}
/* every child clamps to the wrap: a column flex item sizes to content and
   min-width:auto stops it shrinking, which is how the tab rail ended up
   587px wide inside a 335px column and silently clipped. */
.band-in{position:relative;z-index:1;display:flex;flex-direction:column;gap:20px;align-items:flex-start}
.band-in > *{max-width:100%;min-width:0}
/* eyebrow + status chip share one micro row, so the CTA row stays CTAs only */
.band-top{display:flex;flex-wrap:wrap;align-items:center;gap:8px 14px}
.band h1{font-size:clamp(34px,4.6vw,62px);line-height:1.02;letter-spacing:-.032em;max-width:22ch}
.band h1 em{display:block;font-style:normal;color:var(--accent)}
.band .lede{font-size:16.5px;line-height:27px;max-width:60ch}
.band-foot{display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin-top:8px;width:100%;min-width:0}
.crumb{display:flex;align-items:center;gap:8px;color:var(--muted);font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase}
.crumb a{color:var(--muted);transition:color 240ms ease}
@media (hover:hover) and (pointer:fine){ .crumb a:hover{color:var(--ink)} }
.crumb i{font-style:normal;color:var(--line)}

/* ---------- tab rail (reuses the nav shell grammar) ---------- */
/* min-width:0 + align-self:stretch — without them this nowrap flex row keeps
   its min-content width and gets clipped by body{overflow-x:hidden}. */
.rail{display:flex;gap:2px;padding:3px;background:var(--shell);border:1px solid var(--hair);border-radius:999px;overflow-x:auto;max-width:100%;min-width:0;flex:0 1 auto;scrollbar-width:none;-webkit-overflow-scrolling:touch}
.rail a,.rail button{
  display:inline-flex;align-items:center;gap:7px;height:34px;padding:0 15px;border:0;border-radius:999px;
  background:transparent;font-size:13.5px;font-weight:400;color:var(--ink);white-space:nowrap;cursor:pointer;
  transition:background var(--hover) ease,transform var(--press) var(--ease-out);
}
.rail a:active,.rail button:active{transform:scale(.97)}
@media (hover:hover) and (pointer:fine){
  .rail a:hover,.rail button:hover{background:#fff}
}
.rail a.on,.rail button.on{background:#fff;font-weight:500}
.rail::-webkit-scrollbar{height:0}
.docs-side-in{min-width:0}

/* ---------- generic content block ---------- */
.blk{padding:80px 0}
.blk--top{padding-top:64px}
.blk h2.h3{max-width:26ch}
.blk-head{display:flex;flex-direction:column;gap:18px;margin-bottom:38px}
.blk-head .lede{font-size:15px;line-height:25px}
.note{
  display:flex;gap:12px;align-items:flex-start;
  padding:18px 22px;border:1px solid var(--line);border-radius:16px;background:var(--card);
  font-size:14px;line-height:23px;color:var(--muted-card);
}
.note iconify-icon{font-size:18px;color:var(--ink);flex:none;margin-top:2px}
.note strong{color:var(--ink);font-weight:500}

/* ---------- data table ---------- */
.tblwrap{border:1px solid var(--line);border-radius:20px;overflow:hidden;background:#fff}
.tblscroll{overflow-x:auto}
table.tbl{width:100%;border-collapse:collapse;min-width:640px}
table.tbl th{
  text-align:left;padding:14px 20px;background:var(--card);border-bottom:1px solid var(--line);
  font-size:9.5px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:var(--muted-card);white-space:nowrap;
}
table.tbl td{padding:16px 20px;border-top:1px solid var(--hair);font-size:14px;line-height:22px;vertical-align:top}
table.tbl tbody tr:first-child td{border-top:0}
/* t- prefix, deliberately: a bare .path here collided with the homepage's
   unscoped .path closing card and rendered every cell as a rounded panel. */
table.tbl td.t-num{font-family:var(--mono);font-size:11.5px;color:var(--muted);width:44px;white-space:nowrap}
table.tbl td.t-path,table.tbl td.t-code{font-family:var(--mono);font-size:12px;letter-spacing:-.01em;color:var(--ink)}
table.tbl td.t-mid{white-space:nowrap;width:1%}
table.tbl td.t-dim{color:var(--muted)}
table.tbl td{border-radius:0;background:none}
@media (hover:hover) and (pointer:fine){
  table.tbl tbody tr{transition:background var(--hover) ease}
  table.tbl tbody tr:hover{background:rgba(15,17,20,.015)}
}

/* ---------- docs two-column ---------- */
.docs{display:grid;grid-template-columns:252px minmax(0,1fr);gap:0;border-top:1px solid var(--hair)}
.docs-side{border-right:1px solid var(--hair);padding:38px 28px 60px 0}
.docs-side-in{position:sticky;top:100px;display:flex;flex-direction:column;gap:26px}
.docs-grp .docs-h{margin:0;font-size:9.5px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:var(--accent-ink)}
.docs-grp ul{margin-top:12px;display:flex;flex-direction:column}
.docs-grp a{
  display:flex;align-items:center;gap:8px;padding:8px 12px;margin-left:-12px;border-radius:999px;
  color:var(--muted);font-size:13.5px;
  transition:background var(--hover) ease,color var(--hover) ease,transform var(--press) var(--ease-out);
}
.docs-grp a:active{transform:scale(.98)}
@media (hover:hover) and (pointer:fine){
  .docs-grp a:hover{color:var(--ink);background:var(--shell)}
}
.docs-grp a.on{color:var(--ink);font-weight:500;background:var(--card)}
.docs-main{padding:38px 0 80px 40px;min-width:0}
.docs-main > * + *{margin-top:22px}
.docs-main > h2 + *,.docs-main > h3 + *{margin-top:16px}   /* tight under a heading */
.docs-main > * + h3{margin-top:54px}                        /* open above one */
.docs-main > * + h2{margin-top:64px}
.docs-main > * + .tblwrap,.docs-main > * + .steps{margin-top:28px}
.docs-main > * + .note{margin-top:34px}
.docs-main > * + .ep{margin-top:28px}
.docs-main > * + .band-foot{margin-top:40px}
.docs-main h2{font-size:clamp(24px,2.4vw,32px);line-height:1.12;letter-spacing:-.02em}
.docs-main h2 em{display:block;font-style:normal;color:var(--accent)}
.docs-main h3{font-size:19px;letter-spacing:-.01em}
.docs-main h4{font-size:11px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:var(--muted)}
.docs-main p{color:var(--muted);font-size:15px;line-height:25px;max-width:66ch}
.docs-main ol,.docs-main ul.bul{display:flex;flex-direction:column;gap:0;padding:0;list-style:none;counter-reset:s}
.docs-main ol li{display:flex;gap:14px;padding:14px 0;border-top:1px solid var(--hair-soft);font-size:14.5px;line-height:23px}
.docs-main ol li:last-child{border-bottom:1px solid var(--hair-soft)}
.docs-main ol li::before{
  counter-increment:s;content:counter(s,decimal-leading-zero);
  font-family:var(--mono);font-size:11px;color:var(--muted);padding-top:4px;flex:none;
}
.docs-main ul.bul li{display:flex;gap:12px;padding:13px 0;border-top:1px solid var(--hair-soft);font-size:14.5px;line-height:23px}
.docs-main ul.bul li:last-child{border-bottom:1px solid var(--hair-soft)}
.docs-main ul.bul li iconify-icon{font-size:16px;color:var(--ink);flex:none;margin-top:3px}
code.inl{font-family:var(--mono);font-size:12.5px;background:var(--card);border:1px solid var(--hair);border-radius:5px;padding:1px 6px;color:var(--ink)}
.msg--me code.inl{background:rgba(255,255,255,.14);border-color:rgba(255,255,255,.2);color:#fff}

/* ---------- endpoint card ---------- */
.ep{border:1px solid var(--line);border-radius:20px;overflow:hidden;background:#fff}
.ep-h{display:flex;align-items:center;gap:12px;flex-wrap:wrap;padding:18px 22px;border-bottom:1px solid var(--hair);background:var(--card)}
.ep-h code{font-family:var(--mono);font-size:12.5px;color:var(--ink);letter-spacing:-.01em;word-break:break-all}
.ep-b{padding:22px}
.ep-b + .ep-b{border-top:1px solid var(--hair)}
.plist{display:flex;flex-direction:column}
.plist li{display:grid;grid-template-columns:190px 90px 76px minmax(0,1fr);gap:16px;padding:14px 0;border-top:1px solid var(--hair-soft);font-size:13.5px;line-height:21px;align-items:baseline}
.plist li:first-child{border-top:0}
.plist .pn{font-family:var(--mono);font-size:12px;color:var(--ink);word-break:break-all}
.plist .pt{font-family:var(--mono);font-size:11px;color:var(--muted)}
.plist .pr{font-size:9.5px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.plist .pr.req{color:var(--ink)}
.plist .pd{color:var(--muted)}
.plist li.sub .pn{padding-left:18px;position:relative}
.plist li.sub .pn::before{content:"";position:absolute;left:4px;top:8px;width:8px;height:1px;background:var(--line)}

/* ---------- flow steps ---------- */
.steps{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));border:1px solid var(--line);border-radius:20px;overflow:hidden;background:#fff}
.step{padding:22px 22px 24px;border-right:1px solid var(--hair);border-bottom:1px solid var(--hair)}
.step:nth-child(4n){border-right:0}
.step:nth-last-child(-n+4){border-bottom:0}
.step .sn{display:flex;align-items:center;gap:9px;font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent-ink)}
.step h3{font-size:15px;font-weight:500;letter-spacing:-.01em;margin-top:14px;line-height:1.3}
.step code{display:block;margin-top:10px;font-family:var(--mono);font-size:11.5px;color:var(--muted);word-break:break-all}

/* ---------- app / sdk / skill cards ---------- */
.cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}
.cards--2{grid-template-columns:repeat(2,minmax(0,1fr))}
.card{border:1px solid var(--line);border-radius:20px;background:#fff;display:flex;flex-direction:column;overflow:hidden}
.card-h{padding:24px 24px 20px}
.card-k{display:flex;align-items:center;gap:9px;font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent-ink)}
.card-h h3{font-size:19px;letter-spacing:-.01em;margin-top:14px}
.card-h p{color:var(--muted);font-size:14px;line-height:23px;margin-top:12px}
/* ponytail: three lines reserved (3 x 23px) so meta rows start at the same y
   across a row of cards. Ceiling — a description over three lines at 1280px
   misaligns again; use grid subgrid if the copy ever needs to run longer. */
.cards .card-h > p:not(.card-k){min-height:69px}
.cards--tall .card-h > p:not(.card-k){min-height:92px}  /* 4 lines: narrow 3-up columns */
.card-meta{display:flex;flex-direction:column;padding:0 24px}
.card-meta div{display:flex;align-items:baseline;justify-content:space-between;gap:16px;padding:11px 0;border-top:1px solid var(--hair-soft);font-size:13px}
.card-meta dt,.card-meta .k{color:var(--muted);font-size:9.5px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;flex:none}
.card-meta .v{font-family:var(--mono);font-size:12px;color:var(--ink);text-align:right;word-break:break-all}
.card-f{margin-top:auto;padding:20px 24px 22px;background:var(--card);display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.card-f--plain{background:#fff;border-top:1px solid var(--hair)}

/* ---------- copy row (install commands) ---------- */
.cmd{display:flex;align-items:stretch;border:1px solid var(--dark);border-radius:12px;overflow:hidden;background:var(--dark)}
.cmd code{flex:1;min-width:0;padding:13px 16px;font-family:var(--mono);font-size:12px;line-height:1.6;color:var(--dark-fg);overflow-x:auto;white-space:nowrap}
.cmd button{
  flex:none;padding:0 16px;border:0;border-left:1px solid var(--dark-line);background:transparent;cursor:pointer;
  color:var(--dark-muted);font-size:11px;font-weight:500;letter-spacing:.14em;text-transform:uppercase;
  transition:color var(--hover) ease,background var(--hover) ease,transform var(--press) var(--ease-out);
}
.cmd button:active{transform:scale(.96)}
.cmd button.done{color:#fff}
@media (hover:hover) and (pointer:fine){
  .cmd button:hover{color:#fff;background:rgba(255,255,255,.06)}
}

/* ---------- stat strip variant used on inner pages ---------- */
.mini{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));border-top:1px solid var(--hair);border-bottom:1px solid var(--hair)}
.mini div{padding:30px 24px}
.mini div + div{border-left:1px solid var(--hair)}
.mini .n{font-size:clamp(28px,3vw,42px);line-height:1;letter-spacing:-.03em;font-weight:500}
.mini .n u{text-decoration:none;color:var(--accent)}
.mini .c{margin-top:12px;color:var(--muted);font-size:11px;font-weight:500;letter-spacing:.18em;text-transform:uppercase}
.mini--aside{border-bottom:0;background:transparent}
.mini--aside div{padding:30px 22px}
.mini--aside div:first-child{padding-left:0}

/* ---------- auth ---------- */
.auth{min-height:calc(100vh - 76px);display:grid;grid-template-columns:minmax(0,1.02fr) minmax(0,.98fr)}
/* top-aligned, not centred: the register form is far taller than this
   column, and centring pushed the aside's list below the fold. Sticky so
   it stays in view while the form scrolls. */
.auth-aside{position:relative;padding:64px 0 72px;border-right:1px solid var(--hair);overflow:hidden;display:flex;align-items:flex-start}
.auth-aside .wrap{position:sticky;top:0}
.auth-aside .wrap{max-width:none;padding:0 64px 0 max(32px,calc((100vw - var(--wrap)) / 2 + 32px));width:100%}
.auth-aside .ahead{font-size:clamp(30px,3.6vw,50px);line-height:1.04;letter-spacing:-.03em;max-width:18ch;margin-top:22px;color:var(--ink);font-weight:500}
.auth-aside .ahead em{display:block;font-style:normal;color:var(--accent)}
.auth-aside .lede{margin-top:22px;font-size:16px;line-height:26px;max-width:44ch}
.auth-main{display:flex;align-items:center;justify-content:center;padding:64px 32px 72px;background:var(--footer)}
.auth-card{width:100%;max-width:436px;background:#fff;border:1px solid var(--line);border-radius:24px;padding:40px 38px 36px}
.auth-card h1{font-size:clamp(26px,2.6vw,34px);line-height:1.1;letter-spacing:-.025em}
.auth-card > p{color:var(--muted);font-size:14.5px;line-height:23px;margin-top:12px}
.oauth{
  display:flex;align-items:center;justify-content:center;gap:11px;width:100%;height:50px;margin-top:28px;
  border:1px solid var(--line);border-radius:999px;background:#fff;cursor:pointer;
  font-size:14.5px;font-weight:500;
  transition:background var(--hover) ease,border-color var(--hover) ease,
             transform var(--press) var(--ease-out);
}
.oauth:active{transform:scale(.98)}
@media (hover:hover) and (pointer:fine){
  .oauth:hover{background:var(--card);border-color:var(--ink)}
}
.oauth iconify-icon{font-size:19px}
.orline{display:flex;align-items:center;gap:14px;margin:24px 0 22px;color:var(--muted);font-size:11px;font-weight:500;letter-spacing:.14em;text-transform:uppercase}
.orline::before,.orline::after{content:"";flex:1;height:1px;background:var(--hair)}
.fields{display:flex;flex-direction:column;gap:16px}
.fld{display:flex;flex-direction:column;gap:8px;min-width:0}
.fld label{font-size:11px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}
.fld label em{font-style:normal;color:var(--ink)}  /* 11px orange on white is 2.80:1 and fails AA. Kept ink until the
     small-orange-text decision is made — see STATE-LOG. */
.fld input,.fld select{
  height:48px;padding:0 15px;border:1px solid var(--line);border-radius:12px;background:#fff;color:var(--ink);
  font-family:var(--sans);font-size:14.5px;width:100%;transition:border-color var(--hover) var(--ease-out),background var(--hover) ease;
}
.fld select{appearance:none;-webkit-appearance:none;padding-right:38px;cursor:pointer;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%236B7280' stroke-width='1.6'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E");
  background-repeat:no-repeat;background-position:right 14px center;background-size:16px}
@media (hover:hover) and (pointer:fine){
  .fld input:hover,.fld select:hover{border-color:var(--muted)}
}
.fld input:focus,.fld select:focus{border-color:var(--ink);outline:none}
.fld input:focus-visible,.fld select:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.fields--2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
.fld-row{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-top:-4px}
.fld-row a{font-size:13px;color:var(--muted);transition:color 240ms ease}
@media (hover:hover) and (pointer:fine){ .fld-row a:hover{color:var(--ink)} }
.auth-submit{width:100%;justify-content:space-between;margin-top:26px}
.auth-alt{margin-top:22px;padding-top:20px;border-top:1px solid var(--hair);color:var(--muted);font-size:13.5px;text-align:center}
.auth-alt a{color:var(--ink);font-weight:500}
.auth-legal{margin-top:16px;color:var(--muted);font-size:11.5px;line-height:18px;text-align:center}

/* ---------- chat ---------- */
.chat{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:24px;align-items:start}
.chatbox{border:1px solid var(--line);border-radius:24px;background:#fff;overflow:hidden;display:flex;flex-direction:column}
.chat-h{display:flex;align-items:center;gap:13px;padding:20px 24px;border-bottom:1px solid var(--hair)}
.chat-h .av{width:40px;height:40px;border-radius:999px;background:var(--card);border:1px solid var(--hair);display:flex;align-items:center;justify-content:center;font-size:19px;flex:none}
.chat-h strong{display:block;font-size:15px;font-weight:500;letter-spacing:-.01em}
.chat-h span{display:block;margin-top:3px;color:var(--muted);font-size:12px}
.chat-h .dot{margin-left:auto}
.chat-b{padding:26px 24px;display:flex;flex-direction:column;gap:18px;background:var(--footer)}
.msg{max-width:78%;padding:16px 19px;border-radius:18px;font-size:14.5px;line-height:24px}
.msg--ai{background:#fff;border:1px solid var(--hair);color:var(--ink);border-bottom-left-radius:6px}
.msg--me{align-self:flex-end;background:var(--ink);color:#fff;border-bottom-right-radius:6px}
.msg p + p{margin-top:12px}
.chat-in{display:flex;align-items:center;gap:12px;padding:16px 20px;border-top:1px solid var(--hair);background:#fff}
.chat-in input{flex:1;min-width:0;height:46px;padding:0 16px;border:1px solid var(--line);border-radius:999px;font-family:var(--sans);font-size:14.5px;color:var(--ink)}
.chat-in input:focus{border-color:var(--ink);outline:none}
.chat-in input:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.chat-f{padding:14px 24px 18px;color:var(--muted);font-size:11.5px;line-height:18px;background:#fff;border-top:1px solid var(--hair-soft)}
.chat-f a{color:var(--ink);font-weight:500}
.asks{border:1px solid var(--line);border-radius:20px;background:#fff;overflow:hidden;position:sticky;top:100px}
.asks .asks-h{margin:0;padding:16px 20px;border-bottom:1px solid var(--hair);background:var(--card);font-size:9.5px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:var(--muted-card)}
.asks button{
  display:flex;align-items:flex-start;gap:10px;width:100%;text-align:left;padding:15px 20px;border:0;
  border-top:1px solid var(--hair-soft);background:#fff;cursor:pointer;font-size:13.5px;line-height:21px;
  transition:background var(--hover) ease,transform var(--press) var(--ease-out);
}
.asks button:first-of-type{border-top:0}
.asks button:active{transform:scale(.99)}
@media (hover:hover) and (pointer:fine){
  .asks button:hover{background:var(--shell)}
}
.asks button iconify-icon{font-size:15px;color:var(--muted);flex:none;margin-top:3px}

/* ---------- responsive ---------- */
@media (max-width:1180px){
  .docs{grid-template-columns:220px minmax(0,1fr)}
  .docs-main{padding-left:32px}
  .plist li{grid-template-columns:160px 78px 68px minmax(0,1fr);gap:12px}
  .auth-aside .wrap{padding:0 48px 0 max(32px,calc((100vw - var(--wrap)) / 2 + 32px))}
}
@media (max-width:1000px){
  .cards{grid-template-columns:minmax(0,1fr)}
  .cards--2{grid-template-columns:minmax(0,1fr)}
  .steps{grid-template-columns:repeat(2,minmax(0,1fr))}
  .step:nth-child(2n){border-right:0}
  .step:nth-child(4n){border-right:0}
  .step:nth-last-child(-n+4){border-bottom:1px solid var(--hair)}
  .step:nth-last-child(-n+2){border-bottom:0}
  .docs{grid-template-columns:minmax(0,1fr)}
  .docs-side{border-right:0;border-bottom:1px solid var(--hair);padding:26px 0 30px}
  .docs-side-in{position:static;flex-direction:row;flex-wrap:wrap;gap:26px 44px}
  .docs-main{padding:38px 0 72px}
  .auth{grid-template-columns:minmax(0,1fr);min-height:0}
  .auth-aside{border-right:0;border-bottom:1px solid var(--hair);padding:56px 0 52px}
  .auth-aside .wrap{position:static}
  .auth-aside .wrap{max-width:var(--wrap);margin:0 auto;padding:0 32px}
  .auth-main{padding:56px 32px 72px}
  .chat{grid-template-columns:minmax(0,1fr)}
  .asks{position:static}
  .mini{grid-template-columns:minmax(0,1fr)}
  .mini div + div{border-left:0;border-top:1px solid var(--hair)}
  /* stacking starts here, so the flush rule has to start here too — putting it
     in the 640px block left 641-1000px indented */
  .mini--aside div{padding-left:0;padding-right:0}
}
@media (max-width:640px){
  /* wrap the rail instead of scrolling it: a horizontal scroller on a phone
     hides options behind an edge with no affordance */
  .rail{flex-wrap:wrap;overflow:visible;border-radius:18px;gap:4px;padding:5px}
  .rail a,.rail button{height:32px;padding:0 13px;font-size:13px}
  .band{padding:52px 0 42px}
  .blk{padding:60px 0}
  .blk--top{padding-top:48px}
  .steps{grid-template-columns:minmax(0,1fr)}
  .step{border-right:0!important;border-bottom:1px solid var(--hair)!important}
  .step:last-child{border-bottom:0!important}
  .plist li{grid-template-columns:minmax(0,1fr);gap:4px}
  .plist .pr{margin-top:2px}
  .auth-card{padding:30px 22px 28px;border-radius:20px}
  .auth-main{padding:40px 20px 56px}
  .fields--2{grid-template-columns:minmax(0,1fr)}
  .msg{max-width:92%}
  .chat-b{padding:20px 16px}
  .card-h,.card-f,.card-meta{padding-left:20px;padding-right:20px}
  .band-foot .btn{justify-content:flex-start}
}
</style>"""

# ------------------------------------------------------------------ assembly

PAGE = """<!DOCTYPE html>
{head}<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<script src="https://code.iconify.design/iconify-icon/1.0.7/iconify-icon.min.js"></script>
<script>document.documentElement.classList.add('js');</script>
{css}
{pagecss}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<!-- The real FCG wordmark, inlined verbatim once and referenced where needed. -->
{symbol}

{header}

<main id="main">
{body}
</main>

{footer}

{script}
{extra}</body>
</html>
"""

# the copy-button behaviour the SDK/Skills pages need, added only where used
COPY_JS = """<script>
(function(){
  "use strict";
  document.addEventListener('click', function(e){
    var b = e.target.closest('.cmd button');
    if (!b) return;
    var code = b.parentNode.querySelector('code');
    if (!code || !navigator.clipboard) return;
    navigator.clipboard.writeText(code.textContent.trim()).then(function(){
      var was = b.textContent;
      b.textContent = 'Copied';
      b.classList.add('done');
      setTimeout(function(){ b.textContent = was; b.classList.remove('done'); }, 1600);
    });
  });
})();
</script>
"""


# The orange second clause is only ever the part AFTER a comma. A headline with
# no comma has no second clause and stays entirely ink. Enforced, not remembered.
EM_IN_HEADING = re.compile(
    r"<(h1|h2|h3|p class=\"ahead\")[^>]*>(.*?)</(?:h1|h2|h3|p)>", re.S
)


H1_TEXT = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S)

# A heading's orange clause and a lede's orange lead-in are both "the one
# emphasis in this block". Using both stacks two orange runs on top of each
# other and reads as a colour wash, so a block gets one or the other.
DOUBLE_ORANGE = re.compile(
    r'<(?:h1|h2|p class="ahead")[^>]*>(.*?)</(?:h1|h2|p)>\s*(?:<[^>]+>\s*)*'
    r'<p class="lede"[^>]*>(.*?)</p>',
    re.S,
)


# Verified benign: each is a page's own name, appearing as its h1 and as its
# nav/footer link, and both want the same translation. Anything NOT on this
# list is a headline fragment colliding with a label — the bug that translated
# the hero h1 to "FCG平台" — and fails the build.
BENIGN_COLLISIONS = {"AI Assistant", "App Management", "FCG Developer Platform"}


def check_context_collisions(html, slug):
    # both locale tables carry identical keys, so either resolves the overrides
    bad = i18n.find_context_collisions(html, ZH_CN) - BENIGN_COLLISIONS
    if bad:
        raise SystemExit(
            f"{slug}: these strings appear both in a heading and in ordinary copy, "
            f"so one translation has to serve both — split the markup or reword: {sorted(bad)}"
        )


def check_double_orange(html, slug):
    for m in DOUBLE_ORANGE.finditer(html):
        if "<em>" in m.group(1) and "<b>" in m.group(2):
            head = re.sub(r"<[^>]+>", "", m.group(1)).strip()[:50]
            raise SystemExit(
                f"{slug}: heading already carries an orange clause, so its lede "
                f"must not also have an orange lead-in — {head!r}"
            )


def check_h1_rule(html, slug):
    """An h1 is a page title, not a sentence: no trailing full stop."""
    for m in H1_TEXT.finditer(html):
        txt = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        if txt.endswith("."):
            raise SystemExit(f"{slug}: h1 must not end in a full stop — {txt!r}")


def check_em_rule(html, slug):
    bad = []
    for m in EM_IN_HEADING.finditer(html):
        inner = m.group(2)
        for em in re.finditer(r"<em>", inner):
            before = inner[: em.start()].rstrip()
            if not before.endswith(","):
                bad.append(re.sub(r"\s+", " ", inner)[:70])
    if bad:
        raise SystemExit(
            f"{slug}: orange <em> must follow a comma — offending headings: {bad}"
        )


def build(slug, title, desc, body, nav="", minimal=False, extra="", locale="en"):
    """Assemble one page for one locale. English is authored; the other locales
    are the same document with its text nodes swapped, so markup and CSS are
    identical across locales by construction."""
    code, subdir, htmllang, _ = next(l for l in LOCALES if l[0] == locale)
    head = HEAD_OPEN.replace('<html lang="en-GB"', f'<html lang="{htmllang}"')

    html = PAGE.format(
        head=head,
        title=title,
        desc=desc,
        css=CSS,
        pagecss=PAGE_CSS,
        symbol=SYMBOL,
        header=header(nav, minimal, locale, slug),
        body=body.strip("\n"),
        footer=footer(),
        script=SCRIPT,
        extra=extra,
    )

    # the copy rules are checked on the authored English, where they are written
    if locale == "en":
        check_em_rule(html, slug)
        check_h1_rule(html, slug)
        check_double_orange(html, slug)
        check_context_collisions(html, slug)

    missing = set()
    if locale != "en":
        html, missing = i18n.translate(html, TABLES[locale])

    out_dir = HERE / subdir if subdir else HERE
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"{slug}.html").write_text(html, encoding="utf-8")
    return len(html), missing


def patch_index():
    """Point index.html's nav and footer at the real pages, structure unchanged."""
    src = INDEX.read_text(encoding="utf-8")
    old_hdr = cut(src, '<header class="hdr" id="hdr">', "</header>")
    old_ftr = cut(src, '<footer class="ftr">', "</footer>")
    new = src.replace(old_hdr, header("home")).replace(old_ftr, footer())
    if new != src:
        INDEX.write_text(new, encoding="utf-8")
        return True
    return False


def build_index_locale(locale):
    """index.html is the shell donor, not generated from pages_content, so its
    locale copies are made by swapping the chrome and translating in place."""
    code, subdir, htmllang, _ = next(l for l in LOCALES if l[0] == locale)
    src = INDEX.read_text(encoding="utf-8")
    src = src.replace('<html lang="en-GB"', f'<html lang="{htmllang}"')
    old_hdr = cut(src, '<header class="hdr" id="hdr">', "</header>")
    src = src.replace(old_hdr, header("home", False, locale, "index"))
    html, missing = i18n.translate(src, TABLES[locale])
    out = HERE / subdir
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(html, encoding="utf-8")
    return len(html), missing


if __name__ == "__main__":
    import pages_content

    changed = patch_index()
    _idx = INDEX.read_text(encoding="utf-8")
    check_em_rule(_idx, "index.html")
    check_h1_rule(_idx, "index.html")
    check_double_orange(_idx, "index.html")
    check_context_collisions(_idx, "index.html")
    print(f"index.html nav/footer: {'rewritten' if changed else 'already current'}")

    all_missing = {}
    for code, subdir, _, _ in LOCALES:
        total, miss = 0, set()
        for spec in pages_content.PAGES:
            n, m = build(**spec, locale=code)
            total += n
            miss |= m
        if code != "en":
            n, m = build_index_locale(code)
            total += n
            miss |= m
        else:
            total += len(_idx)
        label = subdir or "en (root)"
        print(f"  {label:<12} {len(pages_content.PAGES) + 1:>2} pages  {total/1024:6.0f} KB"
              + (f"  ⚠ {len(miss)} untranslated" if miss else "  fully translated" if code != "en" else ""))
        if miss:
            all_missing[code] = miss

    if all_missing:
        for code, miss in all_missing.items():
            print(f"\n{code} is missing {len(miss)} strings:")
            for s in sorted(miss)[:20]:
                print(f"    {s!r}")
        sys.exit("translation incomplete — every string must have an entry")
