import uvicorn
from fastapi import BackgroundTasks, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config.database import  get_db
from src.jobs.write_notification import write_notification
from src.routers import rotas_produtos, rotas_pedidos, rotas_auth, rotas_usuario


app = FastAPI()


# CORS
origins = ['http://localhost:3000',
            'https://myapp.vercel.com']

app.add_middleware(CORSMiddleware,
                    allow_origins=origins,
                    allow_credentials=True,
                    allow_methods=["*"],
                    allow_headers=["*"],
                    )


# ROTAS PRODUTOS
app.include_router(rotas_produtos.router)

# ROTAS AUTH
app.include_router(rotas_auth.router)

# ROTAS AUSUARIO
app.include_router(rotas_usuario.router)

# ROTAS PEDIDOS
app.include_router(rotas_pedidos.router)


@app.post('/send_email/{email}')
def enviar_email(email:str, background: BackgroundTasks):
    background.add_task(write_notification,
                        email, 'mensagem de teste')
    
    return {'Msg': 'Mensagem enviada'}


@app.middleware('http')
async def processamento_tempo_requisicao(request: Request, next):
    print('interceptado')
    
    response = await next(request)

    print('terminada interceptação')

    return response









if __name__ == '__main__':
    uvicorn.run('server:app', host='0.0.0.0', port=8000, reload=True)