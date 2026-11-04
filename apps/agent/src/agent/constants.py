from enum import StrEnum
from zoneinfo import ZoneInfo

CLINIC_TIMEZONE = ZoneInfo("Asia/Dhaka")
LOGGER_NAME = "bytevoice.agent"
AGENT_DISPLAY_NAME = "Nila"

BANGLADESH_LANGUAGE_CODE = "bn-BD"
RECOGNITION_LANGUAGE_CODES = ["bn-BD", "en-US"]

FADE_OUT_SECONDS = 0.025
TRAILING_SILENCE_SECONDS = 0.15


class VoiceEngine(StrEnum):
    GEMINI_LIVE = "gemini_live"
    GEMINI_PIPELINE = "gemini_pipeline"


BANGLADESHI_ACCENT_INSTRUCTIONS = (
    "Speak as a warm, polite young female receptionist from Dhaka, Bangladesh. Use natural everyday "
    "Bangladeshi Bangla with a standard Dhaka accent, never a Kolkata or West Bengal accent. "
    "Calm, friendly, clear, at a natural phone-call pace. Pronounce English loanwords the way Bangladeshi "
    "people do. Read phone digits slowly, one by one."
)

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
