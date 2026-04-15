from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models
from passlib.context import CryptContext
from schemas import Login

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def hash_senha(senha: str):
    return pwd_context.hash(senha)

def verificar_senha(senha, hash):
    return pwd_context.verify(senha, hash)

@router.post("/registro")
def registrar(dados: Login, db: Session = Depends(get_db)):
    usuario = models.Usuario(email=dados.email, senha=hash_senha(dados.senha))
    db.add(usuario)
    db.commit()
    return {"msg": "Usuário criado"}

@router.post("/login")
def login(dados: Login, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.email == dados.email).first()

    if not usuario or not verificar_senha(dados.senha, usuario.senha):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    return {"msg": "Login OK", "usuario": usuario.email}