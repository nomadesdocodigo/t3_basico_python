idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
    print("Você pode dirigir.")
else: # Se a condição do if não for atendida, o else será executado
    print("Você é menor de idade.")
    print("Você não pode dirigir.")
