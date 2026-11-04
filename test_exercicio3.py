from exercicio3 import validar_documento

def test_11_digitos():
    assert validar_documento('12345678900') is True

def test_formatado():
    assert validar_documento('123.456.789-00') is True

def test_menos_11_digitos():
    assert validar_documento('123456789') is False

def test_mais_11_digitos():
    assert validar_documento('1234567890011') is False

def test_com_letras():
    assert validar_documento('1234567890a') is False

def test_vazio():
    assert validar_documento('') is False