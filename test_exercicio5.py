from unittest.mock import patch
from exercicio5 import acessar_sistema

def test_com_permissao():
    with patch('exercicio5.verificar_permissao') as mock_verificar:
        mock_verificar.return_value = True
        assert acessar_sistema('Carlos') == 'Acesso autorizado'

def test_sem_permissao():
    with patch('exercicio5.verificar_permissao') as mock_verificar:
        mock_verificar.return_value = False
        assert acessar_sistema('João') == 'Acesso negado'

def test_verificar_permissao():
    with patch('exercicio5.verificar_permissao') as mock_verificar:
        acessar_sistema('Carlos')
        assert mock_verificar.called

def test_verificar_permissao_usuario_correto():
    with patch('exercicio5.verificar_permissao') as mock_verificar:
        acessar_sistema('Mariana')
        mock_verificar.assert_called_once_with('Mariana')

def test_mock_ambos_cenarios():
    with patch('exercicio5.verificar_permissao') as mock_verificar:
        mock_verificar.return_value = True
        res_autorizado = acessar_sistema('Admin')
        
        mock_verificar.return_value = False
        res_negado = acessar_sistema('Visitante')
        
        assert res_autorizado == 'Acesso autorizado'
        assert res_negado == 'Acesso negado'