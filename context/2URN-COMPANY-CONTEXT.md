# 2URN Marketing — Company Context

Read this before anything else in the repo. It is the background a collaborator (human or AI) needs to write, edit or judge work for 2URN Marketing. The offer-specific detail lives in `offer-doc/` and `funnel/`; this file is about the company itself.

Last updated: Nov 17, 2026. Public repository: no financials, account identifiers or client contact data belong here.

## Who we are

2URN Marketing (say "to you right now") is a marketing agency for home-service contractors, based in Clarksville, Tennessee, serving the continental US. Core trades: roofing first, then HVAC and windows/doors. The entity is 2URN LLC.

We work inside a contractor's business, not outside it. Agencies that only send leads fail because the owner is on a roof, in an attic or at a measure when the lead arrives. 2URN fixes the ten feet between the CRM and the phone, and puts the owner's real face in every ad so homeowners recognize and trust a person, not a logo.

## What we sell

| Product | What it is | Price |
| --- | --- | --- |
| **Growth Partner** (fractional CMO retainer) | We structure and script the offers, the owner shoots, we edit, run the advertising, automate the follow-up, script and coach the setter, and report a weekly input scorecard. Client funds ad spend from $150/day. | $3,000/mo, 90-day minimum |
| **Content Package** | 45-minute interview with Camron, 5 ad scripts + 5 content scripts in the owner's words, they shoot, we edit 10 finished pieces. | $2,500/month |
| **Competitor Analysis** | Who the client's competitors are, what they are running, where the gaps are. | $1,500 |
| **Scripted ad campaigns** | 5 campaigns, 10 hooks + a full video script each, ready to shoot. | $1,250 for 5 |
| **Home Service Heroes** | Separate pay-per-lead brand run by the same team: exclusive roofing leads by ZIP/zone, sold per lead or as monthly recurring. Pay-per-lead rents demand; Growth Partner builds the asset. Sell both and let price sort the buyer. | Per lead / monthly |

Current acquisition play (winter 2026): the **Growth Partner Giveaway**, a judged contest that gives one contractor 90 days free and offers every other qualified applicant the Second-Place Stack. Full detail in `offer-doc/OFFER-DOC.md`.

## Who we sell to

Owner-operators of roofing, HVAC and window/door companies doing **$1M to $10M** a year in one metro. High ticket ($8K to $25K jobs), local, seasonal, burned by at least one agency, tired of the "are you a roofer doing a million a year" hook.

Must-haves: owner or lead rep willing to be on camera (no AI avatars, no stock footage); ad budget from $150/day; a team that can take appointments; someone on the phone within five minutes of a lead.

Not a fit: under $1M, owner is the only closer, storm chasers with no fixed metro, repair-only HVAC shops, anyone who wants to frame a discount as an insurance deductible.

## How we think about marketing

- **Recognition plus follow-up** beats clever ads. Homeowners go with whoever they recognize and whoever picks up first.
- **Inputs, not revenue.** Owners who only watch revenue cannot see which part is broken. We report leads, cost per lead, set rate, show rate, close rate, average ticket every week.
- **Setter before launch, launch before evergreen.** There is always someone to call the leads the day they arrive.
- **Giveaways as the launch mechanic.** Free Roof / Free System / Free Windows giveaway: 7-day countdown, one first prize, many second prizes with a 72-hour claim, then phones. Modeled on Alex Hormozi's Boulder Adventure Park play (transcript in `research/`).
- **Belief-first copy.** Every piece of copy names the belief it has to install (outcome, identity, problem, solution, product, credibility). Agree with the prospect's cynicism, then reframe the hidden lock.
- **Call-out standard.** Ads open by naming the viewer (trade, market, situation) in the first line.

## Voice and tone

Plain, direct, a little blunt. Short sentences. Numbers said out loud. Agree with the skeptic before you pitch. Fun is allowed in hooks and closes (winter, Christmas, owner-on-the-roof bits); the qualification block is always dead serious.

Never say: "random," "drawing," "odds," "guaranteed results," "everyone wins," any client revenue number we cannot screenshot, anything about list size. Never frame a discount as covering an insurance deductible.

## Brand

- Ink `#0B0B0C`, ink-2 `#16161A`
- Paper `#FFFFFF`, `#F7F6F3`, `#EFEDE8`
- Muted `#6E6E75`, `#93939B`
- Red `#FF2D2D`, red-deep `#D91B1B` (one accent, used sparingly)
- Green `#12A45C` (success states only)
- Type: Archivo 400 to 900. Headlines 900 weight, tight letter-spacing.
- Radius 16px. Text wordmark "2URN", no logo mark.
- Dark hero / light body is the default page rhythm.

## Team

| Person | Role |
| --- | --- |
| Camron Johnson | Founder, lead strategist, on-camera face of 2URN, runs fit interviews |
| Zoe | Sales and interviews, ad production with Camron |
| Angela | Client success manager: GoHighLevel builds, sequences, setter hiring and coaching, scorecards |
| Shabi | Video editor |
| Tumi | Lead ops / data (Home Service Heroes) |
| Josh Johnston | Outside coach (Hydra); shaped the giveaway on the Nov 13, 2026 call |

## Stack

- **GoHighLevel (GHL)** for every client CRM, funnel page, form, workflow, calendar and SMS/email sequence. Pages are built as Custom Code paste files (see `funnel/`).
- **Meta Ads** as the primary paid channel. Pixel + CAPI, learning-phase budgets respected.
- **Vercel** for proposal and landing sites.
- **Fathom** for call recording; call notes are synced into GHL contacts.
- **2URN Creative Engine** (internal app) produces 5-campaign ad packages: 10 hooks + full script per campaign.
- Video: owner-shot footage, edited by 2URN. Eye-matched cuts, no pauses, captions in the Meta safe area off the face.

## Delivery standards

- Lead called in under 5 minutes, 7 touches in 72 hours, every outcome logged by stage.
- Weekly scorecard call with the owner.
- Everything we build lives in the client's own accounts (GHL, domain, ad account).
- Capacity: five Growth Partner seats per trade per quarter, one per metro. A seat opens when a client's setter holds a 25% set rate without us on the call.

## Compliance habits

Giveaways are run as judged contests (winner chosen by 2URN against published criteria), with NO PURCHASE NECESSARY and a free alternate entry. Official rules go through an attorney. State registration thresholds (NY, FL) are checked per launch. We do not advise on insurance claims and never tie a discount to a deductible.

## Working with this repo

Edit any file and open a pull request, or commit to `main` if you have access. Keep public copy consistent with the rule that second place is described as "second place," never "everyone wins." `[CHECK]` marks open items awaiting a human decision.
