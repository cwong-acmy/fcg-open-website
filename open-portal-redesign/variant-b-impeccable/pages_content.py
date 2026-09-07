# -*- coding: utf-8 -*-
"""
Page content for the Direction B portal build.

Every fact here — endpoint paths, methods, versions, error codes, rate limits,
SDK install commands — was read off the live portal at open.fusionconnectgroup.com
on 7 September 2026. Nothing is invented. Copy is rewritten into FCG's
declarative voice in British English; the substance is unchanged.
"""

ARROW = '<iconify-icon icon="solar:arrow-right-linear" aria-hidden="true"></iconify-icon>'
DL = '<iconify-icon icon="solar:download-minimalistic-linear" aria-hidden="true"></iconify-icon>'


def band(eyebrow, h1, lede, crumb=None, foot=None, chip=None):
    """Page band. `chip` sits on the eyebrow line — the CTA row holds only CTAs."""
    c = ""
    if crumb:
        parts = []
        for label, href in crumb:
            parts.append(f'<a href="{href}">{label}</a>' if href else f"<span>{label}</span>")
        c = f'      <p class="crumb">{" <i>/</i> ".join(parts)}</p>\n'
    ch = (
        f'<span class="chip chip--live"><span class="dot" aria-hidden="true"></span>{chip}</span>'
        if chip else ""
    )
    f = f'      <div class="band-foot">{foot}</div>\n' if foot else ""
    return f"""<section class="band">
  <div class="band-grid" aria-hidden="true"></div>
  <div class="wrap band-in">
{c}      <div class="band-top">
        <p class="eyebrow micro">{eyebrow}</p>
        {ch}
      </div>
      <h1>{h1}</h1>
      <p class="lede">{lede}</p>
{f}  </div>
</section>"""


def tbl(head, rows, minw=640):
    ths = "".join(f"<th>{h}</th>" for h in head)
    trs = "\n".join("      <tr>" + "".join(r) + "</tr>" for r in rows)
    return f"""<div class="tblwrap"><div class="tblscroll">
  <table class="tbl" style="min-width:{minw}px">
    <thead><tr>{ths}</tr></thead>
    <tbody>
{trs}
    </tbody>
  </table>
</div></div>"""


def rail(items, active):
    out = []
    for label, href in items:
        on = ' class="on"' if label == active else ""
        out.append(f'<a{on} href="{href}">{label}</a>')
    return '<nav class="rail" aria-label="Section">' + "".join(out) + "</nav>"


DOCS_RAIL = [
    ("G-Link Hotel", "api-docs-hotel.html"),
    ("F-Link Flight", "api-docs-flink.html"),
    ("Integration flow", "api-docs-hotel-process.html"),
    ("API reference", "api-docs-hotel-apis.html"),
    ("Error codes", "api-docs-errors.html"),
]


def docs_side(active):
    def grp(t, links):
        gid = "nav-" + t.lower().replace(" ", "-")
        lis = "".join(
            f'<li><a{" class=\"on\"" if lb == active else ""} href="{h}">{lb}</a></li>'
            for lb, h in links
        )
        return (
            f'      <div class="docs-grp"><p class="docs-h" id="{gid}">{t}</p>'
            f'<nav aria-labelledby="{gid}"><ul>{lis}</ul></nav></div>'
        )
    return f"""  <aside class="docs-side">
    <div class="docs-side-in">
{grp("Product docs", [("G-Link Hotel API", "api-docs-hotel.html"), ("F-Link Flight API", "api-docs-flink.html"), ("Error code reference", "api-docs-errors.html")])}
{grp("G-Link sections", [("Integration flow", "api-docs-hotel-process.html"), ("API reference", "api-docs-hotel-apis.html")])}
{grp("Developer tools", [("SDK downloads", "sdk.html"), ("Skills packages", "skills.html"), ("AI Assistant", "ai-assistant.html")])}
    </div>
  </aside>"""


# ============================================================ app management

APPS = [
    (
        "G-Link Hotel",
        "G-Link Hotel API",
        "Hotel search, booking, payment and cancellation workflows.",
        "28 April 2026",
        None,
    ),
    (
        "F-Link Flight",
        "F-Link Flight API",
        "Flight search, ticketing, refunds and changes.",
        "28 April 2026",
        None,
    ),
    (
        "TMC API",
        "TMC API",
        "Rapid deployment of corporate travel platforms.",
        "28 April 2026",
        "The TMC API sandbox supports USD only.",
    ),
]


def app_cards():
    out = []
    for code, name, what, created, note in APPS:
        n = (
            f'      <div class="note" style="margin:0 24px 20px"><iconify-icon icon="solar:info-circle-linear"></iconify-icon>'
            f"<span>{note}</span></div>"
            if note
            else ""
        )
        out.append(
            f"""  <article class="card rv">
    <div class="card-h">
      <p class="card-k"><span class="dot" aria-hidden="true"></span>{code}</p>
      <h3>{name}</h3>
      <p>{what}</p>
    </div>
    <div class="card-meta">
      <div><span class="k">App key</span><span class="v">••••••••••••</span></div>
      <div><span class="k">App secret</span><span class="v">••••••••••••</span></div>
      <div><span class="k">Created</span><span class="v">{created}</span></div>
      <div><span class="k">Environment</span><span class="v">Sandbox</span></div>
    </div>
{n}    <div class="card-f">
      <a class="btn btn--sm" href="login.html">View credentials {ARROW}</a>
      <a class="tlink" href="api-docs-hotel.html">Product docs {ARROW}</a>
    </div>
  </article>"""
        )
    return "\n".join(out)


APP_MANAGEMENT = f"""
{band(
    "Independent credentials per product",
    "App Management",
    "<b>Manage the applications behind an API integration.</b> Each product carries its own credential set, "
    "so a hotel key never unlocks a flight endpoint and a sandbox key never reaches production.",
    foot=f'<a class="btn" href="register.html">Create an application {ARROW}</a>'
         f'<a class="btn btn--ghost" href="login.html">Sign in to the console {ARROW}</a>',
)}

<section class="blk blk--top">
  <div class="wrap">
    <div class="blk-head">
      <p class="eyebrow micro">Applications</p>
      <h2 class="h3">Three applications, <em>three credential sets.</em></h2>
      <p class="lede">Credentials are shown in the console once signed in. Nothing on this page reveals a live key.</p>
    </div>
    <div class="cards">
{app_cards()}
    </div>
  </div>
</section>

<hr class="rule">

<section class="blk">
  <div class="wrap">
    <div class="cards cards--2">
      <article class="card rv">
        <div class="card-h">
          <p class="card-k"><span class="dot" aria-hidden="true"></span>Application example</p>
          <h3>Traveller-facing client homepage.</h3>
          <p>A complete client example wired to G-Link hotel and F-Link flight real-time inventory.
             Open it, read it, then take the source and start building.</p>
        </div>
        <div class="card-meta" style="padding-bottom:4px">
          <div><span class="k">Inventory</span><span class="v">G-Link &amp; F-Link, live</span></div>
          <div><span class="k">Source</span><span class="v">Available on request</span></div>
          <div><span class="k">Environment</span><span class="v">Sandbox</span></div>
        </div>
        <div class="card-f card-f--plain">
          <a class="btn btn--sm" href="api-docs-hotel.html">Open full client {ARROW}</a>
          <a class="tlink" href="sdk.html">Download source {DL}</a>
        </div>
      </article>
      <article class="card rv">
        <div class="card-h">
          <p class="card-k"><span class="dot" aria-hidden="true"></span>Environments</p>
          <h3>Sandbox first, production by volume.</h3>
          <p>Test the full API set in sandbox at no upfront cost. Production keys are issued once
             integration testing passes, and billed on usage with no minimum spend.</p>
        </div>
        <div class="card-meta" style="padding-bottom:4px">
          <div><span class="k">Sandbox</span><span class="v">Open on registration</span></div>
          <div><span class="k">Production rate limit</span><span class="v">100 req / min</span></div>
          <div><span class="k">Billing</span><span class="v">Usage-based</span></div>
        </div>
        <div class="card-f card-f--plain">
          <a class="btn btn--sm" href="register.html">Register for free {ARROW}</a>
        </div>
      </article>
    </div>
  </div>
</section>
"""

