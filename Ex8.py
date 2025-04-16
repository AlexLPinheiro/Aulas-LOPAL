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


