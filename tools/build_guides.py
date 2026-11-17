#!/usr/bin/env python3
"""Build /guides (index) and /guides/<slug> article pages for sonderproject.co.

Edit GUIDES below, then run:  python3 tools/build_guides.py
Writes public/guides.html and public/guides/<slug>.html and refreshes public/sitemap.xml.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_pages import page, faq_html, faq_schema, esc, SITE, CAL, SURFDESK, PROTOCOL, ORG_ID, OUT  # noqa: E402

PUBLISHED = "2026-11-17"
AUTHOR = {"@type": "Organization", "@id": ORG_ID, "name": "Sonder Project"}

GUIDES = [
    {
        "slug": "website-cost-san-diego",
        "title": "How Much Does a Website Cost in San Diego? (2026)",
        "desc": "What a small business website really costs in 2026: DIY, freelancer and agency price ranges, hidden costs, and how to budget in San Diego.",
        "h1": "How much does a website cost in San Diego?",
        "kicker": "Web design",
        "read": 6,
        "faqs": [
            ("How much does a small business website cost?", "Across published 2026 estimates, a 5–10 page site typically costs about $300–$1,000 to build yourself, $1,500–$5,000 with a freelancer, and $5,000–$15,000 with an agency for a custom build. Complex sites and e-commerce cost more."),
            ("Are there ongoing costs?", "Yes. Expect hosting, a domain, maintenance and any paid plugins or tools every year, plus content updates. Ask for these in writing before you start."),
            ("Why do quotes vary so much?", "Scope. The number of pages, custom design versus a template, copywriting, photography, integrations and SEO setup all change the price. Copy, photos and SEO alone can add a large share on top of a design-only quote."),
        ],
        "body": f"""
<p>&ldquo;How much is a website?&rdquo; is the first question every business owner asks, and the honest answer is: it depends on who builds it and what it has to do. Here&rsquo;s what the 2026 market looks like, so you can budget with your eyes open.</p>
<h2>Typical price ranges in 2026</h2>
<p>Published estimates from across the industry cluster around these ranges for a 5&ndash;10 page small business site:</p>
<ul class="check">
<li><strong>Do it yourself</strong> (website builder): roughly $300&ndash;$1,000 to set up, plus monthly plan and plugin costs.</li>
<li><strong>Freelancer</strong>: roughly $1,500&ndash;$5,000.</li>
<li><strong>Agency, custom build</strong>: roughly $5,000&ndash;$15,000, more for complex sites or online stores.</li>
</ul>
<p>Most of these figures come from companies that sell websites, so treat them as a guide, not a quote. San Diego pricing generally sits in line with national ranges for remote-friendly work.</p>
<h2>What actually drives the price</h2>
<ul class="check">
<li><strong>Custom design vs. template.</strong> A template is faster and cheaper; custom design is built around your brand and how your customers decide.</li>
<li><strong>Content.</strong> Copywriting and professional photography are often quoted separately and can add a large share on top.</li>
<li><strong>Features.</strong> Booking, listings, lead forms, AI chat, payments and integrations each add build time.</li>
<li><strong>SEO setup.</strong> Fast load times, structured data and a sitemap are what get you found on Google.</li>
</ul>
<h2>Hidden costs to ask about</h2>
<p>Before you sign, get these in writing: hosting, domain, maintenance, who owns the site and files, how updates are billed, and whether SEO setup is included.</p>
<h2>How to spend your budget wisely</h2>
<p>If the site&rsquo;s job is to bring in clients, the cheapest build is rarely the cheapest outcome. A site that converts even a few extra leads a month usually pays for the difference in design. Start from your goal &mdash; calls, bookings, listings, signups &mdash; and scope backwards.</p>
<p>Sonder Studio builds custom websites for San Diego businesses and real estate professionals. <a href="/web-design">See how we work</a> or <a href="{CAL}" rel="noopener">book a free 30-minute call</a> for a fixed-scope proposal.</p>
""",
        "related": ["/web-design"],
    },
    {
        "slug": "real-estate-agent-website",
        "title": "What Every Real Estate Agent Website Needs",
        "desc": "The 9 things every real estate agent website needs to win clients: from a clear first screen and lead capture to neighborhood pages, speed and SEO.",
        "h1": "What every real estate agent website needs",
        "kicker": "Real estate",
        "read": 5,
        "faqs": [
            ("Do real estate agents still need their own website?", "Yes. Your brokerage page lists you among many agents. Your own site is where buyers and sellers decide you're the one to call, and it's the asset you keep if you change brokerages."),
            ("Should my site include IDX listings?", "If your market and MLS allow it, IDX search keeps buyers on your site. Even without it, featured listings and neighborhood pages give Google and visitors a reason to stay."),
        ],
        "body": f"""
