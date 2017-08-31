"""
desafio #029
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada km acima da velocidade permitida.
"""

vel = int(input("Qual a velocidade atual (km/h)? "))
if vel > 80:
    print("Velocidade acima da permitida. \nVocê será multado no valor de R$ {:.2f}".format((vel-80)*7))
else:
    print("Você está dentro da velocidade permitida.")
