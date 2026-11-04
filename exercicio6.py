def obter_proximo_cliente():
    return None

def registrar_atendimento(cliente):
    return True

def atender_proximo_cliente():
    cliente = obter_proximo_cliente()
    if not cliente:
        return 'Fila vazia'
    
    sucesso = registrar_atendimento(cliente)
    if sucesso:
        return 'Atendimento realizado'
    return 'Falha no atendimento'