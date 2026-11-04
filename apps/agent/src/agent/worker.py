import asyncio
import logging
from collections.abc import AsyncIterable

from dotenv import load_dotenv
from livekit import rtc
from livekit.agents import Agent, AgentServer, JobContext, ModelSettings, cli

from agent.audio.smoothing import fade_out_tail
from agent.config import get_settings
from agent.constants import LOGGER_NAME
from agent.engines import build_session
from agent.prompts.persona import GREETING_INSTRUCTION, build_instructions

load_dotenv(".env.local")
load_dotenv(".env")

logger = logging.getLogger(LOGGER_NAME)
server = AgentServer()


class Receptionist(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=build_instructions())

    async def tts_node(self, text: AsyncIterable[str], model_settings: ModelSettings):
        return fade_out_tail(Agent.default.tts_node(self, text, model_settings))

    async def realtime_audio_output_node(
        self, audio: AsyncIterable[rtc.AudioFrame], model_settings: ModelSettings
    ) -> AsyncIterable[rtc.AudioFrame]:
        return fade_out_tail(Agent.default.realtime_audio_output_node(self, audio, model_settings))


async def _enforce_call_limit(session_close, max_call_seconds: int) -> None:
    await asyncio.sleep(max_call_seconds)
    logger.debug("call limit reached, closing session", extra={"max_call_seconds": max_call_seconds})
    await session_close()


async def _cancel_task(task: asyncio.Task) -> None:
    task.cancel()


@server.rtc_session(agent_name=get_settings().agent_name)
async def receptionist_session(context: JobContext) -> None:
    settings = get_settings()
    context.log_context_fields = {"room": context.room.name, "voice_engine": settings.voice_engine.value}
    try:
        session = build_session(settings)
        await session.start(room=context.room, agent=Receptionist())
        call_limit_task = asyncio.create_task(_enforce_call_limit(session.aclose, settings.max_call_seconds))
        context.add_shutdown_callback(lambda: _cancel_task(call_limit_task))
        await session.generate_reply(instructions=GREETING_INSTRUCTION)
    except Exception:
        logger.exception("receptionist session failed")
        raise


if __name__ == "__main__":
    cli.run_app(server)
