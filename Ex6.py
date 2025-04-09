contador = 1
listaPares = []
listaImpares = []
while True:
    if contador <= 10:
        numero = int(input(f"Digite o {contador}° número: "))
        if numero % 2 ==0:
            listaPares.append(numero)
        else:
            listaImpares.append(numero)
        contador +=1
    else:
        break


print(f"Lista de números ímpares: {listaImpares}")
print(f"Lista de números pares: {listaPares}")