<p>Buyers and sellers look you up before they ever call. In real estate, the best-looking agent online often gets the first conversation. Here&rsquo;s what your site needs to earn it.</p>
<h2>1. A first screen that says who you are and where you sell</h2>
<p>Your name, your market and one clear action (&ldquo;Book a call&rdquo;, &ldquo;Get a home value&rdquo;) &mdash; visible without scrolling, on a phone.</p>
<h2>2. Lead capture that feels like help</h2>
<p>A home-value request, a neighborhood guide or a &ldquo;new listings&rdquo; alert converts better than a generic contact form.</p>
<h2>3. Neighborhood pages</h2>
<p>One page per area you serve, with what it&rsquo;s like to live there. These are also how you rank for &ldquo;homes in [neighborhood]&rdquo; searches.</p>
<h2>4. Proof</h2>
<p>Real reviews, recent sales and your story. Trust is the product.</p>
<h2>5. Listings</h2>
<p>Featured listings at minimum; IDX search if your MLS allows it.</p>
<h2>6. Speed</h2>
<p>Most visitors are on phones. A slow site loses them before your photos load.</p>
<h2>7. SEO basics</h2>
<p>A unique title and description on every page, structured data, a sitemap and a Google Business Profile that links to your site.</p>
<h2>8. Fast follow-up</h2>
<p>The site only creates the lead. Answer within minutes &mdash; automated replies and a client tracker like <a href="{SURFDESK}" rel="noopener">Surfdesk</a> make sure nobody goes cold.</p>
<h2>9. A brand that isn&rsquo;t your brokerage&rsquo;s</h2>
<p>Your site should look like you, not like every other agent in the office.</p>
<p>Sonder Studio designs custom real estate websites for agents and brokerages in San Diego. <a href="/web-design">See our web design</a> or <a href="{CAL}" rel="noopener">book a free call</a>.</p>
""",
        "related": ["/web-design", "/surfdesk"],
    },
    {
        "slug": "ai-automation-small-business",
        "title": "7 Things a Small Business Can Automate With AI",
        "desc": "Practical AI automation ideas for small businesses: lead follow-up, intake, scheduling, email drafts, reporting, support answers and data entry.",
        "h1": "7 things a small business can automate with AI",
        "kicker": "AI & automation",
        "read": 6,
        "faqs": [
            ("Is AI automation expensive for a small business?", "It doesn't have to be. Many automations run on tools you already pay for, and the right first project often saves hours a week. Start with one repetitive task and measure the time saved."),
            ("Will AI replace my staff?", "The best small-business automations remove busywork — copying data, drafting the same email, chasing follow-ups — so your team spends more time with customers."),
        ],
        "body": f"""
