from google.genai import Client
from google.genai.types import GenerateContentResponse
from config.settings import settings
from models.request import GenerationRequest
from providers.base import BaseProvider, GenerationResponse
from typing import Iterator



class GeminiProvider:

    def __init__(self):
        self.client = Client(api_key=settings.gemini_api_key)

    def generate(self, request:GenerationRequest) -> GenerationResponse:
        if request.config.stream:
            response = self.client.models.generate_content_stream(
                model=settings.gemini_model,
                contents=request.prompt,
                config={
                    "temperature": request.config.temperature,
                    "system_instruction": request.config.system_prompt,
                    "max_output_tokens": request.config.max_tokens,
                },
            )

            return self._stream_response(response)
        else:
            response = self.client.models.generate_content(
                model=settings.gemini_model,
                contents=request.prompt,
                config={
                    "temperature": request.config.temperature,
                    "system_instruction": request.config.system_prompt,
                    "max_output_tokens": request.config.max_tokens,
                },
            )

            return response.text
    
    def _stream_response(self, response: Iterator[GenerateContentResponse]) -> Iterator[str]:
        for chunk in response:
            content = chunk.text
            if content:
                yield content

       