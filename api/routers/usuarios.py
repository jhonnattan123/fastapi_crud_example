from uuid import UUID
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, Union
from ..models.usuario import Usuario
from fastapi import Body, Path, Query
from starlette.requests import Request
from ..models.respuesta_listar import Respuesta_Listar
from fastapi import APIRouter, Depends, HTTPException
from ..services.usuarios_services import Usuarios_Services
from ..dependencies import validar_token_header, oapi_code_response

class usuarios_router:
    
    router = APIRouter(
        prefix="/usuarios",
        tags=["usuarios"],
        dependencies=[Depends(validar_token_header)],
        responses={
            404: {"description": "Not found"},
            500: {"description": "Internal Server Error"}
        }
    )

    class reponse_id(BaseModel):
        ID: UUID

    @router.get("/", response_model = Respuesta_Listar(Usuario))
    def listar_usuarios(
            pagina: Optional[int] = Query(
                None,
                ge=1,
                title="Pagina",
                description="Pagina a consultar"
            ),
            cantidad: Optional[int] = Query(
                None,
                ge=1,
                title="Cantidad",
                description="Cantidad de registros que se desea obtener"
            ),
            order_by: Optional[str] = Query(
                None,
                title="Order By",
                description="Campo por el cual se desea ordenar"
            ),
            sort: Optional[bool] = Query(
                None,
                title="Sort",
                description="Orden ascendente o descendente"
            ),
            request: Request = Request
        ):

        """ Retorna una lista de usuarios

        :param pagina: Numero de pagina a retornar
        :param cantidad: Cantidad de usuarios a retornar
        :param order_by: Campo por el cual se ordenará la lista
        :param sort: Orden ascendente o descendente
        :param request: Request de FastApi
        """

        return Usuarios_Services().listar_usuarios( pagina, cantidad, order_by, sort, request )

    @router.post("/", response_model = reponse_id, responses = {
        400: oapi_code_response(
            description="Bad Request",
            schema={
                "type": "object",
                "properties": { "error": { "type": "string" } }
            },
            examples={
                "email_invalido": {
                    "error":"El email no es válido"
                },
                "fecha_nacimiento_invalida": { 
                    "error": "El formato de la fecha de nacimiento no es válido"
                },
                "edad_invalida": {
                    "error": "La edad no es válida"
                }
            }
        )
    })
    def agregar_usuario(
            usuario: Usuario = Body(...), 
            request:Request = Request
        ):
        """ Agrega un usuario a la base de datos.

        :param usuario: Usuario a agregar
        :param request: Request de FastApi
        """
        return Usuarios_Services().agregar_usuario(usuario, request)

    @router.get("/{usuario_id}", response_model = Union[Usuario,dict] )
    def obtener_usuario(
            usuario_id: UUID = Path(
                ...,
                title="Usuario ID",
                description="ID del usuario a consultar"
            ), 
            request: Request = Request
        )->Union[Usuario, HTTPException]:
        """ Retorna un usuario por su ID

        :param usuario_id: ID del usuario a retornar
        :param request: Request de FastApi
        """

        response = Usuarios_Services().obtener_usuario( usuario_id, request )

        return response

    @router.put("/{usuario_id}")
    def editar_usuario(
            usuario_id: UUID = Path(
                ...,
                title="ID del usuario a editar",
                description="ID del usuario a editar"
            ),
            usuario: Usuario = Body(
                ...,
                title="Datos del usuario a editar",
                description="Datos del usuario a editar"
            ),
            request: Request = Request
        ):
        """ Edita un usuario en la base de datos.

        :param usuario_id: ID del usuario a editar
        :param usuario: Datos del usuario a editar
        :param request: Request de FastApi
        """

        return Usuarios_Services().editar_usuario(usuario_id, usuario, request)

    @router.delete("/{usuario_id}", response_model = reponse_id)
    def eliminar_usuario(
        usuario_id: UUID = Path(...),
        request: Request = Request
        ):
        """ Elimina un usuario de la base de datos.
        
        :param usuario_id: ID del usuario a eliminar
        :param request: Request de FastApi
        """

        return Usuarios_Services().eliminar_usuario(usuario_id, request)
