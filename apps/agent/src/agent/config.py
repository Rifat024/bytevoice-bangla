from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

from agent.constants import VoiceEngine


class AgentSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=(".env", ".env.local"), extra="ignore")

    voice_engine: VoiceEngine = VoiceEngine.GEMINI_LIVE
    agent_name: str = "bytevoice-bn"
    max_call_seconds: int = 300

    gemini_live_model: str = "gemini-3.8-live"
    gemini_live_voice: str = "Kore"

    pipeline_stt_model: str = "gemini-3.5-transcribe-live"
    pipeline_llm_model: str = "gemini-2.5-flash"
    pipeline_tts_model: str = "gemini-3.8-flash-tts"
    pipeline_tts_voice: str = "Aoede"


@lru_cache
def get_settings() -> AgentSettings:
    return AgentSettings()
