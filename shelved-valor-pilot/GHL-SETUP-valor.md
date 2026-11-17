# GHL Setup: Valor Free Roof Giveaway

Sub-account: Valor Roofing Solutions. Everything below is a paste-and-click list. Where a value lives in a file, the file and the line are named. Domain and calendar links below are placeholders until the real ones exist.

Hard rule for every page, text and email in this funnel: never mention insurance deductibles.

## 1. Funnel and pages
Sites → Funnels → + New Funnel → "Valor Free Roof Giveaway". Domain: go.valorroofingsolutions.com (placeholder).

| Step | Path | Paste file | Element |
|---|---|---|---|
| Giveaway | `/free-roof` | `01-valor-giveaway-ghl.html` | one Custom Code element, full width, no section padding |
| Thank you | `/thank-you` | `02-valor-thankyou-ghl.html` | same |
| Claim | `/claim` | `03-valor-claim-ghl.html` | same |
| Rules | `/rules` | paste the attorney-approved rules as plain text (draft: `official-rules-valor-DRAFT.md`) | text element |

Open each .html in TextEdit → Cmd+A → Cmd+C → paste into the Custom Code element → Save. Set the page's section padding to 0 and width to full. Each file already carries the Valor logo inline, so there is nothing to upload.

The footer on the giveaway page links to `/privacy` and `/terms`. Create both pages in the funnel, or remove those two links before launch.

Add the Meta pixel in Funnel Settings → Tracking Code (head). The pages fire `Lead` on entry and `CompleteRegistration` on the thank-you page.

Constants to update when the real domain exists:
- `02-valor-thankyou-ghl.html`: `window.GW_TY.landingUrl` (currently `https://go.valorroofingsolutions.com/free-roof`)
- `03-valor-claim-ghl.html`: `window.GW_CLAIM.bookingUrl` (see section 5)

