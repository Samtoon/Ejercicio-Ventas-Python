from sqlmodel import Session
from models.DTO.auth import ClientRegistrationDto
from models.DB.client import Client
from utils.database import engine

def register_client(client: ClientRegistrationDto):
    newClient = Client(
        id_cliente = client.id,
        nombres = client.names,
        apellidos = client.lastnames,
        email = client.email,
        celular = client.phone,
        contrasena = client.password 
    )

    session = Session(engine)
    session.add(newClient)
    session.commit()