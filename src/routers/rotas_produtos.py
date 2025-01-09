from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.routers.auth_utils import obter_usuario_logado
from src.schemas.schemas import Produto, ProdutoSimples, Usuario
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto


router = APIRouter(prefix="/produtos")

# PRODUTOS

@router.post('/add', status_code=status.HTTP_201_CREATED, response_model= ProdutoSimples)
def criar_produto(produto: Produto, usuario: Usuario= Depends(obter_usuario_logado), db: Session= Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    produto_criado.usuario_id = usuario.id
    return produto_criado


@router.get('/all', status_code=status.HTTP_200_OK, response_model= List[ProdutoSimples])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()

    return produtos


@router.get('/view/{produto_id}')
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    
    produto_encontrado = RepositorioProduto(db).obter(produto_id)

    if not produto_encontrado:
        raise HTTPException(status_code=404)
    return produto_encontrado


@router.get('/listar/meus_produtos', response_model= List[ProdutoSimples])
def meus_produtos(usuario: Usuario = Depends(obter_usuario_logado), db: Session = Depends(get_db)):
    
    produtos_encontrados = RepositorioProduto(db).obter_meus_produtos(usuario.id)

    if not produtos_encontrados:
        raise HTTPException(status_code=404)
    return produtos_encontrados


@router.delete('/delete/{produto_id}')
def deletar_produto(produto_id: int, db: Session= Depends(get_db)):
    RepositorioProduto(db).remover(produto_id)

    return{'Msg': 'Produto removido com sucesso'}


@router.put('/edit/{produto_id}', response_model= ProdutoSimples)
def atualizar_produto(produto_id: int, produto: Produto, db: Session= Depends(get_db)):

    produto.id = produto_id

    RepositorioProduto(db).editar(produto_id, produto)

    return produto

