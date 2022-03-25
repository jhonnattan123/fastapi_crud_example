from api.configuration import BaseConfig
from fastapi import FastAPI

def create_app() -> FastAPI:
    """ Crea la aplicación FastAPI.
    Llama a obtener_routers() para registrar las rutas.
    """
    try:

        base_config = BaseConfig()
        app = FastAPI(
            title=base_config.API_NAME,
            version=base_config.VERSION,
        )
        app.config = base_config.config
        app.memory = dict()
        app.key_memory = dict()
        
        obtener_routers(app)

        return app
    
    except Exception as e:
        raise Exception(f"Error al crear la aplicación: {str(e)}")

def obtener_routers( app: FastAPI ) -> None:
    """ Importa los routers de los módulos y los registra en la aplicación.

    :param app: aplicación FastAPI
    """
    try:

        from api.routers import usuarios
        app.include_router(usuarios.usuarios_router().router, prefix=app.config["API_PREFIX"])

    except Exception as e:
        raise Exception("Error al obtener los routers: " + str(e))