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