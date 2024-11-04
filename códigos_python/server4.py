# estudo dos parâmetros query string

from fastapi import FastAPI # type: ignore


app = FastAPI()


@app.get('/')
def home():
    return {"mensagem": "Olá mundo 2024.2"}

# parametro query string
@app.get('/dobro')
# dobro?valor=42
def dobro(valor: int):
    resultado = 2 * valor
    return {"resultado": f'O dobro de {valor} é {resultado}'}


@app.get('/area-retangulo')
# ?largura= &altura=
def area_retangulo(largura: int, altura: int):
    area = largura * altura
    return {'area': area}


@app.get('/area-retangulo2')
# para que um dos parametros não seja obrigatório
def area_retangulo(largura: int, altura: int = 2):
    area = largura * altura
    return {'area': area}
