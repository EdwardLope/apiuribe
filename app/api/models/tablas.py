from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base  

Base = declarative_base()


class Poveedor(Base):

    __tablename__='proveedores'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres=Column(String(50))
    documento=Column(String(50))
    Direccion=Column(String(50))
    Ciudad=Column(String(50))
    Representante=Column(String(50))
    telefonoContacto=Column(String(50))
    Correo=Column(String(50))
    fechaDeEnvio=Column(Date)
    costoDeEnvio=Column(Integer)
    Descripcion=Column(String(100))

class Logistica(Base):  


    __tablename__ = 'logistica'  

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombreEncargado = Column(String(50))
    correoEncargado = Column(String(50))  
    contactoEncargado = Column(String(50))  
    fechaEnvio = Column(Date)
    Descripcion = Column(String(50))