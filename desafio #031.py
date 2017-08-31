"""
desafio #031
Desenvolva um programa que pergunte a distância de uma viagem em KM.
Calcule o preço da passagem, cobrando R$ 0.50 por KM para viagens de até 200KM
e R$ 0.45 para viagens mais longas.
"""

dist = int(input("Qual a distância da viagem em km? "))
if dist <= 200:
    print("O valor da viagem será R$ {:.2f}.".format(dist * 0.5))
else:
    print("O valor da viagem será R$ {:.2f}.".format(dist * 0.45))