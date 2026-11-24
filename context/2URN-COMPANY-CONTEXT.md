# 2URN Marketing — Company Context

Read this before anything else in the repo. It is the background a collaborator (human or AI) needs to write, edit or judge work for 2URN Marketing. The offer-specific detail lives in `offer-doc/` and `funnel/`; this file is about the company itself.

Last updated: Nov 24, 2026. Public repository: no financials, account identifiers or client contact data belong here.

## Who we are

2URN Marketing (say "to you right now") is a marketing agency for home-service contractors, based in Clarksville, Tennessee, serving the continental US. Our core trade is roofing. We also serve HVAC and windows/doors contractors. The entity is 2URN LLC.

We work inside a contractor's business, not outside it. Agencies that only send leads fail because the owner is on a roof, in an attic or at a measure when the lead arrives. 2URN fixes the ten feet between the CRM and the phone, and puts the owner's real face in every ad so homeowners recognize and trust a person, not a logo.

## What we sell

| Product | What it is | Price |
| --- | --- | --- |
| **Growth Partner** (fractional CMO retainer) | We structure and script the offers, the owner shoots, we edit, run the advertising, automate the follow-up, script and coach the setter, and report a weekly input scorecard. Client funds ad spend of $200 to $1,000 a day, paid to Meta. | $3,000/mo, 90-day minimum |
| **One-Month Content Package** | 45-minute interview with Camron, 5 ad scripts + 5 content scripts in the owner's words, they shoot, we edit 10 finished pieces. | $2,500 |
| **Competitor Analysis** | Who the client's competitors are, what they are running, where the gaps are. | $1,500 |
| **Scripted ad campaigns** | 5 campaigns, 10 hooks + a full video script each, ready to shoot. | $1,250 for 5 |
| **Website buildout, with hosting and maintenance** | 2URN builds the company's website and hosts and maintains it. Free build for giveaway winners (second place if they need one, third place). | $189/mo hosting and maintenance; standard build price `[DECIDE: standard build price]` |
| **Marketing audit** | Your website, your Google Business Profile, your ads and your follow-up, with what to fix first `[DECIDE: confirm audit scope]`. | Free in the giveaway (third place); standard price `[DECIDE: standard audit price]` |
| **Home Service Heroes** | Separate pay-per-lead brand run by the same team: exclusive roofing leads by ZIP/zone, sold per lead or as monthly recurring. Pay-per-lead rents demand; Growth Partner builds the asset. Sell both and let price sort the buyer. | Per lead / monthly |

Current acquisition play (winter 2026): the **Growth Partner Giveaway**, three prize levels: one grand prize (90 days of Growth Partner, free), three second places (the Second-Place Stack) and five third places (a free audit and website), all picked by our panel on Dec 5. Full detail in `offer-doc/OFFER-DOC.md`.

## Who we sell to

Owner-operators of roofing companies. The sweet spot is **$1M to $10M** a year in one metro, with no revenue minimum to enter the giveaway. High ticket ($12K to $25K jobs), local, seasonal, burned by at least one agency, tired of the "are you a roofer doing a million a year" hook.

Must-haves: owner or lead rep willing to be on camera (no AI avatars, no stock footage); ad budget of $200 to $1,000 a day ($100 a day is enough for second place in the giveaway); someone on the phone within five minutes of a lead.

Weak fits (sales notes, not the `not-a-fit` tag): owner is the only closer, storm chasers with no fixed metro, nobody on the phone, anyone who wants to frame a discount as an insurance deductible. The `not-a-fit` tag means only: will not be on camera, or cannot fund $100 a day in ad spend.

## How we think about marketing

- **Recognition plus follow-up** beats clever ads. Homeowners go with whoever they recognize and whoever picks up first.
- **Inputs, not revenue.** Owners who only watch revenue cannot see which part is broken. We report leads, cost per lead, set rate, show rate, close rate, average ticket every week.
- **Setter before launch, launch before evergreen.** There is always someone to call the leads the day they arrive.
- **Giveaways as the launch mechanic.** Free Roof Giveaway: 7-day countdown, one first prize, many second prizes with a 72-hour claim, then phones. Modeled on Alex Hormozi's Boulder Adventure Park play (transcript in `research/`).
- **Belief-first copy.** Every piece of copy names the belief it has to install (outcome, identity, problem, solution, product, credibility). Agree with the prospect's cynicism, then reframe the hidden lock.
- **Call-out standard.** Ads open by naming the viewer (roofing, market, situation) in the first line.

## Voice and tone

Plain, direct, a little blunt. Short sentences. Numbers said out loud. Agree with the skeptic before you pitch. Fun is allowed in hooks and closes (winter, Christmas, owner-on-the-roof bits); the qualification block is always dead serious.

Never say: "guaranteed results," any client revenue number we cannot screenshot; anything about list size. The counts are public: one grand prize, three second places, five third places. Still never say "everyone wins", "everybody gets", "all applicants" or that missing one place gets you another. Never describe any prize as random, a drawing or as having odds. Our panel picks all three places on Dec 5, and nobody wins before then. The only guarantee wording is the revenue ROI guarantee. Never frame a discount as covering an insurance deductible. No em dashes or en dashes in customer-facing copy.

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
- Capacity: five Growth Partner seats per quarter, one per metro. A seat opens when a client's setter holds a 25% set rate without us on the call.

## Compliance habits

All three prizes are picked by 2URN's panel on Dec 5, 2026, and nobody wins before then. There is no random drawing and no chance-based tier. Second-place winners fund ad spend of $100 to $1,000 a day; the grand prize and the standard program stay at $200 to $1,000. The grand prize is chosen against six published criteria; second place (3 winners) is the three highest-scoring applicants on the same ranked scorecard list who completed the interview by the cutoff and meet its two minimum requirements, after removing the grand-prize winner and a referrer who shares the grand prize `[DECIDE: whether the revenue ROI guarantee covers second-place clients who fund $100 to $199 a day, or only those who fund $200 a day or more]`; five third places are picked from the remaining eligible entrants `[DECIDE: on what basis the panel picks the five third-place winners]`. NO PURCHASE NECESSARY and a free alternate entry stay on every page. Official rules go through an attorney, who has questions to settle `[CHECK]`: whether this is a judged contest in every state where it runs, whether stating the numbers (1, 3, 5) in the rules is sufficient, whether New York and Florida registration and bonding for games of chance do not apply now that no tier is chance-based, whether any state's rules for skill contests require disclosures or filings for prizes of this value, and changing rules after entries open. Legal text and customer-facing copy both state the counts: one grand prize, three second prizes, five third prizes.

Nominated roofers have given no consent. They get one manual call from the setter, and a voicemail naming the referrer if there is no answer, then nothing. No automated texts, no automated emails, no auto-dialer. If they say no, they are tagged and never contacted again. A nomination is not an entry and never changes judging. Once the nominated company enters itself, the nomination counts as a referral: if that company wins the grand prize, the nominator wins it too.

We do not advise on insurance claims and never tie a discount to a deductible.

## Working with this repo

Edit any file and open a pull request, or commit to `main` if you have access. Keep public copy consistent with the copy rules above: second place is "second place", our panel picks all three places on Dec 5, nobody wins before then, and copy states the counts (one grand prize, three second places, five third places). `[DECIDE: ...]` marks a business decision only Camron can make, and `[CHECK: ...]` marks an item awaiting the attorney. Search for both before you finish any edit, and never replace one with a guess.
