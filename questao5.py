def pode_dirigir(idade, cnh_suspensa):
    """
    Verifica se uma pessoa pode dirigir.

    Args:
        idade (int): A idade da pessoa.
        cnh_suspensa (bool): True se a CNH está suspensa, False caso contrário.

    Returns:
        bool: True se a pessoa pode dirigir, False caso contrário.
    """
    maior_de_idade = idade >= 18
    # Implemente os conectivos lógicos "AND" e "NOT" para verificar se a pessoa é maior de idade E a CNH não está suspensa
    # Preencha a linha abaixo com os conectivos apropriados
    if :
        return True
    else:
        return False

# Testes
print(pode_dirigir(20, False))  # Esperado: True
print(pode_dirigir(17, False))  # Esperado: False
print(pode_dirigir(25, True))   # Esperado: False
