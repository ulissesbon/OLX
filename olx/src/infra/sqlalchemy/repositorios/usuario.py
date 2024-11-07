from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioUsuario():
    
    def __init__(self, db: Session):
        self.db = db


    def criar(self, usuario: schemas.Usuario):
        db_usuario = models.Usuario(
            nome = usuario.nome,
            telefone = usuario.telefone)
        
        self.db.add(db_usuario)
        self.db.commit() 
        self.db.refresh(db_usuario) 
        return db_usuario


    def listar(self):
        usuarios = self.db.query(models.Usuario).all()
        return usuarios


    def obter(self):
        pass


    def remover(self):
        pass