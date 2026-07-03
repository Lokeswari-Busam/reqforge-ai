from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    
    # App
    APP_NAME: str
    APP_VERSION: str
    ENVIRONMENT: str

    # Server
    HOST: str
    PORT: int

     # Database
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_SSL_MODE: str

     # Authentication
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # AI
    GOOGLE_API_KEY: str = ""

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
            f"?sslmode={self.DB_SSL_MODE}"
        )
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()