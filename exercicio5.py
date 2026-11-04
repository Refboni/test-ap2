def verificar_permissao(usuario):
    return False

def acessar_sistema(usuario):
    if verificar_permissao(usuario):
        return 'Acesso autorizado'
    return 'Acesso negado'