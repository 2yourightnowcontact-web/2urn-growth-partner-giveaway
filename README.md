# 2URN Growth Partner Giveaway — Offer Kit

Internal working repository for 2URN Marketing's winter acquisition offer: a judged giveaway that sells the **Growth Partner** fractional-CMO retainer to roofing contractors.

**Status (Nov 23, 2026):** offer is roofing only, decided by Camron on Nov 23, 2026. Offer structure locked by Camron, Zoe and Josh Johnston (Hydra). Nothing is live in GoHighLevel yet. Official rules are a draft awaiting attorney review. VSL shoot scheduled Nov 17; winner announced Dec 4, 2026.

## The offer in one paragraph
Growth Partner is $3,000/month, 90-day minimum. 2URN comes into the business, structures and scripts the offers, the owner shoots the ads (real face, no AI avatars), 2URN edits, runs the advertising and automates the follow-up. The client funds ad spend from $150/day. The giveaway: **first place** wins 90 days free ($10,000 value; the referrer wins too). **Second place** is the Second-Place Stack: 90 days at 50% off plus, free, a one-month Content Package ($2,500), a Competitor Analysis ($1,500) and five scripted ad campaigns ($1,250), with an ROI guarantee tied to the winner's commitment list. Publicly the copy says "second place" only; internally every qualified applicant who is not the winner receives it. Winner is chosen by 2URN after a 20-minute interview with every applicant, against six published criteria.

## Folders
| Path | What it is |
|---|---|
| `context/2URN-COMPANY-CONTEXT.md` | Start here. Who 2URN Marketing is, what we sell, who we sell to, voice, brand, team, stack, delivery standards. |
| `offer-doc/OFFER-DOC.md` | The offer document: decisions from the Nov 13 call, offer on one page, fit for roofers, deliverables, pricing, unit economics, sales process, team, compliance, scorecard, 30-day checklist. Exported from the live Claude doc; the 90-day roadmap diagram did not export. |
| `offer-write-up.html` | Standalone page: breakdown of the Hormozi theme-park giveaway the offer is modeled on, plus a per-client ROI calculator. Open in a browser. |
| `funnel/01-giveaway-ghl.html` | Giveaway landing page. GoHighLevel Custom Code paste file. Six-field form, countdown, VSL slot. `window.GHL_CONFIG` at the top holds form id, webhook, announcement date. |
| `funnel/02-thankyou-ghl.html` | Thank-you page with the referral loop. |
| `funnel/03-claim-ghl.html` | Second-place claim page with the 72-hour timer and interview booking. |
| `funnel/VSL-script.md` | Camron's VSL script with 15/30/60 ad cuts and hook variants. |
| `funnel/sequence-email-sms.md` | Email and SMS sequence: entry through announcement, second place, claim reminders, evergreen. |
| `funnel/setter-script.md` | Appointment-setter script: book the interview, interview questions, deliver second place. |
| `funnel/official-rules-DRAFT.md` | Judged-contest rules draft. **Attorney review required.** `[CHECK]` marks open items. |
| `funnel/GHL-SETUP.md` | Step-by-step GoHighLevel setup: pages, form, fields, workflows, calendar, announcement-day runbook. |
| `funnel/email-to-josh.md` | Draft email to Josh (Hydra) with questions for him. |
| `research/` | Timestamped transcript of the Hormozi "Can I Save This Failing Theme Park in 90 Days?" video. |
| `shelved-valor-pilot/` | A client-side Free Roof Giveaway kit built for Valor Roofing on Nov 12, then shelved. Kept for reference only; not part of the current plan. |

## Brand
Black `#0B0B0C`, white and warm paper `#F7F6F3` / `#EFEDE8`, one red accent `#FF2D2D`, Archivo at 900 weight with tight tracking, 16px radii, "2URN" text wordmark.

## Open decisions
- Whether second place is capped or open to every qualified applicant.
- Kill line for the 14-day, $200/day test (proposed: stop at day 7 if cost per application is over $25 or fewer than 10 interviews are held).
- Attorney: judged-contest wording, the ROI guarantee, and whether "free" is the right word for stack items delivered inside the discounted engagement.
