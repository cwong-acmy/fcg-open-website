// Motion audit for the Direction B portal pages.
//
// Checks the rules Emil Kowalski's design-engineering framework actually cares
// about, against the live stylesheets in Chrome for Testing on :9222.
//
// Usage: NODE_PATH=$(npm root -g) node verify-motion.js [pageName ...]

const puppeteer = require("puppeteer-core");
const path = require("path");

const DIR = path.join(__dirname, "variant-b-impeccable");
const ALL = [
  "index", "app-management", "api-docs-hotel", "api-docs-hotel-process",
  "api-docs-hotel-apis", "api-docs-flink", "api-docs-errors", "sdk",
  "skills", "ai-assistant", "login", "register",
];
const pages = process.argv.slice(2).length ? process.argv.slice(2) : ALL;

// Pressable things that must give press feedback, and the selector each one
// needs an :active rule for.
const PRESSABLE = [
  ".btn", ".shell a", ".lang button", ".burger", ".rail a",
  ".oauth", ".asks button", ".cmd button", ".docs-grp a",
];

function audit(pressable) {
  // NOTE: in current Chrome a CSSStyleRule ALSO exposes .cssRules (an empty
  // list) because nested CSS made it a grouping rule. A truthiness check on
  // .cssRules therefore recurses into every leaf and collects nothing — test
  // .style first, and recurse only on a non-empty list.
  const flat = [];
  const inMedia = new Set();

  function walk(list, mediaText) {
    for (const rule of list) {
      if (rule.style) {
        flat.push(rule);
        if (mediaText) inMedia.add(rule);
      }
      if (rule.cssRules && rule.cssRules.length) {
        walk(rule.cssRules, rule.conditionText || rule.media?.mediaText || mediaText);
      }
    }
  }
  for (const sheet of document.styleSheets) {
    try {
      walk(sheet.cssRules, null); // cross-origin sheets throw; skipped
    } catch (e) {}
  }

  const sel = (r) => r.selectorText || "";
  const ms = (v) =>
    (v || "")
      .split(",")
      .map((x) => x.trim())
      .map((x) => (x.endsWith("ms") ? parseFloat(x) : parseFloat(x) * 1000))
      .filter((x) => !isNaN(x));

  const findings = {
    ruleCount: flat.length,
    transitionAll: [],
    scaleZero: [],
    easeIn: [],
    slowUI: [],
    layoutAnimated: [],
    missingPress: [],
    ungatedHover: [],
  };

  for (const r of flat) {
    const tp = (r.style.transitionProperty || "").trim();
    if (tp === "all") findings.transitionAll.push(sel(r));

    // nothing in the real world appears from nothing
    if (/scale\(0\)/.test(r.style.transform || "")) findings.scaleZero.push(sel(r));

    // ease-in delays the moment the user is watching most closely
    const tf = (r.style.transitionTimingFunction || "") + " " + (r.style.animationTimingFunction || "");
    if (/(^|[\s,])ease-in([\s,]|$)/.test(tf)) findings.easeIn.push(sel(r));

    // UI transitions stay under 300ms; the scroll reveal is explanatory and exempt
    if (!/\.rv\b/.test(sel(r)) && ms(r.style.transitionDuration).some((x) => x > 300)) {
      findings.slowUI.push(sel(r) + " " + r.style.transitionDuration);
    }

    // only transform and opacity skip layout and paint
    if (/(^|[\s,])(width|height|margin|padding|top|left|right|bottom|gap|font-size)([\s,]|$)/.test(tp)) {
      findings.layoutAnimated.push(sel(r) + " -> " + tp);
    }

    // a hover animation outside a hover-capable query fires on tap
    if (/:hover/.test(sel(r)) && !inMedia.has(r)) findings.ungatedHover.push(sel(r));
  }

  for (const s of pressable) {
    if (!document.querySelector(s)) continue;
    const has = flat.some((r) =>
      sel(r)
        .split(",")
        .some((part) => part.trim().startsWith(s + ":active"))
    );
    if (!has) findings.missingPress.push(s);
  }

  for (const k of Object.keys(findings)) {
    if (Array.isArray(findings[k])) findings[k] = [...new Set(findings[k])];
  }
  return findings;
}

(async () => {
  const browser = await puppeteer.connect({ browserURL: "http://localhost:9222" });
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 900 });

  let failing = 0;
  for (const name of pages) {
    await page.goto("file://" + path.join(DIR, name + ".html"), {
      waitUntil: "domcontentloaded",
      timeout: 20000,
    });
    await new Promise((r) => setTimeout(r, 350));
    const m = await page.evaluate(audit, PRESSABLE);

    const f = [];
    if (!m.ruleCount) f.push("NO RULES READ (audit is broken, not the page)");
    if (m.transitionAll.length) f.push("transition:all " + m.transitionAll);
    if (m.scaleZero.length) f.push("scale(0) " + m.scaleZero);
    if (m.easeIn.length) f.push("ease-in " + m.easeIn);
    if (m.slowUI.length) f.push("UI>300ms " + m.slowUI.slice(0, 3));
    if (m.layoutAnimated.length) f.push("layout-animated " + m.layoutAnimated.slice(0, 3));
    if (m.missingPress.length) f.push("no :active on " + m.missingPress);
    if (m.ungatedHover.length) f.push("ungated hover " + m.ungatedHover.slice(0, 3));

    if (f.length) failing++;
    console.log(`${name.padEnd(24)}${f.length ? "FAIL " + f.join(" | ") : "ok"}  (${m.ruleCount} rules)`);
  }

  console.log(`\nMotion failures: ${failing} / ${pages.length}`);
  await page.close();
  browser.disconnect();
  process.exit(failing ? 1 : 0);
})();
