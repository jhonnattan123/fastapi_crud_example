import os
from pydantic import BaseModel
from dotenv import dotenv_values

class BaseConfig(BaseModel):
    """ Configuracion base de la API.

    Attributes:
        API_NAME (str): Nombre de la API.
        API_PREFIX (str): Prefijo de la API.
        VERSION (str): Versión de la API.
    """
    config = {
        **dotenv_values(".env"),
        **os.environ,
    }
    API_NAME: str = config.get("NOMBRE_API", "API_USUARIOS")
    API_PREFIX: str = config.get("API_PREFIX", "/api/v1")
    OPENAPI_URL: str = config.get("OPENAPI_URL", "openapi.json")
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    VERSION: str = open(os.path.join(BASE_DIR, "VERSION")).read().strip()
    config = {
        **config,
        "API_NAME": API_NAME,
        "API_PREFIX": API_PREFIX,
        "VERSION": VERSION,
        "BASE_DIR": BASE_DIR,
        "OPENAPI_URL": OPENAPI_URL,
    }