# ============================================================ G-Link overview

HOTEL_MANDATORY = [
    ("1", "Available hotel ID list", "POST", "/openapi/v1/glink/search/hotelIdList"),
    ("2", "Query hotel basic information", "POST", "/openapi/v1/glink/hotel/detail"),
    ("3", "Hotel real-time product query", "POST", "/openapi/v1/glink/booking/productDetails"),
    ("4", "Trial booking (availability check)", "POST", "/openapi/v1/glink/booking/availabilityCheck"),
    ("5", "Create order", "POST", "/openapi/v1/glink/booking/createOrder"),
    ("6", "Order payment", "POST", "/openapi/v1/glink/booking/payOrder"),
    ("7", "Cancel order", "POST", "/openapi/v1/glink/order/cancelOrder"),
    ("8", "Order detail query", "POST", "/openapi/v1/glink/order/orderDetail"),
]


def mandatory_rows():
    return [
        (
            f'<td class="t-num">{n}</td>',
            f"<td>{name}</td>",
            f'<td class="t-mid"><span class="method">{m}</span></td>',
            f'<td class="t-path">{p}</td>',
        )
        for n, name, m, p in HOTEL_MANDATORY
    ]


API_DOCS_HOTEL = f"""
{band(
    "Supports both SDK and API integration",
    "G-Link Hotel API",
    "<b>Major global hotel inventory</b> over one standardised interface. The full workflow runs from "
    "real-time search and trial booking through to reservation, payment and cancellation.",
    crumb=[("Docs centre", "api-docs-hotel.html"), ("G-Link Hotel API", None)],
    foot=rail(DOCS_RAIL, "G-Link Hotel")
         + f'<a class="btn btn--sm" href="sdk.html">Download SDK {DL}</a>',
)}

<div class="wrap">
<div class="docs">
{docs_side("G-Link Hotel API")}
  <div class="docs-main">
    <h2>Eight interfaces carry a complete hotel booking.</h2>
    <p>These are the mandatory endpoints. Everything else in the reference is static data,
       incremental updates or callback handling built around them.</p>

    {tbl(["No.", "Interface", "Method", "Path"], mandatory_rows(), 700)}

    <h3>Mandatory interfaces, and when to call them</h3>
    <ul class="bul">
      <li><iconify-icon icon="solar:magnifer-linear"></iconify-icon><span><strong>Hotel daily lowest price</strong> —
        <code class="inl">hotel/lowestPrice</code>. Queries the lowest price for mapped hotels, as the reference for
        whether a hotel appears in a local hotel list.</span></li>
      <li><iconify-icon icon="solar:bed-linear"></iconify-icon><span><strong>Hotel real-time product query</strong> —
        <code class="inl">booking/productDetails</code>. Called in real time when a customer enters the hotel detail
        or booking path.</span></li>
      <li><iconify-icon icon="solar:check-circle-linear"></iconify-icon><span><strong>Trial booking</strong> —
        <code class="inl">booking/availabilityCheck</code>. Validates that a bookable product can be reserved,
        passing the actual number of rooms.</span></li>
      <li><iconify-icon icon="solar:document-add-linear"></iconify-icon><span><strong>Create order</strong> —
        <code class="inl">booking/createOrder</code>. Called once trial booking passes and the local order is created.
        Run trial booking again immediately before this call.</span></li>
      <li><iconify-icon icon="solar:card-linear"></iconify-icon><span><strong>Order payment</strong> —
        <code class="inl">booking/payOrder</code>. Called after the local customer pays, or when an order needs
        confirmation, to notify the service team to process it.</span></li>
      <li><iconify-icon icon="solar:close-circle-linear"></iconify-icon><span><strong>Cancel order</strong> —
        <code class="inl">order/cancelOrder</code>. Called when an order is unpaid for 30 minutes, or the customer
        cancels. A success response means polling should stop.</span></li>
      <li><iconify-icon icon="solar:bell-linear"></iconify-icon><span><strong>Order status push</strong> —
        <code class="inl">notify/orderStatus</code>. After payment notification, the service team processes the order
        and pushes status. This interface must be idempotent.</span></li>
      <li><iconify-icon icon="solar:refresh-linear"></iconify-icon><span><strong>Order detail query</strong> —
        <code class="inl">order/orderDetail</code>. Compensation only, if no confirmation arrives after payment.
        Frequent polling is unnecessary; stop once the order is confirmed or cancelled.</span></li>
    </ul>

    <h3>Static data and incremental updates</h3>
    <p>Pull the available hotel list from <code class="inl">search/hotelIdList</code>, then take hotel and room-type
       detail from <code class="inl">/hotel/detail</code>. <code class="inl">region/countries</code> and
       <code class="inl">region/cities</code> supply country and city reference data, normally used to build
       foundational data and map against the FCG hotel system.</p>
    <p>Call <code class="inl">/hotel/increment</code> periodically for the list of hotel IDs whose static information
       has changed — additions, modifications and deletions — then resynchronise the affected records rather than
       re-pulling the full set.</p>

    <div class="note">
      <iconify-icon icon="solar:info-circle-linear"></iconify-icon>
      <span><strong>Rate limits.</strong> Production defaults to 100 requests per minute per application.
      Cache static data locally and reserve live calls for search, trial booking and order operations.</span>
    </div>

    <div class="band-foot">
      <a class="btn" href="api-docs-hotel-process.html">Read the integration flow {ARROW}</a>
      <a class="tlink tlink--o" href="api-docs-hotel-apis.html">Full API reference {ARROW}</a>
    </div>
  </div>
</div>
</div>
"""

# ============================================================ integration flow

HOTEL_STEPS = [
    ("Query all available hotel IDs", "/search/hotelIdList"),
    ("Query hotel static information by hotel ID", "/hotel/detail"),
    ("Real-time query of sales information and lowest price", "/booking/productDetails"),
    ("Check the rate plan is bookable and return the latest price", "/booking/availabilityCheck"),
    ("Create the order once trial booking succeeds", "/booking/createOrder"),
    ("Take payment after order creation", "/booking/payOrder"),
    ("Query order details", "/order/orderDetail"),
    ("Cancel the order as needed", "/order/cancelOrder"),
]


def steps():
    out = []
    for i, (what, path) in enumerate(HOTEL_STEPS, 1):
        out.append(
            f"""  <div class="step rv">
    <p class="sn"><span class="dot" aria-hidden="true"></span>Step {i:02d}</p>
    <h3>{what}</h3>
    <code>{path}</code>
  </div>"""
        )
    return "\n".join(out)


