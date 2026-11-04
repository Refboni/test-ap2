from unittest.mock import patch
from exercicio4 import criar_identificacao

def test_correta():
    with patch('exercicio4.gerar_codigo') as mock_gerar:
        mock_gerar.return_value = 'USR-1234'
        resultado = criar_identificacao('Carlos')
        assert resultado == 'Usuário Carlos cadastrado com código USR-1234.'

def test_gerar_codigo():
    with patch('exercicio4.gerar_codigo') as mock_gerar:
        criar_identificacao('Carlos')
        assert mock_gerar.called

def test_gerar_codigo_chamada_apenas_uma_vez():
    with patch('exercicio4.gerar_codigo') as mock_gerar:
        criar_identificacao('Carlos')
        mock_gerar.assert_called_once()

def test_mock_diferentes_codigos():
    with patch('exercicio4.gerar_codigo') as mock_gerar:
        mock_gerar.return_value = 'USR-9999'
        resultado = criar_identificacao('Carlos')
        assert 'USR-9999' in resultado

def test_nomes_diferentes():
    with patch('exercicio4.gerar_codigo') as mock_gerar:
        mock_gerar.return_value = 'USR-1234'
        resultado = criar_identificacao('Ana')
        assert 'Usuário Ana' in resultado