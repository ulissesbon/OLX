def write_notification(email: str, msg=''):
    with open('log.txt', mode='a') as email_file:
        conteudo = f'Email: {email} - msg: {msg}\n'
        email_file.write(conteudo)