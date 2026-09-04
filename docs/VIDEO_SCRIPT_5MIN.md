# BAZAAR - the 5-minute pitch video (final, detailed shot list)

This is the definitive script. Use this one. It targets ~4 min 50 s, matches what the
Razorpay form wants ("a 5-min pitch video" + "what broke, and how you got out"), and
tells you exactly what to open, what to click, what to say, and how to transition between
scenes.

Legend: **OPEN** = what to have on screen. **CLICK** = what to do. **SAY** = read this
(short, punchy, close to word-for-word). **TEXT** = big caption to add on screen while
editing. **TRANSITION** = how to move to the next scene. `/` = short pause.

---

## PART A - Set up before you record (~10 min)

Open three terminals in your `bazaar` folder and one browser:
- **Terminal 1:** `make run`   (backend on :8000)
- **Terminal 2:** `make web`   (console on :5173)
- **Terminal 3:** keep free for `make live` (your `rzp_test_` keys must be in `.env`)
- **Browser:** open **http://localhost:5173** (your console, the Console/Results screen)

Do one silent dry run of `make live`, and one click-through of the console, so nothing
surprises you. Turn on Do Not Disturb. Terminal font 18-22 pt. Record 1080p, 30fps.

Reliability note: if the backend will not cooperate on the day, you can record the
interactive parts on the always-on page **https://vedantjaiswal001.github.io/bazaar-work/**
instead (its tabs are named differently: Red Team and Benchmark). The terminal `make live`
scene is identical either way. But the local console is the richer "real backend" demo, so
use it if it is running.

Record in this order (safest): Scene 4 (`make live`) first, re-run until one take is clean;
then the console scenes; then record your voice over the whole thing, or narrate live.

---

## PART B - The script

### TITLE CARD (0:00 - 0:03)
**OPEN:** black, then your BAZAAR mark.
**TEXT (center):** `BAZAAR - a deterministic authorization gate for AI-to-AI commerce`
No voice. Hold 3 seconds.
**TRANSITION:** hard cut to the console header.

### SCENE 1 - Hook (0:03 - 0:20)
**OPEN:** the console header (Bazaar, the KPIs: 94 tests, 100% blocked, 0% false-block).
**TEXT:** `AI agents can already spend money. Should they be allowed to?`
**SAY:**
> "AI agents can already spend your money. / The real question is whether they should be **allowed** to. / BAZAAR decides that on every payment / in a tenth of a millisecond / and the agent **cannot** overrule it."
**TRANSITION:** slow zoom in on the "Authorization" pipeline in the middle of the screen.

### SCENE 2 - The problem and why now (0:20 - 0:50)
**OPEN:** stay on the console; gesture at the Buyer to Ledger pipeline.
**TEXT:** `The global race: AP2, x402, UPI Reserve Pay. The missing piece: a verifiable gate.`
**SAY:**
> "The whole industry is racing to let agents pay / Google's AP2, x402, Razorpay's own UPI Reserve Pay. / But an agent can buy the **wrong thing**, at the **wrong price**, **twice**, or because it was **told to** by hidden text. / So the missing piece is not another way to pay. / It is a boundary that can **verify** every payment. / That is BAZAAR."
**TRANSITION:** quick cut to Terminal 3.

