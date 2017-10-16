"""
desafio #037

Escreva um programa que leia um número inteiro (em decimal) e peça para o usuário escolher qual será a base de conversão:

1 para binário
2 para octal
3 para hexadecimal
"""

"""
num = int(input("Digite um número: "))

opc = int(input(\"""Selecione uma das base de conversão desejada: 

                    1 => binário
                    2 => octal
                    3 => hexadecimal
                    digite: \"""))

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
"""

## Guanabara

num = int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('\nSua opção: '))
print('')

if opcao == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Favor selecionar uma das opções disponíveis.')
