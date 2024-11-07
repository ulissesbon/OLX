from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import criar_db, get_db
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.series import RepositorioSerie

criar_db()


app = FastAPI()


@app.post('/series')
def criar_serie(serie: schemas.Series, db: Session= Depends(get_db)):
    serie_criada = RepositorioSerie(db).criar(serie)
    return serie_criada

@app.get('/series')
def listar_series(db: Session= Depends(get_db)):
    #series = RepositorioSerie(db).listar()
    return RepositorioSerie(db).listar()