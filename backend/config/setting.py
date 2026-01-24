from pydantic import BaseSettings

class Settings(BaseSettings):
    # OpenAI API Configuration
    openai_api_key: str
    openai_model: str = "gpt-3.5-turbo"  # Default model
    openai_max_tokens: int = 1000
    openai_temperature: float = 0.7

    # Application Settings
    app_name: str = "Resume AI Analysis"
    debug: bool = False

    # Database or other configs can be added here
    # database_url: Optional[str] = None

    class Config:
        env_file = ".env"
        case_sensitive = False

# Create a global settings instance
settings = Settings()