<p>You don&rsquo;t need a data science team to get value from AI. The best first projects are boring, repetitive tasks your team does every day. Here are seven we see pay off again and again.</p>
<h2>1. Lead follow-up</h2>
<p>Reply to every new inquiry within minutes with a personalized message, then remind your team to call.</p>
<h2>2. Intake and qualification</h2>
<p>Turn a form or a call transcript into a structured record and a priority, so the best leads get attention first.</p>
<h2>3. Scheduling</h2>
<p>Let customers book, reschedule and get reminders without back-and-forth.</p>
<h2>4. Drafting emails and documents</h2>
<p>Proposals, follow-ups and summaries drafted from your notes, then reviewed by a person.</p>
<h2>5. Reporting</h2>
<p>Weekly numbers pulled together automatically instead of copied from three systems.</p>
<h2>6. Answering common questions</h2>
<p>An assistant trained on your services and policies handles the questions you answer every day.</p>
<h2>7. Data entry between apps</h2>
<p>When a sale, booking or form comes in, update every system it touches automatically.</p>
<h2>Where to start</h2>
<p>List the tasks your team repeats every week, estimate the hours, and automate the biggest one first. We built <a href="/surfdesk">Surfdesk</a> on the same idea: say one sentence and it files the note, sets the reminder and counts the result.</p>
<p>Want help picking the first project? <a href="/ai-consulting">Sonder Consulting</a> works with businesses in San Diego and across the US. <a href="{CAL}" rel="noopener">Book a free 30-minute AI call</a>.</p>
""",
        "related": ["/ai-consulting", "/surfdesk"],
    },
    {
        "slug": "ai-website-builder-vs-web-designer",
        "title": "AI Website Builder vs Web Designer: Which Is Better?",
        "desc": "AI website builders are fast and cheap. A web designer builds for conversion. An honest comparison of cost, quality and when each one makes sense.",
        "h1": "AI website builder vs. web designer: which is better?",
        "kicker": "Web design",
        "read": 5,
        "faqs": [
            ("Can an AI website builder make a good website?", "Yes, for simple needs. AI builders produce clean, competent sites quickly. They tend toward generic layouts, and they can't make strategic decisions about your audience and conversion for you."),
            ("When should I hire a web designer?", "When your website has to win business: competitive markets, premium brands, real estate, or anywhere a few extra leads a month are worth more than the price difference."),
        ],
        "body": f"""
<p>AI website builders can produce a decent-looking site in minutes. So why would anyone still hire a designer? Here&rsquo;s an honest breakdown &mdash; from a studio that uses AI every day.</p>
<h2>Where AI builders win</h2>
<ul class="check"><li>Speed: a working site in an afternoon.</li><li>Cost: a monthly plan instead of a project fee.</li><li>Good enough for simple, low-stakes sites.</li></ul>
<h2>Where they fall short</h2>
<ul class="check">
<li><strong>They regress to the average.</strong> Trained on millions of sites, they hand you a blend of all of them.</li>
<li><strong>They don&rsquo;t know your customer.</strong> Conversion is psychology: what earns trust, where the eye goes, when someone decides.</li>
<li><strong>You have to know what good looks like to steer them.</strong> Most people ship something that &ldquo;works&rdquo; and never learn why it underperforms.</li>
</ul>
<h2>The best of both</h2>
<p>AI in a designer&rsquo;s hands is a superpower: faster builds, more iterations, and every decision still made by someone who understands your market.</p>
<h2>How to decide</h2>
<p>If your website is a digital business card, use a builder. If it has to bring in clients, the last 20% of craft is the whole game.</p>
<p>See how <a href="/web-design">Sonder Studio</a> designs websites in San Diego, or <a href="{CAL}" rel="noopener">book a free call</a>.</p>
""",
        "related": ["/web-design"],
    },
    {
        "slug": "nonprofit-impact-report",
        "title": "How to Write a Nonprofit Impact Report Funders Love",
        "desc": "How to write a nonprofit impact report: what funders want to see, outputs vs outcomes, the numbers to track all year, and a free template.",
        "h1": "How to write a nonprofit impact report funders love",
        "kicker": "Nonprofits",
        "read": 7,
        "faqs": [
            ("What should a nonprofit impact report include?", "People served, services delivered, outcomes reached against your targets, a short story or two that shows the change, and what you'll do next. Keep the numbers consistent with your grant agreement."),
            ("What's the difference between outputs and outcomes?", "Outputs are what you did, like sessions held or people served. Outcomes are the change that resulted, like a job, stable housing or a completed program."),
            ("How do I make reporting easier?", "Track outcomes as they happen instead of reconstructing them at the end. A shared spreadsheet works for small programs; case management software like Surfdesk counts them automatically."),
        ],
        "body": f"""
