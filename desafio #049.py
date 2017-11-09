"""
desafio #049

Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora
utilizando um laço for
"""

num = int(input("Digite um número: "))

print("A tabuada do número {} é:".format(num))
for i in range(1, 11):
    valor = num * i
    print("{} X {} = {}".format(num, i, valor))