API_DOCS_HOTEL_PROCESS = f"""
{band(
    "Recommended integration flow",
    "G-Link Integration Flow",
    "<b>The order in which to wire the G-Link hotel API.</b> Eight steps, "
    "search through to cancellation, each one a single endpoint.",
    crumb=[("Docs centre", "api-docs-hotel.html"), ("G-Link Hotel API", "api-docs-hotel.html"), ("Integration flow", None)],
    foot=rail(DOCS_RAIL, "Integration flow"),
)}

<div class="wrap">
<div class="docs">
{docs_side("Integration flow")}
  <div class="docs-main">
    <h2>Standard API integration, <em>in order.</em></h2>
    <p>Follow the sequence. Steps one and two build local reference data and run on a schedule;
       steps three onwards are live and run per booking.</p>

    <div class="steps">
{steps()}
    </div>

    <h3>What runs on a schedule, and what runs live</h3>
    <ul class="bul">
      <li><iconify-icon icon="solar:calendar-linear"></iconify-icon><span><strong>Scheduled.</strong>
        Hotel ID list, hotel and room-type static information, country and city reference data, and the
        <code class="inl">/hotel/increment</code> change feed. Cache all of it locally.</span></li>
      <li><iconify-icon icon="solar:bolt-linear"></iconify-icon><span><strong>Live.</strong>
        Product details, trial booking, order creation, payment, cancellation and order detail. These are
        called per traveller action and count against the rate limit.</span></li>
      <li><iconify-icon icon="solar:shield-check-linear"></iconify-icon><span><strong>Idempotent.</strong>
        The order status push, <code class="inl">notify/orderStatus</code>, may be delivered more than once.
        Handle repeats without creating duplicate state.</span></li>
    </ul>

    <div class="note">
      <iconify-icon icon="solar:danger-triangle-linear"></iconify-icon>
      <span><strong>Trial booking twice.</strong> Run <code class="inl">booking/availabilityCheck</code> again
      immediately before <code class="inl">booking/createOrder</code>. Inventory and price can move between the
      customer's decision and the order call.</span>
    </div>

    <div class="band-foot">
      <a class="btn" href="api-docs-hotel-apis.html">Open the API reference {ARROW}</a>
      <a class="tlink tlink--o" href="skills.html">Install the G-Link Skills package {ARROW}</a>
    </div>
  </div>
</div>
</div>
"""

# ============================================================ API reference

COUNTRY_REQ = [
    ("language", "string", "Optional", "Language. <code class=\"inl\">zh-CN</code> for Chinese, <code class=\"inl\">en-US</code> for English. Defaults to English.", False),
]

COUNTRY_RES = [
    ("code", "string", "Required", "Platform business code. <code class=\"inl\">SUCCESS</code> indicates success. A supplier business failure can still return HTTP 200 with <code class=\"inl\">code=SUPPLIER_BIZ_ERROR</code>.", False),
    ("data", "array&lt;object&gt;", "Optional", "Country list.", False),
    ("countryCode", "string", "Required", "Country code.", True),
    ("countryId", "string", "Required", "Country ID.", True),
    ("countryName", "string", "Required", "Country name.", True),
    ("downstream_request_id", "string", "Optional", "G-Link downstream request ID. Usually returned after a successful call.", False),
    ("message", "string", "Required", "Platform message. Typically <code class=\"inl\">ok</code> on success.", False),
    ("request_id", "string", "Required", "Platform request ID.", False),
    ("trace_id", "string", "Required", "Platform trace ID.", False),
]


def plist(rows):
    out = []
    for name, typ, req, desc, sub in rows:
        cls = ' class="sub"' if sub else ""
        rq = ' req' if req == "Required" else ""
        out.append(
            f'    <li{cls}><span class="pn">{name}</span><span class="pt">{typ}</span>'
            f'<span class="pr{rq}">{req}</span><span class="pd">{desc}</span></li>'
        )
    return '<ul class="plist">\n' + "\n".join(out) + "\n  </ul>"


REF_GROUPS = [
    ("Regional static information", [
        ("Query country list", "POST", "/openapi/v1/glink/region/countries", True),
        ("Query city list", "POST", "/openapi/v1/glink/region/cities", False),
        ("Query popular city list", "POST", "/openapi/v1/glink/region/hotCities", False),
        ("Query business district list", "POST", "/openapi/v1/glink/region/businessZones", False),
        ("Query administrative district list", "POST", "/openapi/v1/glink/region/districts", False),
    ]),
    ("Hotel information", [
        ("Available hotel ID list", "POST", "/openapi/v1/glink/search/hotelIdList", False),
        ("Query hotel basic information", "POST", "/openapi/v1/glink/hotel/detail", False),
        ("Hotel daily lowest price", "POST", "/openapi/v1/glink/hotel/lowestPrice", False),
        ("Hotel static information increment", "POST", "/openapi/v1/glink/hotel/increment", False),
    ]),
    ("Hotel booking", [
        ("Hotel real-time product query", "POST", "/openapi/v1/glink/booking/productDetails", False),
        ("Trial booking (availability check)", "POST", "/openapi/v1/glink/booking/availabilityCheck", False),
        ("Create order", "POST", "/openapi/v1/glink/booking/createOrder", False),
        ("Order payment", "POST", "/openapi/v1/glink/booking/payOrder", False),
    ]),
    ("Order information", [
        ("Order detail query", "POST", "/openapi/v1/glink/order/orderDetail", False),
        ("Cancel order", "POST", "/openapi/v1/glink/order/cancelOrder", False),
    ]),
    ("Callback notification", [
        ("Order status push", "POST", "/openapi/v1/glink/notify/orderStatus", False),
    ]),
]


def ref_rows():
    rows = []
    for group, eps in REF_GROUPS:
        rows.append((f'<td colspan="3" style="background:var(--card);font-size:9.5px;font-weight:600;'
                     f'letter-spacing:.18em;text-transform:uppercase;color:var(--muted-card);padding:11px 20px">'
                     f'{group}</td>',))
        for name, m, path, cur in eps:
            mark = ' style="background:rgba(15,17,20,.02)"' if cur else ""
            rows.append((
                f"<td{mark}>{name}</td>",
                f'<td class="t-mid"{mark}><span class="method">{m}</span></td>',
                f'<td class="t-path"{mark}>{path}</td>',
            ))
    return rows


