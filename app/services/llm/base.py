from abc import ABC, abstractmethod
from typing import Dict, Any
import asyncio


class LLMProvider(ABC):
    @abstractmethod
    async def generate(self, prompt: str, context: Dict[str, Any]) -> str:
        """Generate response from LLM based on prompt and context."""
        pass
