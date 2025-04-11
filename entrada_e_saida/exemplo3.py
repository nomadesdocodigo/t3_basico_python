entrada = input("Digite um número: ")
print(type(entrada))
# A função input() sempre retorna uma string, mesmo que o usuário digite um número
# Para converter a string para um número, usamos a função int() ou float()  
entrada = int(entrada)
# ou
# entrada = float(entrada)
print(type(entrada))
print("O dobro do número digitado é:", entrada * 2)