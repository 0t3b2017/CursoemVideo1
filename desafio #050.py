"""
desafio #050

Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o número for impar, desconsidere-o.
"""
lista = []
total = 0
for i in range(1, 7):
    lista.append(int(input("Digite um número: ")))

for i in lista:
    if i % 2 == 0:
        total = total + i
print("A soma dos números pares é {}".format(total))
