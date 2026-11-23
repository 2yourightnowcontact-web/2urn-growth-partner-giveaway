# Giveaway Email + SMS Sequence

Sender: Camron (email) / 2URN (SMS). All sends are from the GHL workflow "Giveaway Entry". `{{contact.first_name}}`, `{{contact.referral_link}}`, `{{contact.interview_link}}`, `{{contact.claim_link}}`, `{{contact.claim_deadline}}` are GHL custom fields (see GHL-SETUP.md). Winner announced Dec 4, 2026, 7:00 PM CT; change every mention if GHL_CONFIG.announcementAt changes.

The program is 2URN Growth Partner: $3,000 per month, 90-day minimum, client funds ad spend (from $150 a day, recommended $150 to $300). There are two prizes. Grand prize (1, plus the referrer): 90 days of Growth Partner, free ($10,000 value). Second place: the Second-Place Stack. When a second-place winner claims (books the interview within 72 hours and moves forward on the 50% deal) they get, free: a one-month Content Package ($2,500 value: a 45-minute interview with Camron; we write 5 ad scripts and 5 content scripts in their words; they shoot on a phone with our shot list; we edit 10 finished pieces), a Competitor Analysis ($1,500 value: who their current competitors are, what they are running, their offers, hooks, review counts and the gaps) and five advertising campaigns scripted for them ($1,250 value: each with 10 hooks and a full video script, ready to shoot; not edited ads, not loaded audiences). Plus 50% off the first 90 days of Growth Partner ($1,500 per month instead of $3,000, a $4,500 saving), then $3,000, with the ROI guarantee if they do everything on the commitment list. Headline math, used everywhere: "$5,250 in deliverables, free, plus $4,500 off: $9,750 of value for second place." Delivery: the Competitor Analysis within 7 days of booking the interview (whether or not they sign); the Content Package and the five scripted campaigns in month 1 of the engagement.

Public wording: say only "second place" and "second-place winners" in any message. Do not describe second place as open to a group of people.

The guarantee, worded the same everywhere: "If you do everything on the list (on camera within 14 days, ad spend funded from $150/day, the follow-up sequence live, weekly scorecard call) and Growth Partner has not paid for itself in closed jobs by day 90, we keep working for free until it has." [CHECK with attorney, see official-rules-DRAFT.md]

Who gets this: every entrant. There is no form-level disqualification. A contact who is tagged `not-a-fit` after the setter call or interview is removed from the sequence and gets nothing further (see GHL-SETUP.md, workflow E).

Rules: one SMS a day max. Every SMS ends with "Reply STOP to opt out" on the first send only (GHL appends after that). Keep SMS under 160 chars where possible. This is a judged contest: never describe the winner as drawn or picked by chance, and never offer extra entries.

---

## Immediately on entry

**SMS**
> 2URN: {{contact.first_name}}, you're entered to win 90 days of Growth Partner, free. Winner announced Dec 4, 7pm CT. If a company you refer wins, you win too: {{contact.referral_link}} Reply STOP to opt out

**Email.** Subject: You're entered. Here's what happens next.
> {{contact.first_name}},
>
> You're entered. One roofing company wins 2URN Growth Partner free for 90 days, a $10,000 value. Second place is the Second-Place Stack: $5,250 in deliverables, free, plus 50% off your first 90 days of Growth Partner ($1,500 a month instead of $3,000). That's $9,750 of value, with a guaranteed ROI if you do everything on the winner's commitment list.
>
> Here's what happens next:
>
> 1. We call within 2 business days to book your 20-minute interview. It's an interview, not a sales call. You can book it yourself now: {{contact.interview_link}}
> 2. Our panel picks the winner. People choose the winner, not chance. We choose from interviewed applicants against the published criteria in the Official Rules. We announce on Dec 4.
> 3. Second-place winners are notified after the announcement and get 72 hours to claim the Second-Place Stack.
>
> One more thing. If the company you refer wins, you win too. Send your link to a company in a different market:
> {{contact.referral_link}}
>
> Camron
> 2URN Marketing

