"""
desafio #052

Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
while True:
    num = int(input("Digite um número: "))
    if num == 1:
        print("Digite um número inteiro a partir de 2.")
    else:
        break

teste = 0

for n in range(num, 0, -1):
    if (n == 1) or (n == num):
        continue
    else:
        expressao = (num % n) == 0
        if expressao:
            print("Número {} \033[31mnão\033[m é primo".format(num))
            teste = 1
            break
if teste == 0:
    print("Número {} \033[32mé\033[m primo".format(num))



