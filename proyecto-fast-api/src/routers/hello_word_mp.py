from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class MensajeInterno(BaseModel):
    texto: str
    prioridad: int = 1
    campo_interno: str


class MensajePublico(BaseModel):
    texto: str
    prioridad: int = 1


@router.get("/")
def read_root() -> dict[str, str]:
    return {
        "mensaje": "Hola desde FastAPI + uv",
        "autor": "Victor Pinargote",
        "version": "0.1.0",
    }


@router.get("/victor")
def endpoint_victor() -> MensajeInterno:
    return MensajeInterno(
        texto="Hola",
        campo_interno="imprime desde endpoint de Victor Pinargote",
    )


@router.get("/publico", response_model=MensajePublico)
def endpoint_publico():
    return {
        "texto": "Hola",
        "prioridad": 5,
        "campo_interno": "no debería salir",
    }


@router.get("/campo-extra", response_model=MensajeInterno)
def endpoint_campo_extra():
    return {
        "texto": "Hola Victor",
        "prioridad": 5,
        "campo_interno": "si debe salir incluido en el modelo",
        "campo_extra": "no debe salir esto",
    }