from datetime import datetime, timedelta, timezone
from jose import jwt  

#JOSE Config vars
SECRET_KEY = '9e2501934d067d71bb1c5850722a73d1'
ALGORITHM = 'HS256'
EXPIRES_IN_MINUTES = 300


def criar_token_acesso(data: dict):
    dados = data.copy()
    expiracao = datetime.now(timezone.utc) + timedelta(minutes= EXPIRES_IN_MINUTES)

    dados.update({'exp': expiracao})

    token_jwt = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt


def verificar_token_acesso(token: str):
    carga = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    return carga.get('sub')