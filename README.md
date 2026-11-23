# 2URN Growth Partner Giveaway — Offer Kit

Internal working repository for 2URN Marketing's winter acquisition offer: a giveaway with a judged grand prize, a randomly drawn second place and a third place, that sells the **Growth Partner** retainer to roofing contractors. The kit is made of GoHighLevel (GHL) paste files and markdown docs.

**Status (Nov 23, 2026):** roofing only. Winners are announced Dec 5, 2026. Three prizes. Nothing is live in GHL yet. The official rules are a draft awaiting attorney review, and the Nov 23 change to a random drawing for second place adds new legal questions (see the attorney list under Open decisions). The VSL script is v3; any cut shot on Nov 17 predates these terms and needs checking against them before it runs.

## The offer in one paragraph
Growth Partner is $3,000 a month, 90-day minimum. 2URN structures and scripts the offers, the owner or a lead rep shoots on a phone (real face, no AI avatars), 2URN edits, runs the advertising, automates the follow-up, scripts and coaches the setter and reports a weekly scorecard. The client funds ad spend of $200 to $1,000 a day, paid directly to Meta. The giveaway has three prizes. The **grand prize** is 90 days of Growth Partner, free ($10,000 value); it is judged, chosen by 2URN's panel after a 20-minute interview against six published criteria, and the referrer wins it too if the winner was referred by an eligible entrant in a different market (through that entrant's referral link, or nominated by them on the thank-you form before entering). **Second place** is the Second-Place Stack and is drawn at random from eligible applicants: a One-Month Content Package ($2,500), a Competitor Analysis ($1,500), Five Advertising Campaigns, scripted ($1,250) and a Website Buildout if the winner has no website, all included free with second place (the Competitor Analysis when they book the claim call, the rest delivered inside the 90-day program), plus 50% off the 90-day program ($1,500 a month instead of $3,000, a $4,500 saving), with a revenue ROI guarantee. That is $5,250 in deliverables plus a website if you need one, free, plus $4,500 off. **Third place** is a free marketing audit and a website built for the company: no build fee, hosting and maintenance $189 a month. Second and third place have 72 hours from notification to claim by booking a 20-minute claim call. Winners are notified Saturday, Dec 5, 2026 at 7:00 PM CT; the public announcement goes up only after the grand prize winner signs the publicity and case-study release. After day 90 the grand prize winner may continue at $3,000 a month. No obligation. There is no revenue minimum to enter.

## Folders
| Path | What it is |
|---|---|
| `context/2URN-COMPANY-CONTEXT.md` | Start here. Who 2URN Marketing is, what we sell, who we sell to, voice, brand, team, stack, delivery standards. |
| `offer-doc/OFFER-DOC.md` | The offer document: decisions, offer on one page, fit for roofers, deliverables, pricing, unit economics, sales process, team, compliance, scorecard, setup checklist dated back from Dec 5. It mirrors the live Claude doc. |
| `offer-write-up.html` | Standalone page: breakdown of the Hormozi theme-park giveaway the offer is modeled on, how 2URN mirrors it, plus a per-client ROI calculator. Open in a browser. |
| `funnel/01-giveaway-ghl.html` | Giveaway landing page at `/lead-engine`. GHL Custom Code paste file. First screen, no scrolling: headline, VSL and the apply form (on phones the form opens with first name and mobile, then shows the other four fields). Below it, a "What you can win" band with the three prize cards, the commitments and the countdown. `window.GHL_CONFIG` at the top holds form id, webhook, announcement date. |
| `funnel/02-thankyou-ghl.html` | Thank-you page at `/thank-you`. Referral link to the referral page, plus the nominate-a-roofer form. |
| `funnel/03-claim-ghl.html` | Second-place claim page at `/claim`: 72-hour timer and booking for the 20-minute claim call. |
| `funnel/04-referral-ghl.html` | Referral landing page at `/refer`. With a valid `ref` code in the link it shows "[Name] nominated you" and the referrer's code carried in from the link; without one it is a plain entry page. Same first screen (headline, VSL, apply form) and the same six-field form as 01. |
| `funnel/05-claim-third-ghl.html` | Third-place claim page at `/claim-third`: 72-hour timer and booking for the Free Audit + Website Call. |
| `funnel/VSL-script.md` | Camron's VSL script (v3) with 15/30/60 ad cuts and hook variants. |
| `funnel/sequence-email-sms.md` | Email and SMS sequence: entry through announcement, second place, third place, claim reminders, evergreen. |
| `funnel/setter-script.md` | Appointment-setter script: book the interview, interview questions, deliver second place and third place, and the one manual call to a nominated roofer. |
| `funnel/official-rules-DRAFT.md` | Hybrid rules draft: judged grand prize, random drawing for second place. **Attorney review required.** `[CHECK]` marks open items. |
| `funnel/GHL-SETUP.md` | Step-by-step GHL setup: five pages, two forms (entry and nomination), workflows A to H, custom fields, calendars, announcement-day runbook. |
| `funnel/email-to-josh.md` | Draft update to Josh (Hydra) with the three questions for him. |
| `tools/make-previews.py` | Builds preview copies of pages 02 to 05 with sample link data (a preview host passes no query string, so the real files would show their empty states). Never changes the files in `funnel/`. |
| `research/` | Timestamped transcript of the Hormozi "Can I Save This Failing Theme Park in 90 Days?" video. |
| `shelved-valor-pilot/` | A client-side Free Roof Giveaway kit built for Valor Roofing on Nov 12, then shelved. Kept for reference only; not part of the current plan. |

