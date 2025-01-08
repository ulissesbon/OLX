from sqlalchemy import delete, select, update
from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioPedido():
    
    def __init__(self, db: Session):
        self.db = db


    def criar(self, pedido: schemas.PedidoSchema): # pega o schema do pedido e transforma para o banco de dados
        db_pedido = models.Pedido(
            quantidade = pedido.quantidade,
            endereco_entrega = pedido.endereco_entrega,
            entrega = pedido.entrega,
            observacoes = pedido.observacoes,
            vendedor_id = pedido.vendedor_id,
            comprador_id = pedido.comprador_id,
            produto_id = pedido.produto_id,
            )
        
        self.db.add(db_pedido)     # adiciona ao banco de dados
        self.db.commit()           # confirma a adição
        self.db.refresh(db_pedido) # recarregar o pedido
        return db_pedido           # retorna para o solicitante


    def listar_todos(self):
        pedido = self.db.query(models.Pedido).all()
        return pedido


    def obter(self, pedido_id: int):
        stmt = select(models.Pedido).filter_by(id=pedido_id)
        pedido = self.db.execute(stmt).one()
        return pedido[0]


    def remover(self, pedido_id: int):
        stmt = delete(models.Pedido).where(models.Pedido.id == pedido_id)

        self.db.execute(stmt)
        self.db.commit()


    def editar(
                self, id_pedido: int, 
                pedido: schemas.Produto
            ):
        
        pedido_existente = self.db.query(models.Pedido).filter(models.Pedido.id == pedido.id).first()
        if not pedido_existente:
            raise HTTPException(status_code=404, detail= "Pedido não encontrado")
        
        update_stmt = update(models.Pedido
                             ).where(models.Pedido.id == id_pedido
                                     ).values(
                                            quantidade = pedido.quantidade,
                                            endereco_entrega = pedido.endereco_entrega,
                                            entrega = pedido.entrega,
                                            observacoes = pedido.observacoes
                                            )
        
        self.db.execute(update_stmt)
        self.db.commit()

    def listar_pedidos_usuario(self, id_usuario: int):
        query = select(models.Pedido).where(models.Pedido.comprador_id == id_usuario)
        resultado = self.db.execute(query).scalars().all()  
        return resultado


    def listar_vendas_usuario(self, id_usuario: int):
        query = select(models.Pedido, models.Produto)\
            .join_from(models.Pedido, models.Produto)\
            .where(models.Produto.usuario_id == id_usuario)
        resultado = self.db.execute(query).scalars().all()  
        return resultado

    