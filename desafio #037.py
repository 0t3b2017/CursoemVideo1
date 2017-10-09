"""
desafio #037

Escreva um programa que leia um número inteiro (em decimal) e peça para o usuário escolher qual será a base de conversão:

1 para binário
2 para octal
3 para hexadecimal
"""

num = int(input("Digite um número: "))

opc = int(input("""Selecione uma das base de conversão desejada: 

                    1 => binário
                    2 => octal
                    3 => hexadecimal
                    digite: """))

if opc == 1:
    base = 2
    rest = []
    divisor = num
    while divisor >= 1:
        rest.append(divisor % base)
        divisor = divisor // base
    rest.reverse()

    print("\nO valor {} em binário é ".format(num), *rest, sep='')
elif opc == 2:
    base = 8
    rest = []
    divisor = num
    while divisor >= 1:
        rest.append(divisor % base)
        divisor = divisor // base
    rest.reverse()

    print("\nO valor {} em binário é ".format(num), *rest, sep='')
elif opc == 3:
    base = 16
    rest = []
    divisor = num
    while divisor >= 1:
        rest.append(divisor % base)
        divisor = divisor // base
    rest.reverse()

    print("\nO valor {} em binário é ".format(num), *rest, sep='')
else:
    print("\n\033[31mOpção inválida\033[m")
