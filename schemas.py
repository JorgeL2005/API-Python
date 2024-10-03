from pydantic import BaseModel
class Item(BaseModel):
    nombre: str
    especialidad: str
    dni: int
    telefono: str

class Item2(BaseModel):
    nomc: str
    numc: int