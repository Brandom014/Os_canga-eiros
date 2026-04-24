from pydantic import BaseModel

class ProdutoCreate(BaseModel):
    nome: str
    quantidade: int
    preco: float

class VendaCreate(BaseModel):
    produto_id: int
    quantidade: int

class Login(BaseModel):
    email: str
    senha: str