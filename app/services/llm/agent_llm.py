from app.services.llm.openai_provider import ChatGPTProvider
from app.services.llm.gemini_provider import GeminiProvider
from typing import Dict, Any
from app.settings import get_settings

settings = get_settings()

# Initialize providers
try:
    chatgpt_provider = ChatGPTProvider(settings.openai_api_key) if settings.openai_api_key else None
except Exception as e:
    print(f"Failed to initialize ChatGPT: {e}")
    chatgpt_provider = None

try:
    gemini_provider = GeminiProvider(settings.gemini_api_key) if settings.gemini_api_key else None
except Exception as e:
    print(f"Failed to initialize Gemini: {e}")
    gemini_provider = None


AGENT_LLM_MAP = {
    "researcher": gemini_provider,
    "coder": chatgpt_provider,
    "summarizer": gemini_provider,
    "orchestrator": chatgpt_provider,
}


async def get_llm_response(agent_role: str, prompt: str, context: Dict[str, Any] = None) -> str:
    """Get LLM response for a given agent role."""
    provider = AGENT_LLM_MAP.get(agent_role)
    if not provider:
        raise ValueError(f"Unknown agent role: {agent_role}")
    if provider is None:
        return f"LLM provider for {agent_role} not available. Please check API keys."
    return await provider.generate(prompt, context)
