from pydantic import BaseModel
class Persona(BaseModel):
    codigo_persona: int
    tipo_persona: str
    indicador_lista_negra: int
    nacionalidad: str
    pais_procedencia: str