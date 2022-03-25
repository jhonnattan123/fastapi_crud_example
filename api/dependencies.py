import re
import datetime
from fastapi import Header, HTTPException

def oapi_code_response( description: str, schema: dict, examples: dict ) -> dict:
    """ Genera un diccionario con el código de respuesta de OpenAPI

    :param description: Descripción del código de respuesta
    :param schema: Diccionario con el esquema de respuesta
    :param examples: Diccionario con los ejemplos de respuesta
    """
    try:

        example_correct = {}

        for example in examples:
            example_correct[example] = {
                "value": examples[example],
            }

        return {
            "description": description,
            "content": {
                "application/json": {
                    "schema": schema,
                    "examples": example_correct
                }
            }
        }

    except Exception as e:
        print("Error al generar el código de respuesta: {}", str(e))
        raise HTTPException( status_code=500 )

def validar_token_header(token: str = Header(...)):
    """ Valida que el token en el header sea correcto

    :param token: token a validar
    """
    if token != "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9":
        raise HTTPException(status_code=401, detail="Token header invalid")

def validar_token_query(token: str):
    """ Valida que el token en el query sea correcto

    :param token: token a validar
    """
    if token != "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9":
        raise HTTPException(status_code=401, detail="Token query invalid")

def validar_email( email: str) -> bool:
    """Valida que el email sea correcto

    :param email: correo electrónico a validar
    """ 
    regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

    if type(email) == str and re.fullmatch(regex, email):
        return True
    
    return False

def validar_formato_fecha( fecha: str, formato: str ) -> bool:
    """Valida que la fecha tenga el formato correcto

    :param fecha: fecha a validar
    :param formato: formato de la fecha
    """  
    try:
        
        datetime.datetime.strptime(fecha, formato)

        return True

    except ValueError:

        return False

def validar_edad( fecha_nacimiento: str, edad_min: int, edad_max: int) -> bool:
    """Valida que la fecha de nacimiento sea correcta

    :param fecha_nacimiento: fecha de nacimiento a validar
    :param edad_min: edad mínima
    :param edad_max: edad máxima
    """ 
    try:

        fecha_actual = datetime.datetime.now()
        rectifier = datetime.datetime(fecha_actual.year, fecha_nacimiento.month, fecha_nacimiento.day) >= fecha_actual
        edad = fecha_actual.year - fecha_nacimiento.year - rectifier
        if edad > edad_min and edad < edad_max:
            return True
        
        return False

    except Exception as e:
        print("Error al validadar la edad: {}", str(e))
        raise HTTPException( status_code=500 )