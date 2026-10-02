import openai
from typing import Dict, Any
from app.services.llm.base import LLMProvider
from app.settings import get_settings


class ChatGPTProvider(LLMProvider):
    def __init__(self, api_key: str = None):
        settings = get_settings()
        self.api_key = api_key or settings.openai_api_key
        if not self.api_key:
            raise ValueError("OpenAI API key not provided")
        self.client = openai.AsyncOpenAI(api_key=self.api_key)

    async def generate(self, prompt: str, context: Dict[str, Any] = None) -> str:
        try:
            response = await self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert AI assistant helping with complex tasks."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
                max_tokens=2048,
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error from ChatGPT: {str(e)}"
