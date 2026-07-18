from dataclasses import dataclass
from config.prompt_config import GenerationConfig

@dataclass
class GenerationRequest:

    prompt: str

    provider: str

    config: GenerationConfig