from unittest.mock import patch
from exercicio6 import atender_proximo_cliente

def test_sucesso():
    with patch('exercicio6.obter_proximo_cliente') as mock_obter, \
         patch('exercicio6.registrar_atendimento') as mock_registrar:
        mock_obter.return_value = 'Maria'
        mock_registrar.return_value = True
        assert atender_proximo_cliente() == 'Atendimento realizado'

def test_fila_vazia():
    with patch('exercicio6.obter_proximo_cliente') as mock_obter:
        mock_obter.return_value = None
        assert atender_proximo_cliente() == 'Fila vazia'

def test_falha_registrar_():
    with patch('exercicio6.obter_proximo_cliente') as mock_obter, \
         patch('exercicio6.registrar_atendimento') as mock_registrar:
        mock_obter.return_value = 'João'
        mock_registrar.return_value = False
        assert atender_proximo_cliente() == 'Falha no atendimento'

def test_obter_proximo():
    with patch('exercicio6.obter_proximo_cliente') as mock_obter:
        mock_obter.return_value = None
        atender_proximo_cliente()
        mock_obter.assert_called_once()

def test_registrar_atendimento_cliente_correto():
    with patch('exercicio6.obter_proximo_cliente') as mock_obter, \
         patch('exercicio6.registrar_atendimento') as mock_registrar:
        mock_obter.return_value = 'Beatriz'
        mock_registrar.return_value = True
        atender_proximo_cliente()
        mock_registrar.assert_called_once_with('Beatriz')

def test_registrar_nao_foi_chamado_fila_vazia():
    with patch('exercicio6.obter_proximo_cliente') as mock_obter, \
         patch('exercicio6.registrar_atendimento') as mock_registrar:
        mock_obter.return_value = None
        atender_proximo_cliente()
        mock_registrar.assert_not_called()

        #ola