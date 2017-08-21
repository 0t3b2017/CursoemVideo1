"""
Crie um programa que leia o nome completo de uma pessoa e mostre:

- O nome com todas as letras maiúsculas
- O nome com todas as letras minusculas
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome.
"""

name = str(input("Type your name: ")).strip()
print("Seu nome em letras maiúsculas é {}.".format(name.upper()))
print("Seu nome em letras minúsculas é {}.".format(name.lower()))
# print(name.strip())
# print(name.capitalize())
# print(name.title())
# Minha ideia
print("Seu nome ao todo tem {} letras.".format(len(''.join(name.split()))))
# Guanabara ideia
print("Seu nome ao todo tem {} letras.".format(len(name) - name.count(' ')))
# Minha ideia # Split the name in a list and then verify the lenght of the first name.
print("Seu primeiro nome tem {} letras.".format(len(name.split()[0])))
# Guanabara ideia # Find de first space position. As the index starts with 0, the count matches.
print("Seu primeiro nome tem {} letras.".format(name.find(' ')))
