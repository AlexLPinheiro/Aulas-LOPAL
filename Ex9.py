#9) Crie um programa que leia uma sequência de números e determine quantos números são menores que a média.
listaNumeros = []
soma = 0
while True:
    opcao = input("Digite 1 para adicionar o número na sequência || Digite 2 para terminar a sequência.")
    if opcao == "1":
        numero = float(input("Digite o número: "))
        soma += numero
        listaNumeros.append(numero)

    elif opcao == "2":
        break
    else:
        print("\nOpção fora da sequência!! Digite novamente.")
media = soma/ len(listaNumeros)
print(f"\nA média é igual a : {media:.2f}")
menores = ""
for n in listaNumeros:
    if n < media:
        menores  = menores + str(n) + ", "
print(f"\nNúmeros menores que a média: {menores[:len(menores)-1]}.")