API_DOCS_HOTEL_APIS = f"""
{band(
    "Sandbox and production",
    "G-Link API Reference",
    "<b>Every G-Link endpoint, grouped by what it does.</b> One is expanded in full below as the "
    "worked example; the request and response shape is consistent across the set.",
    crumb=[("Docs centre", "api-docs-hotel.html"), ("G-Link Hotel API", "api-docs-hotel.html"), ("API reference", None)],
    foot=rail(DOCS_RAIL, "API reference"),
)}

<div class="wrap">
<div class="docs">
{docs_side("API reference")}
  <div class="docs-main">
    <h2>Twenty endpoints, <em>five groups.</em></h2>
    <p>Static data first, then live booking, then orders and callbacks. Paths are shown against the
       production host; the sandbox host is issued with sandbox credentials.</p>

    {tbl(["Interface", "Method", "Path"], ref_rows(), 660)}

    <h3>Worked example — query country list</h3>
    <div class="ep">
      <div class="ep-h">
        <span class="method">POST</span>
        <code>https://open.fusionconnectgroup.com/openapi/v1/glink/region/countries</code>
      </div>
      <div class="ep-b">
        <h4>Interface description</h4>
        <div class="card-meta" style="padding:0;margin-top:14px">
          <div><span class="k">Caller</span><span class="v">Partner</span></div>
          <div><span class="k">Responder</span><span class="v">FCG</span></div>
          <div><span class="k">Rate limit</span><span class="v">100 req / min</span></div>
        </div>
        <p style="color:var(--muted);font-size:14px;line-height:23px;margin-top:16px;max-width:70ch">
          Partners call this endpoint to query the country list held in the FCG system, normally once,
          as part of building local reference data.</p>
      </div>
      <div class="ep-b">
        <h4>Body parameters</h4>
        <div style="margin-top:14px">{plist(COUNTRY_REQ)}</div>
      </div>
      <div class="ep-b">
        <h4>Response structure</h4>
        <div style="margin-top:14px">{plist(COUNTRY_RES)}</div>
      </div>
      <div class="ep-b" style="padding:0">
        <div class="term" style="border-radius:0;border:0">
          <div class="term-bar">
            <span class="dot" aria-hidden="true"></span>
            <span class="t-label">Request</span>
            <span class="t-right">application/json</span>
          </div>
          <div class="term-body"><pre>{{
  <span class="t-key">"language"</span>: <span class="t-dim">"en-US"</span>
}}</pre></div>
          <div class="term-split"><span>Response</span></div>
          <div class="term-body"><pre>{{
  <span class="t-key">"code"</span>: <span class="t-dim">"SUCCESS"</span>,
  <span class="t-key">"data"</span>: [
    {{
      <span class="t-key">"countryCode"</span>: <span class="t-dim">"CN"</span>,
      <span class="t-key">"countryId"</span>: <span class="t-dim">"5302980"</span>,
      <span class="t-key">"countryName"</span>: <span class="t-dim">"China"</span>
    }}
  ],
  <span class="t-key">"message"</span>: <span class="t-dim">"ok"</span>,
  <span class="t-key">"request_id"</span>: <span class="t-dim">"req_dc3qor2zg6omq…"</span>,
  <span class="t-key">"trace_id"</span>: <span class="t-dim">"trc_dc3qor2zg6omq…"</span>
}}</pre></div>
        </div>
      </div>
    </div>

    <div class="note">
      <iconify-icon icon="solar:info-circle-linear"></iconify-icon>
      <span><strong>Read <code class="inl">code</code>, not the HTTP status.</strong> A supplier business failure
      returns HTTP 200 with <code class="inl">code=SUPPLIER_BIZ_ERROR</code>. Branch on the body.</span>
    </div>

    <div class="band-foot">
      <a class="btn" href="api-docs-errors.html">Error code reference {ARROW}</a>
      <a class="tlink tlink--o" href="sdk.html">Use an SDK instead {ARROW}</a>
    </div>
  </div>
</div>
</div>
"""

# ============================================================ F-Link

FLINK = [
    ("1", "Flight search", "POST", "/openapi/v1/flink/{lang}/flight/search"),
    ("2", "Get more fare quotes", "POST", "/openapi/v1/flink/{lang}/flight/cabin"),
    ("3", "Pre-booking price verification", "POST", "/openapi/v1/flink/{lang}/flight/verify"),
    ("4", "Submit pre-booking order", "POST", "/openapi/v1/flink/{lang}/flight/order/create"),
    ("5", "Order payment", "POST", "/openapi/v1/flink/{lang}/flight/order/pay"),
    ("6", "Standard order details", "POST", "/openapi/v1/flink/{lang}/flight/order/detail"),
    ("7", "Cancel standard order", "POST", "/openapi/v1/flink/{lang}/flight/order/cancel"),
    ("8", "Change flight search", "POST", "/openapi/v1/flink/{lang}/flight/change/search"),
    ("9", "Submit change request", "POST", "/openapi/v1/flink/{lang}/flight/change/apply"),
    ("10", "Cancel change request", "POST", "/openapi/v1/flink/{lang}/flight/change/cancel"),
    ("11", "Change request details", "POST", "/openapi/v1/flink/{lang}/flight/change/detail"),
    ("12", "Submit refund request", "POST", "/openapi/v1/flink/{lang}/flight/refund/apply"),
    ("13", "Refund request details", "POST", "/openapi/v1/flink/{lang}/flight/refund/detail"),
    ("14", "Confirm or cancel refund", "POST", "/openapi/v1/flink/{lang}/flight/refund/confirm"),
    ("15", "Query airport information", "POST", "/openapi/v1/flink/{lang}/airports/list"),
    ("16", "Query airline information", "POST", "/openapi/v1/flink/{lang}/airlines/list"),
    ("17", "Search airport information", "POST", "/openapi/v1/flink/{lang}/airports/search"),
    ("18", "Query nationality list", "POST", "/openapi/v1/flink/{lang}/nationality/list"),
    ("19", "Query translation information", "GET", "/openapi/v1/flink/fields"),
]


def flink_rows():
    out = []
    for n, name, m, p in FLINK:
        cls = "method method--get" if m == "GET" else "method"
        out.append((
            f'<td class="t-num">{n}</td>',
            f"<td>{name}</td>",
            f'<td class="t-mid"><span class="{cls}">{m}</span></td>',
            f'<td class="t-path">{p.replace("{lang}", "&#123;lang&#125;")}</td>',
        ))
    return out


API_DOCS_FLINK = f"""
{band(
    "Direct airline seat inventory",
    "F-Link Flight API",
    "<b>Direct airline seat inventory.</b> Domestic and international carriers with BSP support, "
    "covering search, pricing, ticketing, refunds and changes. Nineteen endpoints, one path pattern.",
    crumb=[("Docs centre", "api-docs-hotel.html"), ("F-Link Flight API", None)],
    foot=rail(DOCS_RAIL, "F-Link Flight")
         + f'<a class="btn btn--sm" href="sdk.html">Download SDK {DL}</a>',
)}

<div class="wrap">
<div class="docs">
{docs_side("F-Link Flight API")}
  <div class="docs-main">
    <h2>All F-Link endpoints.</h2>
    <p>Every flight path carries a <code class="inl">&#123;lang&#125;</code> segment — <code class="inl">zh-CN</code>
       or <code class="inl">en-US</code> — which sets the language of returned labels and error messages.
       The translation endpoint is the one exception and takes no language segment.</p>

    {tbl(["No.", "Interface", "Method", "Path"], flink_rows(), 720)}

    <h3>How the set divides</h3>
    <ul class="bul">
      <li><iconify-icon icon="solar:magnifer-linear"></iconify-icon><span><strong>Search and price</strong> —
        <code class="inl">flight/search</code>, <code class="inl">flight/cabin</code>,
        <code class="inl">flight/verify</code>. Verify before booking; fares move.</span></li>
      <li><iconify-icon icon="solar:ticket-linear"></iconify-icon><span><strong>Book and ticket</strong> —
        <code class="inl">flight/order/create</code>, <code class="inl">flight/order/pay</code>,
        <code class="inl">flight/order/detail</code>, <code class="inl">flight/order/cancel</code>.</span></li>
      <li><iconify-icon icon="solar:restart-linear"></iconify-icon><span><strong>Change</strong> —
        four endpoints, from change search through to change detail. Changes inside four hours of departure
        are rejected and need manual handling.</span></li>
      <li><iconify-icon icon="solar:hand-money-linear"></iconify-icon><span><strong>Refund</strong> —
        apply, detail, then confirm or cancel.</span></li>
      <li><iconify-icon icon="solar:global-linear"></iconify-icon><span><strong>Reference data</strong> —
        airports, airlines, airport search, nationality list and field translations. Cache these locally.</span></li>
    </ul>

    <div class="note">
      <iconify-icon icon="solar:danger-triangle-linear"></iconify-icon>
      <span><strong>Verify immediately before order creation.</strong> <code class="inl">flight/verify</code>
      returns the current price and confirms the fare is still bookable. Skipping it is the most common cause
      of a failed <code class="inl">order/create</code>.</span>
    </div>

    <div class="band-foot">
      <a class="btn" href="api-docs-errors.html">Error code reference {ARROW}</a>
      <a class="tlink tlink--o" href="skills.html">Install the F-Link Skills package {ARROW}</a>
    </div>
  </div>
</div>
</div>
"""

