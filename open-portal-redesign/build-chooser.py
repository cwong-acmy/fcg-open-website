#!/usr/bin/env python3
"""Build choose.html — a self-contained tabbed comparison of the homepage directions.

Each variant is base64-embedded and decoded into an iframe srcdoc at runtime, so the
chooser is one file with no dependencies on local paths. Safe to host anywhere.

    python3 build-chooser.py

ponytail: base64 rather than escaping the variants into srcdoc attributes — no
quote/`</script>` hazards to get wrong. Re-run after editing any variant.
"""
import base64
import pathlib
import sys

HERE = pathlib.Path(__file__).parent

VARIANTS = [
    ("a", "Direction A", "Huashu", "variant-a-huashu/index.html",
     "Editorial. The marketing site's typographic confidence, grown a developer portal."),
    ("b", "Direction B", "Impeccable", "variant-b-impeccable/index.html",
     "Product surface. Same brand language, solved for an engineer deciding whether to integrate."),
]

LIVE_REF = "https://fusionconnectgroup.com/"
CURRENT = "https://open.fusionconnectgroup.com/home"


def load(rel):
    p = HERE / rel
    if not p.exists():
        return None
    return base64.b64encode(p.read_bytes()).decode()


def main():
    payloads, tabs, panes, missing = [], [], [], []

    for key, name, skill, rel, blurb in VARIANTS:
        b64 = load(rel)
        if b64 is None:
            missing.append(rel)
            continue
        size = round(len(base64.b64decode(b64)) / 1024)
        payloads.append(f'<script type="application/octet-stream" id="src-{key}">{b64}</script>')
        tabs.append(
            f'<button class="tab" role="tab" aria-selected="false" aria-controls="pane-{key}" '
            f'data-pane="{key}"><b>{name}</b><span>{skill}</span></button>'
        )
        panes.append(
            f'<section class="pane" id="pane-{key}" role="tabpanel" hidden>'
            f'<div class="meta"><span class="lbl"><i class="dash"></i>{name} &middot; {skill}</span>'
            f'<span class="note">{blurb}</span><span class="sz">{size} KB</span></div>'
            f'<div class="frame"><iframe title="{name}" data-src="{key}" loading="lazy"></iframe></div>'
            f"</section>"
        )

    if missing:
        print("MISSING:", *missing, file=sys.stderr)
    if not panes:
        sys.exit("no variants found — nothing to build")

    # Reference panes point at the live sites directly.
    for key, name, url, blurb in [
        ("ref", "Brand reference", LIVE_REF, "The target design language. This is what we are aligning to."),
        ("cur", "Portal today", CURRENT, "The current portal, for before/after only. Not a design to preserve."),
    ]:
        tabs.append(
            f'<button class="tab" role="tab" aria-selected="false" aria-controls="pane-{key}" '
            f'data-pane="{key}"><b>{name}</b><span>live</span></button>'
        )
        panes.append(
            f'<section class="pane" id="pane-{key}" role="tabpanel" hidden>'
            f'<div class="meta"><span class="lbl"><i class="dash"></i>{name}</span>'
            f'<span class="note">{blurb}</span>'
            f'<a class="sz" href="{url}" target="_blank" rel="noopener">open &#8599;</a></div>'
            f'<div class="frame"><iframe title="{name}" src="{url}" loading="lazy"></iframe></div>'
            f"</section>"
        )

    html = TEMPLATE.replace("<!--TABS-->", "\n".join(tabs))
    html = html.replace("<!--PANES-->", "\n".join(panes))
    html = html.replace("<!--PAYLOADS-->", "\n".join(payloads))

    out = HERE / "choose.html"
    out.write_bytes(html.encode())
    print(f"wrote {out} — {round(len(html)/1024)} KB, {len(panes)} panes")


TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>FCG Developer Platform — homepage directions</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
  :root{--bg:#fff;--ink:#0F1114;--accent:#F97316;--card:#F3F4F6;--line:#D1D5DB;--muted:#6B7280;--ink2:#111827;--hair:rgba(15,17,20,.1)}
  *{box-sizing:border-box;margin:0;padding:0}
  body{background:var(--bg);color:var(--ink);font:400 16px/1.5 Inter,-apple-system,sans-serif;-webkit-font-smoothing:antialiased}
  .bar{position:sticky;top:0;z-index:10;background:rgba(255,255,255,.92);backdrop-filter:blur(12px);border-bottom:1px solid var(--hair);padding:16px clamp(16px,3vw,32px)}
  .top{display:flex;justify-content:space-between;align-items:baseline;gap:20px;flex-wrap:wrap;max-width:1560px;margin:0 auto}
  h1{font-size:clamp(17px,2vw,24px);font-weight:500;letter-spacing:-.02em}
  .lbl{font-size:11px;font-weight:500;text-transform:uppercase;letter-spacing:.18em;color:var(--muted);display:inline-flex;align-items:center;gap:10px}
  .dash{width:12px;height:2px;background:var(--accent);display:inline-block;flex:none}
  .tabs{display:flex;gap:3px;flex-wrap:wrap;max-width:1560px;margin:14px auto 0;background:rgba(15,17,20,.04);border:1px solid rgba(15,17,20,.08);border-radius:999px;padding:3px;width:max-content}
  .tab{font:inherit;cursor:pointer;border:0;background:none;color:var(--muted);border-radius:999px;padding:9px 18px;display:flex;align-items:baseline;gap:9px;transition:background-color 240ms ease,color 240ms ease}
  .tab b{font-weight:500;font-size:14px}
  .tab span{font-size:10px;text-transform:uppercase;letter-spacing:.16em;opacity:.75}
  .tab:hover{color:var(--ink)}
  .tab[aria-selected=true]{background:#fff;color:var(--ink);box-shadow:0 1px 2px rgba(15,17,20,.06)}
  .tab:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
  main{max-width:1560px;margin:0 auto;padding:0 clamp(16px,3vw,32px) clamp(24px,4vw,48px)}
  .meta{display:flex;align-items:center;gap:18px;flex-wrap:wrap;padding:18px 0 14px}
  .note{font-size:14px;color:var(--muted);flex:1;min-width:220px}
  .sz{font-size:11px;text-transform:uppercase;letter-spacing:.16em;color:var(--muted);text-decoration:none;border:1px solid var(--line);border-radius:999px;padding:5px 12px;white-space:nowrap}
  a.sz:hover{color:var(--ink);border-color:var(--ink)}
  .frame{border:1px solid var(--hair);border-radius:15px;overflow:hidden;background:var(--card)}
  iframe{display:block;width:100%;height:min(80vh,900px);border:0;background:#fff}
  .hint{max-width:1560px;margin:0 auto;padding:0 clamp(16px,3vw,32px) 40px;font-size:13px;color:var(--muted)}
</style>
</head>
<body>
<div class="bar">
  <div class="top">
    <div>
      <div class="lbl" style="margin-bottom:8px"><i class="dash"></i>Pick a direction</div>
      <h1>FCG Developer Platform &mdash; homepage, realigned to the FCG brand</h1>
    </div>
    <div class="lbl">open.fusionconnectgroup.com/home</div>
  </div>
  <div class="tabs" role="tablist" aria-label="Design directions"><!--TABS--></div>
</div>
<main><!--PANES--></main>
<p class="hint">Both directions use the same tokens, the same real wordmark and the same content. They differ in posture: A is editorial, B is a product surface. Scroll inside a frame to review the full page; the two live tabs are there for comparison only. Once you choose, the rest of the portal pages get built in the chosen direction.</p>

<!--PAYLOADS-->
<script>
(function(){
  var tabs=[].slice.call(document.querySelectorAll('.tab'));
  var loaded={};
  function show(key){
    tabs.forEach(function(t){
      var on=t.dataset.pane===key;
      t.setAttribute('aria-selected',on?'true':'false');
      document.getElementById('pane-'+t.dataset.pane).hidden=!on;
    });
    if(!loaded[key]){
      var payload=document.getElementById('src-'+key);
      var frame=document.querySelector('iframe[data-src="'+key+'"]');
      if(payload&&frame){
        // base64 -> UTF-8 without mangling non-ASCII
        var bin=atob(payload.textContent.trim());
        var bytes=new Uint8Array(bin.length);
        for(var i=0;i<bin.length;i++)bytes[i]=bin.charCodeAt(i);
        frame.srcdoc=new TextDecoder('utf-8').decode(bytes);
      }
      loaded[key]=true;
    }
    try{location.hash=key}catch(e){}
  }
  tabs.forEach(function(t){t.addEventListener('click',function(){show(t.dataset.pane)})});
  var start=(location.hash||'').replace('#','');
  show(tabs.some(function(t){return t.dataset.pane===start})?start:tabs[0].dataset.pane);
})();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
