# Giveaway Email + SMS Sequence

Sender: Camron (email) / 2URN (SMS). All sends come from the GHL workflows (A "Giveaway Entry", B "Second Place", C "Grand Prize", G "Third Place", see GHL-SETUP.md). Merge fields used: `{{contact.first_name}}`, `{{contact.referral_link}}`, `{{contact.interview_link}}`, `{{contact.claim_link}}`, `{{contact.claim3_link}}`, `{{contact.claim_deadline}}`. They are GHL standard and custom fields (see GHL-SETUP.md). `{{contact.interview_link}}` opens the booking page, `https://2urnagency.com/interview?c={{contact.referral_code}}` (the code only: no name, email or phone in the link). Entries close and winners are notified Dec 11, 2026, 7:00 PM CT; change every mention if GHL_CONFIG.announcementAt changes. The public announcement (video, banner, socials) is posted only after the grand prize winner has accepted and signed the publicity and case-study release.

The program is 2URN Growth Partner: $3,000 per month, 90-day minimum, client funds ad spend ($200 to $1,000 a day, paid to Meta). There are three prizes.

- **Grand prize** (one winner, plus the referrer): 90 days of Growth Partner, free ($10,000 value). Picked by our panel on Dec 11, judged after a 20-minute interview. People choose, not chance.
- **Second place: the Second-Place Stack.** Picked by our panel on Dec 11, from applicants who completed the interview, on the same published criteria. Included free with second place (claimed by booking the 20-minute claim call on /claim-second within 72 hours of notification; nothing else is required to claim): a one-month Content Package ($2,500 value: a 45-minute interview with Camron; we write 5 ad scripts and 5 content scripts in their words; they shoot on a phone with our shot list; we edit 10 finished pieces), a Competitor Analysis ($1,500 value: who their current competitors are, what they are running, their offers, hooks, review counts and the gaps), five advertising campaigns scripted for them ($1,250 value: each with 10 hooks and a full video script, ready to shoot; not edited ads, not loaded audiences) and, if they do not have a website, a Website Buildout (free, no dollar value assigned). Plus 50% off the first 90 days of Growth Partner ($1,500 per month instead of $3,000, a $4,500 saving), then $3,000, with the revenue ROI guarantee. Second-place winners fund ad spend of $100 to $1,000 a day. Headline math, used everywhere: "$5,250 in deliverables, free, plus $4,500 off: $9,750 of value." With the website in the same sentence: "$5,250 in deliverables plus a website if you need one, free, plus $4,500 off". Never put a dollar figure on the website. Delivery: the Competitor Analysis within 7 days of booking the claim call (whether or not they sign); the Content Package, the five scripted campaigns and the Website Buildout inside the 90-day program, conditioned on signing the Growth Partner agreement [CHECK: signing deadline]. [DECIDE: website timeline, and whether hosting is included during the engagement or billed at $189/month]
- **Third place: Free Audit + Website Buildout.** Picked by our panel on Dec 11. A marketing audit and a website built for the company. No build fee. The winner pays hosting and maintenance only, $189 a month. 72 hours to claim by booking a 20-minute call. Every third-place email carries "Hosting and maintenance terms are in your agreement." Every third-place SMS puts the fee next to the build ("No build fee. Hosting and maintenance $189/mo") and links to /claim-third, which carries the terms line. [DECIDE: confirm audit scope] [DECIDE: hosting term, cancellation, site and domain ownership, build timeline, ARV]

The guarantee, worded the same everywhere: "If you do these four things (content shot within 14 days, ad spend funded from $200/day, the follow-up sequence live, weekly scorecard call) and Growth Partner has not paid for itself in closed jobs by day 90, we keep working for free until it has." A second-place client who funds $100 to $199 a day does not meet condition two, so any message that gives second place's ad spend next to the guarantee adds: "The guarantee applies at $200 a day or more." The four items are "the guarantee's four conditions". Never call them "the commitment list"; the five public items are "what the winner commits to". The public name is "revenue ROI guarantee". [CHECK: performance guarantee wording, and how "paid for itself in closed jobs" is measured; see official-rules-DRAFT.md]

