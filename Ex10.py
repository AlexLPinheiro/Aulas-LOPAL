#10) Crie um programa que leia uma sequência de números e determine o segundo maior número.
listaNumeros = []
maior = 0
while True:
    opcao = input("Digite 1 para adicionar o número na sequência || Digite 2 para terminar a sequência.")
    if opcao == "1":
        numero = float(input("Digite o número: "))
        listaNumeros.append(numero)

    elif opcao == "2":
        break
    else:
        print("\nOpção fora da sequência!! Digite novamente.")

listaNumeros.sort()
print(f"O segundo maior número na lista {listaNumeros} é {listaNumeros[len(listaNumeros)-2]}")
