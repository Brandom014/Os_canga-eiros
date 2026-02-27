from fastapi import FastAPI

app = FastAPI()

produtos = []

@app.get("/")
def home():
    return{"mensagem": "API funcionando ✔"}

@app.get("/")
def criar_produto(nome: str, quantidade: int):
    produto = {
        "id": len(produtos) + 1,
        "nome": nome,
        "quantidade": quantidade
    }
    produtos.append(produto)
    return produto