# ============================================================ error codes

ERRORS = [
    ("10001", "Signature verification failed", "—", "API", "AppSecret is incorrect, or the signing algorithm does not match.", "Check the AppSecret and regenerate the signature using the signing guide."),
    ("10002", "AppKey does not exist or is disabled", "—", "—", "Application status is abnormal.", "Sign in to the console and check the application status. Contact support if it is disabled."),
    ("10003", "Request rate limit exceeded", "—", "API", "Call frequency exceeded the limit.", "Reduce call frequency and cache locally. Production defaults to 100 requests per minute."),
    ("20001", "Invalid city code", "G-Link", "—", "The cityCode is not in the supported list.", "Use a standard city code from the G-Link city code table."),
    ("20002", "Invalid date format", "G-Link", "—", "The date does not follow YYYY-MM-DD.", "Send dates as YYYY-MM-DD, for example 2026-04-01."),
    ("20003", "Hotel is not bookable", "G-Link", "—", "The selected hotel or room type is temporarily unavailable.", "Choose another room type, or contact support to confirm the hotel status."),
    ("30001", "Flight is fully booked", "F-Link", "—", "No economy seats remain on the selected flight.", "Search for another flight or cabin."),
    ("30002", "Change request is too late", "F-Link", "—", "Departure is less than four hours away.", "Submit changes earlier, or contact support for manual handling."),
    ("MCP001", "MCP connection timed out", "—", "MCP", "Network is unstable, or the server is busy.", "Check the network, raise the timeout to 30 seconds and add retry handling."),
    ("MCP002", "MCP authentication failed", "—", "MCP", "Token has expired or has an invalid format.", "Get a new token and pass it in the Authorization header as a Bearer token."),
    ("SDK001", "SDK initialisation failed", "—", "SDK", "AppKey or AppSecret is empty or malformed.", "Check the initialisation parameters and confirm both values are supplied."),
    ("SDK002", "SDK version is incompatible", "—", "SDK", "The SDK version is too old for this capability.", "Upgrade to the latest SDK and review the changelog."),
]


def error_rows():
    return [
        (
            f'<td class="t-code">{c}</td>',
            f"<td>{msg}</td>",
            f'<td class="t-mid t-dim">{prod}</td>',
            f'<td class="t-mid t-dim">{integ}</td>',
            f'<td class="t-dim">{reason}</td>',
            f"<td>{fix}</td>",
        )
        for c, msg, prod, integ, reason, fix in ERRORS
    ]


API_DOCS_ERRORS = f"""
{band(
    "All products, all integration methods",
    "Error Code Reference",
    "<b>Every error code the platform returns</b>, what causes it and what to do about it. Codes are stable "
    "across products; the product and integration columns say where each one can appear.",
    crumb=[("Docs centre", "api-docs-hotel.html"), ("Error code reference", None)],
    foot=rail(DOCS_RAIL, "Error codes"),
)}

<div class="wrap">
<div class="docs">
{docs_side("Error code reference")}
  <div class="docs-main">
    <h2>Twelve codes, <em>four families.</em></h2>
    <p>Platform errors in the <code class="inl">1xxxx</code> range apply everywhere. Product errors are
       scoped to G-Link or F-Link. <code class="inl">MCP</code> and <code class="inl">SDK</code> prefixes
       are integration-layer failures and never reach the travel supplier.</p>

    {tbl(["Code", "Message", "Product", "Integration", "Reason", "Resolution"], error_rows(), 1020)}

    <div class="note">
      <iconify-icon icon="solar:info-circle-linear"></iconify-icon>
      <span><strong>HTTP 200 is not success.</strong> Read the <code class="inl">code</code> field in the response
      body. A supplier business failure returns HTTP 200 with
      <code class="inl">code=SUPPLIER_BIZ_ERROR</code>, and the codes above appear the same way.</span>
    </div>

    <h3>What to log</h3>
    <ul class="bul">
      <li><iconify-icon icon="solar:document-text-linear"></iconify-icon><span>Keep <code class="inl">request_id</code>
        and <code class="inl">trace_id</code> against every call. Support cannot trace a failure without them.</span></li>
      <li><iconify-icon icon="solar:link-linear"></iconify-icon><span>Keep
        <code class="inl">downstream_request_id</code> where it is returned — it identifies the call at the supplier,
        not at the platform.</span></li>
      <li><iconify-icon icon="solar:clock-circle-linear"></iconify-icon><span>Record the request timestamp in UTC.
        Rate-limit disputes are settled on the platform's clock.</span></li>
    </ul>

    <div class="band-foot">
      <a class="btn" href="ai-assistant.html">Ask the AI Assistant {ARROW}</a>
      <a class="tlink tlink--o" href="index.html#start-integration">Submit a ticket {ARROW}</a>
    </div>
  </div>
</div>
</div>
"""

# ============================================================ SDK

SDKS = [
    ("TMC API", "Java", "TMC Java SDK", "v1.0.0", "30 July 2026",
     "mvn install:install-file -Dfile=tmc-sdk-java-1.0.0.jar -DgroupId=com.platform.tmc -DartifactId=tmc-sdk-java -Dversion=1.0.0 -Dpackaging=jar"),
    ("TMC API", "Python", "TMC Python SDK", "v1.0.0", "30 July 2026",
     "pip install tmc_sdk_python-1.0.0-py3-none-any.whl"),
    ("TMC API", "Go", "Open Platform Go SDK", "v1.0.0", "30 July 2026",
     "go get open-platform/sdk/tmc"),
    ("G-Link Hotel", "Python", "G-Link Hotel Python SDK", "v2.5.3", "13 July 2026",
     "pip install glink-sdk-python"),
]


def sdk_cards():
    out = []
    for prod, lang, name, ver, date, cmd in SDKS:
        out.append(
            f"""  <article class="card rv">
    <div class="card-h">
      <p class="card-k"><span class="dot" aria-hidden="true"></span>{prod} · {lang}</p>
      <h3>{name}</h3>
      <p>Published release. Confirm runtime versions from the release notes before installing.</p>
    </div>
    <div class="card-meta">
      <div><span class="k">Version</span><span class="v">{ver}</span></div>
      <div><span class="k">Released</span><span class="v">{date}</span></div>
      <div><span class="k">Status</span><span class="v">Published</span></div>
    </div>
    <div class="ep-b" style="border-top:1px solid var(--hair);padding:20px 24px">
      <h4>Install</h4>
      <div class="cmd" style="margin-top:12px">
        <code>{cmd}</code>
        <button type="button">Copy</button>
      </div>
    </div>
    <div class="card-f">
      <a class="btn btn--sm" href="api-docs-hotel.html">View docs {ARROW}</a>
      <a class="tlink" href="login.html">Download {DL}</a>
    </div>
  </article>"""
        )
    return "\n".join(out)


