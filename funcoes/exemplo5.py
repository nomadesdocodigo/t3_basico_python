def soma(a, b):
    return a + b

while True:
    a = int(input("Digite o primeiro número (ou digite zero para finalizar): "))
    if a == 0:
        break
    b = int(input("Digite o segundo número: "))
    resultado = soma(a, b)
    print(f"A soma entre {a} e {b} é igual a {resultado}.")

print("Programa finalizado.")