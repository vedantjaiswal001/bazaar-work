# BAZAAR - the pitch video (final cut, cinematic transitions)

THE script to record. Aligned with the current repo: 94 tests, domestic test card
`5267 3181 8797 5449` + Netbanking fallback, all links on `bazaar-work`, Track 01. It
runs ~4 min 30 s (a 5-minute slot, and under is fine). It tells you exactly what to open,
what to click, what to say, and how each scene flows into the next.

The "what broke, and how you got out" story is NOT in the video by design, it goes in the
form's own field and it is already in the README (the section that splits all three into
What broke / How we got out). The video is 4.5 minutes of the product actually working.

Legend: **OPEN** = what is on screen. **CLICK** = what to do. **SAY** = read aloud
(close to word-for-word). **TEXT** = big caption to burn on screen. **>>>** = the
transition into the next scene. `/` = short pause. **bold** = hit that word harder.

---

## PART A - Set up before you record (~10 min)

Three terminals in your `bazaar` folder and one browser:
- **Terminal 1:** `make run`   (backend on :8000)
- **Terminal 2:** `make web`   (console on :5173)
- **Terminal 3:** free, for `make live` (your `rzp_test_` keys in `.env`)
- **Browser:** **http://localhost:5173** (the Console/Results screen)

One silent dry run of `make live`, one click-through of the console, so nothing surprises
you. Do Not Disturb on. Terminal font 18-22 pt. Record 1080p, 30 fps.

Reliability note: if the backend misbehaves on the day, record the interactive parts on
**https://vedantjaiswal001.github.io/bazaar-work/** instead (tabs there are Red Team and
Benchmark). The `make live` scene is identical either way.

Record Scene 4 (`make live`) FIRST and re-run until one take is clean, it is the only part
that touches the network. Everything else is deterministic and cannot glitch. Then record
voice over the top, or narrate live.

---

## PART B - The script (7 scenes)

### TITLE CARD (0:00 - 0:03)
**OPEN:** pure black. The BAZAAR mark fades up over 0.5 s.
**TEXT (center):** `BAZAAR - a deterministic authorization gate for AI-to-AI commerce`
No voice. Let a soft music pad build for 3 seconds.
**>>> TRANSITION:** hard cut on the first music downbeat, straight to the live console.
The cut on the beat is what makes it feel intentional, not amateur.

### SCENE 1 - Hook (0:03 - 0:20)
**OPEN:** the console header (BAZAAR, KPIs visible: 94 tests, 100% blocked, 0% false-block).
**TEXT:** `AI agents can already spend money. Should they be allowed to?`
**SAY:**
> "AI agents can already spend your money. / The real question is whether they should be **allowed** to. / BAZAAR decides that on every payment / in a tenth of a millisecond / and the agent **cannot** overrule it."
**>>> TRANSITION:** begin a slow push-in (Ken Burns) toward the pipeline in the center,
and let that same motion CARRY into Scene 2 with no cut. Continuous motion = premium feel.

### SCENE 2 - The problem and why now (0:20 - 0:50)
**OPEN:** the push-in lands on the Buyer -> Ledger pipeline.
**TEXT:** `The race is on: ACP, AP2, x402, UPI. The missing piece: a verifiable gate.`
**SAY:**
> "The whole industry is racing to let agents pay / Google's AP2, x402, NPCI's UAP, Razorpay's own in-app pilots. / But an agent can buy the **wrong thing**, at the **wrong price**, **twice**, or because hidden text **told it to**. / So the missing piece is not another way to pay. / It is a boundary that can **verify** every payment. / That is BAZAAR."
**>>> TRANSITION:** quick **whip-pan** (a fast 0.2 s motion-blur swish) to Terminal 3. The
energy jump signals "now we do it for real," and swish + a music riser sells it.

