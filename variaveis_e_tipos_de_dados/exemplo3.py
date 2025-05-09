minha_lista = [1, 2, 3, 4, 5]

# A lista é uma variável imutável, ou seja, não podemos alterar os elementos dela diretamente.
# Para alterar um elemento, precisamos criar uma nova lista com os elementos desejados.
print("Lista original:", minha_lista)
print("Tipo da variável minha_lista:", type(minha_lista))

# Adicionando um elemento à lista
minha_lista.append(6)
print("Lista após adicionar 6:", minha_lista)

# Removendo um elemento da lista
minha_lista.remove(3)
print("Lista após remover 3:", minha_lista)

# Alterando um elemento da lista
minha_lista[0] = 10
print("Lista após alterar o primeiro elemento:", minha_lista)

#mostrando um elemento específico da lista
print("Primeiro elemento da lista:", minha_lista[3])