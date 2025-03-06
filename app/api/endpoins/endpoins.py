from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends

from app.api.DTO.dtos import PoveedorDTO,PoveedorDTOEnvio,LogisticaDTO,LogisticaDTOEnvio
from app.api.models.tablas import Poveedor,Logistica

rutas=APIRouter()
#Rutinas para conectarse a la bese de datos 

#Rutina para construir servicion wed

def guardarPoveedor(datosPoveedor):
    try:
        Poveedor(
            nombres=datosPoveedor.nombres,
            documento=datosPoveedor.documento,
            Direccion=datosPoveedor.Direccion,
            Ciudad=datosPoveedor.Ciudad,
            Representante=datosPoveedor.Representante,
            telefonoContacto=datosPoveedor.telefonoContacto,
            Correo=datosPoveedor.Correo,
            fechaDeEnvio=datosPoveedor.fechaDeEnvio,
            costoDeEnvio=datosPoveedor.costoDeEnvio,
            Descripcion=datosPoveedor.Descripcion
        )
        
    

    except Exception as error:
        pass 


def guardarLogistica(datosLogistica):
    try:
        Logistica(
            nombreEncargado=datosLogistica.nombreEncargado,
            correoEncargado=datosLogistica.correoEncargado,
            contactoEncargado=datosLogistica.contactoEncargado,
            fechaEnvio=datosLogistica.fechaEnvio,
            Descripcion=datosLogistica.Descripcion
        )
        

    except Exception as error:
        pass 