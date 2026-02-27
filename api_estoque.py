from fastapi import FastAPI

app = FastAPI()

produtos = []

@app.get("/")
def home():
    return{"mensagem": "API funcionando ✔"}