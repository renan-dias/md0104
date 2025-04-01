def verificar_desconto(membro_clube, valor_compra):
    """
    Verifica se um cliente tem direito a desconto.

    Args:
        membro_clube (bool): True se o cliente é membro do clube, False caso contrário.
        valor_compra (float): O valor total da compra.

    Returns:
        bool: True se o cliente tem direito a desconto, False caso contrário.
    """
    # Implemente o conectivo lógico "OR" para verificar se o cliente é membro do clube OU a compra é acima de R$100
    # Preencha a linha abaixo com o conectivo apropriado
    if :
        return True
    else:
        return False

# Testes
print(verificar_desconto(True, 50))   # Esperado: True
print(verificar_desconto(False, 150))  # Esperado: True
print(verificar_desconto(False, 50))   # Esperado: False