SDK = f"""
{band(
    "Auth, retry and serialisation built in",
    "SDK Integration Centre",
    "<b>Multilingual SDKs</b> with install commands, example code, changelogs and security verification. "
    "Go, Java and Python are published today; Node.js is in progress.",
    foot=f'<a class="btn" href="register.html">Get sandbox credentials {ARROW}</a>'
         f'<a class="btn btn--ghost" href="skills.html">Skills packages {ARROW}</a>',
)}

<section class="blk blk--top">
  <div class="wrap">
    <div class="mini rv">
      <div><p class="n">8</p><p class="c">Published SDK releases</p></div>
      <div><p class="n">3</p><p class="c">Languages · Go · Java · Python</p></div>
      <div><p class="n">100<u>%</u></p><p class="c">Core integration coverage</p></div>
    </div>
  </div>
</section>

<section class="blk" style="padding-top:24px">
  <div class="wrap">
    <div class="blk-head">
      <p class="eyebrow micro">Available now</p>
      <h2 class="h3">Install, configure the key pair, <em>call the API.</em></h2>
      <p class="lede">Every SDK ships with the same three things: a quick start, a changelog and a signature
         verification helper. Download the package, install it, then configure AppKey and AppSecret on your server —
         never in a client.</p>
    </div>
    <div class="cards cards--2">
{sdk_cards()}
    </div>

    <div class="note rv" style="margin-top:24px">
      <iconify-icon icon="solar:info-circle-linear"></iconify-icon>
      <span><strong>Node.js is in progress.</strong> Until it publishes, call the REST endpoints directly —
      the <a href="api-docs-hotel-apis.html" style="color:var(--ink);font-weight:500">API reference</a>
      carries the full request and response shape.</span>
    </div>
  </div>
</section>

<hr class="rule">

<section class="blk">
  <div class="wrap">
    <div class="blk-head">
      <p class="eyebrow micro">Integration options</p>
      <h2 class="h3">Three ways in.</h2>
    </div>
    <div class="iopts">
      <article class="icard rv">
        <div class="icard-ic"><iconify-icon icon="solar:cpu-bolt-linear"></iconify-icon></div>
        <h3>MCP smart integration</h3>
        <span class="k">Model Context Protocol</span>
        <p>Lets an AI model call travel capabilities directly. Built for LLM applications and assistants.</p>
        <div class="icard-foot"><a class="tlink tlink--o" href="skills.html">Skills packages {ARROW}</a></div>
      </article>
      <article class="icard rv">
        <div class="icard-ic"><iconify-icon icon="solar:code-square-linear"></iconify-icon></div>
        <h3>Fast SDK integration</h3>
        <span class="k">Go · Java · Python</span>
        <p>Authentication, retry and serialisation handled for you. Node.js is in progress.</p>
        <div class="icard-foot"><div class="langs">
          <span class="chip">Go</span><span class="chip">Java</span><span class="chip">Python</span>
          <span class="chip soon">Node.js</span>
        </div></div>
      </article>
      <article class="icard rv">
        <div class="icard-ic"><iconify-icon icon="solar:global-linear"></iconify-icon></div>
        <h3>REST API</h3>
        <span class="k">Any language</span>
        <p>Standard APIs callable from any language or framework. No SDK required.</p>
        <div class="icard-foot"><a class="tlink tlink--o" href="api-docs-hotel-apis.html">API reference {ARROW}</a></div>
      </article>
    </div>
  </div>
</section>
"""

# ============================================================ Skills

SKILL_PKGS = [
    ("G-Link", "G-Link Hotel API Skills", "v2.0.0", "5 April 2026",
     "Full hotel integration flow: auth, search, booking, payment, order management, webhooks "
     "and troubleshooting.",
     "npx @mongoui/skills install glink-hotel-api --tool codex"),
    ("F-Link", "F-Link Flight API Skills", "v2.0.0", "5 April 2026",
     "Full flight integration flow: auth, search, booking, ticketing, change and refund, "
     "webhooks and troubleshooting.",
     "npx @mongoui/skills install flink-flight-api --tool codex"),
    ("TMC", "TMC API Skills", "v1.0.0", "30 July 2026",
     "Full TMC integration flow: auth, flight and hotel booking, approvals, policy standards, "
     "organisation hierarchy, webhooks and troubleshooting.",
     "npx @mongoui/skills install tmc-api --tool codex"),
]

TOOLS = ["Codex", "Cursor", "Claude Code", "Kiro", "Gemini CLI"]


def skill_cards():
    out = []
    for code, name, ver, date, what, cmd in SKILL_PKGS:
        chips = (
            '<span class="chip chip--live"><span class="dot" aria-hidden="true"></span>Sandbox ready</span>'
            '<span class="chip chip--live"><span class="dot" aria-hidden="true"></span>Production ready</span>'
            + "".join(f'<span class="chip chip--plain">{t}</span>' for t in TOOLS)
        )
        out.append(
            f"""  <article class="card rv">
    <div class="card-h">
      <p class="card-k"><span class="dot" aria-hidden="true"></span>{code}</p>
      <h3>{name}</h3>
      <p>{what}</p>
      <div class="chips" style="margin-top:18px">{chips}</div>
    </div>
    <div class="card-meta">
      <div><span class="k">Version</span><span class="v">{ver}</span></div>
      <div><span class="k">Updated</span><span class="v">{date}</span></div>
    </div>
    <div class="ep-b" style="border-top:1px solid var(--hair);padding:20px 24px">
      <h4>Remote install</h4>
      <div class="cmd" style="margin-top:12px">
        <code>{cmd}</code>
        <button type="button">Copy</button>
      </div>
    </div>
    <div class="card-f">
      <a class="btn btn--sm" href="api-docs-hotel.html">View details {ARROW}</a>
      <a class="tlink" href="login.html">Download SKILL.md {DL}</a>
    </div>
  </article>"""
        )
    return "\n".join(out)


