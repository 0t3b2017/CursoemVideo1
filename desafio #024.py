"""
desafio #024
Crie um programa que leia o nome de uma cidade e diga se ela começa com o nome "SANTO".
"""

## PRIMEIRA OPCAO
#cid = str(input("Digite o nome da cidade: "))
#if cid.lower().split()[0] == "santo":
#    print("O nome da cidade {} começa com santo.".format(cid))
#else:
#    print("O nome da cidade {} não começa com santo.".format(cid))

## SEGUNDA OPCAO
#cid = str(input("Digite o nome da cidade: "))
#print("A cidade começa com 'santo': {}".format("santo" in cid.lower().split()[0]))

## Guanabara resolução
cid = str(input("Digite o nome da cidade: ")).strip()
print(cid[:5].upper == "SANTO")
