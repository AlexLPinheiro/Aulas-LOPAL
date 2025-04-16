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