SKILLS = f"""
{band(
    "One official package per API",
    "Skills Installation Centre",
    "<b>Integration skill packages for AI coding assistants.</b> Import one into Claude, Codex, Cursor, Kiro or "
    "Gemini CLI and the assistant writes more accurate authentication code, debugs API calls and diagnoses "
    "failures against the real interface.",
    chip="New",
    foot=f'<a class="btn" href="#packages">Browse packages {ARROW}</a>'
         f'<a class="tlink tlink--o" href="sdk.html">SDK downloads {ARROW}</a>',
)}

<section class="blk blk--top">
  <div class="wrap">
    <div class="mini rv">
      <div><p class="n">3</p><p class="c">Official Skills packages</p></div>
      <div><p class="n">100<u>%</u></p><p class="c">Core integration coverage</p></div>
      <div><p class="n">5</p><p class="c">AI assistant categories</p></div>
    </div>
  </div>
</section>

<section class="blk" style="padding-top:24px" id="packages">
  <div class="wrap">
    <div class="blk-head">
      <p class="eyebrow micro">Packages</p>
      <h2 class="h3">Install by command, <em>or download the file.</em></h2>
      <p class="lede">Each package installs remotely with one command, or downloads as a single
         <code class="inl">SKILL.md</code> you drop into the assistant yourself. Both routes carry the same content.</p>
    </div>
    <div class="cards cards--tall">
{skill_cards()}
    </div>
  </div>
</section>

<hr class="rule">

<section class="blk">
  <div class="wrap">
    <div class="skills">
      <div>
        <p class="eyebrow micro">How to install</p>
        <h2 class="h3" style="margin-top:22px">Two routes, <em>one outcome.</em></h2>
        <p class="lede" style="margin-top:22px">Remote install is the shorter path and stays current.
           The downloadable file suits an assistant with no network access, or a repository that should
           carry its own copy.</p>
        <ul class="tick">
          <li><iconify-icon icon="solar:command-linear"></iconify-icon>
            <span>Run the install command with <code class="inl">--tool</code> set to your assistant.</span></li>
          <li><iconify-icon icon="solar:file-download-linear"></iconify-icon>
            <span>Or download <code class="inl">SKILL.md</code> and place it where your assistant reads skills.</span></li>
          <li><iconify-icon icon="solar:refresh-linear"></iconify-icon>
            <span>Packages are updated continuously — reinstall to pick up interface changes.</span></li>
          <li><iconify-icon icon="solar:key-minimalistic-linear"></iconify-icon>
            <span>Prompt templates are included. Credentials are not; configure those yourself.</span></li>
        </ul>
      </div>
      <div class="tree">
        <div class="tree-h">
          <span class="dot" aria-hidden="true"></span>
          <span>SKILL.md structure</span>
        </div>
        <pre>glink-hotel-api/
├── SKILL.md          <span class="d"># entry point</span>
├── auth/
│   ├── signature.md  <span class="d"># signing algorithm</span>
│   └── keys.md       <span class="d"># AppKey / AppSecret</span>
├── flows/
│   ├── search.md
│   ├── booking.md
│   ├── payment.md
│   └── orders.md
├── webhooks/
│   └── orderStatus.md
└── troubleshooting/
    └── error-codes.md</pre>
      </div>
    </div>
  </div>
</section>
"""

# ============================================================ AI Assistant

ASKS = [
    "How do I generate a request signature?",
    "Why does availabilityCheck return not bookable?",
    "What is the production rate limit?",
    "How should I handle a duplicate orderStatus push?",
    "Which SDK covers the TMC API?",
    "What does SUPPLIER_BIZ_ERROR mean?",
]

AI_ASSISTANT = f"""
{band(
    "Technical support · Integration consulting",
    "AI Assistant",
    "<b>Running into an integration issue?</b> Ask directly and get an answer with code examples in seconds, "
    "grounded in the platform's own API documentation.",
    chip="Online",
    foot=f'<a class="btn" href="#ask">Start a conversation {ARROW}</a>'
         f'<a class="tlink tlink--o" href="api-docs-errors.html">Error code reference {ARROW}</a>',
)}

<section class="blk blk--top" id="ask">
  <div class="wrap">
    <div class="chat">
      <div class="chatbox rv">
        <div class="chat-h">
          <span class="av"><iconify-icon icon="solar:chat-square-code-linear"></iconify-icon></span>
          <span>
            <strong>FCG Developer Platform AI Assistant</strong>
            <span>Technical support · Integration consulting</span>
          </span>
          <span class="dot" aria-hidden="true" title="Online"></span>
        </div>
        <div class="chat-b">
          <div class="msg msg--ai">
            <p>Hello. I am the FCG Developer Platform AI Assistant. I can help with API integration,
               signature authentication, order workflows and more.</p>
            <p>Type a question, or pick one of the common questions to start.</p>
          </div>
          <div class="msg msg--me">
            <p>How do I generate a request signature?</p>
          </div>
          <div class="msg msg--ai">
            <p>Sign with your AppSecret using the algorithm in the signing guide, then send the signature
               with the request. If verification fails you will get
               <code class="inl">10001 Signature verification failed</code> — the usual cause is a wrong
               AppSecret or a mismatched algorithm.</p>
            <p>Keep the AppSecret on your server. Never ship it to a client.</p>
          </div>
        </div>
        <div class="chat-in">
          <label for="ask-in" class="micro" style="position:absolute;left:-9999px">Your question</label>
          <input id="ask-in" type="text" placeholder="Ask about authentication, booking flow, error codes…">
          <button class="btn btn--sm" type="button">Send {ARROW}</button>
        </div>
        <p class="chat-f">AI responses are for reference only. For professional support,
          <a href="index.html#start-integration">submit a ticket</a> and contact the technical team.</p>
      </div>

      <div class="asks rv" role="group" aria-labelledby="asks-h">
        <p class="asks-h" id="asks-h">Common questions</p>
{chr(10).join(f'        <button type="button"><iconify-icon icon="solar:arrow-right-up-linear"></iconify-icon><span>{q}</span></button>' for q in ASKS)}
      </div>
    </div>
  </div>
</section>

<hr class="rule">

<section class="blk">
  <div class="wrap">
    <div class="blk-head sec-head--c" style="align-items:center;text-align:center">
      <p class="eyebrow eyebrow--c micro">If the assistant cannot resolve it</p>
      <h2 class="h3" style="max-width:26ch">Three routes to a human.</h2>
    </div>
    <div class="iopts">
      <article class="icard rv">
        <div class="icard-ic"><iconify-icon icon="solar:ticket-linear"></iconify-icon></div>
        <h3>Submit a ticket</h3>
        <span class="k">Technical support</span>
        <p>Include the <code class="inl">request_id</code> and <code class="inl">trace_id</code> from the failing
           call. Support cannot trace a failure without them.</p>
        <div class="icard-foot"><a class="tlink tlink--o" href="login.html">Open the console {ARROW}</a></div>
      </article>
      <article class="icard rv">
        <div class="icard-ic"><iconify-icon icon="solar:document-text-linear"></iconify-icon></div>
        <h3>Read the docs</h3>
        <span class="k">Docs centre</span>
        <p>Interface lists, request and response shapes, worked examples and the full error code table.</p>
        <div class="icard-foot"><a class="tlink tlink--o" href="api-docs-hotel.html">Docs centre {ARROW}</a></div>
      </article>
      <article class="icard rv">
        <div class="icard-ic"><iconify-icon icon="solar:users-group-rounded-linear"></iconify-icon></div>
        <h3>Business consultation</h3>
        <span class="k">Commercial</span>
        <p>Custom solutions, dedicated pricing and TMC API deployment go to the business team, not to support.</p>
        <div class="icard-foot"><a class="tlink tlink--o" href="index.html#start-integration">Book a demo {ARROW}</a></div>
      </article>
    </div>
  </div>
</section>
"""

# ============================================================ login

