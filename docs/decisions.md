# Decisions log

| Date (BST) | Decision | Why | Alternatives considered |
|---|---|---|---|
| 2026-11-04 | Next.js (Vercel) + Python LiveKit Agents worker + Supabase (Singapore) | WebRTC, interruption handling and one-line engine swaps from LiveKit; Python keeps tools, validation and extraction in one place; Singapore is the nearest Supabase region to Dhaka | Single Next.js app with a browser-side realtime SDK |
| 2026-11-04 | ~~Output voice fixed to Azure Neural TTS `bn-BD`~~ (superseded) | Native Bangladeshi voice | — |
| 2026-11-04 | **Gemini only:** `gemini_live` = Gemini 3.8 Live with `language="bn-BD"` (default); `gemini_pipeline` = Gemini transcribe-live (`bn-BD`+`en-US`, custom vocabulary) → 2.5 Flash → 3.8 Flash TTS with Dhaka-accent instructions | Azure requires a paid/card-verified account (owner could not sign up free); edge-tts is unofficial and returned HTTP 503 on first use; probe showed 3.8 Live accepts `bn-BD` (2.5 native audio rejects it) and no Live model supports text-only output, ruling out a Live + separate-TTS hybrid | Azure bn-BD voices, edge-tts, OpenAI Realtime |
| 2026-11-04 | Live voice: **Kore** (`GEMINI_LIVE_VOICE=Kore`) | Owner listened to Kore / Leda / Aoede `bn-BD` samples and picked Kore as the most natural Dhaka receptionist | Leda, Aoede |
| 2026-11-04 | 25 ms fade-out + 150 ms silence on the last frame of every agent utterance | Owner heard noise at the end of samples; analysis showed an abrupt cut (click), not model noise | Leave raw output |
| 2026-11-04 | Demo clinic modelled on One Smile Dental Lounge, Uttara (public Facebook info); hours, fees and two doctors are demo values; UI labelled "Demo, not affiliated" | Realistic Bangladeshi clinic context for the reviewer | Fully fictional clinic |

## Voice test results

Probe (text-prompted, 4 Nov): `gemini-3.8-live` bn-BD first audio 1.59–1.66 s across Kore/Leda/Aoede; `gemini-3.1-flash-live-preview` 1.73 s; Flash TTS 6.5–7.3 s for a 20 s paragraph (non-streamed).

Fill in after running the README §3 test script by voice (scores 1–5).

| Engine / voice | Sounds Bangladeshi | Natural phrasing | Code-switching | Digits | Names | Latency (s) | Barge-in | Total |
|---|---|---|---|---|---|---|---|---|
| gemini_live / Kore | | | | | | | | |
| gemini_live / Leda | | | | | | | | |
| gemini_pipeline / Aoede | | | | | | | | |

## Free-tier-only rule (owner requirement)

Every service must run on a free tier; no paid usage.

| Service | Free tier used | Watch out for |
|---|---|---|
| Google AI Studio (Gemini 2.5 Flash / Live) | Free API key | Per-minute request limits; fall back to `gemini-2.5-flash-lite` if a call hits 429 |
| LiveKit Cloud | Build (free) plan | Monthly agent-session minutes |
| Supabase | Free project (Singapore) | Project pauses after a week idle; keep it active until assessment ends |
| Vercel | Hobby | None for this demo |
| GitHub | Free private repo | Add reviewers as collaborators or make public at submission |
| Agent hosting | LiveKit Cloud agent deploy (free plan) or Render free web service + uptime ping | Render free sleeps when idle |

No OpenAI or Azure usage.