### SCENE 3 - The idea, in one line (0:50 - 1:12)
**OPEN:** a clean terminal, cursor blinking.
**TEXT:** `Not "ask the AI if it's OK." A fixed checklist of 11 cryptographic checks.`
**SAY:**
> "BAZAAR does not ask a model 'is this payment OK.' / It runs a fixed checklist / eleven cryptographic checks. / All pass, it settles. / Any fail, it blocks / with one clear reason code, never 'the AI decided no.'"
**>>> TRANSITION:** NO cut. You are already in the terminal, so just start typing the
command. Letting the action continue is its own transition and keeps the momentum.

### SCENE 4 - It really pays: a live Razorpay payment (1:12 - 2:22)
**OPEN:** Terminal 3. **CLICK/type:** `make live`, Enter. Let each step land on screen.
**PAY WITH:** the domestic test card **`5267 3181 8797 5449`**, any future expiry, any CVV, then **Success**. If a card is ever refused as "international," click **Netbanking**, pick any bank, then **Success** (that path never hits the international issue). Test the payment step once off-camera first.
**TEXT (change per step):** `AUTHORIZE` -> `REAL ORDER: NOT PAID` -> `PAID (test card)` -> `SETTLED - once` -> `RETRY -> REFUSED`
**SAY, step by step:**
> (AUTHORIZE) "First, the gate authorizes it. Eleven checks, all pass."
> (ORDER, NOT PAID) "A **real** order on Razorpay Test Mode. / And notice, it defaults to **not paid**."
> (you pay with test card 5267 3181 8797 5449) "I pay with Razorpay's test card. / No real money moves / it refuses any non-test key."
> (SETTLED) "It reconciles against Razorpay, and settles. **Exactly once**."
> (RETRY REFUSED) "Charge the same order again / **refused**. It can never charge twice."
> (banner SETTLED ONCE. NEVER TWICE.) "One real payment, settled once, proven."
**>>> TRANSITION:** hold on the "SETTLED ONCE. NEVER TWICE." banner for a full beat, then a
gentle **0.4 s cross-dissolve** to the browser console. Dissolve = calm after the win, and
it visually says "same guarantee, new surface."

### SCENE 5 - Sellable to a real AI buyer: the AP2 rail (2:22 - 3:15)
**OPEN:** the console, **Console** tab. Left panel, top group "AP2 rail - signed carts."
**TEXT:** `A real AI buyer, over Google's AP2 protocol.`
**CLICK "Legit cart".** Watch it run Buyer -> Adapter -> Mandate -> Risk -> Gate -> Settle -> Ledger, verdict **Approved**, a signed Trust receipt on the right.
**SAY:**
> "This is a real AI buyer, paying over Google's AP2 protocol. / A signed cart, at the real price, in budget. / Watch it flow through the pipeline / verified, authorized by the gate, settled, and logged. / Approved, with a signed receipt."
**CLICK "Signature tamper".** Blocks: `AP2_INVALID_SIGNATURE`, at AP2 verification, before the gate.
**SAY:**
> "Now flip **one byte** of the signature. / Rejected at verification / before it ever reaches the money."
**CLICK "Over budget".** Blocks at the gate: `MANDATE_LIMIT_EXCEEDED`.
**SAY:**
> "And a **validly** signed cart, but over the cap. / The gate stops it at the limit."
**>>> TRANSITION:** NO cut. Slowly **scroll the left panel down** to "Red-team - direct
rail." A continuous in-UI scroll is the smoothest transition there is, no edit needed.

### SCENE 6 - The attack that is the whole thesis (3:15 - 3:58)
**OPEN:** left panel, bottom group "Red-team - direct rail."
**TEXT:** `The agent forges its own mandate. The gate catches it.`
**CLICK "Policy forgery".** Blocks: `MANDATE_IMMUTABLE`. Let it sit.
**SAY:**
> "This is the whole idea. / The agent forges its **own** mandate / doubles its **own** spending limit / and signs it with its **own** key. / But the gate pins the signature to a trusted issuer / so the forgery is caught. / An agent **cannot escalate its own authority**."
**CLICK "Prompt injection".** Blocks: `UNTRUSTED_INSTRUCTION`.
**SAY:**
> "Hide a payment instruction inside product text / the gate treats text as data, never a command. / Refused."
**CLICK** the Audit log on the right (point at it).
**SAY:**
> "Every refusal is written to a tamper-proof, hash-chained log, / and every decision gets a signed receipt. / Nothing here is faked. This is the real backend."
**>>> TRANSITION:** click the **Results** tab. Let the UI's own tab-switch (a quick slide)
BE the transition, then a barely-there 0.2 s speed-ramp so the scoreboard "snaps" in.

