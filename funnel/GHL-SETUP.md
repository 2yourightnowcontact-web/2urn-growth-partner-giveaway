# GHL Setup: 2URN Growth Partner Giveaway

Sub-account: 2URN Marketing (our own). Everything below is a paste-and-click list. Where a value lives in a file, the file and the line are named.

The offer: 2URN Growth Partner, $3,000 per month, 90-day minimum, client funds ad spend (from $150 a day, recommended $150 to $300). There are two prizes. Grand prize (1): 90 days of Growth Partner, free ($10,000 value), plus the referrer if there is one. Second place, "The Second-Place Stack": every qualified applicant who is not the grand-prize winner gets second place (stated plainly here for the team; the purpose is to bring them into Growth Partner; public pages and messages say only "second place" and "second-place winners"). When a second-place winner claims (books the interview within 72 hours and moves forward on the 50% deal) they get, free: a one-month Content Package ($2,500 value: a 45-minute interview with Camron; we write 5 ad scripts and 5 content scripts in their words; they shoot on a phone with our shot list; we edit 10 finished pieces), a Competitor Analysis ($1,500 value: who their current competitors are, what they run, offers, hooks, review counts and the gaps) and five advertising campaigns scripted for them ($1,250 value: each with 10 hooks and a full video script, ready to shoot; not edited ads, not loaded audiences), plus 50% off the first 90 days of Growth Partner ($1,500 per month instead of $3,000, a $4,500 saving), then $3,000, with the ROI guarantee if they do everything on the commitment list. Headline math: "$5,250 in deliverables, free, plus $4,500 off: $9,750 of value for second place." Delivery split [CHECK in rules]: the Competitor Analysis within 7 days of booking the interview (whether or not they sign); the Content Package and the five scripted campaigns in month 1 of the engagement. The guarantee, worded the same on every page: "If you do everything on the list (on camera within 14 days, ad spend funded from $150/day, the follow-up sequence live, weekly scorecard call) and Growth Partner has not paid for itself in closed jobs by day 90, we keep working for free until it has." Every applicant gets a 20-minute call; there is no form-level disqualification. Qualification (revenue, on camera, ad budget, team) happens on the setter call and interview. The winner is chosen by 2URN's panel from interview scorecards against the published criteria. It is a judged contest.

## 1. Funnel and pages
Sites → Funnels → + New Funnel → "Growth Partner Giveaway". Domain: go.2urnmarketing.com.

| Step | Path | Paste file | Element |
|---|---|---|---|
| Giveaway | `/lead-engine` | `01-giveaway-ghl.html` | one Custom Code element, full width, no section padding |
| Thank you | `/thank-you` | `02-thankyou-ghl.html` | same |
| Claim | `/claim` | `03-claim-ghl.html` | same |
| Rules | `/rules` | paste the attorney-approved rules as plain text | text element |

The path `/lead-engine` is kept so existing links keep working. Change it to `/growth-partner` if you want, then update `landingUrl` in `02-thankyou-ghl.html`.

Open each .html in TextEdit → Cmd+A → Cmd+C → paste into the Custom Code element → Save. Set the page's section padding to 0 and width to full.

Add the Meta pixel in Funnel Settings → Tracking Code (head). The pages fire `Lead` on entry and `CompleteRegistration` on the thank-you page. Neither carries a qualified or not-a-fit flag any more, because the form no longer qualifies anyone. Everyone who enters is a Lead.

## 2. Form
Sites → Forms → + New → "Growth Partner Giveaway Entry". Add these fields (the names must match exactly; they're what the page posts):

| Field | Type | Options |
|---|---|---|
| first_name, last_name, email, phone | standard | |
| company | standard Company Name | |
| revenue_12mo | custom dropdown "Revenue Last 12 Months" | under_1m, 1m_3m, 3m_10m, over_10m (self-reported, not disqualifying; confirmed on the call) |
| ad_attribution | custom text | |
| referred_by | custom text "Referred By Code" | |
| referral_code | custom text "Referral Code" | |
| lead_source | custom text | |
| lead_note | custom multi-line "Lead Note" | |

The old fields `trade`, `volume`, `problem`, `city`, `city_state`, `on_camera`, `ad_budget`, `biggest_problem`, `agrees_requirements` and `disqualified` are gone from the page (6 form fields now). Delete them from the GHL form, or leave them unused. If you still want them as contact fields, the setter fills `on_camera` and `ad_budget` by hand after the call.

Every entry submits and is treated the same. Nobody is flagged or blocked by the form. Under-$1M answers still arrive with `revenue_12mo` = under_1m so the setter can see it, but they get the same call.

Save → Integrate → copy the **form id** → paste into `01-giveaway-ghl.html` at `window.GHL_CONFIG.formId`. Re-paste the page.

## 3. Custom values and fields for the sequence
Settings → Custom Fields (folder "Giveaway"):
- `referral_link` (text): set by workflow: `https://go.2urnmarketing.com/lead-engine?ref={{contact.referral_code}}`
- `interview_link` (text): set by workflow: the Growth Partner Interview calendar widget link plus `?first_name={{contact.first_name}}&last_name={{contact.last_name}}&email={{contact.email}}&phone={{contact.phone}}`
- `claim_deadline` (date/time): set by workflow on announcement day: now + 72 hours
- `claim_link` (text): `https://go.2urnmarketing.com/claim?until={{contact.claim_deadline}}&first={{contact.first_name}}&last={{contact.last_name}}&email={{contact.email}}&phone={{contact.phone}}`
- `cma_delivered` (date): the date the Competitor Analysis report was sent. Set by hand when the "Deliver Competitor Analysis" task is completed (or by a workflow step on task completion). Empty means not yet delivered.
- `giveaway_result` (dropdown): entered, grand_prize, second_place, not_eligible
- `interview_score` (number, 0 to 100): the panel's total from the interview scorecard (rules, Section 6)
- `referral_count` (number)

Tags used: `giveaway-entrant`, `not-a-fit`, `interview-booked`, `interviewed`, `grand-prize`, `second-place`, `evergreen`.

## 4. Workflows
Automation → Workflows.

**A. "Giveaway Entry"**: Trigger: Form Submitted (Growth Partner Giveaway Entry). Also add an Inbound Webhook trigger; copy its URL into `01-giveaway-ghl.html` at `window.GHL_CONFIG.webhook` (optional belt-and-braces).
1. **Every entrant:** add tag `giveaway-entrant`. Set `giveaway_result` = entered. There is no form-level Not a Fit branch.
2. Update fields `referral_link` and `interview_link` with the values above.
3. Add to pipeline "Giveaway" → stage "Entered".
4. Send the "Immediately on entry" SMS and email from `sequence-email-sms.md`.
5. Create a task for the setter: "Call to book interview", due in 2 business days.
6. Wait until next morning, 10 AM → send the "Book your interview" SMS (skip if the contact has the tag `interview-booked`). Then the Day 1 email.
7. Wait 1 day → Day 2 SMS + email. Continue through Day 6 and Announcement-day morning exactly as the file lists them, including the Day 3 conditional SMS (only if no interview booked). Use "Wait until" steps pinned to calendar dates so late entrants don't get Day 1 after the announcement: anyone entering after Dec 2 only gets the entry message, the interview SMS and the 24-hour message.
8. If `referred_by` is not empty → internal notification to Camron ("Referral entry: {{contact.first_name}} referred by {{contact.referred_by}}") and add 1 to `referral_count` on the referrer (Find Contact by `referral_code` = `referred_by` → Update field). If GHL can't do the lookup natively, export entries on announcement day and match referrers in a sheet. A referral does not add an entry or change judging. It only identifies who gets the referral bonus if the referred company wins.

**B. "Second Place"**: Trigger: tag added `second-place`.
1. Set `giveaway_result` = second_place. Set `claim_deadline` = now + 72h. Set `claim_link`.
2. Send the Second-Place Stack SMS + email from `sequence-email-sms.md`. Move stage to "Second Place Notified".
3. Wait 24h → if no appointment booked → 48-hours-left SMS (it says the Competitor Analysis arrives within 7 days of booking). Wait 36h → 12-hours-left SMS (same line). Wait 12h → "The Stack is gone" email, tag `evergreen`.
4. Trigger "Appointment booked" on the Growth Partner Interview calendar → remove from this workflow, stage "Interview Booked", and **create the task "Deliver Competitor Analysis within 7 days"** (assignee: Camron or the analyst; due = booking date + 7 days). When the task is completed, set `cma_delivered` = today. The Competitor Analysis is delivered on claim whether or not the contact signs.
5. If the contact already has the tag `interview-booked` when this workflow starts (they booked before the announcement), create the same task at once with due = tag date + 7 days, or the second-place notification date + 7 days if later [our assumption, confirm]. The Content Package and the five scripted campaigns are not tasked here: they are delivered in month 1 of the engagement, so create those tasks when the engagement agreement is signed.

**C. "Grand Prize"**: Trigger: tag `grand-prize`. Set result = grand_prize, send the winner SMS, task for Camron to call within the hour. If the winner has a `referred_by`, the referrer gets the same tag by hand.

**D. "Interview Booked"**: Trigger: appointment booked on the Growth Partner Interview calendar.
1. Add tag `interview-booked`. Stage "Interview Booked". Complete the setter's "Call to book interview" task. Stop any pending interview-reminder SMS. (If the contact has the tag `second-place`, the Competitor Analysis task is created in workflow B step 4, not here.)
2. When the appointment status becomes Showed: add tag `interviewed`, stage "Interviewed", create a task for the interviewer: "Fill in the scorecard and `interview_score`".
3. If No Show: send one SMS with the rebook link and set a setter task.

**E. "Not a Fit"**: Trigger: tag added `not-a-fit` (the only way a contact becomes Not a Fit: the setter or interviewer tags it by hand after the call, when revenue is under $1M or they will not be on camera. Politely, and they are never pitched). Remove from workflows A, B, C2 and D. Set stage "Not a Fit". Set Do Not Disturb for calls. Cancel open setter tasks.

## 5. Calendar
Calendars → + New → "Growth Partner Interview", 20 min, interviewer [Camron or named team members], buffer 10 min, availability [set]. Share → copy widget link → paste into `03-claim-ghl.html` at `window.GW_CLAIM.bookingUrl`, and use the same link in `interview_link`. Leave the calendar's default confirmation page; do not redirect it to `/thank-you` (that page is for giveaway entries).

## 6. Announcement-day runbook (Dec 4, 7:00 PM CT)
This is a judged contest. A panel picks the winner. The winner comes from the scorecards.
1. By the interview cutoff in the rules (proposed 5:00 PM CT): every interviewer has entered `interview_score` and notes for each interviewed applicant. [CHECK: confirm cutoff with counsel, see rules Section 3.]
2. Export all contacts tagged `giveaway-entrant` and not tagged `not-a-fit`, with `interview_score`, revenue, the on-camera answer from the interview notes and notes. Remove duplicates and anyone who fails criterion 1 or 2 after interview.
3. Panel picks the grand prize winner from scorecards. Rank by the published criteria and weights in the rules, Section 6. Apply them exactly as published. Break ties as the rules state. Record the winner, the scores and who was on the panel. Keep the scorecards.
4. Check the winner's `referred_by`. If set and the referrer is eligible and in a different market, the referrer also wins the grand prize.
5. 7:00 PM: announce. Tag the winner(s) `grand-prize`. Camron calls within the hour. Workflow C fires.
6. Bulk-tag every other qualified applicant `second-place` (no `not-a-fit` tag). Workflow B fires. Interviews not yet held are booked inside the claim window. Every booking creates the "Deliver Competitor Analysis within 7 days" task.
7. Post the winner announcement (video) to the landing page top banner and socials. The countdown closes the form itself, no code change needed.
8. Next morning: setter starts dialing second-place winners who haven't booked, per `setter-script.md`.

## 7. Test before launch
- Submit one test entry from your phone on `/lead-engine` with formId set (all 6 fields). Confirm: contact created, note attached, `referral_link` and `interview_link` populated, entry SMS received, pipeline stage Entered, setter task created, the "Book your interview" SMS arrives the next morning, and the thank-you page shows the standard "You're entered" message and referral loop.
- Submit a second test with revenue `under_1m`. Confirm it behaves exactly like the first: same SMS and email, same setter task, same thank-you page. Nothing is flagged on entry.
- Add tag `not-a-fit` by hand to that second contact (simulating the post-call outcome). Confirm workflow E fires: removed from A, B and D, stage Not a Fit, Do Not Disturb for calls, open setter tasks cancelled.
- Open the referral link in a private window and enter a third test contact. Confirm `referred_by` is set.
- Book the Growth Partner Interview calendar as the first test contact. Confirm tag `interview-booked`, stage Interview Booked, the setter task is complete.
- Add tag `second-place` to the test contact. Confirm the Second-Place Stack SMS and email arrive and `/claim` shows a 72-hour timer and the calendar loads prefilled. Then book the interview and confirm the task "Deliver Competitor Analysis within 7 days" is created with a due date 7 days out, and that completing it lets you set `cma_delivered`.
- Delete all test contacts.

## 8. Before shooting the VSL
Fill the proof placeholder in `VSL-script.md` with two client results we can screenshot. Replace the video placeholder in `01-giveaway-ghl.html` (the `#video` div) with the GHL video embed. The VSL is being rewritten separately to match the Growth Partner offer.
