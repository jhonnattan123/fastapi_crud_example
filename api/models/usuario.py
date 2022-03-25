from uuid import UUID
from datetime import date
from typing import Optional, Union
from pydantic import BaseModel, Field

class Usuario(BaseModel):

    ID: Optional[UUID] = Field(
        title="ID del usuario",
        description="ID del usuario",
        example="3fa85f64-5717-4562-b3fc-2c963f66afa6"
    )

    nombre: str = Field(
        ...,
        title="Nombre del usuario",
        description="Nombre del usuario",
        min_length=3,
        max_length=50,
        example="Juan"
    )

    apellido: str = Field(
        ...,
        title="Apellido del usuario",
        description="Apellido del usuario",
        min_length=3,
        max_length=50,
        example="Perez"
    )

    email: str = Field(
        ...,
        title="Email del usuario",
        description="Email del usuario",
        min_length=3,
        max_length=50,
        example="test@test.com"
    )
    
    fecha_nacimiento: Union[str,date] = Field(
        ...,
        title="Fecha de nacimiento del usuario",
        description="Fecha de nacimiento del usuario",
        example="2020-01-01"
    )

    def u_key(self):
        return "email" 