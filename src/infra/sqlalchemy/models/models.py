from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import relationship

# instância do modelo orm
class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)
    tamanhos = Column(String)
    usuario_id = Column(Integer, ForeignKey('usuario.id', name='fk_usuario'))

    usuario = relationship('Usuario', back_populates='produtos')



class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    telefone = Column(String)
    senha = Column(String)

    produtos = relationship('Produto', back_populates='usuario')
    vendas = relationship(
        'Pedido',
        foreign_keys='Pedido.vendedor_id',
        back_populates='vendedor'
    )
    compras = relationship(
        'Pedido',
        foreign_keys='Pedido.comprador_id',
        back_populates='comprador'
    )
    

    def to_dict(self):
        """Retorna uma representação do objeto em formato de dicionário."""
        data = {
            "id": self.id,
            "nome": self.nome,
        }

        return data



class Pedido(Base):
    __tablename__ = 'pedido'

    id = Column(Integer, primary_key=True, index=True)
    quantidade = Column(Integer)
    endereco_entrega = Column(String)
    entrega = Column(Boolean)
    observacoes = Column(String)

    # RELACIONAMENTOS:
    vendedor_id = Column(Integer, ForeignKey(
        'usuario.id', name='fk_pedido_vendedor'))
    comprador_id = Column(Integer, ForeignKey(
        'usuario.id', name='fk_pedido_comprador'))
    produto_id = Column(Integer, ForeignKey(
        'produto.id', name='fk_pedido_produto'))

    vendedor = relationship('Usuario', foreign_keys=[vendedor_id], back_populates='vendas')
    comprador = relationship('Usuario', foreign_keys=[comprador_id], back_populates='compras')
    produto = relationship('Produto')
    
    
