from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Usuario, UsuarioSimples, LoginData
from src.infra.sqlalchemy.config.database import get_db, criar_db
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.providers import hash_provider


router = APIRouter(prefix="/auth")


# AUTENTICAÇÃO DE USUÁRIO

@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model= UsuarioSimples)
def criar_usuario(usuario: Usuario, db: Session= Depends(get_db)):
    # verificação se já existe
    usuario_localizado = RepositorioUsuario(db).obter_por_telefone(usuario.telefone)

    if usuario_localizado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Usuário já existente')

    # criando o usuario
    usuario.senha = hash_provider.gerar_hash(usuario.senha)

    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado


@router.post('/token', status_code=status.HTTP_202_ACCEPTED)
def login(login_data: LoginData, db: Session= Depends(get_db)):
    senha = login_data.senha
    telefone = login_data.telefone

    usuario = RepositorioUsuario(db).obter_por_telefone(telefone)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Telefone ou senha incorretos')

    senha_valida = hash_provider.verificar_hash(senha, usuario.senha)
    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Telefone ou senha incorretos')

    # Gerar KWT

    return usuario


