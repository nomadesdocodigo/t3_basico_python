idade = int(input("Digite sua idade: "))

if idade > 60:
    print("Você é idoso.")
elif idade >= 18:
    print("Você é adulto.")
elif idade >= 12:
    print("Você é adolescente.")
elif idade >= 5:
    print("Você é criança.")
else:
    print("Você é bebê.")

# A estrutura if-elif-else permite verificar várias condições em sequência,
# porém para de verificar as condições posteriores quando uma das condições
# é atendida (Verdadeira).