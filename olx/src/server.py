from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from typing import List
from src.schemas import schemas
from src.schemas.schemas import Produto, ProdutoSimples, Usuario
from src.infra.sqlalchemy.config.database import get_db, criar_db
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario


criar_db()


app = FastAPI()

# PRODUTOS

@app.post('/produtos', status_code=status.HTTP_201_CREATED, response_model= ProdutoSimples)
def criar_produto(produto: Produto, db: Session= Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)

    return produto_criado


@app.get('/produtos', status_code=status.HTTP_200_OK, response_model= List[Produto])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()

    return produtos


@app.get('/produto/{produto_id}')
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    return RepositorioProduto(db).obter(produto_id)


@app.delete('/produtos/{produto_id}')
def deletar_produto(produto_id: int, db: Session= Depends(get_db)):
    RepositorioProduto(db).remover(produto_id)

    return{'Msg': 'Produto removido com sucesso'}


@app.put('/produtos/{produto_id}', response_model= ProdutoSimples)
def atualizar_produto(produto_id: int, produto: Produto, db: Session= Depends(get_db)):

    produto.id = produto_id

    RepositorioProduto(db).editar(produto_id, produto)

    return produto





# USUARIOS

@app.post('/usuario', status_code=status.HTTP_201_CREATED, response_model= Usuario)
def criar_usuario(usuario: Usuario, db: Session= Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado



# @app.get('/usuarios')#, response_model= Usuario)
@app.get('/usuarios', response_model= List[Usuario])
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios


@app.get('/usuario/{usuario_id}')
def obter_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return RepositorioUsuario(db).obter(usuario_id)


@app.delete('/usuarios/{usuario_id}')
def deletar_usuario(usuario_id: int, db: Session= Depends(get_db)):
    RepositorioUsuario(db).remover(usuario_id)

    return{'Msg': 'Usuario removido com sucesso'}