## 2. Form
Sites → Forms → + New → "Valor Free Roof Giveaway Entry". Add these fields (the names must match exactly; they're what the page posts):

| Field | Type | Options |
|---|---|---|
| first_name, last_name, email, phone | standard | |
| address1 | standard Street Address | |
| city | standard City | |
| postal_code | standard Postal Code | 5 digits, required (the page also checks this) |
| roof_age | custom dropdown "Roof Age" | under_10, 10_15, 15_20, over_20, not_sure |
| concern | custom dropdown "Concern" | leak, storm_damage, age, selling_home, just_curious |
| ad_attribution | custom text | |
| referred_by | custom text "Referred By Code" | |
| referral_code | custom text "Referral Code" | |
| lead_source | custom text | |
| lead_note | custom multi-line "Lead Note" | |

Save → Integrate → copy the **form id** → paste into `01-valor-giveaway-ghl.html` at `window.GHL_CONFIG.formId`. Re-paste the page.

The page also adds a readable lead note (name, address, roof age, concern, referral code, ad) to every entry.

## 3. Custom values and fields for the sequence
Settings → Custom Fields (folder "Giveaway"):
- `referral_link` (text): set by workflow: `https://go.valorroofingsolutions.com/free-roof?ref={{contact.referral_code}}`
- `claim_deadline` (date/time): set by workflow on drawing day: now + 72 hours
- `claim_link` (text): `https://go.valorroofingsolutions.com/claim?until={{contact.claim_deadline}}&first={{contact.first_name}}&last={{contact.last_name}}&email={{contact.email}}&phone={{contact.phone}}`
- `giveaway_result` (dropdown): entered, first_prize, second_prize, not_eligible

## 4. Workflows
Automation → Workflows. Message copy lives in `sequence-homeowner.md`.

**A. "Giveaway Entry"**: Trigger: Form Submitted (Valor Free Roof Giveaway Entry). Also add an Inbound Webhook trigger; copy its URL into `01-valor-giveaway-ghl.html` at `window.GHL_CONFIG.webhook` (optional belt-and-braces).
1. Add tag `giveaway-entrant`. Set `giveaway_result` = entered.
2. Update field `referral_link` with the value above.
3. Add to pipeline "Giveaway" → stage "Entered".
4. Send the "On entry" SMS and email from `sequence-homeowner.md`.
5. Wait 1 day → Day 1 email. Wait 1 day → Day 2 SMS. Continue through Day 6 and Drawing-day morning exactly as the file lists them. Use "Wait until" steps pinned to calendar dates so late entrants don't get Day 1 after the drawing: anyone entering after Dec 9 only gets the entry message and the 24-hour message.
6. If `referred_by` is not empty → internal notification to Camron and Valor's office contact [set] ("Referral entry: {{contact.first_name}} referred by {{contact.referred_by}}") and add 1 to a "referral count" field on the referrer (Find Contact by `referral_code` = `referred_by` → Update field). If GHL can't do the lookup natively, export entries on drawing day and count referrals in a sheet. The drawing uses that sheet.

**B. "Second Prize"**: Trigger: tag added `second-prize`.
1. Set `giveaway_result` = second_prize. Set `claim_deadline` = now + 72h. Set `claim_link`.
2. Send second-prize SMS + email. Move stage to "Second Prize Notified".
3. Wait 24h → if no appointment booked → 48-hours-left SMS. Wait 36h → 12-hours-left SMS. Wait 12h → "claim window closed" email, tag `evergreen`.
4. Trigger "Appointment booked" on the Free Roof Inspection calendar → remove from this workflow, stage "Inspection Booked".

**C. "First Prize"**: Trigger: tag `first-prize`. Set result, send the winner SMS, task for Matt Willard (or Valor's designated caller [set]) to call within the hour. Also tag the referrer, if there is one, so Valor can honor the $5,000 referral reward.

## 5. Calendar
Calendars → + New → "Free Roof Inspection", 45 min, assigned to [set: Valor's scheduler or crew lead], buffer [set], availability [set]. Share → copy widget link → paste into `03-valor-claim-ghl.html` at `window.GW_CLAIM.bookingUrl`. The file currently holds the placeholder `https://link.2urnmarketing.com/widget/booking/VALOR_INSPECTION`; swap it for the real widget link. Leave the calendar's default confirmation page; do not redirect it to `/thank-you` (that page is for giveaway entries).

The claim page passes first name, last name, email and phone to the widget so the form comes prefilled.

## 6. Drawing day runbook (Dec 11, 7:00 PM CT)
1. 5:00 PM: export all contacts tagged `giveaway-entrant`. Remove ineligible entries (not a Middle Tennessee homeowner, not a single-family home, under 18, duplicates). Build the entry list: 1 row per entry, plus 1 row per verified referral (cap per the Official Rules).
2. 7:00 PM: random draw on camera (record it). Note whether the winner's `referred_by` is set; if so, the referrer gets the $5,000 off their own replacement.
3. Tag the winner `first-prize`. Matt (or the designated caller) calls within the hour.
4. Bulk-tag every other eligible entrant `second-prize`. Workflow B fires.
5. Post the winner announcement (video) to the landing page top banner and socials. Changing `drawingAt` in `01-valor-giveaway-ghl.html` is not needed; the countdown closes itself.
6. Next morning: the office starts dialing per `setter-script-valor.md`.

## 7. Test before launch
- Submit one test entry from your phone on `/free-roof` with formId set. Confirm: contact created with street address, city and ZIP, note attached, `referral_link` populated, entry SMS received, pipeline stage Entered.
- Submit once with a 4-digit ZIP. Confirm the page blocks it and shows the ZIP message.
- Open the referral link in a private window and enter a second test contact. Confirm `referred_by` is set on the second contact.
- Add tag `second-prize` to the test contact. Confirm the claim SMS arrives and `/claim` shows a 72-hour timer and the calendar loads prefilled.
- Check all three pages at 390px width (phone) and confirm nothing scrolls sideways.
- Read every text and email once and confirm none mentions insurance deductibles.
- Delete both test contacts.

## 8. Before shooting the VSL
Shoot Matt's 3-minute video from `VSL-script-matt.md`. Replace the video placeholder in `01-valor-giveaway-ghl.html` (the `#video` div, "Matt's 3-minute video goes here") with the GHL video embed.
