#!/usr/bin/env python3
"""Generate the NIBBI Become a Dealer GemPages page JSON."""

from __future__ import annotations

import datetime
import hashlib
import json
from pathlib import Path


ROOT = ".{{rootClassName}}"
ASSET = "https://saikalee.github.io/nibbi-dealer-v1/nibbi"
PAGE_ID = 720260721000000001
STORE_RELEASE_ID = 317576412
OUT_DIR = Path(__file__).resolve().parent / "output"


BASE_CSS = f"""
@import url("https://fonts.bunny.net/css?family=montserrat:400,500,600,700,800&display=swap");
{ROOT} *,{ROOT} *::before,{ROOT} *::after{{margin:0;padding:0;box-sizing:border-box}}
{ROOT}{{font-family:'Montserrat',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;font-size:16px;line-height:1.5;color:#121212;width:100%}}
{ROOT} img{{display:block;max-width:100%;height:auto}}
{ROOT} a{{color:inherit;text-decoration:none}}
{ROOT} button,{ROOT} input,{ROOT} select,{ROOT} textarea{{font:inherit}}
{ROOT} .gp-wrap{{width:100%;padding-left:6vw;padding-right:6vw}}
{ROOT} .gp-kicker{{font-size:11px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#6c6c66;margin-bottom:26px}}
{ROOT} .gp-kicker-yellow{{color:#f6ed3e}}
{ROOT} .gp-heading{{font-size:clamp(38px,4.2vw,62px);line-height:1;letter-spacing:-.035em;font-weight:700}}
{ROOT} .gp-button{{display:inline-flex;align-items:center;justify-content:space-between;gap:28px;background:#f6ed3e;color:#080808;border:0;border-radius:5px;padding:14px 18px;font-size:11px;font-weight:800;text-transform:uppercase;cursor:pointer}}
@media (min-width:768px){{{ROOT} .gp-wrap{{padding-left:5vw;padding-right:5vw}}}}
"""


def scoped(extra: str) -> str:
    return " ".join((BASE_CSS + extra).split())


