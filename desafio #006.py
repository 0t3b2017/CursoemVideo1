"""
# desafio #006
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""

num=int(input("Digite um número: "))
print("O dobro de {} é {}\nO triplo de {} é {}\nA raiz quadrada de {} é {}".format(num,(num * 2), num,(num*3),num,int(num ** (1/2))))