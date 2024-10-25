from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {"mensagem": "Olá mundo 2024.2"}