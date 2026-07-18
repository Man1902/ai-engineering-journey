from abc import ABC, abstractmethod
from models.request import GenerationRequest
from models.response import GenerationResponse
from typing import Iterator, Union

class BaseProvider(ABC):

    @abstractmethod
    def generate(self, request: GenerationRequest) -> GenerationResponse:
        pass