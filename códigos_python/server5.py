# estudo de request body

from fastapi import FastAPI # type: ignore
from pydantic import BaseModel # type: ignore

app = FastAPI()


@app.get('/')
def home():
    return {"mensagem": "Olá mundo 2024.2"}


class Produto(BaseModel):
    nome: str
    preco: float

# uso do Insomnia para request
@app.post('/produtos')
def produtos(produto: Produto):
    return {'mensagem': f'Produto: ({produto.nome} -- R$ {produto.preco}) cadastrado com sucesso'}


# request com tipo get
@app.get('/saudacao/{nome}')
def saudacao(nome: str):
    texto = f'Olá {nome}, bem vindo!'    
    return {"mensagem": texto}
