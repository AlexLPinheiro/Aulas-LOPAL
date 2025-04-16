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


