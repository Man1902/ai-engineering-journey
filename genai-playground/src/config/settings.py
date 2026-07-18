from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    default_provider: str = "ollama"

    ollama_model: str
    ollama_host: str

    gemini_model: str
    gemini_api_key: str

    openai_model: str
    openai_api_key: str

    class Config:
        env_file = ".env"


settings = Settings()