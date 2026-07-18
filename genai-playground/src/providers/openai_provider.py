from openai import OpenAI, Stream
from openai.types.responses import ResponseStreamEvent
from config.settings import settings
from models.request import GenerationRequest
from providers.base import BaseProvider, GenerationResponse
from typing import Iterator

class OpenAIProvider:

    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)

    def generate(self, request:GenerationRequest) -> GenerationResponse:
        response = self.client.responses.create(
            model=settings.openai_model,
            input=[
                {
                    "role": "system",
                    "content": request.config.system_prompt,
                },
                {
                    "role": "user",
                    "content": request.prompt,
                },
            ],
            temperature=request.config.temperature,
            max_output_tokens=request.config.max_tokens,
            stream=request.config.stream
        )

        if request.config.stream:
            return self._stream_response(response)
        else:
            return response.output_text
        
    def _stream_response(self, response: Stream[ResponseStreamEvent]) -> Iterator[str]:
        for chunk in response:
            content = chunk.output_text
            if content:
                yield content