LOGIN = f"""
<section class="auth">
  <div class="auth-aside">
    <div class="band-grid" aria-hidden="true"></div>
    <div class="wrap" style="position:relative;z-index:1">
      <p class="eyebrow micro">Developer console</p>
      <p class="ahead">Travel API integration in one place.</p>
      <p class="lede">Built for distributors and travel management companies, with full hotel and flight API
         coverage and support for both SDK and REST integration.</p>
      <div class="mini mini--aside" style="margin-top:48px">
        <div><p class="n">200<u>+</u></p><p class="c">Partners</p></div>
        <div><p class="n">99.9<u>%</u></p><p class="c">Uptime</p></div>
        <div><p class="n">7<u>×24</u></p><p class="c">Technical support</p></div>
      </div>
    </div>
  </div>

  <div class="auth-main">
    <div class="auth-card rv">
      <h1>Welcome back</h1>
      <p>Sign in to access your developer console.</p>

      <button class="oauth" type="button">
        <iconify-icon icon="solar:login-3-linear" aria-hidden="true"></iconify-icon>
        Continue with Google
      </button>

      <p class="orline">Or use your account</p>

      <form class="fields" action="#" method="post" novalidate>
        <div class="fld">
          <label for="acct">Account</label>
          <input id="acct" name="account" type="text" autocomplete="username" placeholder="Username or email">
        </div>
        <div class="fld">
          <label for="pw">Password</label>
          <input id="pw" name="password" type="password" autocomplete="current-password" placeholder="••••••••">
        </div>
        <div class="fld-row">
          <span></span>
          <a href="#reset">Forgotten your password?</a>
        </div>
        <button class="btn auth-submit" type="submit">Sign in {ARROW}</button>
      </form>

      <p class="auth-alt">No account yet? <a href="register.html">Register for free</a></p>
    </div>
  </div>
</section>
"""

# ============================================================ register

REGISTER = f"""
<section class="auth">
  <div class="auth-aside">
    <div class="band-grid" aria-hidden="true"></div>
    <div class="wrap" style="position:relative;z-index:1">
      <p class="eyebrow micro">Free access</p>
      <p class="ahead">Register once, <em>test everything.</em></p>
      <p class="lede">Set up a company account and complete the onboarding details to reach the platform console.
         The sandbox opens immediately and costs nothing upfront.</p>
      <ul class="tick" style="margin-top:38px;max-width:40ch">
        <li><iconify-icon icon="solar:check-circle-linear"></iconify-icon><span>Instant sandbox access</span></li>
        <li><iconify-icon icon="solar:check-circle-linear"></iconify-icon><span>Full API documentation access</span></li>
        <li><iconify-icon icon="solar:check-circle-linear"></iconify-icon><span>Technical ticket support</span></li>
        <li><iconify-icon icon="solar:check-circle-linear"></iconify-icon><span>TMC API application eligibility</span></li>
      </ul>
    </div>
  </div>

  <div class="auth-main">
    <div class="auth-card rv">
      <h1>Create your account</h1>
      <p>Set up your company account and complete the onboarding details to access the platform console.</p>

      <button class="oauth" type="button">
        <iconify-icon icon="solar:login-3-linear" aria-hidden="true"></iconify-icon>
        Sign up with Google
      </button>

      <p class="orline">Or register with your details</p>

      <form class="fields" action="#" method="post" novalidate>
        <div class="fields--2">
          <div class="fld">
            <label for="user">Username <em aria-hidden="true">*</em></label>
            <input id="user" name="username" type="text" autocomplete="username" required>
          </div>
          <div class="fld">
            <label for="pw2">Password <em aria-hidden="true">*</em></label>
            <input id="pw2" name="password" type="password" autocomplete="new-password" required>
          </div>
        </div>
        <div class="fld">
          <label for="co">Company name <em aria-hidden="true">*</em></label>
          <input id="co" name="company" type="text" autocomplete="organization" required>
        </div>
        <div class="fields--2">
          <div class="fld">
            <label for="who">Contact person <em aria-hidden="true">*</em></label>
            <input id="who" name="contact" type="text" autocomplete="name" required>
          </div>
          <div class="fld">
            <label for="tel">Phone number <em aria-hidden="true">*</em></label>
            <input id="tel" name="phone" type="tel" autocomplete="tel" required>
          </div>
        </div>
        <div class="fld">
          <label for="mail">Email <em aria-hidden="true">*</em></label>
          <input id="mail" name="email" type="email" autocomplete="email" required>
        </div>
        <div class="fld">
          <label for="cur">Settlement currency <em aria-hidden="true">*</em></label>
          <select id="cur" name="currency" required>
            <option value="CNY">CNY — Chinese Yuan</option>
            <option value="USD">USD — US Dollar</option>
          </select>
        </div>
        <button class="btn auth-submit" type="submit">Create account {ARROW}</button>
      </form>

      <p class="auth-legal">The TMC API sandbox supports USD only. Settlement currency can be changed later
        from the console.</p>
      <p class="auth-alt">Already registered? <a href="login.html">Sign in</a></p>
    </div>
  </div>
</section>
"""

# ============================================================ registry

# Copy-to-clipboard, added only to the two pages that show install commands.
COPY = """<script>
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

PAGES = [
    dict(slug="app-management", nav="apps",
         title="App Management — FCG Developer Platform",
         desc="Manage the applications behind an FCG API integration. Each product carries its own credential set.",
         body=APP_MANAGEMENT),
    dict(slug="api-docs-hotel", nav="docs",
         title="G-Link Hotel API — FCG Developer Platform",
         desc="Mandatory interfaces, static data handling and rate limits for the G-Link hotel API.",
         body=API_DOCS_HOTEL),
    dict(slug="api-docs-hotel-process", nav="docs",
         title="G-Link Integration Flow — FCG Developer Platform",
         desc="The recommended eight-step G-Link hotel API integration flow, search through to cancellation.",
         body=API_DOCS_HOTEL_PROCESS),
    dict(slug="api-docs-hotel-apis", nav="docs",
         title="G-Link API Reference — FCG Developer Platform",
         desc="Every G-Link hotel endpoint with methods, paths and a worked request and response example.",
         body=API_DOCS_HOTEL_APIS),
    dict(slug="api-docs-flink", nav="docs",
         title="F-Link Flight API — FCG Developer Platform",
         desc="All nineteen F-Link flight endpoints: search, ticketing, changes, refunds and reference data.",
         body=API_DOCS_FLINK),
    dict(slug="api-docs-errors", nav="docs",
         title="Error Code Reference — FCG Developer Platform",
         desc="Every FCG platform error code, its cause and its resolution, across API, SDK and MCP integration.",
         body=API_DOCS_ERRORS),
    dict(slug="sdk", nav="sdk",
         title="SDK Integration Centre — FCG Developer Platform",
         desc="Go, Java and Python SDKs for the FCG travel APIs, with install commands and changelogs.",
         body=SDK, extra=COPY),
    dict(slug="skills", nav="skills",
         title="Skills Installation Centre — FCG Developer Platform",
         desc="Official integration skill packages for AI coding assistants, one per FCG travel API.",
         body=SKILLS, extra=COPY),
    dict(slug="ai-assistant", nav="ai",
         title="AI Assistant — FCG Developer Platform",
         desc="Ask the FCG Developer Platform AI Assistant about API integration, authentication and order workflows.",
         body=AI_ASSISTANT),
    dict(slug="login", nav="", minimal=True,
         title="Sign in — FCG Developer Platform",
         desc="Sign in to the FCG Developer Platform console.",
         body=LOGIN),
    dict(slug="register", nav="", minimal=True,
         title="Register — FCG Developer Platform",
         desc="Register a company account for free sandbox access to the FCG Developer Platform.",
         body=REGISTER),
]
