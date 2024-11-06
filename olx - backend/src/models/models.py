from pydantic import BaseModel
from typing import Optional, List



class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    tel: str
    produtos: List[Produto]
    vendas: List[Pedido]
    compras: List[Pedido]


class Produto(BaseModel):
    id: Optional[str] = None
    dono: Usuario
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False


class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observação!'