<p>Funders don&rsquo;t want a scrapbook. They want to know that their money changed something &mdash; and that you can prove it. Here&rsquo;s how to build an impact report that does that, without losing the last week of the quarter to spreadsheets.</p>
<h2>1. Start from your grant agreement</h2>
<p>List every metric and target you promised. Your report should answer each one directly.</p>
<h2>2. Separate outputs from outcomes</h2>
<p><strong>Outputs</strong> are what you did: people served, sessions held. <strong>Outcomes</strong> are what changed: jobs, housing, completions. Funders increasingly ask for both.</p>
<h2>3. Count unduplicated people</h2>
<p>If one person came ten times, they&rsquo;re one person served and ten services. Mixing these up is the most common reporting error.</p>
<h2>4. Track all year, not at the end</h2>
<p>The painful part of reporting is reconstruction. Record outcomes the moment they happen and the report is just a total.</p>
<h2>5. Add one or two real stories</h2>
<p>Numbers prove scale; a story proves change. Get consent and keep it short.</p>
<h2>6. Show what&rsquo;s next</h2>
<p>Close with what you learned and what you&rsquo;ll do with continued support.</p>
<h2>Free template</h2>
<p>Download the free <a href="{SURFDESK}/templates/funder-impact-report" rel="noopener">funder impact report template</a> to track people served, services and outcomes by month.</p>
<p>Or let the report build itself: <a href="/surfdesk">Surfdesk</a> counts people served and outcomes as your team works and turns them into a polished Impact report PDF in one click.</p>
""",
        "related": ["/surfdesk"],
    },
    {
        "slug": "power-outage-checklist",
        "title": "Power Outage Checklist: What to Do in the First 24 Hours",
        "desc": "A practical power outage checklist for households: what to do in the first hour, the first day, and what to have ready before the lights go out.",
        "h1": "Power outage checklist: what to do in the first 24 hours",
        "kicker": "Preparedness",
        "read": 5,
        "faqs": [
            ("How long does food stay safe in the fridge without power?", "Food safety agencies generally advise that a closed refrigerator keeps food safe for about 4 hours and a full closed freezer for about 48 hours. Keep the doors shut and check official guidance for your area."),
            ("Is it safe to use a generator or grill indoors?", "No. Never run a generator, grill or camp stove indoors or in a garage. They produce carbon monoxide, which can be deadly. Use a battery-powered carbon monoxide alarm."),
        ],
        "body": f"""
