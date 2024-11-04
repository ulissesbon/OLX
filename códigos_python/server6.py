# atividade de cadastro de animais domesticos

from fastapi import FastAPI, HTTPException # type: ignore
from pydantic import BaseModel # type: ignore
from typing import Optional, List
from uuid import uuid4
import random

app = FastAPI()

class Animal(BaseModel):
    id: Optional[str] = None
    nome: str
    idade: int
    sexo: str #True = macho, False = fêmea
    cor_pelagem: str

#lista de animais cadastrados
animais: List[Animal] = []

#animais cadastrados de animal
@app.get('/animais')
def listar_animais():
    return animais

#cadastro de animal
@app.post('/animais')
def cadastro(animal: Animal):
    animal.id = str(uuid4())
    animais.append(animal)
    return None


# retornar um animal pelo seu ID
@app.get('/animais/{id_animal}')
def get_animal(id_animal: str):
    for animal in animais:
        if animal.id == id_animal:
            return animal
    raise HTTPException(status_code=404, detail='Animal não encontrado!')


# apagar os dados de um animal pelo seu ID
@app.delete('/animais/{id}')
def deletar_animal(id: str):
    posicao = -1
    for index, animal in enumerate(animais):
        if animal.id == id:
            return animais.pop(index)
    raise HTTPException(status_code=404, detail='Animal não encontrado!')