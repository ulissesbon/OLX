from pydantic import BaseModel
from typing import Optional


class Series(BaseModel):
    id: Optional[int] = None
    titulo: str
    ano: int
    genero: str
    qtd_temps: int
    
    class Config:
        orm_mode = True

