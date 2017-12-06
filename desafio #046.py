"""
desafio #046
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de
artifícios, indo de 10 até 0, com pausa de 1 segundo entre eles.
"""
from time import sleep
import emoji

for i in range(10, 0, -1):
    print(i)
    sleep(1)
print(emoji.emojize(u'media:bomb:'))





