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
