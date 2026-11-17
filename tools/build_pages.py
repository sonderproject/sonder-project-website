#!/usr/bin/env python3
"""Build the static subpages of sonderproject.co (one per Sonder business + about + 404).

Edit the PAGES content below, then run:  python3 tools/build_pages.py
Writes public/<slug>.html. The homepage (public/index.html) is hand-edited, not generated.
"""
import html, json, os

SITE = "https://www.sonderproject.co"
OUT = os.path.join(os.path.dirname(__file__), "..", "public")
CAL = "https://cal.com/dante-valentino/ai-consulting"
SURFDESK = "https://thesurfdesk.app"
STUDIO = "https://sonderstudio.space"
PROTOCOL = "https://sonderprotocol.vercel.app"
ORG_ID = SITE + "/#organization"

NAV = [("/surfdesk", "Surfdesk"), ("/web-design", "Websites"), ("/ai-consulting", "AI"),
       ("/guides", "Guides"), ("/about", "About")]

CSS = """
@font-face{font-family:'Inter';font-style:normal;font-weight:300 700;font-display:swap;src:url(/fonts/inter-latin.woff2) format('woff2')}
@font-face{font-family:'Outfit';font-style:normal;font-weight:300 700;font-display:swap;src:url(/fonts/outfit-latin.woff2) format('woff2')}
:root{--bg:#0A0A09;--accent:#3E9BD4;--accent-rgb:62,155,212;--text:#EDE9E3;--dim:rgba(237,233,227,.66);--line:rgba(255,255,255,.10);
--glass:linear-gradient(135deg,rgba(255,255,255,.10) 0%,rgba(255,255,255,.03) 100%),rgba(18,20,24,.6);--ff-d:'Outfit',sans-serif;--ff-s:'Inter',sans-serif}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--text);font-family:var(--ff-s);font-weight:300;line-height:1.7;-webkit-font-smoothing:antialiased;
background-image:radial-gradient(ellipse 80% 50% at 15% 0%,rgba(var(--accent-rgb),.13),transparent 60%),radial-gradient(ellipse 60% 40% at 100% 30%,rgba(120,110,255,.06),transparent 60%);background-repeat:no-repeat}
a{color:var(--accent)}
.wrap{max-width:1100px;margin:0 auto;padding:0 56px}
header.top{position:sticky;top:0;z-index:20;background:rgba(10,10,9,.78);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);border-bottom:1px solid var(--line)}
header.top .wrap{display:flex;align-items:center;justify-content:space-between;height:68px;gap:20px}
.logo{display:flex;align-items:center;gap:12px;color:var(--text);text-decoration:none;font-family:var(--ff-s);font-size:12px;font-weight:600;letter-spacing:.14em;text-transform:uppercase}
.logo img{height:22px;width:auto}
.links{display:flex;align-items:center;gap:28px}
.links a{color:rgba(237,233,227,.75);text-decoration:none;font-size:11px;letter-spacing:.12em;text-transform:uppercase}
.links a:hover,.links a[aria-current]{color:var(--text)}
.pill{background:linear-gradient(180deg,#6fc3f0,var(--accent));color:#04121c!important;font-weight:600;padding:9px 18px;border-radius:6px}
.crumbs{font-size:12px;color:var(--dim);padding:28px 0 0}
.crumbs a{color:var(--dim);text-decoration:none}.crumbs a:hover{color:var(--text)}
.hero{padding:56px 0 64px}
.eyebrow{font-size:11px;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--accent);margin-bottom:22px}
h1{font-family:var(--ff-d);font-weight:600;font-size:clamp(36px,5.2vw,68px);line-height:1.03;letter-spacing:-.03em;max-width:900px;margin-bottom:24px}
h1 em,h2 em{font-style:normal;color:var(--accent)}
.lede{font-size:clamp(16px,1.5vw,19px);color:var(--dim);max-width:640px;margin-bottom:34px}
.ctas{display:flex;flex-wrap:wrap;gap:14px;align-items:center}
.btn{display:inline-block;font-size:12px;font-weight:600;letter-spacing:.13em;text-transform:uppercase;text-decoration:none;padding:15px 30px;border-radius:999px;transition:transform .2s ease}
.btn:hover{transform:translateY(-1px)}
.btn-p{background:linear-gradient(180deg,#6fc3f0,var(--accent));color:#04121c;box-shadow:0 8px 28px rgba(var(--accent-rgb),.3)}
.btn-g{border:1px solid rgba(255,255,255,.22);color:var(--text);background:rgba(255,255,255,.04)}
.micro{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:rgba(237,233,227,.5);margin-top:14px}
.figure{margin:8px 0 72px;border-radius:16px;overflow:hidden;border:1px solid var(--line)}
.figure img{display:block;width:100%;height:auto}
section.block{padding:64px 0;border-top:1px solid var(--line)}
h2{font-family:var(--ff-d);font-weight:600;font-size:clamp(26px,3.2vw,42px);line-height:1.1;letter-spacing:-.02em;margin-bottom:18px;max-width:820px}
h3{font-family:var(--ff-d);font-weight:600;font-size:20px;letter-spacing:-.01em;margin-bottom:8px;color:var(--text)}
.block p.intro{color:var(--dim);max-width:680px;margin-bottom:36px}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.grid.two{grid-template-columns:repeat(2,1fr)}.grid.four{grid-template-columns:repeat(4,1fr)}
.card{padding:30px 28px;border-radius:14px;border:1px solid rgba(255,255,255,.13);background:var(--glass)}
.card p{color:var(--dim);font-size:15px}
.card .num{font-family:var(--ff-d);color:var(--accent);font-size:13px;letter-spacing:.14em;margin-bottom:14px}
.card .price{font-family:var(--ff-d);font-size:38px;font-weight:600;letter-spacing:-.02em;color:var(--text);line-height:1.1;margin:6px 0 10px}
.card .price span{font-family:var(--ff-s);font-size:13px;font-weight:300;color:var(--dim)}
.card.feat{border-color:rgba(var(--accent-rgb),.5)}
.note{font-size:12px;color:var(--accent);margin-top:10px}
ul.check{list-style:none;display:grid;gap:10px;max-width:760px}
ul.check li{position:relative;padding-left:26px;color:var(--dim)}
ul.check li::before{content:'\\2713';position:absolute;left:0;color:var(--accent);font-weight:600}
.faq{display:grid;gap:12px;max-width:860px}
.faq details{border:1px solid rgba(255,255,255,.13);border-radius:12px;background:var(--glass);padding:20px 24px}
.faq summary{cursor:pointer;font-family:var(--ff-d);font-weight:600;font-size:18px;color:var(--text);list-style:none}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:'+';float:right;color:var(--accent)}
.faq details[open] summary::after{content:'\\2013'}
.faq p{color:var(--dim);margin-top:12px}
.closer{padding:90px 0;text-align:center;border-top:1px solid var(--line)}
.closer h2{margin:0 auto 16px}.closer p{color:var(--dim);max-width:560px;margin:0 auto 30px}.closer .ctas{justify-content:center}
.family{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.family a{display:block;padding:20px;border:1px solid var(--line);border-radius:12px;text-decoration:none;color:var(--text);transition:border-color .2s}
.family a:hover{border-color:rgba(var(--accent-rgb),.5)}
.family small{display:block;color:var(--dim);font-size:12px;margin-top:4px}
footer{border-top:1px solid var(--line);padding:36px 0 48px;font-size:13px;color:rgba(237,233,227,.55)}
footer .wrap{display:flex;flex-wrap:wrap;gap:16px 28px;justify-content:space-between}
footer nav{display:flex;flex-wrap:wrap;gap:10px 22px}
footer a{color:rgba(237,233,227,.7);text-decoration:none}footer a:hover{color:var(--text)}
.orange{--accent:#ff7a33;--accent-rgb:255,122,51}
@media(max-width:900px){.wrap{padding:0 22px}.links a:not(.pill){display:none}.grid,.grid.two,.grid.four,.family{grid-template-columns:1fr}.hero{padding:36px 0 48px}}
"""