SECTIONS = [
    {
        "name": "navigation",
        "label": "NIBBI dealer navigation",
        "html": f"""
<header class="gp-site-header" aria-label="NIBBI dealer navigation">
  <a class="gp-brand" href="#gp-top" aria-label="NIBBI Racing home"><img src="{ASSET}/nibbi-logo.png" alt="NIBBI Racing" loading="eager" width="300" height="80"></a>
  <nav class="gp-nav" aria-label="Dealer page navigation"><a href="#gp-why">Why NIBBI</a><a href="#gp-systems">Product Systems</a><a href="#gp-support">Dealer Support</a><a href="#gp-process">How It Works</a></nav>
  <a class="gp-button gp-header-cta" href="#gp-apply">Apply now <span aria-hidden="true">↗</span></a>
</header>""",
        "css": f"""
{ROOT} .gp-site-header{{height:70px;padding:0 3.5vw;background:#0b0b0b;color:#fff;border-bottom:1px solid #2a2a2a;display:flex;align-items:center;justify-content:space-between}}
{ROOT} .gp-brand{{display:block;line-height:0}}
{ROOT} .gp-brand img{{width:150px;max-height:40px;object-fit:contain}}
{ROOT} .gp-nav{{display:none;align-items:center;gap:24px;font-size:11px;font-weight:600}}
{ROOT} .gp-header-cta{{padding:11px 16px}}
@media (min-width:900px){{{ROOT} .gp-nav{{display:flex}}}}
""",
    },
    {
        "name": "hero",
        "label": "Become a NIBBI dealer hero",
        "html": f"""
<div class="gp-hero" id="gp-top" aria-label="Become a NIBBI dealer">
  <img class="gp-hero-image" src="{ASSET}/hero.webp" alt="NIBBI Racing off-road riders" loading="eager" fetchpriority="high" width="1920" height="1080">
  <div class="gp-hero-shade"></div>
  <div class="gp-hero-content">
    <p class="gp-eyebrow">Become a NIBBI dealer</p>
    <h1>Built for riders.<br>Backed for dealers.</h1>
    <p class="gp-hero-copy">Bring NIBBI performance products to more riders with structured dealer pricing, product guidance and practical sales support.</p>
    <div class="gp-actions"><a class="gp-button" href="#gp-apply">Start your application <span aria-hidden="true">↗</span></a><a class="gp-text-link" href="#gp-why">Explore the partnership ↓</a></div>
  </div>
</div>""",
        "css": f"""
{ROOT} .gp-hero{{height:570px;position:relative;overflow:hidden;background:#111;color:#fff}}
{ROOT} .gp-hero-image{{width:100%;height:100%;object-fit:cover}}
{ROOT} .gp-hero-shade{{position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.88),rgba(0,0,0,.38) 55%,rgba(0,0,0,.08)),linear-gradient(0deg,rgba(0,0,0,.45),transparent 50%)}}
{ROOT} .gp-hero-content{{position:absolute;left:6vw;right:6vw;top:50%;transform:translateY(-48%);max-width:720px}}
{ROOT} .gp-eyebrow{{font-size:11px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#f6ed3e;margin-bottom:18px}}
{ROOT} .gp-hero h1{{font-size:clamp(40px,11vw,92px);line-height:.92;letter-spacing:-.045em;text-transform:uppercase;font-weight:700}}
{ROOT} .gp-hero-copy{{font-size:14px;line-height:1.55;max-width:560px;color:#dedede;margin:18px 0 20px}}
{ROOT} .gp-actions{{display:flex;align-items:flex-start;flex-direction:column;gap:18px}}
{ROOT} .gp-text-link{{font-size:11px;text-transform:uppercase;border-bottom:1px solid #888;padding-bottom:6px}}
@media (min-width:768px){{{ROOT} .gp-hero{{height:600px}}{ROOT} .gp-hero-content{{left:5vw}}{ROOT} .gp-hero h1{{font-size:clamp(52px,6.2vw,92px)}}{ROOT} .gp-hero-copy{{font-size:15px;margin:22px 0 24px}}{ROOT} .gp-actions{{align-items:center;flex-direction:row;gap:22px}}}}
""",
    },
    {
        "name": "partner-signals",
        "label": "NIBBI partner value signals",
        "html": """
<div class="gp-signal-strip" aria-label="NIBBI partnership values">
  <div><strong>Race-proven</strong><span>Products tested in competition</span></div>
  <div><strong>Performance leader</strong><span>Built on specialist engineering</span></div>
  <div><strong>Dealer-first</strong><span>Support through the full sales cycle</span></div>
  <div><strong>Win together</strong><span>Long-term partnership, shared growth</span></div>
</div>""",
        "css": f"""
{ROOT} .gp-signal-strip{{display:grid;grid-template-columns:repeat(2,1fr);background:#f6ed3e;padding:0 3vw}}
{ROOT} .gp-signal-strip>div{{min-height:88px;padding:14px;display:flex;justify-content:center;align-items:flex-start;flex-direction:column;gap:5px;border-right:1px solid rgba(0,0,0,.24)}}
{ROOT} .gp-signal-strip>div:nth-child(2n){{border-right:0}}
{ROOT} .gp-signal-strip strong{{font-size:15px;line-height:1.08;text-transform:uppercase;font-style:italic}}
{ROOT} .gp-signal-strip span{{font-size:8px;line-height:1.35;text-transform:uppercase;font-weight:700}}
@media (min-width:768px){{{ROOT} .gp-signal-strip{{grid-template-columns:repeat(4,1fr);padding:0 4vw}}{ROOT} .gp-signal-strip>div{{min-height:0;padding:19px 18px}}{ROOT} .gp-signal-strip>div:nth-child(2n){{border-right:1px solid rgba(0,0,0,.24)}}{ROOT} .gp-signal-strip>div:last-child{{border-right:0}}{ROOT} .gp-signal-strip strong{{font-size:20px}}{ROOT} .gp-signal-strip span{{font-size:9px}}}}
""",
    },
    {
        "name": "why-nibbi",
        "label": "Why partner with NIBBI",
        "html": f"""
<div class="gp-why gp-wrap" id="gp-why" aria-label="Why partner with NIBBI">
  <p class="gp-kicker">01 / Why partner with NIBBI</p>
  <div class="gp-why-grid"><div><h2 class="gp-heading">More than parts.<br><em>A performance system.</em></h2><p class="gp-intro">NIBBI connects fuel delivery, intake, control, braking, electronics, transmission and rider gear into one focused off-road product story.</p></div><figure><img src="{ASSET}/rally.jpg" alt="NIBBI rally motorcycle" loading="lazy" width="1200" height="800"><figcaption>Built around the ride</figcaption></figure></div>
  <div class="gp-benefits">
    <article><span>01</span><h3>Dealer pricing</h3><p>Approved partners receive structured dealer pricing matched to their business and market.</p></article>
    <article><span>02</span><h3>Technical onboarding</h3><p>Product selection, fitment, installation and basic tuning guidance help teams sell with confidence.</p></article>
    <article><span>03</span><h3>Marketing toolkit</h3><p>Approved product imagery, campaign assets and launch materials support local activation.</p></article>
    <article><span>04</span><h3>Growth opportunities</h3><p>Qualified partners may receive dealer visibility, priority support and market development opportunities.</p></article>
  </div>
</div>""",
        "css": f"""
{ROOT} .gp-why{{background:#f7f7f7;padding-top:54px;padding-bottom:54px}}
{ROOT} .gp-why-grid{{display:grid;grid-template-columns:1fr;gap:34px}}
{ROOT} .gp-heading em{{color:#8d8c85;font-style:normal;font-weight:400}}
{ROOT} .gp-intro{{margin-top:24px;font-size:15px;color:#62625d;line-height:1.55}}
{ROOT} .gp-why figure{{position:relative}}
{ROOT} .gp-why figure img{{width:100%;height:320px;object-fit:cover}}
{ROOT} .gp-why figcaption{{position:absolute;left:0;bottom:24px;background:#f6ed3e;padding:12px 16px;font-size:10px;font-weight:800;letter-spacing:.14em;text-transform:uppercase}}
{ROOT} .gp-benefits{{display:grid;grid-template-columns:repeat(2,1fr);margin-top:38px;border-top:1px solid #d8d8d8}}
{ROOT} .gp-benefits article{{min-height:160px;padding:22px 14px;border-right:1px solid #d8d8d8;border-bottom:1px solid #d8d8d8}}
{ROOT} .gp-benefits article:nth-child(2n){{border-right:0}}
{ROOT} .gp-benefits article>span{{font-size:10px;color:#777}}
{ROOT} .gp-benefits h3{{font-size:17px;margin:18px 0 8px}}
{ROOT} .gp-benefits p{{font-size:12px;line-height:1.5;color:#62625d}}
@media (min-width:900px){{{ROOT} .gp-why{{padding-top:72px;padding-bottom:72px}}{ROOT} .gp-why-grid{{grid-template-columns:1.08fr .92fr;gap:5vw}}{ROOT} .gp-intro{{margin-left:20%;max-width:520px}}{ROOT} .gp-why figure img{{height:360px}}{ROOT} .gp-benefits{{grid-template-columns:repeat(4,1fr);margin-top:56px}}{ROOT} .gp-benefits article{{min-height:178px;padding:24px 20px;border-bottom:0}}{ROOT} .gp-benefits article:nth-child(2n){{border-right:1px solid #d8d8d8}}{ROOT} .gp-benefits article:last-child{{border-right:0}}}}
""",
    },
    {
        "name": "product-systems",
        "label": "NIBBI product ecosystem",
        "html": """
<div class="gp-systems gp-wrap" id="gp-systems" aria-label="NIBBI product ecosystem">
  <p class="gp-kicker gp-kicker-yellow">02 / Product ecosystem</p>
  <div class="gp-systems-head"><h2 class="gp-heading">One brand.<br>Eight ways to grow.</h2><p>Start with the categories that fit your market, then expand the basket as product knowledge and demand grow.</p></div>
  <div class="gp-system-list">
    <article><span>01</span><h3>Fuel systems</h3><p>Carburetors, jets, manifolds and tuning components</p></article><article><span>02</span><h3>Intake systems</h3><p>Air filters and intake solutions</p></article><article><span>03</span><h3>Engine systems</h3><p>Performance and maintenance components</p></article><article><span>04</span><h3>Control systems</h3><p>Handlebars, grips, levers and rider controls</p></article><article><span>05</span><h3>Braking systems</h3><p>Components built for confident control</p></article><article><span>06</span><h3>Electronic systems</h3><p>Ignition and electrical performance parts</p></article><article><span>07</span><h3>Transmission systems</h3><p>Drivetrain and power-delivery components</p></article><article><span>08</span><h3>Rider gear</h3><p>Off-road jerseys, suits, gloves and goggles</p></article>
  </div>
</div>""",
        "css": f"""
{ROOT} .gp-systems{{background:#121212;color:#fff;padding-top:54px;padding-bottom:54px}}
{ROOT} .gp-systems-head{{display:grid;grid-template-columns:1fr;gap:22px;margin-bottom:34px}}
{ROOT} .gp-systems-head p{{color:#a8a8a5;font-size:14px;line-height:1.5;max-width:470px}}
{ROOT} .gp-system-list{{border-top:1px solid #383a3b}}
{ROOT} .gp-system-list article{{display:grid;grid-template-columns:44px 1fr;gap:10px;align-items:center;padding:18px 0;border-bottom:1px solid #383a3b}}
{ROOT} .gp-system-list span{{font-size:10px;color:#777}}
{ROOT} .gp-system-list h3{{font-size:19px}}
{ROOT} .gp-system-list p{{display:none;color:#929292;font-size:12px}}
@media (min-width:900px){{{ROOT} .gp-systems{{padding-top:72px;padding-bottom:72px}}{ROOT} .gp-systems-head{{grid-template-columns:1.3fr .7fr;gap:5vw;align-items:end;margin-bottom:42px}}{ROOT} .gp-system-list article{{grid-template-columns:62px 1fr 1fr;padding:18px 0}}{ROOT} .gp-system-list h3{{font-size:21px}}{ROOT} .gp-system-list p{{display:block}}}}
""",
    },
    {
        "name": "dealer-support",
        "label": "NIBBI dealer support",
        "html": f"""
<div class="gp-support gp-wrap" id="gp-support" aria-label="NIBBI dealer support">
  <div class="gp-support-visual"><img src="{ASSET}/paddock.webp" alt="NIBBI paddock technical support" loading="lazy" width="900" height="900"><div><span>Track</span><span>Workshop</span><span>Market</span></div></div>
  <div class="gp-support-copy"><p class="gp-kicker">03 / Dealer enablement</p><h2 class="gp-heading">Support that moves from launch to sell-through.</h2><ul><li><b>01</b><span><strong>Product onboarding</strong>Practical training for product selection, fitment and core NIBBI systems.</span></li><li><b>02</b><span><strong>Fitment &amp; tuning</strong>Guidance for installation, basic jetting and common product questions.</span></li><li><b>03</b><span><strong>Marketing toolkit</strong>Approved product, brand and campaign assets for local use.</span></li><li><b>04</b><span><strong>Warranty &amp; RMA</strong>A clear support path for product questions and after-sales cases.</span></li></ul></div>
</div>""",
        "css": f"""
{ROOT} .gp-support{{background:#f7f7f7;display:grid;grid-template-columns:1fr;gap:34px;padding-top:54px;padding-bottom:54px}}
{ROOT} .gp-support-visual{{position:relative}}
{ROOT} .gp-support-visual img{{width:100%;aspect-ratio:1.05;object-fit:cover}}
{ROOT} .gp-support-visual>div{{position:absolute;left:0;bottom:22px;display:flex;flex-direction:column;background:#f6ed3e;padding:14px 18px;font-size:9px;font-weight:800;letter-spacing:.16em;text-transform:uppercase}}
{ROOT} .gp-support-copy ul{{list-style:none;margin-top:34px;border-top:1px solid #d8d8d8}}
{ROOT} .gp-support-copy li{{display:flex;gap:18px;padding:16px 0;border-bottom:1px solid #d8d8d8;font-size:13px}}
{ROOT} .gp-support-copy li>b{{font-size:10px;color:#777}}
{ROOT} .gp-support-copy li span{{display:grid;grid-template-columns:1fr;gap:4px;color:#666}}
{ROOT} .gp-support-copy li strong{{color:#111;font-size:14px}}
@media (min-width:900px){{{ROOT} .gp-support{{grid-template-columns:.92fr 1.08fr;gap:5vw;align-items:center;padding-top:72px;padding-bottom:72px}}{ROOT} .gp-support-copy li span{{grid-template-columns:150px 1fr}}}}
""",
    },
    {
        "name": "partnership-process",
        "label": "NIBBI partnership process",
        "html": """
<div class="gp-process gp-wrap" id="gp-process" aria-label="NIBBI dealer partnership process">
  <p class="gp-kicker">04 / How it works</p><h2 class="gp-heading">From application<br>to long-term growth.</h2>
  <div class="gp-process-grid">
    <article><b>01</b><i></i><h3>Submit application</h3><p>Tell us about your business, market and sales channels.</p></article><article><b>02</b><i></i><h3>Qualification review</h3><p>We assess your business credentials and market capability.</p></article><article><b>03</b><i></i><h3>Partnership confirmation</h3><p>Confirm the partnership scope, requirements and next steps.</p></article><article><b>04</b><i></i><h3>Product consultation</h3><p>Identify the product range that best fits your customers and market.</p></article><article><b>05</b><i></i><h3>Receive quotation</h3><p>Receive dealer pricing and a quotation based on your selected products.</p></article><article><b>06</b><i></i><h3>Confirm order details</h3><p>Finalize quantities, payment terms, shipping and delivery information.</p></article><article><b>07</b><i></i><h3>Delivery</h3><p>Your order is prepared, shipped and tracked through delivery.</p></article><article><b>08</b><i></i><h3>After-sales support</h3><p>Access product guidance and support for after-sales cases.</p></article><article><b>09</b><i></i><h3>Long-term partnership</h3><p>Review performance, expand the range and grow the market together.</p></article>
  </div>
</div>""",
        "css": f"""
{ROOT} .gp-process{{background:#f7f7f7;padding-top:54px;padding-bottom:54px}}
{ROOT} .gp-process .gp-heading{{margin-bottom:30px}}
{ROOT} .gp-process-grid{{display:grid;grid-template-columns:1fr}}
{ROOT} .gp-process-grid article{{display:grid;grid-template-columns:34px 24px minmax(92px,120px) 1fr;gap:8px;align-items:center;border-bottom:1px solid #d8d8d8;padding:16px 0}}
{ROOT} .gp-process-grid b{{font-size:11px}}
{ROOT} .gp-process-grid i{{width:1px;height:38px;background:#a9a79f;position:relative}}
{ROOT} .gp-process-grid i::after{{content:'';width:9px;height:9px;border-radius:50%;background:#f6ed3e;position:absolute;left:-4px;top:0;border:1px solid #111}}
{ROOT} .gp-process-grid h3{{font-size:16px;line-height:1.25}}
{ROOT} .gp-process-grid p{{font-size:12px;line-height:1.5;color:#696963}}
@media (min-width:900px){{{ROOT} .gp-process{{padding-top:72px;padding-bottom:72px}}{ROOT} .gp-process .gp-heading{{margin-bottom:45px}}{ROOT} .gp-process-grid{{grid-template-columns:repeat(3,1fr);column-gap:32px;row-gap:46px}}{ROOT} .gp-process-grid article{{display:block;min-height:168px;padding:0 16px 0 0;border-bottom:0}}{ROOT} .gp-process-grid i{{display:block;width:auto;height:1px;margin:12px 0 20px}}{ROOT} .gp-process-grid i::after{{left:auto;right:0;top:-4px}}{ROOT} .gp-process-grid h3{{font-size:19px;margin-bottom:8px}}{ROOT} .gp-process-grid p{{font-size:13px;max-width:340px}}}}
""",
    },
    {
        "name": "partner-profile",
        "label": "NIBBI partner profile",
        "html": """
<div class="gp-fit gp-wrap" aria-label="Ideal NIBBI dealer profile"><div><p class="gp-kicker gp-kicker-yellow">05 / Partner profile</p><h2 class="gp-heading">Built for dealers who know the ride—and the market.</h2></div><div class="gp-fit-list"><p><span>01</span>Established motorcycle retailer, workshop, distributor or specialist e-commerce business</p><p><span>02</span>Strong knowledge of local riders, channels and product demand</p><p><span>03</span>Ability to represent NIBBI products and provide credible customer support</p><p><span>04</span>Commitment to responsible channels and long-term brand growth</p></div></div>""",
        "css": f"""
{ROOT} .gp-fit{{background:#121212;color:#fff;display:grid;grid-template-columns:1fr;gap:34px;padding-top:54px;padding-bottom:54px}}
{ROOT} .gp-fit-list{{border-top:1px solid #3d3e3f}}
{ROOT} .gp-fit-list p{{display:grid;grid-template-columns:42px 1fr;padding:16px 0;border-bottom:1px solid #3d3e3f;font-size:14px;line-height:1.5}}
{ROOT} .gp-fit-list span{{font-size:10px;color:#777}}
@media (min-width:900px){{{ROOT} .gp-fit{{grid-template-columns:1fr 1fr;gap:6vw;padding-top:72px;padding-bottom:72px}}}}
""",
    },
    {
        "name": "product-proof",
        "label": "NIBBI product capability",
        "html": f"""
<div class="gp-proof gp-wrap" aria-label="NIBBI product development and quality"><div><img src="{ASSET}/factory.webp" alt="NIBBI production and quality control" loading="lazy" width="1200" height="800"></div><div><p class="gp-kicker">06 / Built around the product</p><h2 class="gp-heading">Support grounded in real product knowledge.</h2><p class="gp-proof-copy">NIBBI combines product development, quality control and real-world riding feedback with practical materials that help partners explain, recommend and support the range.</p><div class="gp-proof-note"><b>Partner enablement</b><span>Product guidance, approved assets and an after-sales path designed to support confident selling.</span></div></div></div>""",
        "css": f"""
{ROOT} .gp-proof{{background:#f7f7f7;display:grid;grid-template-columns:1fr;gap:34px;align-items:center;padding-top:54px;padding-bottom:54px}}
{ROOT} .gp-proof img{{width:100%;min-height:300px;object-fit:cover}}
{ROOT} .gp-proof-copy{{color:#65655f;line-height:1.55;font-size:14px;margin-top:22px}}
{ROOT} .gp-proof-note{{border:1px dashed #aaa;padding:18px;margin-top:24px;display:flex;flex-direction:column;gap:10px}}
{ROOT} .gp-proof-note b{{font-size:11px;letter-spacing:.12em;text-transform:uppercase}}
{ROOT} .gp-proof-note span{{font-size:13px;color:#6a6a65}}
@media (min-width:900px){{{ROOT} .gp-proof{{grid-template-columns:1fr 1fr;gap:5vw;padding-top:72px;padding-bottom:72px}}{ROOT} .gp-proof img{{min-height:350px}}}}
""",
    },
    {
        "name": "dealer-application",
        "label": "NIBBI dealer application",
        "html": """
<div class="gp-apply gp-wrap" id="gp-apply" aria-label="NIBBI dealer application">
  <div><p class="gp-kicker">07 / Start the conversation</p><h2 class="gp-heading">Ready to build your market with NIBBI?</h2><p class="gp-apply-copy">Tell us about your business, market and sales channels. Qualified applicants will receive the program level, commercial discussion and onboarding path that best fit their capabilities.</p><div class="gp-next"><b>What happens next</b><span>Application review → Sales contact → Qualification call → Commercial discussion</span></div></div>
  <form class="gp-dealer-form"><div class="gp-fields"><label>Full name<input required placeholder="Your name"></label><label>Business email<input required type="email" placeholder="name@company.com"></label><label>Company name<input required placeholder="Company"></label><label>Business website / store URL<input required type="url" placeholder="https://"></label><label>Country / market<input required placeholder="Country or region"></label><label>Primary sales channel<select required><option value="" selected disabled>Select one</option><option>Physical retail store</option><option>Workshop / service center</option><option>Distributor / wholesaler</option><option>Online retail</option><option>Multi-channel</option></select></label><label>Years in business<select required><option value="" selected disabled>Select one</option><option>Less than 1 year</option><option>1–3 years</option><option>4–10 years</option><option>10+ years</option></select></label><label>Current NIBBI interest<select required><option value="" selected disabled>Select one</option><option>Authorized dealer</option><option>Workshop / installer</option><option>Regional distributor</option><option>Not sure yet</option></select></label></div><label>Tell us about your business<textarea required placeholder="Current brands, customer base, sales coverage and why NIBBI fits your market"></textarea></label><label class="gp-consent"><input type="checkbox" required> I agree that NIBBI may use this information to evaluate and contact me about a potential dealer relationship.</label><button class="gp-submit" type="submit">Submit application ↗</button><p class="gp-form-message" role="status" hidden>Prototype only — connect this form to GemPages, Shopify Forms or your CRM before publishing.</p></form>
</div>""",
        "css": f"""
{ROOT} .gp-apply{{background:#f6ed3e;display:grid;grid-template-columns:1fr;gap:34px;padding-top:54px;padding-bottom:54px}}
{ROOT} .gp-apply .gp-kicker{{color:#111}}
{ROOT} .gp-apply-copy{{line-height:1.55;margin-top:22px}}
{ROOT} .gp-next{{border-left:3px solid #111;padding-left:18px;margin-top:28px;display:flex;flex-direction:column;gap:8px;font-size:12px}}
{ROOT} .gp-next b{{text-transform:uppercase;letter-spacing:.1em}}
{ROOT} .gp-fields{{display:grid;grid-template-columns:1fr;gap:14px 20px}}
{ROOT} .gp-dealer-form label{{display:flex;flex-direction:column;gap:8px;font-size:10px;text-transform:uppercase;font-weight:700;letter-spacing:.08em}}
{ROOT} .gp-dealer-form input,{ROOT} .gp-dealer-form select,{ROOT} .gp-dealer-form textarea{{width:100%;border:0;border-bottom:1px solid #111;background:transparent;padding:10px 0;outline:none;font-size:14px;text-transform:none;font-weight:400;letter-spacing:0}}
{ROOT} .gp-dealer-form textarea{{height:82px;resize:vertical}}
{ROOT} .gp-dealer-form .gp-consent{{margin:16px 0;display:flex;flex-direction:row;align-items:flex-start;text-transform:none;font-weight:400;letter-spacing:0;line-height:1.45}}
{ROOT} .gp-consent input{{width:auto;margin-top:2px}}
{ROOT} .gp-submit{{width:100%;background:#111;color:#fff;border:0;border-radius:5px;padding:15px 18px;font-size:11px;font-weight:800;text-transform:uppercase;cursor:pointer}}
{ROOT} .gp-form-message{{font-size:12px;font-weight:700;margin-top:12px}}
@media (min-width:900px){{{ROOT} .gp-apply{{grid-template-columns:.82fr 1.18fr;gap:5vw;padding-top:72px;padding-bottom:72px}}{ROOT} .gp-fields{{grid-template-columns:1fr 1fr}}}}
""",
        "javascript": """(function(){var root=document.querySelector('.{{rootClassName}}');if(!root)return;var form=root.querySelector('.gp-dealer-form');var message=root.querySelector('.gp-form-message');if(!form||!message)return;form.addEventListener('submit',function(event){event.preventDefault();message.hidden=false;});})();""",
    },
    {
        "name": "faq",
        "label": "NIBBI dealer FAQ",
        "html": """
<div class="gp-faq gp-wrap" aria-label="NIBBI dealer frequently asked questions"><div><p class="gp-kicker">08 / FAQ</p><h2 class="gp-heading">Before you apply.</h2></div><div class="gp-faq-list"><details open><summary>What types of businesses can apply?<span>＋</span></summary><p>We welcome qualified motorcycle and powersports retailers, workshops, distributors and specialist e-commerce businesses that can represent and support NIBBI products.</p></details><details><summary>Will dealer pricing be shown publicly?<span>＋</span></summary><p>Approved partners receive program details and pricing after qualification. Commercial terms may vary by market, product range and partner type.</p></details><details><summary>Do you offer exclusive territories?<span>＋</span></summary><p>Territory opportunities are evaluated case by case based on market coverage, performance, inventory, service capability and a shared growth plan. Exclusivity is not automatic.</p></details><details><summary>What warranty and technical support is included?<span>＋</span></summary><p>Approved dealers receive product guidance and a structured path for technical questions, warranty requests and after-sales cases.</p></details><details><summary>Can I sell on third-party marketplaces?<span>＋</span></summary><p>Approved sales channels are confirmed during onboarding. Marketplace, cross-border and sub-distribution activity may require separate written approval.</p></details></div></div>""",
        "css": f"""
{ROOT} .gp-faq{{background:#f7f7f7;display:grid;grid-template-columns:1fr;gap:34px;padding-top:54px;padding-bottom:54px}}
{ROOT} .gp-faq-list{{border-top:1px solid #d8d8d8}}
{ROOT} details{{border-bottom:1px solid #d8d8d8;padding:17px 0}}
{ROOT} summary{{list-style:none;font-size:16px;font-weight:700;display:flex;justify-content:space-between;gap:20px;cursor:pointer}}
{ROOT} summary::-webkit-details-marker{{display:none}}
{ROOT} details p{{color:#62625d;line-height:1.6;max-width:650px;font-size:13px;margin-top:12px}}
@media (min-width:900px){{{ROOT} .gp-faq{{grid-template-columns:.72fr 1.28fr;gap:5vw;padding-top:72px;padding-bottom:72px}}}}
""",
    },
    {
        "name": "footer",
        "label": "NIBBI storefront footer",
        "html": """
<footer class="gp-footer" aria-label="NIBBI footer"><div class="gp-footer-grid"><div><h3>Contact Us</h3><p><strong>Address:</strong> 5901 Christie Ave Suite 406, Emeryville, CA 94608</p><p><strong>Email:</strong> <a href="mailto:customer@nibbiracing.com">customer@nibbiracing.com</a></p><p><strong>Phone:</strong> <a href="tel:+15102307223">+1 (510) 230-7223</a></p></div><div><h3>Customer Service</h3><ul><li><a href="https://nibbiracing.com/policies/privacy-policy">Privacy Policy</a></li><li><a href="https://nibbiracing.com/policies/terms-of-service">Terms of Service</a></li><li><a href="https://nibbiracing.com/policies/refund-policy">Refund Policy</a></li><li><a href="https://nibbiracing.com/pages/shipping-information">Shipping Information</a></li><li><a href="https://nibbiracing.com/a/tracking">Track Order</a></li></ul></div><div><h3>Support</h3><ul><li><a href="https://nibbiracing.com/pages/about-us">About Us</a></li><li><a href="https://nibbiracing.com/pages/contact-us">Contact Us</a></li><li><a href="https://nibbiracing.com/pages/manual">Carburetor Manual</a></li><li><a href="https://nibbiracing.com/pages/nibbi-rider-support-program">Ambassador Program</a></li><li><a href="https://nibbiracing.com/pages/tech-support">Tech Support</a></li></ul></div><div><h3>Subscribe to our newsletter</h3><form class="gp-newsletter"><label><span>Email</span><input type="email" placeholder="Email" required><button type="submit" aria-label="Submit email">→</button></label><label class="gp-newsletter-consent"><input type="checkbox" required>I agree to receiving marketing emails and special deals</label></form></div></div><div class="gp-footer-bottom"><p>© 2026 NIBBI RACING, All rights reserved.</p></div></footer>""",
        "css": f"""
{ROOT} .gp-footer{{background:#181818;color:#d9d9d9;padding:44px 6vw 22px;font-size:12px;line-height:1.6}}
{ROOT} .gp-footer-grid{{display:grid;grid-template-columns:1fr;gap:0}}
{ROOT} .gp-footer-grid>div{{padding:18px 0;border-bottom:1px solid #343434}}
{ROOT} .gp-footer h3{{color:#fff;font-size:14px;font-weight:600;margin-bottom:12px}}
{ROOT} .gp-footer p{{margin-bottom:7px}}
{ROOT} .gp-footer a{{color:#aaaeb6}}
{ROOT} .gp-footer ul{{list-style:none;columns:2}}
{ROOT} .gp-footer li{{margin-bottom:8px}}
{ROOT} .gp-newsletter>label:first-child{{display:grid;grid-template-columns:1fr 42px;border-bottom:1px solid #f6ed3e}}
{ROOT} .gp-newsletter>label:first-child span{{position:absolute;opacity:0}}
{ROOT} .gp-newsletter input[type=email]{{width:100%;border:0;background:transparent;color:#fff;padding:11px 0;outline:none}}
{ROOT} .gp-newsletter button{{border:0;background:transparent;color:#f6ed3e;font-size:20px;cursor:pointer}}
{ROOT} .gp-newsletter-consent{{display:flex;gap:9px;margin-top:16px;color:#aaaeb6;font-size:10px;line-height:1.45}}
{ROOT} .gp-footer-bottom{{border-top:1px solid #f6ed3e;margin-top:22px;padding-top:20px;color:#aaaeb6}}
@media (min-width:900px){{{ROOT} .gp-footer{{padding:56px 5vw 24px}}{ROOT} .gp-footer-grid{{grid-template-columns:1.05fr .8fr .8fr 1.15fr;gap:5vw}}{ROOT} .gp-footer-grid>div{{padding:0;border-bottom:0}}{ROOT} .gp-footer h3{{margin-bottom:22px}}{ROOT} .gp-footer ul{{columns:1}}{ROOT} .gp-footer-bottom{{margin-top:48px}}}}
""",
        "javascript": """(function(){var root=document.querySelector('.{{rootClassName}}');if(!root)return;var form=root.querySelector('.gp-newsletter');if(form)form.addEventListener('submit',function(event){event.preventDefault();});})();""",
    },
]