Public wording:
- No prize is ever described as drawn, random, picked by chance or as having odds. Our panel picks all three places on Dec 11.
- Nobody wins before Dec 11. No message sent before the Dec 11 notification tells a reader they have won, will win or are in line for a prize.
- The counts are public: one grand prize, three second places, five third places. Still never say "everyone wins", "everybody gets", "all applicants" or that missing one place gets you another.
- Nothing tells a reader that people who do not win a higher tier get a lower one.
- Winner-facing copy never says "book your interview". It says "book your 20-minute call" or "book your claim call". The claim call is never called "not a sales call" and a winner is never told they might be judged not a fit. The pre-announcement interview is still "an interview, not a sales call".
- The referral bonus is always stated as: a roofer in another market, and "if they win the grand prize, you win it too". The one allowed follow-on, only if the message needs it: "You both get 90 days of Growth Partner free." Say "grand prize", never "first place".
- Never offer extra entries.
- No em dashes or en dashes. No exclamation marks.

Who gets this: every entrant. Most entrants book their interview on the booking page (`/interview`) right after the form, so every message with a booking line has a booked variant without it (workflow A If/Else on the tag `interview-booked`). There is no form-level disqualification and no revenue minimum. A contact tagged `not-a-fit` after the setter call or interview (not a fit for Growth Partner: will not be on camera, or cannot fund $100 a day in ad spend) stops getting the interview reminders and is out of the grand prize and second place, but stays eligible for third place and gets the third-place messages if they are tagged `third-place` (see GHL-SETUP.md, workflows E and G). A not-a-fit contact is not put on Do Not Disturb.

Rules: one SMS a day at most per contact, counting workflow texts and setter texts together. The first SMS ends with "Reply STOP to opt out" (first send only; GHL appends after that). Keep every SMS as short as it can be, under 160 characters where possible, and keep "2URN:" as the prefix. Never offer extra entries.

Timing: the Day 1 to Day 5 sends go out relative to the entry date and carry no countdowns; they say "Winners are picked Dec 11." Two sends are pinned to dates: the day-before message (Dec 10, 10:00 AM CT) and the announcement-morning message (Dec 11, 10:00 AM CT). A contact who entered that same day skips the pinned send. If a relative SMS and a pinned SMS fall on the same day, send only the pinned one: so anyone entering on or after Dec 9 gets the entry message and the pinned sends still ahead of them, and no "Book your interview" SMS (the entry email and the Dec 10 email both carry the interview link). A pinned send is skipped only for a contact who entered on or after that day. Nothing from this sequence goes out after Dec 11, 7:00 PM CT, when entries close.

---

## On entry (email at once, SMS 10 minutes later)

Workflow A picks one SMS with an If/Else on the tag `interview-booked`, 5 minutes after entry (Camron, Nov 25), so a person still on the booking page has time to book.

**SMS rules added Nov 25 (after a compliance, timing and build review).** They apply to every SMS in the entry sequence below (entry, +1 day, Day 2, Day 3, Day 4):
- No first name in any text. Workflow A matches an existing contact by phone or email, so the stored first name can be stale or empty, and a wrong name reads as a wrong-number text.
- The links are written out with the referral code (`{{contact.referral_code}}`), so the `referral_link` and `interview_link` fields are not needed for these texts.
- Texts go out only 10:00 AM to 6:45 PM Central, Monday to Saturday (8 AM Pacific to 7:45 PM Eastern; no Sunday texts). A text due outside that window waits for it. Alaska and Hawaii numbers are not texted automatically; Camron gets a notification instead.
- No text to a mail-in entrant, to a contact with no consent text or no referral code, or after entries close. From Dec 10 only the two pinned texts go out.
- Reworded Nov 25 on Camron's notes: the entry text goes 5 minutes after entry (was 10); the next-day text says the grand prize and second place are picked only from roofers who do the interview; the Day 2 text is the "digital door knocking" idea with the booking link (it goes to everyone, so the booking line is a question); the Day 3 text says a one-on-one interview is required to be considered for the grand prize or second place. Camron's notes said "added to the drawing"; the texts say "our panel picks" instead, because the giveaway is judged and the kit never calls it a drawing.
- The texts are built in their own workflow, `Giveaway A3: Entry texts (SMS)`, triggered by the tag `giveaway-entrant` being added, so the intake workflow A is not touched. A reply from the contact ends the sequence for them.
- Nov 25, 2026: win date moved from Dec 5 to Dec 11 (Camron).

