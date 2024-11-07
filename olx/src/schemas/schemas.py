from pydantic import BaseModel
from typing import Optional, List



class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    # produtos: List[Produto]
    # vendas: List[Pedido]
    # compras: List[Pedido]
    
    class Config:
        orm_mode = True


class Produto(BaseModel):
    id: Optional[str] = None
    # dono: Usuario
    nome: str
    descricao: str
    preco: float
    disponivel: bool = False

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