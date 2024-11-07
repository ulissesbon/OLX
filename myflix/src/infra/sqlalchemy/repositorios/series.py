from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioSerie():
    
    def __init__(self, db: Session):
        self.db = db


    def criar(self, serie: schemas.Series): 
        db_serie = models.Series(
            titulo = serie.titulo,
            ano = serie.ano,
            genero = serie.genero,
            qtd_temps = serie.qtd_temps)
        
        self.db.add(db_serie) 
        self.db.commit()      
        self.db.refresh(db_serie)
        return db_serie          


    def listar(self):
        series = self.db.query(models.Series).all()
        return series


    def obter(self):
        pass


    def remover(self):
        pass

