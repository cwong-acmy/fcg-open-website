// Observation check for the Direction B portal pages.
//
// Attaches to the always-on Chrome for Testing on :9222 (never launches one),
// loads every page at 1280 and 375, forces the scroll-reveal animations to their
// end state so full-page captures are not blank, and asserts the brand rules that
// a screenshot alone will not tell you about.
//
// Usage: NODE_PATH=$(npm root -g) node verify-pages.js [pageName ...]

const puppeteer = require("puppeteer-core");
const path = require("path");

// first arg may be a locale subdirectory: node verify-pages.js zh-Hans [pages...]
const argv = process.argv.slice(2);
const LOCALE = ["zh-Hans", "zh-Hant"].includes(argv[0]) ? argv.shift() : "";
const DIR = path.join(__dirname, "variant-b-impeccable", LOCALE);
const OUT = path.join(__dirname, "shots", "b-pages");
const ALL = [
  "index", "app-management", "api-docs-hotel", "api-docs-hotel-process",
  "api-docs-hotel-apis", "api-docs-flink", "api-docs-errors", "sdk",
  "skills", "ai-assistant", "login", "register",
];

const pages = argv.length ? argv : ALL;

function audit() {
  const surf = [], smallOrange = [], overlap = [], misalign = [], fonts = new Set();

  const accentInk = getComputedStyle(document.documentElement)
    .getPropertyValue("--accent-ink").trim();
  const offToken = [];

  document.querySelectorAll("body *").forEach((e) => {
    const cs = getComputedStyle(e);
    // The accent may fill a dot, a dash, a thin arc, the terminal cursor and the
    // small circle on a tertiary link. It must never fill a button or a panel,
    // so the failure threshold is button scale, not any fill at all.
    if (cs.backgroundColor === "rgb(249, 115, 22)") {
      const r = e.getBoundingClientRect();
      if (r.width > 44 && r.height > 44) surf.push(e.className || e.tagName);
    }
    // Small orange text is intended — it is the marketing site's own eyebrow
    // treatment. Just count it, so a jump in the count is visible in review.
    if (e.textContent.trim() && parseFloat(cs.fontSize) < 18 &&
        cs.color === "rgb(249, 115, 22)") {
      smallOrange.push(e.tagName + "." + e.className);
    }
  });
  // Every small orange label must resolve through --accent-ink, so switching to
  // the AA-passing #C2410C stays a one-token change.
  if (accentInk !== "#F97316" && accentInk !== "#C2410C") offToken.push("--accent-ink=" + accentInk);

  document
    .querySelectorAll("h1,h2,h3,h4,p,a,button,code,pre,td,th,li,label,input,select,span")
    .forEach((e) => fonts.add(getComputedStyle(e).fontFamily.split(",")[0].replace(/"/g, "")));

  // sibling boxes in a grid/flex track must not intersect
  document.querySelectorAll(".mini,.steps,.cards,.iopts,.fields--2").forEach((g) => {
    const k = [...g.children].map((x) => x.getBoundingClientRect());
    for (let i = 0; i < k.length; i++)
      for (let j = i + 1; j < k.length; j++)
        if (k[i].left < k[j].right - 1 && k[j].left < k[i].right - 1 &&
            k[i].top < k[j].bottom - 1 && k[j].top < k[i].bottom - 1)
          overlap.push(g.className);
  });

  // within one visual row of cards, the meta blocks must start at the same y
  document.querySelectorAll(".cards").forEach((g) => {
    const rows = {};
    [...g.children].forEach((c) => {
      const t = Math.round(c.getBoundingClientRect().top / 5) * 5;
      (rows[t] = rows[t] || []).push(c);
    });
    Object.values(rows).forEach((row) => {
      const ys = row
        .map((c) => c.querySelector(":scope > .card-meta"))
        .filter(Boolean)
        .map((x) => Math.round(x.getBoundingClientRect().top));
      if (ys.length > 1 && Math.max(...ys) - Math.min(...ys) > 2) misalign.push(JSON.stringify(ys));
    });
  });

  // A table cell must never inherit panel styling. This is what catches a class
  // collision like td.path picking up an unscoped .path card (radius, big
  // padding, display:flex) from the donor stylesheet.
  const cellStyle = [];
  document.querySelectorAll("table.tbl td, table.tbl th").forEach((c) => {
    const cs = getComputedStyle(c);
    if (parseFloat(cs.borderTopLeftRadius) > 6) cellStyle.push("radius " + cs.borderTopLeftRadius);
    if (parseFloat(cs.paddingTop) > 26) cellStyle.push("padding " + cs.paddingTop);
    if (cs.display === "flex") cellStyle.push("display:flex");
  });

  // body{overflow-x:hidden} means an over-wide child is silently CLIPPED rather
  // than producing a document scrollbar, so H-SCROLL alone misses it. Compare
  // each .wrap's children against the wrap's own content box instead.
  // An element is clipped only if it is WIDER than the wrap's content box and
  // nothing between it and the wrap scrolls. Sitting at the padding edge is
  // fine (a flex row's last item), and so is being wide inside an
  // overflow-x:auto ancestor (the tab rail's links, a <pre>, a table).
  const clipped = [];
  document.querySelectorAll(".wrap").forEach((wrap) => {
    const wcs = getComputedStyle(wrap);
    const ww = wrap.getBoundingClientRect().width;
    if (!ww) return; // display:none wrap (the mobile menu) has no content box
    const inner = ww - parseFloat(wcs.paddingLeft) - parseFloat(wcs.paddingRight);
    wrap.querySelectorAll("*").forEach((el) => {
      const b = el.getBoundingClientRect();
      if (!b.width) return; // not laid out
      if (b.width <= inner + 1) return;
      const cs = getComputedStyle(el);
      if (cs.position === "absolute" || cs.position === "fixed") return;
      for (let a = el.parentElement; a && a !== wrap; a = a.parentElement) {
        const ox = getComputedStyle(a).overflowX;
        if (ox === "auto" || ox === "scroll") return;
      }
      const ox = cs.overflowX;
      if (ox === "auto" || ox === "scroll") return; // scrolls its own content
      clipped.push((el.className || el.tagName) + " " + Math.round(b.width) + "w");
    });
  });

  const hs = [...document.querySelectorAll("h1,h2,h3,h4,h5,h6")].map((e) => +e.tagName[1]);
  let skip = null;
  for (let i = 1; i < hs.length; i++)
    if (hs[i] - hs[i - 1] > 1) { skip = "h" + hs[i - 1] + "->h" + hs[i]; break; }

  return {
    sw: document.documentElement.scrollWidth,
    cw: document.documentElement.clientWidth,
    surf: [...new Set(surf)],
    smallOrangeCount: smallOrange.length,
    offToken: [...new Set(offToken)],
    overlap: [...new Set(overlap)],
    misalign,
    skip,
    badFont: [...fonts].filter((f) => !["Inter", "ui-monospace", "Iconify"].includes(f)),
    h1: document.querySelectorAll("h1").length,
    deadHref: document.querySelectorAll('a[href="#"]').length,
    cellStyle: [...new Set(cellStyle)],
    clipped: [...new Set(clipped)].slice(0, 4),
  };
}

(async () => {
  const browser = await puppeteer.connect({ browserURL: "http://localhost:9222" });
  const page = await browser.newPage();
  const errors = [];
  page.on("pageerror", (e) => errors.push("pageerror: " + e.message));
  page.on("console", (m) => { if (m.type() === "error") errors.push("console: " + m.text()); });

  let failing = 0;
  for (const w of [1280, 768, 375]) {
    await page.setViewport({ width: w, height: 900 });
    for (const name of pages) {
      // domcontentloaded, not networkidle2 — the Google Fonts / Iconify CDN stalls
      await page.goto("file://" + path.join(DIR, name + ".html"), {
        waitUntil: "domcontentloaded", timeout: 20000,
      });
      await page.evaluate(async () => {
        // force reveal animations to their end state, or a full-page shot comes out blank
        document.querySelectorAll(".rv").forEach((e) => {
          e.classList.add("in");
          e.style.transition = "none";
          e.style.opacity = 1;
          e.style.transform = "none";
        });
        try { await document.fonts.ready; } catch (_) {}
      });
      await new Promise((r) => setTimeout(r, 900));

      const m = await page.evaluate(audit);
      const f = [];
      if (m.sw > m.cw + 1) f.push(`H-SCROLL ${m.sw}>${m.cw}`);
      if (m.overlap.length) f.push("OVERLAP " + m.overlap);
      if (m.surf.length) f.push("ACCENT-SURFACE " + m.surf);
      if (m.offToken.length) f.push("ORANGE-OFF-TOKEN " + m.offToken);
      if (m.badFont.length) f.push("FONT " + m.badFont);
      if (m.h1 !== 1) f.push("H1=" + m.h1);
      if (m.skip) f.push("HEADING-SKIP " + m.skip);
      if (m.deadHref) f.push("DEAD-HREF x" + m.deadHref);
      if (m.cellStyle.length) f.push("TABLE-CELL-PANEL " + m.cellStyle);
      if (m.clipped.length) f.push("CLIPPED-BY-WRAP " + m.clipped);
      if (w === 1280 && m.misalign.length) f.push("META-MISALIGN " + m.misalign);

      if (f.length) failing++;
      const info = w === 1280 ? `  small-orange x${m.smallOrangeCount}` : "";
      console.log(`${w} ${name.padEnd(26)}${f.length ? " FAIL " + f.join(" | ") : " ok"}${info}`);
      try {
        await page.screenshot({ path: path.join(OUT, `${LOCALE ? LOCALE + "-" : ""}${name}-${w}.png`), fullPage: true });
      } catch (e) {
        // a capture hiccup on a very tall page must not mask the checks above
        console.log(`     (screenshot skipped: ${e.message.split("\n")[0]})`);
      }
    }
  }

  console.log(`\nJS errors: ${errors.length ? JSON.stringify([...new Set(errors)].slice(0, 6)) : "none"}`);
  console.log(`Failing checks: ${failing} / ${pages.length * 3}`);
  await page.close();
  browser.disconnect();
  process.exit(failing || errors.length ? 1 : 0);
})();
