# Exercício Python 11: Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
# viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia=float(input("distancia da viagem em km: "))
if distancia <= 200:
    print(f"valor da viagem: R${distancia*0.50:.2f}")
else:
    print(f"valor da viagem: R${distancia*0.45:.2f}")