import logging

from google.genai import types
from livekit.agents import AgentSession
from livekit.plugins import google, silero

from agent.config import AgentSettings
from agent.constants import (
    BANGLADESH_LANGUAGE_CODE,
    BANGLADESHI_ACCENT_INSTRUCTIONS,
    LOGGER_NAME,
    RECOGNITION_LANGUAGE_CODES,
    SPEECH_PHRASE_HINTS,
    VoiceEngine,
)

logger = logging.getLogger(LOGGER_NAME)


def build_session(settings: AgentSettings) -> AgentSession:
    engine = settings.voice_engine
    logger.debug("building agent session", extra={"voice_engine": engine.value})

    if engine is VoiceEngine.GEMINI_LIVE:
        return AgentSession(
            llm=google.realtime.RealtimeModel(
                model=settings.gemini_live_model,
                voice=settings.gemini_live_voice,
                language=BANGLADESH_LANGUAGE_CODE,
                temperature=0.6,
                input_audio_transcription=types.AudioTranscriptionConfig(),
                output_audio_transcription=types.AudioTranscriptionConfig(),
            ),
        )

    if engine is VoiceEngine.GEMINI_PIPELINE:
        return AgentSession(
            vad=silero.VAD.load(),
            stt=google.beta.GeminiSTT(
                model=settings.pipeline_stt_model,
                language_codes=RECOGNITION_LANGUAGE_CODES,
                custom_vocabulary=SPEECH_PHRASE_HINTS,
            ),
            llm=google.LLM(model=settings.pipeline_llm_model, temperature=0.6),
            tts=google.beta.GeminiTTS(
                model=settings.pipeline_tts_model,
                voice_name=settings.pipeline_tts_voice,
                instructions=BANGLADESHI_ACCENT_INSTRUCTIONS,
            ),
        )

    raise ValueError(f"Unsupported voice engine: {engine}")
