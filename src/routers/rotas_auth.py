from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Usuario, UsuarioSimples
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.providers import hash_provider



router = APIRouter(prefix="/usuarios")


# USUARIOS

@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model= UsuarioSimples)
def criar_usuario(usuario: Usuario, db: Session= Depends(get_db)):
    usuario.senha = hash_provider.gerar_hash(usuario.senha)

    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado



@router.get('/view/{usuario_id}')
def obter_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario_encontrado = RepositorioUsuario(db).obter(usuario_id)

    if not usuario_encontrado:
        return HTTPException(status_code=404)
    return usuario_encontrado.to_dict()


@router.delete('/delete/{usuario_id}')
def deletar_usuario(usuario_id: int, db: Session= Depends(get_db)):
    RepositorioUsuario(db).remover(usuario_id)

    return{'Msg': 'Usuario removido com sucesso'}


@router.put('/edit/{usuario_id}')
def atualizar_produto(usuario_id: int, usuario: Usuario, db: Session= Depends(get_db)):

    usuario.id = usuario_id

    RepositorioUsuario(db).editar(usuario_id, usuario)

    return usuario