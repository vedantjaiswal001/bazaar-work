# BAZAAR - the final video script (punchy cut, with on-screen text)

Use this one; it replaces the earlier scripts. Every scene gives you four things:
**SHOW** (what is on screen), **TEXT** (the big caption to add on screen while editing),
**SAY** (short, punchy narration, read it almost word-for-word), and the **time**.

`/` means a short pause. **bold** means hit that word a little harder. Keep energy up.
Target 2 min 30 s. All numbers are real.

**Why the on-screen text matters:** many judges watch the first few seconds muted. The
captions carry the story even with no sound, and they make the whole thing look
finished. Any free editor does this in minutes (CapCut, Canva, or DaVinci Resolve).

---

## TITLE CARD (0:00 - 0:02)
**SHOW:** black screen, then your BAZAAR wordmark.
**TEXT (big, centered):** `BAZAAR - a deterministic authorization gate for AI-to-AI commerce`
No narration. Let it sit 2 seconds, then cut to the live page.

---

## SCENE 1 - Hook (0:02 - 0:14)
**SHOW:** the live page header with the stat chips (100%, 0%, 0, +7.72%, 0.13 ms).
**TEXT:** `AI agents can already spend money. Should they be allowed to?`
**SAY:**
> "AI agents can already spend your money. / The real question is whether they should be **allowed** to. / BAZAAR decides that on every payment / in a tenth of a millisecond / and the agent **cannot** overrule it."

Director's note: this is the whole pitch in five breaths. Slow down on "cannot overrule it," then cut.

---

## SCENE 2 - The idea (0:14 - 0:32)
**SHOW:** slowly scroll the page to the line "LLMs propose. Policies constrain. A deterministic verifier authorizes."
**TEXT:** `Not "ask the AI if it's OK." A fixed checklist of 11 cryptographic checks.`
**SAY:**
> "The danger is not that the agent can't buy. / It is that it can buy the **wrong thing**, at the **wrong price**, **twice**, or after being **told to** by hidden text. / So BAZAAR does not ask a model 'is this OK.' / It runs a fixed checklist / eleven cryptographic checks. / All pass, it settles. / Any fail, it blocks / with one clear reason code."

Director's note: the four dangers (wrong thing / wrong price / twice / told to) are the four attacks you fire later. Say them crisply.

---

## SCENE 3 - Moment 1: a real payment, settled once (0:32 - 1:25)
**SHOW:** your terminal. Type `make live`, press Enter, let each step land.
**TEXT (change per step):** `AUTHORIZE` -> `REAL ORDER - status: NOT PAID` -> `PAID (test card)` -> `SETTLED - once` -> `RETRY -> REFUSED`

**SAY, step by step:**
> (AUTHORIZE prints) "First, before any money moves, the gate authorizes it. / Eleven checks, all pass."
> (ORDER prints, NOT PAID) "A **real** order on Razorpay Test Mode. / Notice, it defaults to **not paid**."
> (you pay with test card 5267 3181 8797 5449) "I pay with Razorpay's test card. / No real money moves / the client refuses any non-test key."
> (SETTLED prints) "It reconciles against Razorpay, and settles. / **Exactly once**."
> (RETRY REFUSED prints) "Try to charge the same order again / **refused**. It can never charge twice."
> (banner: SETTLED ONCE. NEVER TWICE.) "One real payment, settled once, proven. / Now watch it turn hostile."

Director's note: record this scene FIRST and re-run until one take is clean, it is the only part that touches the network. Pause on the "SETTLED ONCE. NEVER TWICE." banner.

---

## SCENE 4 - Moment 2: the attack it refuses (1:25 - 2:20)
**SHOW:** the live page, Red Team tab. Click four attacks; let the checklist cascade and the failing check turn red.
**TEXT (per attack):** `Spend over the cap -> BLOCKED` / `Prompt injection -> BLOCKED` / `Replay -> BLOCKED` / `Forge its own mandate -> BLOCKED`

**SAY:**
> "Same gate, live. I'll attack it like a hacked agent would."
> (click **Budget**) "Spend above its limit. / Refused at the cap."
> (click **Prompt injection**) "Hide a payment instruction inside product text. / The gate treats text as data, never a command. / Refused."
> (click **Replay**) "Replay a payment that already happened. / Refused."
> (click **Policy forgery**, let it sit) "And here is the whole idea. / The agent forges its **own** mandate / doubles its **own** limit / signs it with its **own** key. / The gate pins the signature to a trusted issuer / so the forgery is caught. / An agent **cannot escalate its own authority**."
> (point at the audit log) "Every refusal is written to a tamper-proof, hash-chained log. / Nothing here is faked. Each click hit the real backend."

Director's note: **Policy forgery is your money shot.** Save it for last, slow down, let it breathe. This is the moment they remember.

---

## SCENE 5 - The proof (2:20 - 2:40)
**SHOW:** the Benchmark tab. Show the scoreboard cards, then the AP2 panel (1/1, 5/5).
**TEXT:** `144 attacks -> 100% blocked - 0 escapes - 94 tests - green CI` / `Real AP2 AI buyer: 1/1 cleared, 5/5 tampers caught`
**SAY:**
> "This isn't a one-off. / A hundred and forty-four attacks / a hundred percent blocked / zero false blocks / zero escapes across twenty thousand fuzzed states / ninety-four tests re-run on every push. / And it accepts a real Google **AP2** cart from an AI buyer / one cleared, five tampers caught / through the same gate."

Director's note: point at each number as you say it.

---

## SCENE 6 - Close (2:40 - 2:58)
**SHOW:** back to the header, or hold on the AP2 result.
**TEXT (big):** `Don't trust the agent. Test the authorization boundary.`
**SAY:**
> "Agentic commerce doesn't scale until the authorization is **trustworthy**. / That is the unlock / and it doesn't cost growth / the same gate lifted order value seven-point-seven percent with a safe upsell. / The rule is simple. / **Don't trust the agent. Test the authorization boundary.** / Intelligence proposes. / A fixed, cryptographic verifier **decides**. / That is BAZAAR."

Director's note: slow right down for the last four lines. Let "That is BAZAAR." land, then cut.

---

## END CARD (2:58 - 3:00)
**TEXT:** `BAZAAR   -   github.com/vedantjaiswal001/bazaar-work   -   vedantjaiswal001.github.io/bazaar-work`
Hold 2 seconds. Done.

---

## If you're nervous about narration (a fully honest backup plan)
You do **not** have to talk over the whole thing. A great version is: on-screen text
(the TEXT lines above) + soft background music + the live screen recordings, with your
voice only on the hook (Scene 1) and the close (Scene 6). The captions carry the middle.
This still looks professional and is much easier to nail.

## Numbers you can say (all real)
11 checks; 9 attack classes; 144 attacks 100% blocked; 0% false-block on 400 legit;
0 escapes over 20,000 fuzzed states; 94 tests; ~0.13 ms per decision, ~7,000/sec;
AP2 1/1 cleared, 5/5 tampers caught; AOV +7.72%; one Test Mode payment, settled once.

## Never say (keeps you bulletproof)
Say "Test Mode," not "real money." Call the ML "advisory," never a fraud detector, the
**gate** is the guarantee. Say "the verifiable authorization layer," not "the first."

## Make it look pro (5 minutes in any free editor)
- Add the TEXT captions as big, bold text that appears with each scene.
- Soft, quiet background music; duck it under your key lines.
- 1080p, mp4, 30fps. Keep it under 3 minutes.
- Record Scene 3 first, re-run `make live` until one take is flawless; everything else is deterministic and can't glitch.
