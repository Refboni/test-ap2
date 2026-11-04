def validar_documento(documento):
    if not documento:
        return False
    limpo = str(documento).replace('.', '').replace('-', '').replace(' ', '')
    return limpo.isdigit() and len(limpo) == 11