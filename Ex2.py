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

