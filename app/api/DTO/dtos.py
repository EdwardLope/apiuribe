from pydantic import BaseModel, Field
from datetime import date

# Los DTO son odjetos de etransferencua de datos

class PoveedorDTO(BaseModel): # DTO de descripcion
 
    id:int
    nombres:str
    documento:str
    Direccion:str
    Ciudad:str
    Representante:str
    telefonoContacto:str
    Correo:str
    fechaDeEnvio:date
    costoDeEnvio:int
    Descripcion:str

class PoveedorDTOEnvio(BaseModel): # DTO de respuesta

    id:int
    nombres:str
    documento:str
    Direccion:str
    Ciudad:str
    Representante:str
    telefonoContacto:str
    Correo:str
    fechaDeEnvio:date
    costoDeEnvio:int
    Descripcion:str

class LogisticaDTO(BaseModel):

    id:int
    nombreEncargado:str
    correoEncargado:str
    contactoEncargado:str
    fechaEnvio:date
    Descripcion:str

class LogisticaDTOEnvio(BaseModel):

    id:int
    nombreEncargado:str
    correoEncargado:str
    contactoEncargado:str
    fechaEnvio:date
    Descripcion:str