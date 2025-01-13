import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config.database import  get_db
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



if __name__ == '__main__':
    uvicorn.run('server:app', host='0.0.0.0', port=8000, reload=True)