# The Shopify theme supplies the global header and footer.
SECTIONS = [section for section in SECTIONS if section["name"] not in {"navigation", "footer"}]


def uid(seed: int) -> str:
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    value = seed * 7919 + 104729
    chars = []
    while value:
        value, rem = divmod(value, len(alphabet))
        chars.append(alphabet[rem])
    return ("g" + "".join(reversed(chars))).ljust(10, "N")[:10]


def component(section: dict[str, str], index: int) -> str:
    html = " ".join(section["html"].split())
    css = scoped(section["css"])
    javascript = " ".join(section.get("javascript", "(function(){var root=document.querySelector('.{{rootClassName}}');if(!root)return;})();").split())
    tree = {
        "uid": uid(index * 3 + 1), "tag": "Section", "label": "Section",
        "settings": {"layout": {"desktop": {"cols": [12], "display": "fill"}}, "horizontalAlign": {"desktop": "start"}, "verticalAlign": {"desktop": "start"}, "lazy": False},
        "styles": {"verticalGutter": {"desktop": "0px"}, "background": {"desktop": {"type": "color", "color": "transparent", "image": {"src": "", "width": 0, "height": 0}, "size": "cover", "position": {"x": 50, "y": 50}, "repeat": "no-repeat", "attachment": "scroll"}}, "preloadBgImage": False, "width": {"desktop": "100%"}},
        "advanced": {"spacing-setting": {"edited": ["desktop"], "desktop": {"padding": {"top": "0px", "bottom": "0px"}, "link": False}, "tablet": {"padding": {"top": "0px", "bottom": "0px"}}, "mobile": {"padding": {"top": "0px", "bottom": "0px"}}}, "d": {"desktop": True, "tablet": True, "mobile": True}, "op": {"desktop": "100%"}},
        "childrens": [{
            "uid": uid(index * 3 + 2), "tag": "Col", "label": "Block", "settings": {}, "styles": {},
            "advanced": {"d": {"desktop": True, "tablet": True, "mobile": True}, "op": {"desktop": "100%"}},
            "childrens": [{
                "uid": uid(index * 3 + 3), "tag": "CSSCode", "label": "Custom Code", "customLabel": section["name"],
                "settings": {"editorData": {"customLabel": section["name"]}, "customLabel": section["name"], "background": {"desktop": {"type": "color", "color": "transparent", "image": {"src": "", "width": 0, "height": 0}, "size": "cover", "position": {"x": 50, "y": 50}, "repeat": "no-repeat", "attachment": "scroll"}}, "align": {"desktop": "left"}},
                "styles": {},
                "advanced": {"d": {"desktop": True, "tablet": True, "mobile": True}, "op": {"desktop": "100%"}, "spacing-setting": {"desktop": {"margin": {"bottom": 0}}}, "editorData": {"customLabel": section["name"], "rootClassName": "{{rootClassName}}", "html": html, "css": css, "javascript": javascript}}
            }]
        }]
    }
    return json.dumps(tree, ensure_ascii=False, separators=(",", ":"))