<p>Most outages are short. The ones that aren&rsquo;t catch households unprepared. Here&rsquo;s a simple plan for the first day &mdash; and what to have ready before you need it.</p>
<h2>The first hour</h2>
<ul class="check">
<li>Check whether it&rsquo;s just you or the neighborhood, and report it to your utility.</li>
<li>Switch to flashlights or lanterns, not candles.</li>
<li>Unplug sensitive electronics to protect them from a surge when power returns.</li>
<li>Keep the fridge and freezer closed.</li>
</ul>
<h2>The first day</h2>
<ul class="check">
<li>Use your phone sparingly and charge it from a battery bank.</li>
<li>Get updates from a battery or hand-crank radio.</li>
<li>Check on neighbors, especially older adults and anyone who relies on medical equipment.</li>
<li>Never run generators, grills or camp stoves indoors &mdash; carbon monoxide is the biggest outage danger.</li>
</ul>
<h2>Have this ready before an outage</h2>
<ul class="check">
<li>Water and shelf-stable food for every person and pet.</li>
<li>Flashlights, spare batteries and a radio.</li>
<li>A battery bank for phones.</li>
<li>A first aid kit and any medications.</li>
<li>A battery-powered carbon monoxide alarm.</li>
</ul>
<h2>Want the full plan?</h2>
<p><a href="{PROTOCOL}" rel="noopener">The 30-Day Blackout Playbook</a> from Sonder Protocol is a 42-page household plan: what to buy, how much, and what to do hour by hour. <a href="/sonder-protocol">Learn more</a>.</p>
""",
        "related": ["/sonder-protocol"],
    },
]

ARTICLE_CSS = """<style>
.article{max-width:740px}
.article h2{font-size:clamp(22px,2.4vw,30px);margin:40px 0 12px}
.article p{color:var(--dim);margin-bottom:16px;font-size:17px}
.article p a,.article li a{text-decoration:none;border-bottom:1px solid rgba(var(--accent-rgb),.4)}
.article ul.check{margin:8px 0 20px}
.article strong{color:var(--text);font-weight:600}
.meta{font-size:13px;color:var(--dim);margin-top:-8px}
.guide-list{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
.guide-list a{display:block;text-decoration:none;color:var(--text)}
.guide-list .card h3{font-size:21px}
@media(max-width:900px){.guide-list{grid-template-columns:1fr}}
</style>"""


def article(g):
    path = f"/guides/{g['slug']}"
    related = "".join(f'<a class="btn btn-g" href="{r}">{ {"/web-design":"Web design","/surfdesk":"Surfdesk","/ai-consulting":"AI consulting","/sonder-protocol":"Sonder Protocol"}[r] } &rarr;</a>' for r in g["related"])
    body = f"""{ARTICLE_CSS}
<section class="hero"><div class="wrap"><div class="article">
  <div class="eyebrow">Guide &middot; {esc(g['kicker'])}</div>
  <h1>{esc(g['h1'])}</h1>
  <p class="meta">By Sonder Project &middot; San Diego &middot; Updated November 2026 &middot; {g['read']} min read</p>
</div></div></section>
<section class="block" style="border-top:none;padding-top:0"><div class="wrap"><div class="article">
{g['body']}
<div class="ctas" style="margin-top:28px">{related}</div>
</div></div></section>
<section class="block"><div class="wrap"><h2>FAQ</h2>{faq_html(g['faqs'])}</div></section>
"""
    schema = [
        {"@type": "Article", "@id": SITE + path + "#article", "headline": g["h1"], "description": g["desc"],
         "datePublished": PUBLISHED, "dateModified": PUBLISHED, "author": AUTHOR, "publisher": {"@id": ORG_ID},
         "mainEntityOfPage": SITE + path, "image": SITE + "/og-image.jpg", "inLanguage": "en-US"},
        faq_schema(SITE + path, g["faqs"]),
    ]
    return page(f"guides/{g['slug']}", g["title"], g["desc"], body, schema, "Guides")


def index():
    cards = "".join(
        f'<a href="/guides/{g["slug"]}"><div class="card"><div class="num">{esc(g["kicker"])} &middot; {g["read"]} min</div><h3>{esc(g["h1"])}</h3><p>{esc(g["desc"])}</p></div></a>'
        for g in GUIDES)
    body = f"""{ARTICLE_CSS}
<section class="hero"><div class="wrap">
  <div class="eyebrow">Guides</div>
  <h1>Practical guides on websites, <em>AI and running a business.</em></h1>
  <p class="lede">Straight answers from the Sonder Project team in San Diego &mdash; no fluff, no gated downloads.</p>
</div></section>
<section class="block" style="border-top:none;padding-top:0"><div class="wrap"><div class="guide-list">{cards}</div></div></section>
"""
    schema = [{"@type": "CollectionPage", "@id": SITE + "/guides#collection", "url": SITE + "/guides",
               "hasPart": [{"@type": "Article", "url": f"{SITE}/guides/{g['slug']}", "headline": g["h1"]} for g in GUIDES]}]
    return page("guides", "Guides: Websites, AI & Business | Sonder Project",
                "Practical guides from Sonder Project on website costs, real estate websites, AI automation for small business, impact reports and more.",
                body, schema, "Guides")


def sitemap():
    urls = [("", 1.0, "weekly"), ("surfdesk", 0.9, "weekly"), ("web-design", 0.8, "monthly"), ("ai-consulting", 0.8, "monthly"),
            ("guides", 0.7, "weekly"), ("sonder-protocol", 0.6, "monthly"), ("about", 0.5, "monthly")]
    urls += [(f"guides/{g['slug']}", 0.6, "monthly") for g in GUIDES]
    body = "".join(f"  <url>\n    <loc>{SITE}/{u}</loc>\n    <lastmod>{PUBLISHED}</lastmod>\n    <changefreq>{c}</changefreq>\n    <priority>{p}</priority>\n  </url>\n" for u, p, c in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}</urlset>\n'


if __name__ == "__main__":
    os.makedirs(os.path.join(OUT, "guides"), exist_ok=True)
    for g in GUIDES:
        assert len(g["title"]) <= 60 and len(g["desc"]) <= 160, (g["slug"], len(g["title"]), len(g["desc"]))
        with open(os.path.join(OUT, "guides", g["slug"] + ".html"), "w") as f:
            f.write(article(g))
    with open(os.path.join(OUT, "guides.html"), "w") as f:
        f.write(index())
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write(sitemap())
    print(f"wrote {len(GUIDES)} guides + index + sitemap")
