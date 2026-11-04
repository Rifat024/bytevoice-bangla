from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

from agent.constants import VoiceEngine


class AgentSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=(".env", ".env.local"), extra="ignore")

    voice_engine: VoiceEngine = VoiceEngine.AZURE_PIPELINE
    agent_name: str = "bytevoice-bn"
    max_call_seconds: int = 300

    gemini_native_model: str = "gemini-2.5-flash-native-audio-preview-12-2025"
    gemini_hybrid_model: str = "gemini-live-2.5-flash-preview"
    gemini_voice: str = "Aoede"

    openai_realtime_model: str = "openai/gpt-realtime"
    openai_voice: str = "marin"

    azure_stt_languages: list[str] = ["bn-BD", "en-US"]
    azure_tts_voice: str = "bn-BD-NabanitaNeural"
    azure_tts_language: str = "bn-BD"
    pipeline_llm_model: str = "gemini-2.5-flash"


@lru_cache
def get_settings() -> AgentSettings:
    return AgentSettings()
