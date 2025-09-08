from pydantic_settings import BaseSettings, SettingsConfigDict

# Algumas configurações padrões foram definidas, mas informações críticas como a URI de conexão estão na .env
class DatabaseSettings(BaseSettings):
    uri: str = "mongodb://localhost:27017"
    database: str = "cachacho"
    collection: str = "caxarro"

    model_config = SettingsConfigDict(env_file=".env", env_prefix='MONGODB_')