### SCENE 3 - The idea, in one line (0:50 - 1:15)
**OPEN:** a clean terminal (or the console's pipeline).
**TEXT:** `Not "ask the AI if it's OK." A fixed checklist of 11 cryptographic checks.`
**SAY:**
> "BAZAAR does not ask a model 'is this payment OK.' / It runs a fixed checklist / eleven cryptographic checks. / All pass, it settles. / Any fail, it blocks / with one clear reason code, never 'the AI decided no.'"
**TRANSITION:** stay in the terminal, type the command.

### SCENE 4 - It really pays: a live Razorpay payment (1:15 - 2:25)
**OPEN:** Terminal 3. **CLICK/type:** `make live`, press Enter. Let each step land.
**PAY WITH:** the domestic test card **`5267 3181 8797 5449`**, any future expiry, any CVV, then click **Success**. If a card is ever refused as "international," click **Netbanking**, pick any bank, then **Success** (that path never has the international issue). Test the payment step once off-camera first.
**TEXT (change per step):** `AUTHORIZE` -> `REAL ORDER: NOT PAID` -> `PAID (test card)` -> `SETTLED - once` -> `RETRY -> REFUSED`
**SAY, step by step:**
> (AUTHORIZE) "First, the gate authorizes it. Eleven checks, all pass."
> (ORDER, NOT PAID) "A **real** order on Razorpay Test Mode. / And notice, it defaults to **not paid**."
> (you pay with test card 5267 3181 8797 5449, any future expiry, any CVV) "I pay with Razorpay's test card. / No real money moves / it refuses any non-test key."
> (SETTLED) "It reconciles against Razorpay, and settles. **Exactly once**."
> (RETRY REFUSED) "Charge the same order again / **refused**. It can never charge twice."
> (banner SETTLED ONCE. NEVER TWICE.) "One real payment, settled once, proven."
**TRANSITION:** cut to the browser at localhost:5173 (Console tab). A half-second fade works well here.

### SCENE 5 - Sellable to a real AI buyer: the AP2 rail (2:25 - 3:20)
**OPEN:** the console, **Console** tab. Left panel, top group "AP2 rail - signed carts."
**TEXT:** `A real AI buyer, over Google's AP2 protocol.`
**CLICK "Legit cart".** Watch the pipeline run Buyer -> Adapter -> Mandate -> Risk -> Gate -> Settle -> Ledger, verdict **Approved**, a signed Trust receipt appears on the right.
**SAY:**
> "This is a real AI buyer, paying over Google's AP2 protocol. / A signed cart, at the real price, in budget. / Watch it flow through the pipeline / verified, authorized by the gate, settled, and logged. / Approved, with a signed receipt."
**CLICK "Signature tamper".** It blocks: `AP2_INVALID_SIGNATURE`, at AP2 verification, before the gate.
**SAY:**
> "Now flip **one byte** of the signature. / Rejected at verification / before it ever reaches the money."
**CLICK "Over budget".** It blocks at the gate: `MANDATE_LIMIT_EXCEEDED`.
**SAY:**
> "And a **validly** signed cart, but over the cap. / The gate stops it at the limit."
**TRANSITION:** stay in the console; scroll the left panel down to "Red-team - direct rail."

### SCENE 6 - The attack that is the whole thesis (3:20 - 4:05)
**OPEN:** left panel, bottom group "Red-team - direct rail."
**TEXT:** `The agent forges its own mandate. The gate catches it.`
**CLICK "Policy forgery".** It blocks: `MANDATE_IMMUTABLE`. Let it sit.
**SAY:**
> "This is the whole idea. / The agent forges its **own** mandate / doubles its **own** spending limit / and signs it with its **own** key. / But the gate pins the signature to a trusted issuer / so the forgery is caught. / An agent **cannot escalate its own authority**."
**CLICK "Prompt injection".** It blocks: `UNTRUSTED_INSTRUCTION`.
**SAY:**
> "Hide a payment instruction inside product text / the gate treats text as data, never a command. / Refused."
**CLICK** the Audit log on the right (point at it).
**SAY:**
> "Every refusal is written to a tamper-proof, hash-chained log, / and every decision gets a signed receipt. / Nothing here is faked. This is the real backend."
**TRANSITION:** click the **Results** tab at the top.

### SCENE 7 - The proof, in numbers (4:05 - 4:30)
**OPEN:** the **Results** tab (the scoreboard).
**TEXT:** `144 attacks -> 100% blocked - 0 escapes - 94 tests - green CI`
**SAY:**
> "None of this is a one-off. / A hundred and forty-four attacks / a hundred percent blocked / zero false blocks / zero escapes across twenty thousand fuzzed states / ninety-four tests a clean machine re-runs on every push. / And it lifts order value seven-point-seven percent with a safe upsell / because trust is what lets a merchant say **yes**."
**TRANSITION:** slow fade to a plain dark card for the honest-story beat.

### SCENE 8 - What broke, and how we got out (4:30 - 4:55)
**OPEN:** a simple dark slide, or hold on the pipeline.
**TEXT:** `What broke: our security control was fail-open. How we got out: we made it fail-closed.`
**SAY:**
> "One honest story. / Our headline promise is that an agent can't forge its own mandate. / A late review found the check was **opt-in** / if a caller forgot the trusted keys, it silently turned off. / We made it **fail-closed** / it now refuses to run without them / and a test makes sure it never regresses. / A control that is off when you forget / is not a control."
**TRANSITION:** cut to the BAZAAR mark for the close.

### SCENE 9 - Close (4:55 - 5:05)
**OPEN:** the BAZAAR mark or the header.
**TEXT (big):** `Don't trust the agent. Test the authorization boundary.`
**SAY:**
> "Don't trust the agent. / Test the authorization boundary. / Intelligence proposes. / A fixed, cryptographic verifier **decides**. / That is BAZAAR."
**END CARD (hold 3s):** `github.com/vedantjaiswal001/bazaar-work   -   vedantjaiswal001.github.io/bazaar-work`

---

## PART C - Numbers you can say (all real)
11 checks; 9 attack classes; 144 attacks 100% blocked; 0% false-block on 400 legit;
0 escapes over 20,000 fuzzed states; 94 tests; green CI; ~0.13 ms per decision, ~7,000/sec;
AP2: 1/1 cleared, 5/5 tampers caught; AOV +7.72%; one Test Mode payment, settled once.

## PART D - Never say (keeps you bulletproof)
Say "Test Mode," not "real money." Call the ML "advisory," never a fraud detector, the
**gate** is the guarantee. Say "the verifiable authorization layer," not "the first."

## PART E - Transitions cheat-sheet (keep it smooth)
- Scene to scene: a **0.3 to 0.5 second cross-fade** looks pro; use a hard cut only inside the terminal.
- Zoom slowly (Ken Burns) on static screens so nothing feels frozen.
- Add soft, quiet background music; **duck it low** under every SAY line.
- Burn in the TEXT captions, big and bold, appearing as you start each scene.
- Keep it under 5 minutes. Under-run is fine; over-run is not.

Record Scene 4 (`make live`) first and re-run until one take is flawless. Everything else
is deterministic and cannot glitch. That is your world-class five-minute video.
