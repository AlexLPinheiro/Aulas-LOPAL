#4)	Crie um programa que peça dois números inteiros e exiba todos os números entre eles que são primos. Use for.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
primo = True

if num1 > num2:
    num2, num1 = num1 , num2

if num1 == 0:
    primeiroNum = num1+2
else:
    primeiroNum = num1+1

for n in range(primeiroNum, num2):
    contador = 2
    while contador < n:
        if n % contador == 0:
            primo = False
            break
        else:
            primo = True
            contador = contador + 1

    if primo:
        print(n)




