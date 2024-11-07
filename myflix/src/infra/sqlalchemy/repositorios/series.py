from sqlalchemy import select, delete
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


    def obter(self, serie_id: int):
        stmt = select(models.Series).filter_by(id= serie_id)
        serie = self.db.execute(stmt).scalar_one()

        return serie


    def remover(self, serie_id: int):
        stmt = delete(models.Series).where(models.Series.id == serie_id)

        self.db.execute(stmt)
        self.db.commit()

