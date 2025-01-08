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

class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str

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


class PedidoSchema(BaseModel):
    id: Optional[int] = None
    quantidade: Optional[int]
    endereco_entrega: Optional[str]
    entrega: bool = True    # True = entrega, False = retirada
    observacoes: Optional[str] = 'Sem observação!'

    vendedor_id: Optional[int] = None
    comprador_id: Optional[int] = None
    produto_id: Optional[int] = None

    vendedor: Optional[Usuario] = None
    comprador: Optional[Usuario] = None
    produto: Optional[ProdutoSimples] = None

    class Config:
        orm_mode = True