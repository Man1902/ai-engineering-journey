from ollama import Client, ChatResponse
from config.settings import settings
from models.request import GenerationRequest
from providers.base import BaseProvider, GenerationResponse
from typing import Iterator

class OllamaProvider(BaseProvider):

    def __init__(self):
        self.client = Client(host=settings.ollama_host)

    def generate(self, request: GenerationRequest) -> GenerationResponse:
        
        response = self.client.chat(
            model=settings.ollama_model,
            messages=[
                {
                    "role": "system",
                    "content": request.config.system_prompt
                },
                {
                    "role" : "user",
                    "content": request.prompt
                }
            ],
            options={
                "temperature": request.config.temperature,
                "top_p": request.config.top_p
            },
            stream=request.config.stream
        )

        if request.config.stream:
           return self._stream_response(response)
        else:
           return response.message.content
        
    def _stream_response(self, response: Iterator[ChatResponse]) -> Iterator[str]:
        for chunk in response:
            content = chunk.message.content
            if content:
                yield content