## Entry +1 day, morning: Book your interview

**SMS** (Day 1 has no other SMS, so this keeps us at one a day)
> 2URN: {{contact.first_name}}, book your 20-min interview for the Growth Partner giveaway. It's an interview, not a sales call: {{contact.interview_link}}

Skip if the contact already has an interview booked.

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
> The winner gets the first 90 days free, and the program runs right through winter, when a lot of your competitors go quiet.
>
> Winner announced in 6 days. Book your interview if you haven't: {{contact.interview_link}}
>
> Camron

## Day 2: a real face

**SMS**
> 2URN: Homeowners hire faces they recognize. That's why the owner or a lead rep is on camera in every Growth Partner ad. No AI, no stock footage. 5 days left.

**Email.** Subject: Why we won't put an AI avatar in your ad
> Short one.
>
> Every Growth Partner ad has a real person in it. The owner or a lead rep, on camera, talking to homeowners in their own market.
>
> No AI avatars. No stock footage. Trust is the whole job in home services, and trust comes from a face people can recognize at the grocery store.
>
> It's also the one thing we can't do for you. We write the scripts, you shoot them, we edit them. If you're not willing to be on camera, this program isn't a fit, and we'd rather say that now.
>
> 5 days. {{contact.referral_link}}
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
> 3. We edit every video and manage your advertising. You fund the ad spend from $150 a day, paid to Meta.
> 4. We automate the nurture on the back end, so every lead gets worked.
>
> Standard price is $3,000 a month with a 90-day minimum. The winner gets the first 90 days free. It runs through the slow season, which is the point. While competitors go quiet, you don't.
>
> 4 days left. {{contact.referral_link}}
>
> Camron

**SMS (only if no interview booked)**
> 2URN: {{contact.first_name}}, you haven't booked your interview yet. 20 minutes, not a sales call: {{contact.interview_link}}

## Day 4: the slow season

**SMS**
> 2URN: Most of your competitors stop marketing in winter. This program runs right through it. 3 days until the winner is announced.

## Day 5: second place

**Email.** Subject: Even if you don't win, there's a stack
> {{contact.first_name}},
>
> The grand prize goes to one company. Second place is a stack, and it's worth $9,750:
>
> - A one-month Content Package ($2,500): a 45-minute interview with me, then ten finished ads and posts in your own words.
> - A Competitor Analysis ($1,500): who you're up against, what they're running, and where the gaps are.
> - Five advertising campaigns, scripted for you ($1,250): ten hooks and a full video script each, ready to shoot.
>
> That's $5,250 in deliverables, free, plus 50% off your first 90 days of Growth Partner ($1,500 a month instead of $3,000, a $4,500 saving), then $3,000, with a guaranteed ROI if you do everything on the winner's commitment list. You have 72 hours to claim after the announcement, and claiming means booking your interview.
>
> We do it this way because we only take on a few new companies at a time, and second place is how we fill those spots with people who already raised their hand.
>
> That makes winter a good time to start. You'd be running ads and follow-up while the rest of your market sits it out.
>
> 2 days. {{contact.interview_link}}
>
> Camron

## Day 6: 24 hours

**SMS**
> 2URN: 24 hours until the Growth Partner winner is announced. Know a company that should enter? If they win, you win too: {{contact.referral_link}}

**Email.** Subject: Tomorrow, 7pm CT
> The winner is announced tomorrow at 7pm CT. Entries close at that time.
>
> If you haven't booked your 20-minute interview, do it now. We pick from interviewed applicants.
> {{contact.interview_link}}
>
> If you know a company in another market that could meet the winner's commitment list ($1M+, on camera, ad spend from $150/day, a team that can take the appointments), send them your link. If they win, you win.
> {{contact.referral_link}}
>
> Camron

## Announcement day, morning

**SMS**
> 2URN: The Growth Partner winner is announced TONIGHT at 7pm CT. Keep your phone on. Winners hear from us this week.

---

## After the announcement