## Brand
Black `#0B0B0C`, white and warm paper `#F7F6F3` / `#EFEDE8`, one red accent `#FF2D2D`, Archivo at 900 weight with tight tracking, 16px radii, "2URN" text wordmark. Highlighted words in a headline are white on a solid red background, never red text.

## Open decisions
Search the repo for `[DECIDE: ...]` (a call only Camron can make) and `[CHECK: ...]` (needs the attorney) to find every spot these touch.
- `[DECIDE]` How many second-place winners to draw, and the drawing pool. Working default: applicants who completed the interview by the cutoff and met the on-camera and ad-budget minimums, excluding the grand-prize winner and any shared-prize referrer.
- `[DECIDE]` Who receives third place, and whether it is capped. Working default: every other eligible entrant.
- `[DECIDE]` Third-place and website terms: hosting term, cancellation, site and domain ownership, build timeline, and the value of the website. Also who runs the audit call and the audit scope.
- `[DECIDE]` Second-place Website Buildout: value, timeline, and whether hosting is included during the engagement or billed at $189 a month.
- `[DECIDE]` The kill line for the $200/day ad test, a day-7 check with three conditions (proposed: stop if cost per application is over $25 at day 7, if fewer than 10 interviews are held by day 7, or if there is no second-place claim by day 10 after the announcement). For scale: $2,800 over 250 applications is about $11 each.
- `[DECIDE]` Launch date. Today is Nov 23 and nothing is live; with the announcement fixed at Dec 5 a 14-day test cannot finish first. A launch on Nov 26 gives a 10-day run; keep Dec 5 with a shorter test or move the announcement.
- `[DECIDE]` VSL reshoot date for the v3 terms.
- `[CHECK]` Attorney list:
  - The random-drawing tier: whether the interview can be a condition of the drawing, New York and Florida registration and bonding for prizes over $5,000 (normally filed before the promotion starts), the odds and prize-count statements, and changing the rules after entries have opened.
  - The revenue ROI guarantee wording and how "paid for itself in closed jobs" is measured.
  - Whether "free" is the right word for stack items delivered inside the discounted engagement.
  - A prize that carries a recurring fee (third place, $189 a month hosting).
  - Calling nominated roofers (one manual call, no automated messages) and the consent position behind it.
  - The interview cutoff (proposed Dec 5, 2026, 5:00 PM CT) and the judging criteria weights.
  - The grand prize ARV: stated as $10,000, while 90 days at $3,000 a month is $9,000. State what the additional $1,000 represents or use $9,000.
  - The deadline for a second-place winner to sign the engagement agreement (the Content Package, campaigns and website depend on signing).
