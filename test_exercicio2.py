from exercicio2 import inverter_palavras

def test_varias_palavras():
    assert inverter_palavras('Python é muito interessante') == 'interessante muito é Python'

def test_uma_palavra():
    assert inverter_palavras('Python') == 'Python'

def test_string_vazia():
    assert inverter_palavras('') == ''

def test_espacos():
    assert inverter_palavras('  Python   é   bom  ') == 'bom é Python'

def test_numeros_strings():
    assert inverter_palavras('Aula 123 de Python 3') == '3 Python de 123 Aula'