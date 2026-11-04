def gerar_codigo():
    return 'USR-1234'

def criar_identificacao(nome):
    codigo = gerar_codigo()
    return f'Usuário {nome} cadastrado com código {codigo}.'