### SCENE 7 - The proof, in numbers (3:58 - 4:22)
**OPEN:** the **Results** tab (the scoreboard).
**TEXT:** `144 attacks -> 100% blocked - 0 escapes - 94 tests - green CI - AOV +7.72%`
**SAY:**
> "None of this is a one-off. / A hundred and forty-four attacks / a hundred percent blocked / zero false blocks / zero escapes across twenty thousand fuzzed states / ninety-four tests a clean machine re-runs on every push. / And it lifts order value seven-point-seven percent with a safe upsell / because trust is what lets a merchant say **yes**."
**>>> TRANSITION:** point at each number as you say it, then a slow **1 s fade to black**.
The fade is the "breath" before the tagline. Drop the music to almost nothing here.

### CLOSE (4:22 - 4:35)
**OPEN:** from black, the BAZAAR mark fades up.
**TEXT (big):** `Don't trust the agent. Test the authorization boundary.`
**SAY (slow, let each line land):**
> "Don't trust the agent. / Test the authorization boundary. / Intelligence proposes. / A fixed, cryptographic verifier **decides**. / That is BAZAAR."
**END CARD (hold 3 s, music resolves):**
`github.com/vedantjaiswal001/bazaar-work   -   vedantjaiswal001.github.io/bazaar-work`

---

## PART C - The transition map (your edit, at a glance)
1. Title -> Scene 1: **hard cut on the music downbeat.**
2. Scene 1 -> 2: **continuous push-in (Ken Burns), no cut.**
3. Scene 2 -> 3: **whip-pan** (0.2 s motion blur) + music riser.
4. Scene 3 -> 4: **no cut**, action continues (you type the command).
5. Scene 4 -> 5: **0.4 s cross-dissolve** off the SETTLED banner.
6. Scene 5 -> 6: **continuous in-UI scroll**, no edit.
7. Scene 6 -> 7: **the Results tab-switch itself**, + a 0.2 s snap.
8. Scene 7 -> Close: **1 s fade to black**, then fade the mark up.

Rule of thumb: hard cuts for energy (inside the terminal, on beats), dissolves/fades for
calm and "time passing," and continuous camera/UI motion whenever you can, because an
un-cut move always looks more expensive than an edit.

## PART D - Numbers you can say (all real, all reproducible)
11 checks; 9 attack classes; 144 attacks 100% blocked; 0% false-block on 400 legit;
0 escapes over 20,000 fuzzed states; 94 tests; green CI; ~0.10 ms per decision, ~9,600/sec;
AP2 1/1 cleared, 5/5 tampers caught; AOV +7.72%; one Test Mode payment, settled once.

## PART E - Never say (keeps you bulletproof)
Say "Test Mode," not "real money." Call the ML "advisory," never a fraud detector, the
**gate** is the guarantee. Say "the verifiable authorization layer," not "the first."

## PART F - Production polish (5 minutes in any free editor)
- Burn in the TEXT captions, big and bold, fading in as each scene starts (CapCut, Canva, DaVinci Resolve all do this fast).
- Soft, quiet background music; **duck it low** under every SAY line, and let it breathe in the Scene 7 fade and the close.
- Slow Ken Burns on any static screen so nothing feels frozen.
- 1080p, mp4, 30 fps. Under 5 minutes; under-run is fine, over-run is not.
- Record Scene 4 first, re-run `make live` until one take is flawless.

That is your world-class pitch video. Product working, not slides. Every number real.
