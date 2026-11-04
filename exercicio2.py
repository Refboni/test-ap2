def inverter_palavras(texto):
    if not texto.strip():
        return ''
    palavras = texto.split()
    return ' '.join(reversed(palavras))