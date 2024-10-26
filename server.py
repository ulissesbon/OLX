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
    texto = f'O quadrado de {numero} é {resultado}'

    return {"mensagem": texto}

@app.get('/dobro')
def dobro(valor: int):
    resultado = 2 * valor
    return {"resultado": f'O dobro de {valor} é {resultado}'}

# ?largura= &altura=
@app.get('/area-retangulo')
def area_retangulo(largura: int, altura: int):
    area = largura * altura
    return {'area': area}

#para que um dos parametros não seja obrigatório
@app.get('/area-retangulo2')
def area_retangulo(largura: int, altura: int = 2):
    area = largura * altura
    return {'area': area}

