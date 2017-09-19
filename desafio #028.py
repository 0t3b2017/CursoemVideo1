"""
desafio #028
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para
o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa escreverá na tela se o usuário venceu ou perdeu.
"""
from random import randint
from time import sleep

c_num = randint(1, 5)
print("\033[36m=+=\033[m" * 20)
print("Vou pensar em um número de 1 a 5")
print("\033[36m=+=" * 20)

u_num = int(input("\033[33mTente adivinhar um número entre 1 e 5: \033[m"))
print("Hummmmm...")

sleep(3)
if c_num != u_num:
    print("\033[31mVocê perdeu! :( \033[m\nO número {} não foi o escolhido pelo computador. \nO computador escolheu o número {}".format(u_num, c_num))
else:
    print("\033[34mParabéns!!!! :) \033[m\nVocê acertou, o computador escolheu o número {}".format(c_num))

