hobbies = ["futebol", "música", "leitura"]

endereco = {
    "rua": "Rua das Flores",
    "numero": 123,
    "cidade": "São Paulo"
}

for hobby in hobbies:
    print("Hobby:", hobby)

print("---")
for chave in endereco:
    print("Chave:", chave)

print("---")
for valor in endereco.values():
    print("Valor:", valor)

print("---")
for chave, valor in endereco.items():
    print("Chave:", chave)
    print("Valor:", valor)

print("---")
for chave in endereco:
    print("Chave:", chave)
    print("Valor:", endereco[chave])

print("---")
for chave in endereco:
    print(f"Chave: {chave} - Valor: {endereco[chave]}")