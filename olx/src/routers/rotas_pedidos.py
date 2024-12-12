from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Pedido
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_pedido import RepositorioPedido


router = APIRouter(prefix="/pedidos")

# PEDIDOS

@router.post('/add', status_code=status.HTTP_201_CREATED)
def criar_pedido(pedido: Pedido, db: Session= Depends(get_db)):
    pedido_realizado = RepositorioPedido(db).criar(pedido)

    return pedido_realizado


@router.get('/all', status_code=status.HTTP_200_OK, response_model= List[Pedido])
def listar_pedidos(db: Session = Depends(get_db)):
    pedidos = RepositorioPedido(db).listar()

    return pedidos


@router.get('/view/{pedido_id}', status_code=status.HTTP_200_OK, response_model= Pedido)
def obter_pedido(pedido_id: int, db: Session = Depends(get_db)):
    pedido_encontrado = RepositorioPedido(db).obter(pedido_id)

    if not pedido_encontrado:
        raise HTTPException(status_code=404)
    return pedido_encontrado



@router.delete('/delete/{pedido_id}')
def deletar_pedido(pedido_id: int, db: Session= Depends(get_db)):
    RepositorioPedido(db).remover(pedido_id)

    return{'Msg': 'pedido removido com sucesso'}


@router.put('/edit/{pedido_id}', response_model=Pedido)
def atualizar_pedido(pedido_id: int,pedido: Pedido, db: Session= Depends(get_db)):

    pedido.id = pedido_id

    RepositorioPedido(db).editar(pedido_id, pedido)

    return pedido

