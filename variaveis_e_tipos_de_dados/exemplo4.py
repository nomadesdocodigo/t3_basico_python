endereco = {
    "rua": "Rua das Flores",
    "numero": 123,
    "cidade": "São Paulo"
}

# A variável "endereco" é do tipo dicionário
print("Endereço:", endereco)
print("Tipo da variável endereco:", type(endereco))

# mostrando um elemento específico do dicionário
print("Rua:", endereco["rua"])

# adicionando um novo elemento ao dicionário
endereco["estado"] = "SP"

print("Endereço após adicionar estado:", endereco)

# removendo um elemento do dicionário
del endereco["numero"]
print("Endereço após remover numero:", endereco)