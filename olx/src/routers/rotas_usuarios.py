from fastapi import APIRouter, status, Depends
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Usuario
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario



router = APIRouter(prefix="/usuarios")


# USUARIOS

@router.post('/add', status_code=status.HTTP_201_CREATED, response_model= Usuario)
def criar_usuario(usuario: Usuario, db: Session= Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado



# @app.get('/usuarios')#, response_model= Usuario)
@router.get('/all', response_model= List[Usuario])
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios


@router.get('/view/{usuario_id}')
def obter_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return RepositorioUsuario(db).obter(usuario_id)


@router.delete('/delete/{usuario_id}')
def deletar_usuario(usuario_id: int, db: Session= Depends(get_db)):
    RepositorioUsuario(db).remover(usuario_id)

    return{'Msg': 'Usuario removido com sucesso'}