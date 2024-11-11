from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.schemas.schemas import Produto, ProdutoSimples
from src.infra.sqlalchemy.config.database import get_db, criar_db
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario


criar_db()


app = FastAPI()


@app.post('/produtos', status_code=status.HTTP_201_CREATED, response_model= ProdutoSimples)
def criar_produto(produto: schemas.Produto, db: Session= Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)

    return produto_criado



@app.get('/produtos', status_code=status.HTTP_200_OK)
def listar_produto(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()

    return produtos


@app.get('/produto/{produto_id}')
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    return RepositorioProduto(db).obter(produto_id)


@app.delete('/produtos/{produto_id}')
def deletar_produto(produto_id: int, db: Session= Depends(get_db)):
    RepositorioProduto(db).remover(produto_id)

    return{'Msg': 'Removido com sucesso'}


@app.post('/usuario')
def criar_usuario(usuario: schemas.Usuario, db: Session= Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado


@app.get('/usuarios')
def listar_produto(db: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios