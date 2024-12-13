from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import PedidoSchema
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_pedido import RepositorioPedido


router = APIRouter(prefix="/pedidos")

# PEDIDOS

@router.post('/add', status_code=status.HTTP_201_CREATED)
def criar_pedido(pedido: PedidoSchema, db: Session = Depends(get_db)):
    pedido_realizado = RepositorioPedido(db).criar(pedido)

    return pedido_realizado


@router.get('/all', 
            status_code=status.HTTP_200_OK, 
            response_model= List[PedidoSchema])
def listar_pedidos(db: Session = Depends(get_db)):
    pedidos = RepositorioPedido(db).listar_todos()

    return pedidos


@router.get('/view/{pedido_id}', status_code=status.HTTP_200_OK, response_model= PedidoSchema)
def obter_pedido(pedido_id: int, db: Session = Depends(get_db)):
    pedido_encontrado = RepositorioPedido(db).obter(pedido_id)

    if not pedido_encontrado:
        raise HTTPException(status_code=404)
    return pedido_encontrado


@router.get('/view/meus_pedidos/{usuario_id}', status_code=status.HTTP_200_OK, response_model= List[PedidoSchema])
def obter_pedidos_usuario(usuario_id: int, db: Session = Depends(get_db)):
    pedidos_usuario = RepositorioPedido(db).listar_pedidos_usuario(usuario_id)

    if not pedidos_usuario:
        raise HTTPException(status_code=404)
    return pedidos_usuario


@router.get('/view/minhas_vendas/{usuario_id}', status_code=status.HTTP_200_OK, response_model= List[PedidoSchema])
def obter_vendas_usuario(usuario_id: int, db: Session = Depends(get_db)):
    vendas_usuario = RepositorioPedido(db).listar_vendas_usuario(usuario_id)

    if not vendas_usuario: 
        raise HTTPException(status_code=404)
    return vendas_usuario


@router.delete('/delete/{pedido_id}')
def deletar_pedido(pedido_id: int, db: Session= Depends(get_db)):
    RepositorioPedido(db).remover(pedido_id)

    return{'Msg': 'pedido removido com sucesso'}


@router.put('/edit/{pedido_id}', response_model=PedidoSchema)
def atualizar_pedido(pedido_id: int,pedido: PedidoSchema, db: Session= Depends(get_db)):

    pedido.id = pedido_id

    RepositorioPedido(db).editar(pedido_id, pedido)

    return pedido

