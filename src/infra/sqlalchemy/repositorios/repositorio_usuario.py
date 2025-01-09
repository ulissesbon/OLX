from fastapi import HTTPException
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioUsuario():
    
    def __init__(self, db: Session):
        self.db = db


    def criar(self, usuario: schemas.Usuario):
        db_usuario = models.Usuario(
            nome = usuario.nome,
            senha = usuario.senha,
            telefone = usuario.telefone)
        
        self.db.add(db_usuario)
        self.db.commit() 
        self.db.refresh(db_usuario) 
        return db_usuario


    def listar(self):
        stmt = select(models.Usuario)
        usuarios = self.db.execute(stmt).scalars().all()
        return usuarios


    def obter(self, usuario_id: int):
        stmt = select(models.Usuario).filter_by(id= usuario_id)
        usuario = self.db.execute(stmt).scalar()

        return usuario

    def obter_por_telefone(self, telefone: str) -> models.Usuario:
        stmt = select(models.Usuario).where(models.Usuario.telefone == telefone)
        usuario = self.db.execute(stmt).scalars().first()

        return usuario


    def remover(self, usuario_id: int):
        stmt = delete(models.Usuario).where(models.Usuario.id == usuario_id)

        self.db.execute(stmt)
        self.db.commit()


    def editar(self, id_usuario: int, usuario: schemas.Usuario):
        
        usuario_existente = self.db.query(models.Usuario).filter(models.Usuario.id == usuario.id).first()
        if not usuario_existente:
            raise HTTPException(status_code=404, detail= "Usuario não encontrado")
        
        update_stmt = update(models.Usuario
                             ).where(models.Usuario.id == id_usuario
                                     ).values(
                                            nome = usuario.nome,
                                            telefone = usuario.telefone,
                                            senha = usuario.senha,
                                            )
        
        self.db.execute(update_stmt)
        self.db.commit()


    