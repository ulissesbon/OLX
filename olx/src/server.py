from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.config.database import get_db, criar_db
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario


criar_db()


app = FastAPI()


@app.post('/produtos')
def criar_produto(produto: schemas.Produto, db: Session= Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get('/produtos')
def listar_produto(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos



@app.post('/usuario')
def criar_usuario(usuario: schemas.Usuario, db: Session= Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado


@app.get('/usuarios')
def listar_produto(db: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios