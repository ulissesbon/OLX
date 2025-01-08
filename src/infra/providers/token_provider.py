from datetime import datetime, timedelta, timezone
from jose import jwt  # type: ignore


#JOSE Config vars
SECRET_KEY = 'chave-secreta'
ALGORITHM = 'HS256'
EXPIRES_IN_MINUTES = 30


def criar_token_acesso(data: dict):
    dados = data.copy()
    expiracao = datetime.now(timezone.utc) + timedelta(minutes= EXPIRES_IN_MINUTES)

    dados.update({'exp': expiracao})

    token_jwt = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt


def verificar_token_acesso(token: str):
    payload = jwt.encode(token, SECRET_KEY, algorithm=ALGORITHM)

    return payload