def classificar_produto(quantidade):
    if quantidade < 0:
        return 'Quantidade inválida'
    elif quantidade == 0:
        return 'Sem estoque'
    elif 1 <= quantidade <= 5:
        return 'Estoque baixo'
    elif 6 <= quantidade <= 20:
        return 'Estoque normal'
    else:
        return 'Estoque alto'