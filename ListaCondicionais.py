#1)	Peça 10 números e conte quantos são múltiplos de 3. Use for.
multiplos = 0
for n in range(10):
    numero = int(input(f"Digite o {n+1}° número: "))
    if numero % 3 == 0:
        multiplos +=1

print(f"{multiplos} dos seus números digitados são múltiplos de 3.")

#2)	Crie um programa que simule o uso de senha com tentativas infinitas até digitar a senha correta (use while True).
senhaCorreta = "sabonete"
tentativa = 1
while True:
    senha = input(f"{tentativa}° tentativa - Digite a senha: ")
    senha = senha.lower()
    if senha == senhaCorreta:
        print(f"Senha correta!!\nTentativa: {tentativa}")
        break
    else:
        tentativa +=1

#3)	Monte um sistema que repita um menu até o usuário escolher sair. Use while e break.


while True:
    escolha = int(input("Tecle 1 para continuar\nTecle 2 para sair\n"))
    if escolha == 2:
        break
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

#5) O usuário tem 3 tentativas para acertar a senha. Se errar todas, o acesso é bloqueado. Use while.
senha = "Fernandao123"
tentativas = 1
while tentativas <=3:
    senhaTentativa = input(f"{tentativas}° tentativa- Digite a senha: ").strip()
    if senhaTentativa == senha:
        print(f"\nSenha correta!!!\nn° da tentativa: {tentativas}")
        break
    else:
        if tentativas < 3:
            print("Senha incorreta!")
        else:
            print("Senha bloqueada, você atingiu o limite de 3 erros")
        tentativas = tentativas +1

#6) Peça 10 números e separe em duas listas: pares e ímpares. Mostre as duas no final.
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

#7) Peça uma frase e conte quantas vogais há nela. Mostre o total de cada uma (a, e, i, o, u).
frase = input("Digite uma frase: ")
frase = frase.lower()
qtdVogais = 0
qtdA = 0
qtdE = 0
qtdI = 0
qtdO = 0
qtdU = 0
vogais = ["a","â","ã","á","à","e","é","ê","i","í","o","ó","u","ú"]
for c in frase:
    for v in vogais:
        if c == v:
            qtdVogais +=1
            if v == "a" or v == "á" or v == "à" or v == "ã" or v == "â":
                qtdA +=1
            elif v == "e" or v == "é" or v == "ê":
                qtdE +=1
            elif v == "i" or v == "í":
                qtdI +=1
            elif v == "o" or v == "ó":
                qtdO +=1
            else:
                qtdU +=1

print(f"Existem {qtdVogais} vogais na frase: '{frase}' sendo:\n{qtdA} A's,\n{qtdE} E's,\n{qtdI} I's,\n{qtdO} O's,\n{qtdU} U's,")


print(f"Lista de números ímpares: {listaImpares}")
print(f"Lista de números pares: {listaPares}")

#8) Simule o lançamento de uma moeda até sair "cara" três vezes seguidas.
# (Dica: usar random.choice(["cara", "coroa"]) e while).
import random

while True:
    contador = 0
    escolha = int(input("Aperte 1 para iniciar || Aperte 2 para sair"))
    while contador < 3:
        if escolha == 1:
            input("===Cara ou coroa!!!===\n...\nDigite qualquer tecla para sortear a moeda!")

            jogo = random.choice(["cara" , "coroa"])
            print(f"\nCaiu {jogo}!!\n")
            if jogo  == "cara":
                contador +=1
            else:
                contador = 0
        elif escolha == 2:
            break
        else:
            print("\nSeleção inválida!")
            break

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

#1) Simulação de Populações de Coelhos

#Crie um programa que simule o crescimento de uma população de coelhos ao longo de várias gerações. Os coelhos se reproduzem a uma taxa
# fixa a cada geração, e uma porcentagem deles morre a cada geração. O programa deve solicitar ao usuário a taxa de reprodução, a taxa
# de mortalidade e o número inicial de coelhos. Use um loop for ou while para simular várias gerações e exiba a população de coelhos
# após um número de gerações especificado pelo usuário.
populacaoInicial = int(input("Digite a população inicial de coelhos: "))
taxaReproducao = float(input("Digite a taxa de reprodução da população de coelhos: "))
taxaMortalidade = float(input("Digite a taxa de mortalidade da população de coelhos: "))
nGeracoes = int(input("Digite o número de gerações desejados para fazer a previsão: "))
populacao = populacaoInicial
for n in range(nGeracoes):
    nascidos = populacao * (taxaReproducao / 100)
    mortes = populacao * (taxaMortalidade / 100)
    populacao += nascidos - mortes

print(f"A previsão da população de coelhos para daqui {nGeracoes} gerações é de {round(populacao)} indivíduos.")

'''
2) Jogo da Forca. Crie um jogo da forca, onde:
· Palavra oculta: A palavra é escolhida aleatoriamente de uma lista de palavras pré-definidas. A palavra deve ser exibida com espaços (_)
 representando cada letra. O jogador deve tentar adivinhar as letras da palavra.
· Feedback dinâmico:
o O jogo deve mostrar a palavra com as letras corretas já adivinhadas a cada tentativa.
o O jogo também deve mostrar as letras erradas que o jogador já tentou, para evitar que ele repita a mesma letra.
o Caso o jogador tente uma letra que já tenha sido usada (correta ou incorreta), o jogo deve informar que ele já tentou essa letra,
pedindo que ele tente outra.
· Número de tentativas: O jogador tem um total de 6 tentativas para errar antes de perder o jogo. A cada erro, o número de
tentativas diminui.
· Mensagens de vitória ou derrota:
o O jogo deve informar ao jogador quando ele ganhar, revelando a palavra completa.
o Caso o jogador perca, o jogo deve revelar a palavra e informar que ele perdeu
'''

import random

listaPalavras = ["macarrao", "sabonete", "carro", "burro", "python"]
palavra = listaPalavras[random.randint(0, len(listaPalavras) - 1)]
mascara = []
print("Jogo da Forca")
for char in palavra:
    mascara.append("_")
tentativas = 0
erradas = ""
letrasUsadas = ""

while True:
    if tentativas < 6:
        print("\n" + " ".join(mascara))
        print(f"Letras erradas: {erradas}")
        letra = input("Digite uma letra: ").lower()

        if letra in letrasUsadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letrasUsadas += letra
        correto = False

        for c in range(len(palavra)):
            if letra == palavra[c]:
                mascara[c] = letra
                correto = True

        if not correto:
            erradas += letra + " "
            tentativas += 1
            print(f"Letra errada! Tentativas restantes: {6 - tentativas}")

        if "_" not in mascara:
            print("\nParabéns! Você acertou a palavra:", palavra)
            break
    else:
        print("\nVocê perdeu! A palavra era:", palavra)
        break