**SMS, booked** (tag `interview-booked`)
> 2URN: You're entered and your 20-min interview is booked. Refer a roofer in another market. If they win the grand prize, you win it too: https://2urnagency.com/refer?ref={{contact.referral_code}} Reply STOP to opt out

**SMS, not booked**
> 2URN: You're entered in the Growth Partner giveaway. Pick your 20-min interview time: https://2urnagency.com/interview?c={{contact.referral_code}} Reply STOP to opt out

**Email.** Subject: You're entered. Here's what happens next.
> {{contact.first_name}},
>
> You're entered. There are three prizes. The grand prize (1 winner) is 2URN Growth Partner free for 90 days, a $10,000 value. Second place (3 winners) is the Second-Place Stack: $5,250 in deliverables plus a website if you need one, free, plus $4,500 off your first 90 days of Growth Partner ($1,500 a month instead of $3,000). That's $9,750 of value, and the program comes with a revenue ROI guarantee: if you do these four things (content shot within 14 days, ad spend funded from $200/day, the follow-up sequence live, weekly scorecard call) and Growth Partner has not paid for itself in closed jobs by day 90, we keep working for free until it has. For second place you fund your own ad spend, $100 to $1,000 a day, paid to Meta. The guarantee applies at $200 a day or more. Third place (5 winners) is a marketing audit and a website built for your company. No build fee. Hosting and maintenance is $189 a month. Hosting and maintenance terms are in your agreement.
>
> Here's what happens next:
>
> 1. Your 20-minute interview. It's an interview, not a sales call. If you picked a time on the page, it's in your calendar email. If not, pick one here, or we'll call you to set it up: {{contact.interview_link}}
> 2. Our panel picks every winner on Dec 11. People choose, not chance. Nobody wins before then. We judge against the published criteria in the Official Rules.
> 3. Second place is the Second-Place Stack. If our panel picks you, you get 72 hours to claim.
> 4. Third place: a free audit and a website buildout. No build fee. You pay hosting and maintenance only, $189 a month.
>
> One more thing. Refer a roofer in another market. If they win the grand prize, you win it too. Here's your link:
> {{contact.referral_link}}
>
> Camron
> 2URN Marketing

## Entry +1 day, morning: Book your interview

**SMS** (Day 1 has no other SMS, so this keeps us at one a day)
> 2URN: You're entered, but you haven't booked your 20-min interview yet. Our panel picks the grand prize and second place only from roofers who do it. It's not a sales call. Book: https://2urnagency.com/interview?c={{contact.referral_code}}

Skip if the contact already has an interview booked, or is tagged `not-a-fit`.

---

## Day 1 after entry: the hidden lock

**Email.** Subject: Your leads weren't bad. Nobody called them.
> {{contact.first_name}},
>
> Here's what we see in almost every CRM we open.
>
> Lead comes in at 2:14. First call at 8:40 that night. One voicemail. Marked dead.
>
> Meanwhile the homeowner filled out three forms that afternoon. Whoever called first got the job.
>
> That's why Growth Partner has an automated back end. Every lead gets a fast text, a follow-up sequence and a reminder, whether your crew is on a roof or the office is closed.
>
> The grand prize winner gets the first 90 days free, and the program runs right through winter, when a lot of your competitors go quiet.

*Variant, not booked (no tag `interview-booked`):*
> Winners are picked Dec 11. Book your interview if you haven't: {{contact.interview_link}}

*Variant, booked (tag `interview-booked`):*
> Winners are picked Dec 11. Know a roofer in another market? If they win the grand prize, you win it too: {{contact.referral_link}}

