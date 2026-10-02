import google.generativeai as genai
from typing import Dict, Any
from app.services.llm.base import LLMProvider
from app.settings import get_settings


class GeminiProvider(LLMProvider):
    def __init__(self, api_key: str = None):
        settings = get_settings()
        self.api_key = api_key or settings.gemini_api_key
        if not self.api_key:
            raise ValueError("Gemini API key not provided")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel("gemini-pro")

    async def generate(self, prompt: str, context: Dict[str, Any] = None) -> str:
        try:
            response = await self.model.generate_content_async(prompt)
            return response.text
        except Exception as e:
            return f"Error from Gemini: {str(e)}"
