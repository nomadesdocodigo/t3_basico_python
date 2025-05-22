# Comentário de uma linha

"""
Comentário
de
várias
linhas
"""

# Comentário de várias linhas logo depois da definição da função
# é chamado de 'docstring' e serve para documentar a função.
# Docstring é uma string que descreve o que a função faz.

def soma(a, b):
    """
    Função que soma dois números.
    E este é um exemplo de docstring.
    Tudo que eu colocar aqui vai aparecer quando eu passar o mouse sobre a função.

    :param a: Primeiro número da soma.
    :param b: Segundo número da soma.
    :return: Retorna o resultado da soma entre os parâmetros de entrada 'a' e 'b'.
    """
    return a + b

print("Este é o inicio do meu programa")
print(soma(10, 20))