*Both variants end:*
> Camron

## Day 2: a real face

**SMS**
> 2URN: Digital door knocking. We can put your face, or your best rep's, at thousands of local doors a day, on homeowners' phones. Rain or snow. Real video, no AI. Not booked yet? Your interview: https://2urnagency.com/interview?c={{contact.referral_code}}

**Email.** Subject: Why we won't put an AI avatar in your ad
> Short one.
>
> Every Growth Partner ad has a real person in it. The owner or a lead rep, on camera, talking to homeowners in their own market.
>
> No AI avatars. No stock footage. Trust is the whole job in roofing, and trust comes from a face people can recognize at the grocery store.
>
> It's also the one thing we can't do for you. We write the scripts, you shoot them, we edit them. If you're not willing to be on camera, Growth Partner isn't a fit, and we'd rather say that now.
>
> Winners are picked Dec 11. Know a roofer in another market? If they win the grand prize, you win it too: {{contact.referral_link}}
>
> Camron

## Day 3: what the winner gets

**Email.** Subject: What we actually do in 90 days
> {{contact.first_name}},
>
> People ask what "Growth Partner" means. Here's the whole thing.
>
> 1. We come into your business. We structure and script your offers.
> 2. You shoot them. You or a lead rep, on a phone.
> 3. We edit every video and manage your advertising. You fund the ad spend, $200 to $1,000 a day, paid to Meta. Second place: from $100 a day.
> 4. We automate the nurture on the back end, so every lead gets worked.
>
> Standard price is $3,000 a month with a 90-day minimum. The grand prize winner gets the first 90 days free. It runs through the slow season, which is the point. While competitors go quiet, you don't.
>
> Winners are picked Dec 11. Know a roofer in another market? If they win the grand prize, you win it too: {{contact.referral_link}}
>
> Camron

**SMS (only if no interview booked, and not tagged `not-a-fit`)**
> 2URN: To be considered for the grand prize or second place, you have to meet with us one on one. A 20-min interview, a few questions about your business, not a sales call. Winners are picked Dec 11. Book: https://2urnagency.com/interview?c={{contact.referral_code}}

## Day 4: the slow season

**SMS**
> 2URN: Most of your competitors stop marketing in winter. This program runs right through it. Winners are picked Dec 11.

## Day 5: second place

**Email.** Subject: Second place: $9,750 of value, picked by our panel
> {{contact.first_name}},
>
> The grand prize goes to one company. Our panel picks second place too, on Dec 11. It's the Second-Place Stack, $9,750 of value, and this is included free with second place:
>
> - A one-month Content Package ($2,500): a 45-minute interview with me, then ten finished ads and posts in your own words.
> - A Competitor Analysis ($1,500): who you're up against, what they're running, and where the gaps are.
> - Five advertising campaigns, scripted for you ($1,250): ten hooks and a full video script each, ready to shoot.
> - A Website Buildout, free, if you don't have a website. We build it.
>
> That's $5,250 in deliverables plus a website if you need one, free, plus $4,500 off your first 90 days of Growth Partner ($1,500 a month instead of $3,000), then $3,000, with a revenue ROI guarantee: if you do these four things (content shot within 14 days, ad spend funded from $200/day, the follow-up sequence live, weekly scorecard call) and Growth Partner has not paid for itself in closed jobs by day 90, we keep working for free until it has. You fund your own ad spend, $100 to $1,000 a day, paid to Meta. The guarantee applies at $200 a day or more. The Competitor Analysis is yours when you book your claim call. The rest is delivered inside the 90-day program. Second-place winners have 72 hours from notification to claim, and claiming means booking a 20-minute call.
>
> Third place is a marketing audit and a website built for your company. No build fee. Hosting and maintenance is $189 a month. Hosting and maintenance terms are in your agreement.
>
> That makes winter a good time to start. You'd be running ads and follow-up while the rest of your market sits it out.

*Variant, not booked (no tag `interview-booked`):*
> Winners are picked Dec 11. Book your 20-minute interview if you haven't: {{contact.interview_link}}

