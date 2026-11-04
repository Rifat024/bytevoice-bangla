# Decisions log

| Date (BST) | Decision | Why | Alternatives considered |
|---|---|---|---|
| 2026-11-04 | Next.js (Vercel) + Python LiveKit Agents worker + Supabase (Singapore) | WebRTC, interruption handling and one-line engine swaps from LiveKit; Python keeps tools, validation and extraction in one place; Singapore is the nearest Supabase region to Dhaka | Single Next.js app with a browser-side realtime SDK |
| 2026-11-04 | Output voice fixed to Azure Neural TTS `bn-BD` (Nabanita / Pradeep) | Owner requirement: native Bangladeshi Bangla, not Indian/Kolkata. Azure is the major provider with Bangladesh-locale neural voices | Gemini / OpenAI native-audio voices (generic or West-Bengal-leaning accent) |
| 2026-11-04 | Speech recognition: Azure STT with `["bn-BD","en-US"]` and a phrase list | Code-switching ("appointment", "scaling") and doctor-name accuracy | Single-language STT |
| 2026-11-04 | Demo clinic modelled on One Smile Dental Lounge, Uttara (public Facebook info); hours, fees and two doctors are demo values; UI labelled "Demo, not affiliated" | Realistic Bangladeshi clinic context for the reviewer | Fully fictional clinic |

## Voice bake-off results

Fill in after running the test script in README §3 (scores 1–5).

| Engine | Sounds Bangladeshi | Natural phrasing | Code-switching | Digits | Names | Latency (s) | Barge-in | Total |
|---|---|---|---|---|---|---|---|---|
| azure_pipeline | | | | | | | | |
| gemini_hybrid | | | | | | | | |
| openai_hybrid | | | | | | | | |
| gemini_native (reference) | | | | | | | | |

## Free-tier-only rule (owner requirement)

Every service must run on a free tier; no paid usage.

| Service | Free tier used | Watch out for |
|---|---|---|
| Google AI Studio (Gemini 2.5 Flash / Live) | Free API key | Per-minute request limits; fall back to `gemini-2.5-flash-lite` if a call hits 429 |
| Azure Speech | F0 resource, Southeast Asia | Monthly audio-hour (STT) and character (TTS) caps; keep the 5-min call cap |
| LiveKit Cloud | Build (free) plan | Monthly agent-session minutes; `openai_hybrid` only through LiveKit Inference included credits, never a paid OpenAI key |
| Supabase | Free project (Singapore) | Project pauses after a week idle; keep it active until assessment ends |
| Vercel | Hobby | None for this demo |
| GitHub | Free private repo | Add reviewers as collaborators or make public at submission |
| Agent hosting | LiveKit Cloud agent deploy (free plan) or Render free web service + uptime ping | Render free sleeps when idle |

`OPENAI_API_KEY` stays empty. `openai_native` / direct OpenAI are not used.
