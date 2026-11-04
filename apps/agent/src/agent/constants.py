from enum import StrEnum
from zoneinfo import ZoneInfo

CLINIC_TIMEZONE = ZoneInfo("Asia/Dhaka")
LOGGER_NAME = "bytevoice.agent"
AGENT_DISPLAY_NAME = "Nila"


class VoiceEngine(StrEnum):
    AZURE_PIPELINE = "azure_pipeline"
    GEMINI_HYBRID = "gemini_hybrid"
    OPENAI_HYBRID = "openai_hybrid"
    GEMINI_NATIVE = "gemini_native"
    OPENAI_NATIVE = "openai_native"


SPEECH_PHRASE_HINTS = [
    "ওয়ান স্মাইল ডেন্টাল",
    "One Smile",
    "মুশফিকুর রুহান",
    "রাকিব হাসান",
    "নুসরাত জাহান",
    "appointment",
    "scaling",
    "root canal",
    "filling",
    "braces",
    "X-ray",
    "উত্তরা",
    "whitening",
]


BANGLA_WEEKDAY_NAMES = ("সোমবার", "মঙ্গলবার", "বুধবার", "বৃহস্পতিবার", "শুক্রবার", "শনিবার", "রবিবার")
BANGLA_DIGIT_TRANSLATION = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")
