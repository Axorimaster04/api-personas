from pydantic import BaseModel

class Persona(BaseModel):
    codigo_persona: int
    tipo_persona: str
    indicador_lista_negra: int
    nacionalidad: str
    pais_procedencia: str
    
class Poliza(BaseModel):
    codigo_persona: int
    codigo_poliza: int
    numero_poliza: int
    nombre_producto: str
    desc_producto: str
    cat_producto: str
