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
