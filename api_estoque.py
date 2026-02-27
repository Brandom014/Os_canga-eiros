from fastapi import FastAPI

app = FastAPI()

produtos = []

#Cadastro de produtos
@app.post("/produtos")
def criar_produto(nome: str, quantidade: int):
    if quantidade < 0:
        return {"erro": "Quantidade não pode ser negativa!"}
    if not nome:
        return {"erro": "Produto precisa de um nome!"}

    produto = {
        "id": len(produtos) + 1,
        "nome": nome,
        "quantidade": quantidade
    }
    produtos.append(produto)
    return produto

#Listagem de produtos
@app.get("/produtos")
def listar_produtos():
    return produtos

