from pydantic import BaseModel

class ClientRegistrationDto(BaseModel):
    id: str
    names: str
    lastnames: str
    email: str
    phone: str
    password: str

class LoginDto(BaseModel):
    email: str
    password: str
