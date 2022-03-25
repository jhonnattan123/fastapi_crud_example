import datetime
from uuid import UUID
from api.actions import storage
from fastapi import HTTPException
from api.models.usuario import Usuario
from starlette.requests import Request
from api.dependencies import validar_email, validar_formato_fecha,validar_edad

FORMATO_FECHA = "%Y-%m-%d"
EDAD_MINIMA = 18
EDAD_MAXIMA = 100

class Usuarios_Services:
    """ Sección de servicios para el manejo de la logica de negocio
    
    Attributes:
        FORMATO_FECHA (str): Formato de fecha para validar
        EDAD_MINIMA (int): Edad minima para validar
        EDAD_MAXIMA (int): Edad maxima para validar
    """

    def agregar_usuario(self, usuario: Usuario, request: Request) -> dict:
        """ Agrega un usuario a la base de datos.

        :param usuario: Usuario a agregar
        :param request: Request de FastAPI
        """
        try:

            if not validar_email(getattr(usuario, "email")):
                raise HTTPException(
                    status_code=400,
                    detail="El email no es válido"

                )

            fecha_nacimiento = usuario.fecha_nacimiento
            
            if not validar_formato_fecha(fecha_nacimiento, FORMATO_FECHA):
                raise HTTPException(
                    status_code=400,
                    detail="El formato de la fecha de nacimiento no es válida"
                )

            usuario.fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, FORMATO_FECHA)
            
            if not validar_edad(usuario.fecha_nacimiento, EDAD_MINIMA, EDAD_MAXIMA):
                raise HTTPException(
                    status_code=400,
                    detail="La edad no es válida"
                )

            usuario_id = storage.add(usuario, request)

            return { "ID": usuario_id }
        
        except Exception as e:
            print("Error al agregar usuario: {}".format(str(e)))
            raise e


    def editar_usuario(self, usuario_id: UUID, usuario: Usuario, request: Request) -> dict:
        """ Edita un usuario de la base de datos.

        :param usuario: Usuario a editar
        """
        try:
                
            if not validar_email(getattr(usuario, "email")):
                raise HTTPException(
                    status_code=400,
                    detail="El email no es válido"

                )

            fecha_nacimiento = usuario.fecha_nacimiento
            
            if not validar_formato_fecha(fecha_nacimiento, FORMATO_FECHA):
                raise HTTPException(
                    status_code=400,
                    detail="El formato de la fecha de nacimiento no es válida"
                )

            usuario.fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, FORMATO_FECHA)
            
            if not validar_edad(usuario.fecha_nacimiento, EDAD_MINIMA, EDAD_MAXIMA):
                raise HTTPException(
                    status_code=400,
                    detail="La edad no es válida"
                )

            storage.update(usuario_id, usuario, request)

            return { "ID": usuario_id }

        except Exception as e:
            print("Error al editar usuario: {}".format(str(e)))
            raise e


    def eliminar_usuario(self, usuario_id: UUID, request: Request) -> dict:
        """ Elimina un usuario de la base de datos.

        :param usuario_id: ID del usuario a eliminar
        :param request: Request de FastAPI
        """
        try:

            storage.delete(Usuario, usuario_id, request)

            return { "ID": usuario_id }

        except Exception as e:
            print("Error al eliminar usuario: {}".format(str(e)))
            raise e


    def listar_usuarios(self, pagina: int, cantidad: int, order_by: str, sort: str, request: Request)-> dict:
        """ Obtiene una lista de usuarios de la base de datos.
        
        :param pagina: Pagina a retornar
        :param cantidad: Cantidad de usuarios a retornar
        :param order_by: Campo por el cual se ordenará la lista
        :param sort: Orden ascendente o descendente
        :param request: Request de FastAPI
        """
        try:

            return storage.get_all(Usuario, pagina, cantidad, request, order_by, sort)

        except Exception as e:
            print("Error al listar usuarios: {}".format(str(e)))
            raise e


    def obtener_usuario(self, usuario_id: UUID, request: Request) -> Usuario:
        """ Retorna un usuario por su ID

        :param usuario_id: ID del usuario a consultar
        :param request: Request de FastAPI
        """
        try:

            usuario = storage.get_by_id(Usuario, usuario_id, request)

            return usuario

        except Exception as e:
            print("Error al obtener usuario: {}".format(str(e)))
            raise e