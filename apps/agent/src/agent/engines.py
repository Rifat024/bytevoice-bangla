import logging

from google.genai.types import Modality
from livekit.agents import AgentSession, inference
from livekit.plugins import azure, google, openai, silero

from agent.config import AgentSettings
from agent.constants import LOGGER_NAME, SPEECH_PHRASE_HINTS, VoiceEngine

logger = logging.getLogger(LOGGER_NAME)


def _bangladeshi_voice(settings: AgentSettings) -> azure.TTS:
    return azure.TTS(voice=settings.azure_tts_voice, language=settings.azure_tts_language)


def _openai_realtime(settings: AgentSettings, modalities: list[str]):
    if settings.openai_realtime_model.startswith("openai/"):
        return inference.RealtimeModel(model=settings.openai_realtime_model, modalities=modalities)
    return openai.realtime.RealtimeModel(
        model=settings.openai_realtime_model, voice=settings.openai_voice, modalities=modalities
    )


def build_session(settings: AgentSettings) -> AgentSession:
    engine = settings.voice_engine
    logger.debug("building agent session", extra={"voice_engine": engine.value})

    if engine is VoiceEngine.AZURE_PIPELINE:
        return AgentSession(
            vad=silero.VAD.load(),
            stt=azure.STT(language=settings.azure_stt_languages, phrase_list=SPEECH_PHRASE_HINTS),
            llm=google.LLM(model=settings.pipeline_llm_model, temperature=0.6),
            tts=_bangladeshi_voice(settings),
        )

    if engine is VoiceEngine.GEMINI_HYBRID:
        return AgentSession(
            llm=google.realtime.RealtimeModel(
                model=settings.gemini_hybrid_model, modalities=[Modality.TEXT], temperature=0.6
            ),
            tts=_bangladeshi_voice(settings),
        )

    if engine is VoiceEngine.OPENAI_HYBRID:
        return AgentSession(llm=_openai_realtime(settings, ["text"]), tts=_bangladeshi_voice(settings))

    if engine is VoiceEngine.GEMINI_NATIVE:
        return AgentSession(
            llm=google.realtime.RealtimeModel(
                model=settings.gemini_native_model, voice=settings.gemini_voice, temperature=0.7
            ),
        )

    if engine is VoiceEngine.OPENAI_NATIVE:
        return AgentSession(llm=_openai_realtime(settings, ["text", "audio"]))

    raise ValueError(f"Unsupported voice engine: {engine}")
