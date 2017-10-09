"""
desafio #045

Crie um programa que faça o computador jogar Jokenpo com você.
"""

from random import choice

all_opc = ['pedra', 'papel', 'tesoura']

opc_pc = choice(all_opc)
opc_user = int(input("""Selecione uma das opções abaixo:

1 => Pedra
2 => Papel
3 => Tesoura

Digite uma opção: """))

if opc_user == 1:
    if opc_pc == 'pedra':
        print("Empate, eu também escolhi {}. Tente novamente!".format(opc_pc))
    elif opc_pc == 'papel':
        print("Você perdeu! Eu escolhi {}.".format(opc_pc))
    else:
        print("Parabéns, você ganhou! Eu escolhi {}.".format(opc_pc))
elif opc_user == 2:
    if opc_pc == 'papel':
        print("Empate, eu também escolhi {}. Tente novamente!".format(opc_pc))
    elif opc_pc == 'tesoura':
        print("Você perdeu! Eu escolhi {}.".format(opc_pc))
    else:
        print("Parabéns, você ganhou! Eu escolhi {}.".format(opc_pc))
elif opc_user == 3:
    if opc_pc == 'tesoura':
        print("Empate, eu também escolhi {}. Tente novamente!".format(opc_pc))
    elif opc_pc == 'pedra':
        print("Você perdeu! Eu escolhi {}.".format(opc_pc))
    else:
        print("Parabéns, você ganhou! Eu escolhi {}.".format(opc_pc))