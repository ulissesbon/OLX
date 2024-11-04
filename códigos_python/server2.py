## estudo dos tipos de métodos

from fastapi import FastAPI # type: ignore


app = FastAPI()


@app.get('/')
def home():
    return {"mensagem": "Olá mundo 2024.2"}

@app.get('/profile')
def profile():
    return {"nome": "Ulisses Bonfim"}

@app.post('/profile')
def signup():
    return {"mensagem": "Perfil criado com sucesso"}

@app.put('/profile')
def att():
    return {"mensagem": "Perfil atualizado com sucesso"}

@app.delete('/profile')
def delete():
    return {"mensagem": "Perfil deletado com sucesso"}