def build_page() -> dict:
    now = datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")
    page_sections = []
    positions = []
    for index, section in enumerate(SECTIONS, start=1):
        section_id = PAGE_ID + index
        comp = component(section, index)
        if len(comp.encode("utf-8")) >= 256 * 1024:
            raise ValueError(f"{section['name']} component exceeds 256 KB")
        positions.append(str(section_id))
        page_sections.append({
            "id": section_id, "createdAt": now, "updatedAt": now, "deletedAt": None,
            "shopId": 0, "themePageID": PAGE_ID, "cid": uid(index * 17),
            "name": f"Section {section['name']}"[:25], "display": True, "isGlobal": False,
            "isMobile": False, "appBlocks": "", "libraryPosition": None,
            "librarySectionID": None, "elementNames": "CSSCode",
            "globalStoreReleaseID": STORE_RELEASE_ID, "customFontIDs": None,
            "checksum": hashlib.sha256(comp.encode("utf-8")).hexdigest(),
            "layoutColumns": None, "layoutRows": None, "edges": {}, "component": comp,
        })
    meta_value = json.dumps({"showHeader": True, "showFooter": True}, separators=(",", ":"))
    return {
        "id": PAGE_ID, "isMobile": False, "splitPercentage": 0,
        "name": "NIBBI Become a Dealer V3", "type": "GP_STATIC",
        "description": "NIBBI Racing dealer partnership landing page",
        "handle": "become-a-dealer-v3", "sectionPosition": positions,
        "meta": [{"id": PAGE_ID + 100, "createdAt": now, "updatedAt": now, "deletedAt": None, "themePageID": PAGE_ID, "key": "global_layout", "value": meta_value, "edges": {}}],
        "pageSections": page_sections,
    }


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    page = build_page()
    output = OUT_DIR / "nibbi-become-a-dealer-v3.page.json"
    output.write_text(json.dumps(page, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    sizes = [len(section["component"].encode("utf-8")) for section in page["pageSections"]]
    print(f"Wrote {output}")
    print(f"Sections: {len(sizes)}; largest component: {max(sizes)} bytes")


if __name__ == "__main__":
    main()
