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

#Entrada de estoque para produtos existentes
@app.post("/entrada/{id}")
def entrada_estoque(id: int, quantidade: int):
    if quantidade < 0:
        return {"erro": "Quantidade não pode ser negativa"}
    for produto in produtos:
        if produto["id"] == id:
            produto["quantidade"] += quantidade
            return produto
    return {"erro": "Produto não encontrado"}

#Saida de produtos no estoque com validação
@app.post("/saida/{id}")
def saida_estoque(id: int, quantidade: int):
    if quantidade < 0:
        return {"erro": "Quantidade não pode ser negativa!"}
    for produto in produtos:
        if produto["id"] == id:
            if produto["quantidade"] < quantidade:
                return {"erro": "Estoque insuficiente"}
            produto["quantidade"] -= quantidade
            return produto
    return{"erro": "Produto não encontrado."}