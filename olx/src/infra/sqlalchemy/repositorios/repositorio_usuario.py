from sqlalchemy import delete, select
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
        # usuarios = self.db.query(models.Usuario).all()
        return usuarios


    def obter(self, usuario_id: int):
        stmt = select(models.Usuario).filter_by(id= usuario_id)
        usuario = self.db.execute(stmt).scalar_one()

        return usuario


    def remover(self, usuario_id: int):
        stmt = delete(models.Usuario).where(models.Usuario.id == usuario_id)

        self.db.execute(stmt)
        self.db.commit()