*Variant, booked (tag `interview-booked`):*
> Winners are picked Dec 11. Know a roofer in another market? If they win the grand prize, you win it too: {{contact.referral_link}}

*Both variants end:*
> Camron

## Dec 10, 10:00 AM CT (pinned): the day before

Pinned to Dec 10, 10:00 AM CT, not relative to entry. Skip for a contact who entered on Dec 10.

**SMS**
> 2URN: Growth Partner giveaway entries close tomorrow, Dec 11, at 7pm CT. Know a roofer in another market? If they win the grand prize, you win it too: {{contact.referral_link}}

**Email.** Subject: Tomorrow, 7pm CT
> Entries close tomorrow, Dec 11, at 7pm CT, and winners are notified that night.

*Variant, not booked (no tag `interview-booked`):*
> If you haven't booked your 20-minute interview, do it now. Our panel picks the grand prize and second place from interviewed applicants. The last interview times are tomorrow before 5pm CT.
> {{contact.interview_link}}

*Variant, booked (tag `interview-booked`):*
> Your 20-minute interview is booked. If you can't make it, rebook from your calendar email so it still happens before tomorrow, 5pm CT.

*Both variants continue:*
> If you know a roofing company in another market that could meet what the winner commits to (funds ad spend of $200 to $1,000 a day, puts the owner or a lead rep on camera, produces case studies for their own business, lets us build a public case study, records a testimonial for 2URN), send them your link. If they win the grand prize, you win it too.
> {{contact.referral_link}}
>
> Camron

## Dec 11, 10:00 AM CT (pinned): announcement day, morning

Pinned to Dec 11, 10:00 AM CT, not relative to entry. Skip for a contact who entered on Dec 11.

**SMS**
> 2URN: Growth Partner giveaway entries close tonight at 7pm CT. Winners hear from us tonight. Keep your phone on.

---

## After winners are notified (Dec 11, 7:00 PM CT)

### Grand prize winner (workflow C sends this SMS when the tag `grand-prize` is added; Camron calls within the hour)
**SMS**
> 2URN: {{contact.first_name}}, you won. Camron is calling you in the next hour from this number. Pick up.

Referrer check: read the winner's own `referred_by`; if empty, read the winner's own `first_nominated_by_code` (written once by workflow F from the first nomination of a roofer who had not entered yet; never `nominated_by_code`, which every later nomination overwrites). The referrer is the entrant whose `referral_code` equals that value. If that referrer is an eligible entrant in a different market, they are also a grand prize winner (see GHL-SETUP.md runbook). Camron calls both. Do not post the public announcement (video, banner, socials) until the grand prize winner has accepted and signed the publicity and case-study release.

### Second-place winners
Set `claim_deadline` = now + 72h, write it into `claim_until_iso` (ISO 8601, see GHL-SETUP.md) and set `claim_link` in the workflow before this fires.

**SMS**
> 2URN: {{contact.first_name}}, our panel picked you for second place: the Second-Place Stack, $9,750 of value, plus a website if you need one. 72 hrs to claim: {{contact.claim_link}}

