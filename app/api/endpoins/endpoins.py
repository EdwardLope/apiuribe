from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends

from app.api.DTO.dtos import PoveedorDTO,PoveedorDTOEnvio,LogisticaDTO,LogisticaDTOEnvio
from app.api.models.tablas import Poveedor,Logistica

from app.database.connection import SessionLocal, engine

rutas=APIRouter()

#Rutinas para conectarse a la bese de datos 

def conectarConBD ():
    try:

        baseDatos=SessionLocal()
        yield baseDatos

    except Exception as error:
        baseDatos.roback()
        raise error

    finally:
        baseDatos.close()

#Rutina para construir servicion wed
@rutas.post("/proveedor",response_model=PoveedorDTOEnvio,summary="servicio para guardar un proveedor en la base de datos ")

def guardarPoveedor(datosPoveedor:PoveedorDTO,database:Session=Depends(conectarConBD)):
    try:
        proveedorAGuardar=Poveedor(
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
        database.add(proveedorAGuardar)
        database.commit()
        database.refresh(proveedorAGuardar)
        return proveedorAGuardar
    

    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400,detail=("tenemos un error {error}"))


def guardarLogistica(datosLogistica:LogisticaDTO):
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