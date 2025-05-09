# Python utiliza tipos de dados dinâmicos, ou seja, não é necessário declarar o tipo da variável
# para atribuir um valor a ela. O tipo da variável é determinado automaticamente pelo Python com base no valor atribuído.

# Exemplo de variáveis com diferentes tipos de dados
# A variável "nome" é do tipo string
nome = "João"
nome2 = 'João'
# A variável "idade" é do tipo inteiro
idade = 30
# A variável "altura" é do tipo float
altura = 1.75
# A variável "casado" é do tipo booleano (True ou False)
casado = True
# A variável "hobbies" é do tipo lista
hobbies = ["futebol", "música", "leitura"]
endereco_lista = ["Rua das Flores", 123, "São Paulo"]
# A variável "endereco" é do tipo dicionário
endereco = {
    "rua": "Rua das Flores",
    "numero": 123,
    "cidade": "São Paulo"
}
# A variável "nada" é do tipo None
nada = None


print("Idade:", idade)
print("Tipo da variável idade:", type(idade))