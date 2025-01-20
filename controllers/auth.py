from fastapi import APIRouter
from models.DTO.auth import ClientRegistrationDto, LoginDto
from services.clients_service import register_client

router = APIRouter()

@router.post("/register")
async def register(registrationData: ClientRegistrationDto):
    register_client(registrationData)
    return registrationData

@router.post("/login")
async def login(loginData: LoginDto):
    return loginData



