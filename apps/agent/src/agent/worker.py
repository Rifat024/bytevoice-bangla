import asyncio
import logging

from dotenv import load_dotenv
from livekit.agents import Agent, AgentServer, JobContext, cli

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


async def _enforce_call_limit(session_close, max_call_seconds: int) -> None:
    await asyncio.sleep(max_call_seconds)
    logger.debug("call limit reached, closing session", extra={"max_call_seconds": max_call_seconds})
    await session_close()


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


async def _cancel_task(task: asyncio.Task) -> None:
    task.cancel()


if __name__ == "__main__":
    cli.run_app(server)