**Email.** Subject: Our panel picked you for second place: $9,750 of value. 72 hours.
> {{contact.first_name}},
>
> The grand prize went to one company. Our panel picked you for second place. Second place is the Second-Place Stack. Included free with second place:
>
> 1. A one-month Content Package ($2,500 value). A 45-minute interview with me, then we write 5 ad scripts and 5 content scripts in your words. You shoot them on a phone with our shot list, and we edit 10 finished pieces for your brand.
> 2. A Competitor Analysis ($1,500 value). Who your current competitors are, what they are running, their offers, hooks and review counts, and where the gaps are. It's delivered within 7 days of booking your claim call, whether or not you sign.
> 3. Five advertising campaigns, scripted for you ($1,250 value). Each one has 10 hooks and a full video script, ready to shoot.
> 4. A Website Buildout, if you don't have a website. We build it, free.
>
> The Competitor Analysis is yours when you book your claim call. The rest is delivered inside the 90-day program.
>
> That's $5,250 in deliverables plus a website if you need one, free, plus $4,500 off: 50% off your first 90 days of Growth Partner, $1,500 a month instead of $3,000, then the standard $3,000. $9,750 of value. You fund your own ad spend, $100 to $1,000 a day, paid to Meta. Minimum is 90 days.
>
> And the program comes with a revenue ROI guarantee. If you do these four things (content shot within 14 days, ad spend funded from $200/day, the follow-up sequence live, weekly scorecard call) and Growth Partner has not paid for itself in closed jobs by day 90, we keep working for free until it has. Those are the guarantee's four conditions, and the guarantee only applies if you do all four. The guarantee applies at $200 a day or more.
>
> Claiming it means booking your 20-minute claim call before {{contact.claim_deadline}}. On the call we go over what you get, when each piece arrives, and the Growth Partner agreement at $1,500 a month for the first 90 days.
>
> Claim here: {{contact.claim_link}}
>
> The deadline is real. After 72 hours the Stack and the half-off price are gone.
>
> Camron

Every second-place winner gets these messages. The claim is a 20-minute claim call booked on the Introduction Interview calendar (the same one as the interview) AFTER the notification; an interview booked before the notification does not count. The reminders and the +72h email check for a booking made after the notification. The claim-call booking (not the workflow start) creates the task "Deliver Competitor Analysis within 7 days". The setter also calls winners who have not booked (see setter-script.md).

### Claim window, +24h (no claim call booked since the notification)
**SMS**
> 2URN: {{contact.first_name}}, 48 hrs left to claim your Second-Place Stack. Book your 20-min call. Your Competitor Analysis arrives within 7 days of booking: {{contact.claim_link}}

### Claim window, +60h (no claim call booked since the notification)
**SMS**
> 2URN: 12 hrs left. After that the Stack and the $1,500/mo price are gone. Book now and your Competitor Analysis arrives within 7 days: {{contact.claim_link}}

### Claim window, +72h (no claim call booked since the notification): flip to evergreen
**Email.** Subject: The Stack is gone. The offer isn't.
> {{contact.first_name}},
>
> The second-place window closed, and the Second-Place Stack with it. No hard feelings, timing's timing.
>
> Growth Partner is still available at the standard $3,000 a month, 90-day minimum, if a spot is open. It's the same program: we script, you shoot, we edit, we run your ads, we automate the follow-up. You fund the ad spend, $200 to $1,000 a day.
>
> If you want to talk, book a call here: {{contact.claim_link}}
>
> Camron

### Third-place winners
Workflow G (tag `third-place`). Set `claim_deadline` = now + 72h, write it into `claim_until_iso` (ISO 8601, see GHL-SETUP.md) and set `claim3_link` before this fires. The panel may pick contacts tagged `not-a-fit`.

**SMS**
> 2URN: {{contact.first_name}}, you won third place: a marketing audit and a website built for you. No build fee. Hosting and maintenance $189/mo. 72 hrs to claim: {{contact.claim3_link}}

**Email.** Subject: You won third place: a free audit and a website built for you
> {{contact.first_name}},
>
> You won third place in the Growth Partner giveaway. Our panel picked you. Here's what that is:
>
> 1. A free marketing audit. We look at your website, your Google Business Profile, your ads and your follow-up, and tell you what to fix first.
> 2. A website built for your company. No build fee. You pay hosting and maintenance only, $189 a month. Hosting and maintenance terms are in your agreement.
>
> To claim it, book a 20-minute call before {{contact.claim_deadline}}. On the call we go over the audit and what we build for your site. It's not a Growth Partner pitch. If you want to talk about that too, we can, but you don't have to.
>
> Claim here: {{contact.claim3_link}}
>
> The deadline is real. After 72 hours the free build goes away.
>
> Camron

Note: [DECIDE: confirm audit scope] (item 1 of the email above).

If the contact has already booked the Free Audit + Website Call, skip the claim reminders; the setter handles the next step (see setter-script.md).

