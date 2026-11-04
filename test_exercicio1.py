from exercicio1 import classificar_produto

def test_sem_estoque():
    assert classificar_produto(0) == 'Sem estoque'

def test_baixo():
    assert classificar_produto(3) == 'Estoque baixo'

def test_normal():
    assert classificar_produto(10) == 'Estoque normal'

def test_alto():
    assert classificar_produto(25) == 'Estoque alto'

def test_negativa():
    assert classificar_produto(-5) == 'Quantidade inválida'
