"""
desafio #028
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para
o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa escreverá na tela se o usuário venceu ou perdeu.
"""
from random import randint

c_num = randint(1, 5)
u_num = int(input("Tente adivinhar um número entre 1 e 5: "))
if c_num != u_num:
    print("Você perdeu! :( \nO número {} não foi o escolhido pelo computador. \nO computador escolheu o número {}".format(u_num, c_num))
else:
    print("Parabéns!!!! :) \nVocê acertou, o computador escolheu o número {}".format(c_num))

