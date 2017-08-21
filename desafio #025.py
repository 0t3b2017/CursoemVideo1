"""
desagio #025
Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
"""
## Minha resolução ##
#nome = str(input("Digite seu nome: ")).strip()
#print("silva" in nome.lower())

## Guanabara resolução
nome = str(input("Digite seu nome: ")).strip()
print("Seu nome tem Silva: {}".format("silva" in nome.lower()))