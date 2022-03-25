from pydantic import BaseModel, Field

def Respuesta_Listar(clase=False):
    """ Clase que representa la la estructura para la respuesta de listar
        si se pasa una clase, se genera un modelo para la clase
        el modelo se utiliza en documentacion de la API 
        
    :param clase: Clase a generar el modelo
    """

    class Respuesta_Listar:
        def __init__(self):
            self.data = []
            self.total_items = 0
            self.total_paginas = 0

    if clase:
        class Respuesta_Listar(BaseModel):
            
            data: list[clase] = Field(
                title="Total de items"
            )
            
            total_items: int = Field(
                title="Total de items",
                example=1,
                default=10
            )
            total_paginas: int = Field(
                title="Total de paginas",
                example=1,
                default=1
            )

        return Respuesta_Listar
    
    return Respuesta_Listar()