def print_bonito(texto):
    tamanho = len(texto)
    print("#" * 24)

    if tamanho > 20:
        print(f"# {texto[0:17]}... #") # posso também colocar texto[:20]
    else:
        print(f"# {texto: ^20} #")
    print("#" * 24)

print_bonito("Menu principal")
print_bonito("Tela de login")
print_bonito("Tela de cadastro")
print_bonito("Tela de produtos")
print_bonito("Tela de vendas")
print_bonito("Texto muito longo da tela de vendas que não cabe na tela")
print_bonito("Oi")
