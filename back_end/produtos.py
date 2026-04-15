from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models
from schemas import ProdutoCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/produtos")
def criar(dados: ProdutoCreate, db: Session = Depends(get_db)):
    produto = models.Produto(**dados.dict())
    db.add(produto)
    db.commit()
    db.refresh(produto)
    return {"msg": "Produto criado", "produto": produto}

@router.get("/produtos")
def listar(db: Session = Depends(get_db)):
    return db.query(models.Produto).all()

@router.post("/produtos/entrada")
def entrada(id: int, quantidade: int, db: Session = Depends(get_db)):
    produto = db.query(models.Produto).filter(models.Produto.id == id).first()

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    produto.quantidade += quantidade
    db.commit()
    return produto

@router.post("/produtos/saida")
def saida(id: int, quantidade: int, db: Session = Depends(get_db)):
    produto = db.query(models.Produto).filter(models.Produto.id == id).first()

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    if produto.quantidade < quantidade:
        raise HTTPException(status_code=400, detail="Estoque insuficiente")

    produto.quantidade -= quantidade
    db.commit()
    return produto