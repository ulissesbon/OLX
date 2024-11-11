from sqlalchemy import delete, select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioProduto():
    
    def __init__(self, db: Session):
        self.db = db


    def criar(self, produto: schemas.Produto): # pega o schema do produto e transforma para o banco de dados
        db_produto = models.Produto(
            nome = produto.nome,
            descricao = produto.descricao,
            preco = produto.preco,
            disponivel = produto.disponivel)
        
        self.db.add(db_produto) # adiciona ao banco de dados
        self.db.commit()        # confirma a adição
        self.db.refresh(db_produto) # recarregar o produto
        return db_produto           # retorna para o solicitante


    def listar(self):
        produtos = self.db.query(models.Produto).all()
        return produtos


    def obter(self, produto_id: int):
        stmt = select(models.Produto).filter_by(id=produto_id)
        produto = self.db.execute(stmt).scalar_one()

        return produto


    def remover(self, produto_id: int):
        stmt = delete(models.Produto).where(models.Produto.id == produto_id)

        self.db.execute(stmt)
        self.db.commit()