### Grand prize winner (manual, Camron calls first, then:)
**SMS**
> 2URN: {{contact.first_name}}, you won. Camron is calling you in the next hour from this number. Pick up.

If the winner entered through a referral link, the referrer is also a grand prize winner. Camron calls both.

### Second-place winners
Set `claim_deadline` = now + 72h in the workflow before this fires.

**SMS**
> 2URN: {{contact.first_name}}, you won second place: the Second-Place Stack, $9,750 of value (Content Package, Competitor Analysis, 5 scripted campaigns + 50% off 90 days). 72 hrs to claim: {{contact.claim_link}}

**Email.** Subject: You won the Second-Place Stack: $9,750 of value. 72 hours.
> {{contact.first_name}},
>
> The grand prize went to one company. You're a second-place winner, and second place is a stack. When you claim it, you get, free:
>
> 1. A one-month Content Package ($2,500 value). A 45-minute interview with me, then we write 5 ad scripts and 5 content scripts in your words. You shoot them on a phone with our shot list, and we edit 10 finished pieces for your brand.
> 2. A Competitor Analysis ($1,500 value). Who your current competitors are, what they are running, their offers, hooks and review counts, and where the gaps are. It's delivered within 7 days of booking your interview, whether or not you sign.
> 3. Five advertising campaigns, scripted for you ($1,250 value). Each one has 10 hooks and a full video script, ready to shoot. The Content Package and the five campaigns are delivered in your first month of Growth Partner.
>
> That's $5,250 in deliverables, free, plus $4,500 off: 50% off your first 90 days of Growth Partner, $1,500 a month instead of $3,000, then the standard $3,000. $9,750 of value for second place. You fund your own ad spend, from $150 a day, paid to Meta. Minimum is 90 days.
>
> And it comes with a guarantee. If you do everything on the list (on camera within 14 days, ad spend funded from $150/day, the follow-up sequence live, weekly scorecard call) and Growth Partner has not paid for itself in closed jobs by day 90, we keep working for free until it has. The list is the guarantee's conditions, and the guarantee only applies if you do all four.
>
> Claiming it means booking your 20-minute interview before {{contact.claim_deadline}}. It's an interview, not a sales call. We look at your business and the commitment list and tell you plainly if it's a fit. If it isn't, we'll say so.
>
> Claim here: {{contact.claim_link}}
>
> The deadline is real. We take on a few new companies at a time and they go to whoever books first.
>
> Camron

If the interview has already happened, the setter calls instead to confirm the next step (see setter-script.md).

### Claim window, +24h (not yet booked)
**SMS**
> 2URN: 48 hrs left on your Second-Place Stack, {{contact.first_name}}. Book your 20-min interview to lock it in. Your Competitor Analysis arrives within 7 days of booking: {{contact.claim_link}}

### Claim window, +60h (not yet booked)
**SMS**
> 2URN: 12 hrs left. After that the Stack and the $1,500/mo price are gone. Book now and your Competitor Analysis arrives within 7 days: {{contact.claim_link}}

### Claim window, +72h (not booked): flip to evergreen
**Email.** Subject: The Stack is gone. The offer isn't.
> {{contact.first_name}},
>
> The second-place window closed, and the Second-Place Stack with it. No hard feelings, timing's timing.
>
> Growth Partner is still available at the standard $3,000 a month, 90-day minimum, if a spot is open. It's the same program: we script, you shoot, we edit, we run your ads, we automate the follow-up. You fund the ad spend.
>
> If you want to talk, book your interview here: {{contact.claim_link}}
>
> Camron

---

## Setter call attempts (parallel to the above, see setter-script.md)
Applicants who have not booked: call within 2 business days of entry. 3 attempts day 1, 2 attempts day 2, 1 attempt day 3. Text after every unanswered call. After the announcement, call every second-place winner who has not booked: 3 attempts day 1, 2 attempts day 2, 1 attempt day 3, then weekly for 3 weeks. Log outcome in the GHL opportunity stage. Never call a contact tagged `not-a-fit` (applied only after the setter call or interview).
