from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config.database import  get_db
from src.routers import rotas_produtos, rotas_usuarios



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

# ROTAS USUSARIOS

app.include_router(rotas_usuarios.router)
