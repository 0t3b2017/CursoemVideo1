"""
desafio #033
Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.

"""
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

# Verifica o menor número
if (n1 < n2) and (n1 < n3):
    print("O número {} é o menor.".format(n1))
else:
    if n2 < n3:
        print("O número {} é o menor.".format(n2))
    else:
        print("O número {} é o menor.".format(n3))

# Verifica o maior número
if (n1 > n3) and (n1 > n2):
    print("O número {} é o maior.".format(n1))
else:
    if n2 > n3:
        print("O número {} é o maior.".format(n2))
    else:
        print("O número {} é o maior.".format(n3))