### Third-place claim window, +24h (not yet booked)
**SMS**
> 2URN: {{contact.first_name}}, 48 hrs left on your free audit and website build. No build fee, hosting and maintenance $189/mo. Book your 20-min call to claim it: {{contact.claim3_link}}

### Third-place claim window, +60h (not yet booked)
**SMS**
> 2URN: 12 hrs left on your free audit and website build (no build fee, hosting and maintenance $189/mo). After that the free build is gone. Book now: {{contact.claim3_link}}

### Third-place claim window, +72h (not booked): flip to evergreen
**Email.** Subject: The free build is gone. The audit conversation isn't.
> {{contact.first_name}},
>
> The third-place window closed, and the free website build with it. No hard feelings, timing's timing.
>
> If you still want a better website or a straight look at your marketing, book a call and we'll tell you plainly what we'd do and what it would cost. No pressure, and no sales pitch if you don't want one.
>
> Book a call here: {{contact.claim3_link}}
>
> Camron

Add the tag `evergreen` at +72h. Do not quote a standard website price in this email.

---

## Referrals and nominations

**Referrer SMS (optional, manual).** Not sent by workflow A (a workflow cannot message a different contact). When a new entry has a non-empty `referred_by`, the setter may send this once from the REFERRER's own contact (find it by `referral_code` = the new entry's `referred_by`). The referrer consented to texts when they entered. It counts toward the one-SMS-a-day limit for the referrer.
> 2URN: {{contact.first_name}}, the roofer you referred just entered. If they win the grand prize, you win it too.

**Nominated roofers get no automated message of any kind.** A roofer put forward through the nomination form on the thank-you page has given no consent. They get no automated SMS and no automated email, no auto-dialer, and they are set to Do Not Disturb for SMS and email until they enter themselves (workflow F, then workflow A clears it). The only contact is one manual call by the setter, with one voicemail that names the referrer if there is no answer, then stop. See setter-script.md. A nomination counts as a referral once the nominated company enters: if they win the grand prize, the person who nominated them wins it too. Workflow F does not tag, move or silence a contact already tagged `giveaway-entrant` (no tag, no stage move, no Do Not Disturb, no call task: workflow F's Create/Update Contact step has already overwritten `nominated_by_code` / `nominated_by_name` on that contact, so workflow F adds the note "Nominated AFTER entry ... does not count for the referral bonus" and notifies Camron) and skips contacts tagged `nominee-declined`.

---

## Setter call attempts (parallel to the above, see setter-script.md)
Applicants who did not book on the booking page: workflow A waits 30 minutes after entry, then creates the setter task "Call to book interview: entered, did not book" unless the contact has the tag `interview-booked`. The task is due within 1 hour (entries after 6 PM CT: 9 AM next day). 3 attempts on day 1, 2 on day 2, 1 on day 3. Text once, after the last unanswered call of the day, and only if no workflow SMS went to that contact that day (one SMS a day at most, workflow and setter texts together). Never text nominees. After winners are notified, call second-place winners who have not booked a claim call first, then third-place winners who have not booked the Free Audit + Website Call: 3 attempts on day 1, 2 on day 2, 1 on day 3, all inside the 72-hour claim window. After the window the prize is gone: any later call (weekly, up to 3 weeks) is about the standard program only and never mentions the prize as available. Log outcome in the GHL opportunity stage.

Contacts tagged `not-a-fit` (applied only after the setter call or interview) get no interview calls. They get the third-place call only if our panel picks them for third place on Dec 11 (tag `third-place`).

Nominated roofers (tag `nominated`): one manual call, one voicemail that names the referrer if there is no answer, then stop. No texts and no follow-up attempts. A text goes out only if the nominee asks for the link on that call: the setter turns SMS Do Not Disturb off for that contact, notes "asked for the link on the call, [date], [setter]", sends the one text, and leaves Do Not Disturb off only if the nominee then enters. If they say no, tag `nominee-declined` (Do Not Disturb on every channel, stage Not Interested, open tasks cancelled) and never contact them again.
