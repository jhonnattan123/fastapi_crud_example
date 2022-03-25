import uuid
from fastapi import HTTPException
from starlette.requests import Request
from api.models.usuario import Usuario
from api.models.respuesta_listar import Respuesta_Listar

def add(item, request: Request):
    """ Agrega un nuevo item a la lista.
        Si el modelo posee el metodo u_key se usara su respuesta 
        como llave unica.

    :param item: Item a agregar
    :param request: Request
    """
    try:

        item_id = uuid.uuid4()
        setattr(item, "ID", item_id)

        nombre_modelo = item.__class__.__name__

        if nombre_modelo not in request.app.memory:
            request.app.memory[nombre_modelo] = {}

        if nombre_modelo not in request.app.key_memory:
            request.app.key_memory[nombre_modelo] = {}

        if hasattr(item, "u_key"):
            llave = item.u_key()
            valor_llave = getattr(item, llave)

            if nombre_modelo in request.app.key_memory and valor_llave in request.app.key_memory[nombre_modelo]:
                raise HTTPException(
                    status_code=404, 
                    detail="Llave {} esta duplicada".format(valor_llave)
                    )

            request.app.key_memory[nombre_modelo][valor_llave] = str(item_id)

        request.app.memory[nombre_modelo][str(item_id)] = item

        return str(item_id)

    except Exception as e:
        if type(e) != HTTPException:
            raise Exception("Error al agregar el item: {}".format(str(e)))
        raise e

def update( item_id, item, request ):
    """ Actualiza un item en la lista
    
        :param item_id: ID del item a actualizar
        :param item: Item a actualizar
        :param request: Request
    """
    try:

        setattr(item, "ID", item_id)
        nombre_modelo = item.__class__.__name__
        item_original = get_by_id(item.__class__,item_id, request)

        if not item_original:
            raise HTTPException(status_code=404, detail="Item not found")

        if hasattr(item, "u_key"):
            llave = item.u_key()
            IN_llave = getattr(item, llave)
            llave_original = getattr(item_original, llave)

            if IN_llave != llave_original and IN_llave not in request.app.key_memory[nombre_modelo]:
                del request.app.key_memory[nombre_modelo][str(llave_original)]
                request.app.key_memory[nombre_modelo][IN_llave] = str(item_id)

        print(item)
        request.app.memory[nombre_modelo][str(item_id)] = item

        return str(item_id)

    except Exception as e:
        if type(e) != HTTPException:
            raise Exception("Error al actualizar el item: {}".format(str(e)))
        raise e
    

def get_all(modelo, pagina=1, cantidad=10, request=Request, order_by="ID", sort="asc"):
    """ Retorna todos los items de la lista
    
        :param modelo: Clase del modelo
        :param pagina: Pagina a retornar
        :param cantidad: Cantidad de items a retornar
        :param request: Request
        :param order_by: Campo por el cual se ordenara
        :param sort: Orden ascendente o descendente
    """
    try:

        nombre_modelo = modelo.__name__

        if nombre_modelo not in request.app.key_memory:
            return Respuesta_Listar().__dict__

        items = []
        for item_id in request.app.memory[nombre_modelo]:
            items.append(request.app.memory[nombre_modelo][item_id])

        if not order_by:
            order_by = "ID"

        if order_by in list(Usuario.__fields__.keys()) and sort == "desc":
            items.sort(key=lambda x: x[order_by], reverse=True)

        if not pagina:
            pagina = 1
        
        if not cantidad:
            cantidad = 10

        return {
            "data": items[(pagina-1)*cantidad:pagina*cantidad],
            "total_items": len(items),
            "total_paginas": len(items)//cantidad + 1
        }

    except Exception as e:
        if type(e) != HTTPException:
            raise Exception(f"Error al obtener todos los items:",e)
        raise e

def get_by_id(modelo,item_id,request):
    """ Retorna un item por su ID
    
        :param item_id: ID del item a retornar
        :param request: Request
    """
    try:

        nombre_modelo = modelo.__name__

        if nombre_modelo not in request.app.key_memory:
            raise HTTPException(
                    status_code=404,
                    detail="Item not found"
                )


        if str(item_id) not in request.app.memory[nombre_modelo]:
            raise HTTPException(
                    status_code=404,
                    detail="Item not found"
                )

        item = request.app.memory[nombre_modelo][str(item_id)]

        return item

    except Exception as e:
        if type(e) != HTTPException:
            raise Exception(f"Error al obtener el item: {str(e)}")
        raise e


def delete(modelo, item_id, request):
    """ Elimina un item de la lista
    
        :param item_id: ID del item a eliminar
        :param request: Request
    """
    try:

        nombre_modelo = modelo.__name__

        if nombre_modelo not in request.app.key_memory:
            raise HTTPException(
                    status_code=404,
                    detail="Item not found"
                )

        if str(item_id) not in request.app.memory[nombre_modelo]:
            raise HTTPException(
                    status_code=404,
                    detail="Item not found"
                )
        
        item = request.app.memory[nombre_modelo][str(item_id)]
        if hasattr(item, "u_key"):
            llave = item.u_key()
            valor_llave = getattr(item, llave)
            del request.app.key_memory[nombre_modelo][valor_llave]
        
        del request.app.memory[nombre_modelo][str(item_id)]

    except Exception as e:
        if type(e) != HTTPException:
            raise Exception(f"Error al eliminar el item: {str(e)}")
        raise e