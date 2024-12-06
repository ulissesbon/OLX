from pydantic import BaseModel
from typing import Optional, List



class ProdutoSimples(BaseModel):
    id: Optional[int] = None
    nome: str 
    preco: float

    class Config:
        orm_mode = True



class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    senha: str
    produtos: List[ProdutoSimples] = []
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
    usuario_id: Optional[int] 

    usuario: Optional[Usuario] = None

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