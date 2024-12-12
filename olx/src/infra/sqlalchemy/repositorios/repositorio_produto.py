from sqlalchemy import delete, select, update
from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioProduto():
    
    def __init__(self, db: Session):
        self.db = db


    def criar(self, produto: schemas.Produto): # pega o schema do produto e transforma para o banco de dados
        db_produto = models.Pedido(
            nome = produto.nome,
            descricao = produto.descricao,
            preco = produto.preco,
            disponivel = produto.disponivel,
            usuario_id = produto.usuario_id)
        
        self.db.add(db_produto) # adiciona ao banco de dados
        self.db.commit()        # confirma a adição
        self.db.refresh(db_produto) # recarregar o produto
        return db_produto           # retorna para o solicitante


    def listar(self):
        produtos = self.db.query(models.Pedido).all()
        return produtos


    def obter(self, produto_id: int):
        stmt = select(models.Pedido).filter_by(id=produto_id)
        produto = self.db.execute(stmt).scalar()
        print(produto)
        return produto


    def remover(self, produto_id: int):
        stmt = delete(models.Pedido).where(models.Pedido.id == produto_id)

        self.db.execute(stmt)
        self.db.commit()


    def editar(self, id_produto: int, produto: schemas.Produto):
        
        produto_existente = self.db.query(models.Pedido).filter(models.Pedido.id == produto.id).first()
        if not produto_existente:
            raise HTTPException(status_code=404, detail= "Produto não encontrado")
        
        update_stmt = update(models.Pedido
                             ).where(models.Pedido.id == id_produto
                                     ).values(
                                            nome = produto.nome,
                                            descricao = produto.descricao,
                                            preco = produto.preco,
                                            disponivel = produto.disponivel
                                            )
        
        self.db.execute(update_stmt)
        self.db.commit()