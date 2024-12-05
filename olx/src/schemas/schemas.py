from pydantic import BaseModel
from typing import Optional, List



class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    senha: str
    # produtos: List[Produto] = []
    # vendas: List[Pedido]
    # compras: List[Pedido]
    
    class Config:
        orm_mode = True


class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    descricao: str
    preco: float
    disponivel: bool = False
    usuario_id: int

    usuario: Optional[Usuario] = None

    class Config:
        orm_mode = True


class ProdutoSimples(BaseModel):
    id: Optional[int] = None
    # dono: Usuario
    nome: str
    preco: float

    class Config:
        orm_mode = True


class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    # produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observação!'

    class Config:
        orm_mode = True