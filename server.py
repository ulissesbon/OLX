from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def home():
    return {"mensagem": "Olá mundo 2024.2"}

@app.get('/saudacao/{nome}')
def saudacao(nome: str):
    texto = f'Olá {nome}, bem vindo!'
    
    return {"mensagem": texto}

@app.get('/quadrado/{numero}')
def quadrado(numero: int):
    resultado = numero * numero
    texto = f'O quadrade de {numero} é {resultado}'

    return {"mensagem": texto}