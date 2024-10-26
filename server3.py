## estudo dos parâmetros de rota

from fastapi import FastAPI # type: ignore


app = FastAPI()


@app.get('/')
def home():
    return {"mensagem": "Olá mundo 2024.2"}

# /saudacao/Nome
@app.get('/saudacao/{nome}')
def saudacao(nome: str):
    texto = f'Olá {nome}, bem vindo!'    
    return {"mensagem": texto}

# /quadrado/42
@app.get('/quadrado/{numero}')
def quadrado(numero: int):
    resultado = numero * numero
    texto = f'O quadrade de {numero} é {resultado}'
    return {"mensagem": texto}