def esc(s):
    return html.escape(s, quote=True)


def faq_html(faqs):
    return '<div class="faq">' + "".join(
        f"<details><summary>{esc(q)}</summary><p>{a}</p></details>" for q, a in faqs) + "</div>"


def strip_tags(s):
    import re
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def page(slug, title, desc, body, schema, crumb, og_image="/og-image.jpg", theme=""):
    url = f"{SITE}/{slug}" if slug else SITE + "/"
    graph = [
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": title, "description": desc,
         "isPartOf": {"@id": SITE + "/#website"}, "publisher": {"@id": ORG_ID}, "inLanguage": "en-US"},
    ]
    if crumb:
        graph.append({"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Sonder Project", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": crumb, "item": url}]})
    graph += schema
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    nav = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == "/" + slug else ""}>{t}</a>' for h, t in NAV)
    crumbs = (f'<div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="/">Sonder Project</a> / <span>{esc(crumb)}</span></nav></div>'
              if crumb else "")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="{'noindex' if slug == '404' else 'index, follow, max-image-preview:large'}">
<meta name="theme-color" content="#0A0A09">
{'' if slug == '404' else f'<link rel="canonical" href="{url}">'}
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="48x48" href="/favicon-48.png">
<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicon-192.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Sonder Project">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}{og_image}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{SITE}{og_image}">
<link rel="preload" href="/fonts/outfit-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<script type="application/ld+json">
{ld}
</script>
<style>{CSS}</style>
</head>
<body class="{theme}">
<header class="top"><div class="wrap">
  <a href="/" class="logo"><img src="/logo-white.png" alt="" width="40" height="22">Sonder Project</a>
  <nav class="links" aria-label="Main">{nav}<a href="{SURFDESK}" class="pill" rel="noopener">Try Surfdesk</a></nav>
</div></header>
{crumbs}
<main>
{body}
<section class="block"><div class="wrap">
  <h2>The Sonder family</h2>
  <p class="intro">Every brand here is designed, built and run by Sonder Project.</p>
  <div class="family">
    <a href="/surfdesk">Surfdesk<small>Client tracker app</small></a>
    <a href="/web-design">Sonder Studio<small>Websites &amp; design</small></a>
    <a href="/ai-consulting">Sonder Consulting<small>AI &amp; automation</small></a>
    <a href="/sonder-protocol">Sonder Protocol<small>Preparedness guides</small></a>
  </div>
</div></section>
</main>
<footer><div class="wrap">
  <div>&copy; 2026 Sonder Project &middot; San Diego, California</div>
  <nav aria-label="Footer"><a href="/">Home</a><a href="/surfdesk">Surfdesk</a><a href="/web-design">Web design</a><a href="/ai-consulting">AI consulting</a><a href="/sonder-protocol">Sonder Protocol</a><a href="/guides">Guides</a><a href="/about">About</a><a href="{CAL}" rel="noopener">Book a call</a></nav>
</div></footer>
</body>
</html>
"""


def faq_schema(url, faqs):
    return {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
        for q, a in faqs]}


SAN_DIEGO = {"@type": "City", "name": "San Diego", "containedInPlace": {"@type": "State", "name": "California"}}
US = {"@type": "Country", "name": "United States"}

# ─────────────────────────────── SURFDESK ───────────────────────────────
sd_faqs = [
    ("What is Surfdesk?", "Surfdesk is a client tracker that keeps follow-ups from slipping. Say it once — &ldquo;Marcus got the job, call him Friday&rdquo; — and it saves the note, sets the reminder and counts the outcome. Every client, follow-up and visit lives in one place, on any phone."),
    ("Who is Surfdesk for?", "Nonprofits, social-service agencies and case-management teams use it as a shared caseload with outcome tracking and funder-ready Impact reports. Small businesses, freelancers and solo professionals use it to keep every client, service and follow-up in one place."),
    ("How much does Surfdesk cost?", "Individual is $9 a month with a 7-day free trial and no card needed. Small Team is $19 per user per month for 2–18 people. Organization is $349 a month for 19 or more, with 20 seats included and extra seats at $15. Enterprise pricing is custom. Team plans include a 14-day free trial."),
    ("Can Surfdesk build funder reports?", "Yes. Surfdesk counts people served and outcomes reached as your team works, and turns them into a polished Impact report PDF in one click — no end-of-month spreadsheet scramble."),
    ("Does Surfdesk work on my phone?", "Yes. Surfdesk runs in any modern browser on iPhone, Android and desktop, and you can add it to your home screen like an app."),
    ("Is there a discount for skipping the trial?", "Yes. If you'd rather start right away, you get 30% off your first month."),
]
sd_body = f"""
<section class="hero"><div class="wrap">
  <div class="eyebrow">01 &middot; Surfdesk by Sonder Project</div>
  <h1>The client tracker where <em>nothing falls through the cracks.</em></h1>
  <p class="lede">Say it once and Surfdesk saves the note, sets the reminder and counts the outcome. Clients, follow-ups, case notes and reports in one place, on any phone. Built for nonprofits, agencies, small businesses and solo pros.</p>
  <div class="ctas"><a class="btn btn-p" href="{SURFDESK}" rel="noopener">Start your free trial</a><a class="btn btn-g" href="#pricing">See pricing</a></div>
  <p class="micro">7-day free trial &middot; no card needed</p>
</div></section>
<div class="wrap"><div class="figure"><img src="/surfdesk.webp" alt="Surfdesk client tracker on three phones: the People list, today's follow-ups, and the Impact report with outcomes" width="1672" height="941"></div></div>

<section class="block"><div class="wrap">
  <h2>Say it once. <em>Surfdesk does the rest.</em></h2>
  <p class="intro">Most client trackers are forms you fill out after the real work. Surfdesk works the way you talk: type or say what happened and it files the note, schedules the follow-up and records the result.</p>
  <div class="grid">
    <div class="card"><div class="num">01</div><h3>Follow-ups that don&rsquo;t slip</h3><p>Every check-in, callback and renewal on one Today list, with reminders on your phone.</p></div>
    <div class="card"><div class="num">02</div><h3>Case notes in seconds</h3><p>Voice notes and a smart command box turn &ldquo;met with Ava, housing approved&rdquo; into a dated note and an outcome.</p></div>
    <div class="card"><div class="num">03</div><h3>Reports that build themselves</h3><p>People served, outcomes reached and revenue by service, ready as a one-click PDF.</p></div>
  </div>
</div></section>

<section class="block"><div class="wrap">
  <div class="grid two">
    <div class="card"><div class="num">For nonprofits &amp; agencies</div><h3>Case management software your team will actually use</h3>
      <ul class="check" style="margin-top:14px"><li>Shared caseload with roles and access controls</li><li>Check-ins and outcomes tracked as you work</li><li>Funder-ready Impact report in one click</li><li>Team dashboard and activity log</li></ul></div>
    <div class="card"><div class="num">For small businesses &amp; solo pros</div><h3>A simple CRM for people, not pipelines</h3>
      <ul class="check" style="margin-top:14px"><li>Every client and their full history in one place</li><li>Reminders so no regular goes quiet</li><li>See which services bring in the money</li><li>Tasks, to-dos and notes alongside your clients</li></ul></div>
  </div>
</div></section>

<section class="block" id="pricing"><div class="wrap">
  <h2>Simple pricing that gets <em>cheaper as your team grows.</em></h2>
  <p class="intro">Start free. Skip the trial and get 30% off your first month.</p>
  <div class="grid four">
    <div class="card"><h3>Individual</h3><div class="price">$9 <span>/ month</span></div><p>For one person with clients, projects or a busy life to keep straight.</p><p class="note">7-day free trial &middot; no card</p></div>
    <div class="card"><h3>Small Team</h3><div class="price">$19 <span>/ user / month</span></div><p>For teams of 2&ndash;18. Shared workspace, roles, one bill.</p><p class="note">14-day free trial</p></div>
    <div class="card feat"><h3>Organization</h3><div class="price">$349 <span>/ month</span></div><p>For 19+. 20 seats included, extra seats $15. Impact reports and admin controls.</p><p class="note">Save vs. Small Team at 19+ seats</p></div>
    <div class="card"><h3>Enterprise</h3><div class="price">Custom</div><p>Guided onboarding, data import, integrations and priority support.</p><p class="note">Tailored pricing &amp; terms</p></div>
  </div>
  <div class="ctas" style="margin-top:28px"><a class="btn btn-p" href="{SURFDESK}" rel="noopener">Start your free trial</a></div>
</div></section>

<section class="block"><div class="wrap"><h2>Surfdesk FAQ</h2>{faq_html(sd_faqs)}</div></section>
"""
sd_schema = [
    {"@type": "SoftwareApplication", "@id": SURFDESK + "/#app", "name": "Surfdesk", "url": SURFDESK,
     "applicationCategory": "BusinessApplication", "applicationSubCategory": "CRM / Case management",
     "operatingSystem": "Web, iOS, Android", "image": SITE + "/surfdesk.webp",
     "description": "Client tracker and case management app that keeps follow-ups from slipping and builds Impact reports automatically. For nonprofits, agencies, small businesses and solo professionals.",
     "publisher": {"@id": ORG_ID}, "creator": {"@id": ORG_ID},
     "offers": [
         {"@type": "Offer", "name": "Individual", "price": "9.00", "priceCurrency": "USD", "url": SURFDESK, "description": "Per month. 7-day free trial, no card needed."},
         {"@type": "Offer", "name": "Small Team", "price": "19.00", "priceCurrency": "USD", "url": SURFDESK, "description": "Per user per month, teams of 2-18. 14-day free trial."},
         {"@type": "Offer", "name": "Organization", "price": "349.00", "priceCurrency": "USD", "url": SURFDESK, "description": "Per month, 20 seats included; additional seats $15/user/month."}]},
    faq_schema(SITE + "/surfdesk", sd_faqs),
]

# ─────────────────────────────── WEB DESIGN ───────────────────────────────
wd_faqs = [
    ("Do you build websites for real estate agents in San Diego?", "Yes. Sonder Studio designs and builds custom websites for real estate agents, teams and brokerages in San Diego and across California, and works remotely with clients nationwide."),
    ("How much does a custom website cost?", "Every site is scoped to your goals, so pricing is custom. The free 30-minute call is where we map what you need and give you a clear proposal with a fixed scope and timeline."),
    ("Do you use templates?", "No. Every site is designed from scratch around your brand, market and audience. We use AI tools to move fast, but a designer makes every decision."),
    ("How long does a website take?", "Most projects launch in a few weeks, depending on scope. You get a defined timeline in your proposal before any work starts."),
    ("Can you add AI features to my website?", "Yes. We integrate AI where it helps conversion — lead capture and qualification, chat assistants trained on your listings or services, and automated follow-up."),
    ("Is the site optimized for Google?", "Yes. Every build ships with fast load times, clean semantic markup, structured data, meta tags and a sitemap, so search engines understand and rank it."),
]
wd_body = f"""
<section class="hero"><div class="wrap">
  <div class="eyebrow">02 &middot; Sonder Studio &middot; San Diego</div>
  <h1>Custom web design in San Diego, <em>built to convert.</em></h1>
  <p class="lede">Sonder Studio designs high-performance websites for real estate professionals, luxury brands and ambitious businesses. No templates &mdash; strategy first, then scroll-driven design, AI built in, and fast, search-ready code.</p>
  <div class="ctas"><a class="btn btn-p" href="{CAL}" rel="noopener">Book a free call</a><a class="btn btn-g" href="{STUDIO}" rel="noopener">See Sonder Studio &#8599;</a></div>
  <p class="micro">Free &middot; 30 min &middot; no pressure</p>
</div></section>
<div class="wrap"><div class="figure"><img src="/studio.webp" alt="Aerial view of beachfront real estate at sunset — Sonder Studio real estate web design" width="1400" height="933"></div></div>

<section class="block"><div class="wrap">
  <h2>In real estate, <em>the best-looking agent wins.</em></h2>
  <p class="intro">Buyers and sellers judge you by your website before they ever call. A generic brokerage page says you&rsquo;re one of many. A site built around your brand says you&rsquo;re the one to hire.</p>
  <div class="grid">
    <div class="card"><div class="num">01</div><h3>Real estate websites</h3><p>Agent and team sites, listing showcases, neighborhood pages and lead capture that turns visitors into appointments.</p></div>
    <div class="card"><div class="num">02</div><h3>Brand &amp; business sites</h3><p>Premium sites for luxury brands, local businesses and startups that need to look established on day one.</p></div>
    <div class="card"><div class="num">03</div><h3>AI integration</h3><p>Chat assistants, smart lead forms and automated follow-up, wired into the site so leads never sit unanswered.</p></div>
  </div>
</div></section>

<section class="block"><div class="wrap">
  <h2>Why not just use an AI website builder?</h2>
  <p class="intro">AI builders are powerful &mdash; we use AI every day. But they regress to the average: clean, competent and forgettable. High-converting design is psychology: where the eye travels, what earns trust, the exact moment someone decides to act.</p>
  <ul class="check">
    <li>Custom design built around your brand, market and audience</li>
    <li>Engineered on conversion psychology, not decoration</li>
    <li>Fast, accessible, search-optimized code with structured data</li>
    <li>Ten years of design craft behind every decision</li>
  </ul>
</div></section>

<section class="block"><div class="wrap">
  <h2>How it works</h2>
  <div class="grid">
    <div class="card"><div class="num">Step 1</div><h3>Free call</h3><p>30 minutes on your goals, audience and what&rsquo;s not working today.</p></div>
    <div class="card"><div class="num">Step 2</div><h3>Proposal</h3><p>A fixed scope, timeline and price. No surprises.</p></div>
    <div class="card"><div class="num">Step 3</div><h3>Design, build, launch</h3><p>You stay close throughout, and we launch fast without cutting corners.</p></div>
  </div>
</div></section>

<section class="block"><div class="wrap"><h2>Web design FAQ</h2>{faq_html(wd_faqs)}</div></section>
<section class="closer"><div class="wrap"><h2>Let&rsquo;s build the site <em>you&rsquo;ve been putting off.</em></h2><p>San Diego or anywhere in the US &mdash; it starts with one free conversation.</p><div class="ctas"><a class="btn btn-p" href="{CAL}" rel="noopener">Book a free call</a></div></div></section>
"""
wd_schema = [
    {"@type": "ProfessionalService", "@id": SITE + "/web-design#service", "name": "Sonder Studio",
     "url": STUDIO, "image": SITE + "/studio.webp", "parentOrganization": {"@id": ORG_ID},
     "description": "Custom web design and development in San Diego for real estate agents, brokerages, luxury brands and businesses. No templates; conversion-focused design with AI integration.",
     "areaServed": [SAN_DIEGO, US], "priceRange": "$$$",
     "serviceType": ["Web Design", "Real Estate Web Design", "Website Development", "AI Integration", "Brand Identity"]},
    faq_schema(SITE + "/web-design", wd_faqs),
]

# ─────────────────────────────── AI CONSULTING ───────────────────────────────
ai_faqs = [
    ("What does an AI consultant do for a small business?", "We find the repetitive work eating your team&rsquo;s time, decide where AI genuinely pays off, then build and set up the automations and tools — and train your team to use them."),
    ("Do you offer AI consulting in San Diego?", "Yes. Sonder Consulting works with businesses in San Diego in person or remotely, and with companies anywhere in the US."),
    ("How much does AI consulting cost?", "The first 30-minute call is free. After that, every engagement is scoped to a defined outcome with a fixed proposal, so you know the cost before work starts."),
    ("What kinds of things can you automate?", "Lead follow-up, intake and scheduling, document and email drafting, reporting, data entry between apps, customer support answers and internal knowledge search, among others."),
    ("Do I need technical staff to use what you build?", "No. We build around the tools you already use and hand over simple, documented workflows your team can run day to day."),
    ("Which AI tools do you work with?", "We pick the right model and tools for the job — including OpenAI and Anthropic models and common automation platforms — rather than forcing one vendor."),
]
ai_body = f"""
<section class="hero"><div class="wrap">
  <div class="eyebrow">03 &middot; Sonder Consulting &middot; San Diego</div>
  <h1>AI consulting &amp; automation <em>for businesses that want results.</em></h1>
  <p class="lede">Most businesses know AI matters &mdash; few know where to start. We find the busywork, automate it, and build custom AI tools around how you already operate. Based in San Diego, working with teams across the US.</p>
  <div class="ctas"><a class="btn btn-p" href="{CAL}" rel="noopener">Book a free AI call</a></div>
  <p class="micro">Free &middot; 30 min &middot; no pressure</p>
</div></section>
<div class="wrap"><div class="figure"><img src="/consulting.webp" alt="Aerial view of a coastal city and marina — Sonder Consulting AI and automation services" width="1400" height="856"></div></div>

<section class="block"><div class="wrap">
  <h2>Your competitors are already using AI. <em>Let&rsquo;s put you ahead.</em></h2>
  <p class="intro">We don&rsquo;t sell AI for its own sake. Every engagement starts with where your time and money actually go, and ends with something your team uses every day.</p>
  <div class="grid">
    <div class="card"><div class="num">01</div><h3>AI strategy</h3><p>A clear map of where AI pays off in your business &mdash; and where it doesn&rsquo;t &mdash; ranked by return.</p></div>
    <div class="card"><div class="num">02</div><h3>Workflow automation</h3><p>Follow-ups, intake, scheduling, reporting and data entry that run themselves.</p></div>
    <div class="card"><div class="num">03</div><h3>Custom AI tools</h3><p>Assistants and internal tools trained on your documents, services and processes.</p></div>
  </div>
</div></section>

<section class="block"><div class="wrap">
  <h2>We build AI products, too</h2>
  <p class="intro">Sonder Project builds and runs its own AI-powered software. <a href="/surfdesk">Surfdesk</a> turns a spoken sentence into a filed note, a reminder and a tracked outcome. The same thinking goes into the tools we build for clients.</p>
  <ul class="check">
    <li>27+ businesses helped with AI</li>
    <li>Direct partnership &mdash; you work with the builder, not a middleman</li>
    <li>Fixed scope and timeline on every engagement</li>
  </ul>
</div></section>

<section class="block"><div class="wrap"><h2>AI consulting FAQ</h2>{faq_html(ai_faqs)}</div></section>
<section class="closer"><div class="wrap"><h2>Find out where AI <em>pays off for you.</em></h2><p>One free 30-minute call. You&rsquo;ll leave with at least one thing you can automate this month.</p><div class="ctas"><a class="btn btn-p" href="{CAL}" rel="noopener">Book a free AI call</a></div></div></section>
"""
ai_schema = [
    {"@type": "ProfessionalService", "@id": SITE + "/ai-consulting#service", "name": "Sonder Consulting",
     "url": SITE + "/ai-consulting", "image": SITE + "/consulting.webp", "parentOrganization": {"@id": ORG_ID},
     "description": "AI consulting, workflow automation and custom AI tools for small and mid-sized businesses in San Diego and across the US.",
     "areaServed": [SAN_DIEGO, US],
     "serviceType": ["AI Consulting", "Business Automation", "Workflow Automation", "Custom AI Tools", "AI Strategy"]},
    faq_schema(SITE + "/ai-consulting", ai_faqs),
]

# ─────────────────────────────── PROTOCOL ───────────────────────────────
pr_faqs = [
    ("What is Sonder Protocol?", "Sonder Protocol publishes practical household preparedness guides. Protocol 001 is The 30-Day Blackout Playbook, a plan for power outages."),
    ("What's in The 30-Day Blackout Playbook?", "One 42-page household plan: what to buy, how much, and what to do hour by hour when the power goes out — water, light, radios, power, heat and CO safety, food, first aid and sanitation."),
    ("How do I get it?", "It&rsquo;s an instant PDF download from the Sonder Protocol site."),
]
pr_body = f"""
<section class="hero"><div class="wrap">
  <div class="eyebrow">04 &middot; Sonder Protocol</div>
  <h1>When the power goes out, <em>know exactly what to do.</em></h1>
  <p class="lede">Sonder Protocol makes practical preparedness guides for real households. Protocol 001, The 30-Day Blackout Playbook, is one 42-page plan: what to buy, how much, and what to do hour by hour. Prepared, not paranoid.</p>
  <div class="ctas"><a class="btn btn-p" href="{PROTOCOL}" rel="noopener">Get the Playbook &#8599;</a></div>
</div></section>
<div class="wrap"><div class="figure" style="max-width:720px"><img src="/protocol.webp" alt="The 30-Day Blackout Playbook by Sonder Protocol, a household field manual with readiness checklists" width="720" height="720"></div></div>
<section class="block"><div class="wrap">
  <h2>What the Playbook covers</h2>
  <ul class="check">
    <li>Water: how much to store and how to keep it safe</li>
    <li>Light, radios and backup power</li>
    <li>Heat and carbon monoxide safety</li>
    <li>Food, first aid and sanitation</li>
    <li>An hour-by-hour action plan and household readiness checklists</li>
  </ul>
</div></section>
<section class="block"><div class="wrap"><h2>Sonder Protocol FAQ</h2>{faq_html(pr_faqs)}</div></section>
"""
pr_schema = [
    {"@type": "Book", "@id": PROTOCOL + "/#playbook", "name": "The 30-Day Blackout Playbook",
     "bookFormat": "https://schema.org/EBook", "numberOfPages": 42, "url": PROTOCOL,
     "image": SITE + "/protocol.webp", "publisher": {"@id": ORG_ID},
     "description": "A 42-page household plan for power outages: what to buy, how much, and what to do hour by hour."},
    faq_schema(SITE + "/sonder-protocol", pr_faqs),
]

# ─────────────────────────────── ABOUT ───────────────────────────────
ab_body = f"""
<section class="hero"><div class="wrap">
  <div class="eyebrow">About Sonder Project</div>
  <h1>One studio. <em>A family of businesses.</em></h1>
  <p class="lede">Sonder Project is a creative digital agency in San Diego. We design and build the apps, websites and AI tools businesses run on &mdash; and we build and run our own products, starting with Surfdesk.</p>
  <div class="ctas"><a class="btn btn-p" href="{CAL}" rel="noopener">Work with us</a><a class="btn btn-g" href="{SURFDESK}" rel="noopener">Try Surfdesk</a></div>
</div></section>
<section class="block"><div class="wrap">
  <h2>Designed by an artist. <em>Not a template.</em></h2>
  <p class="intro">Sonder Project was founded by a UI/UX designer and artist with ten years of craft, built on one truth: conversion is human psychology. Every color, rhythm and point of friction is designed to move people, not just to look good.</p>
  <p class="intro">That same standard runs through everything under the Sonder name &mdash; client work and our own products alike. We use AI every day, but a designer makes every decision.</p>
</div></section>
<section class="block"><div class="wrap">
  <h2>What we believe</h2>
  <div class="grid">
    <div class="card"><h3>Build what you&rsquo;d use</h3><p>We ship our own software, so we know what it takes for a product to earn a place in someone&rsquo;s day.</p></div>
    <div class="card"><h3>Direct partnership</h3><p>You work with the people building your project. No account managers, no middlemen.</p></div>
    <div class="card"><h3>Strategy before pixels</h3><p>Goals, market and customer first. The design flows from that.</p></div>
  </div>
</div></section>
<section class="closer"><div class="wrap"><h2>Let&rsquo;s build <em>what&rsquo;s next.</em></h2><p>An app, a website, AI in your workflow. It starts with one free conversation.</p><div class="ctas"><a class="btn btn-p" href="{CAL}" rel="noopener">Book a free call</a></div></div></section>
"""
ab_schema = [{"@type": "AboutPage", "@id": SITE + "/about#about", "url": SITE + "/about", "about": {"@id": ORG_ID}}]

nf_body = f"""
<section class="hero"><div class="wrap">
  <div class="eyebrow">404</div>
  <h1>This page drifted <em>out to sea.</em></h1>
  <p class="lede">The page you&rsquo;re looking for doesn&rsquo;t exist. Try one of these instead.</p>
  <div class="ctas"><a class="btn btn-p" href="/">Go home</a><a class="btn btn-g" href="/surfdesk">See Surfdesk</a></div>
</div></section>
"""

PAGES = [
    ("surfdesk", "Surfdesk — Client Tracker & Case Management App",
     "Surfdesk is the client tracker where nothing slips: say it once and it saves the note, sets the reminder and builds your Impact report. From $9/mo, free trial.",
     sd_body, sd_schema, "Surfdesk", ""),
    ("web-design", "Web Design San Diego — Real Estate & Business Websites",
     "Custom web design in San Diego for real estate agents, brokerages and ambitious brands. No templates: conversion-focused design, AI built in. Book a free call.",
     wd_body, wd_schema, "Web Design", ""),
    ("ai-consulting", "AI Consulting San Diego — Automation & Custom AI Tools",
     "AI consulting and workflow automation for businesses in San Diego and across the US. Strategy, automation and custom AI tools. Book a free 30-minute call.",
     ai_body, ai_schema, "AI Consulting", ""),
    ("sonder-protocol", "Sonder Protocol — The 30-Day Blackout Playbook",
     "Sonder Protocol makes practical preparedness guides. The 30-Day Blackout Playbook: a 42-page household plan for power outages, hour by hour.",
     pr_body, pr_schema, "Sonder Protocol", "orange"),
    ("about", "About Sonder Project — Creative Digital Agency in San Diego",
     "Sonder Project is a San Diego creative digital agency building apps, websites and AI tools for businesses, and the maker of Surfdesk and Sonder Protocol.",
     ab_body, ab_schema, "About", ""),
    ("404", "Page not found | Sonder Project", "This page doesn't exist.", nf_body, [], None, ""),
]

if __name__ == "__main__":
    for slug, title, desc, body, schema, crumb, theme in PAGES:
        assert len(desc) <= 160 and len(title) <= 60, (slug, len(title), len(desc))
        path = os.path.join(OUT, slug + ".html")
        with open(path, "w") as f:
            f.write(page(slug, title, desc, body, schema, crumb, theme=theme))
        print(f"wrote {path}  title={len(title)} desc={len(desc)}")
