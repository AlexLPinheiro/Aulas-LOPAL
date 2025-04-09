#1)	Peça 10 números e conte quantos são múltiplos de 3. Use for.
multiplos = 0
for n in range(10):
    numero = int(input(f"Digite o {n+1}° número: "))
    if numero % 3 == 0:
        multiplos +=1

print(f"{multiplos} dos seus números digitados são múltiplos de 3.")