"""
desafio #043

Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com
a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Subrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""

peso = float(input("Digite seu peso (Kg): "))
altura = float(input("Digite sua altura (Mts): "))

IMC = peso / (altura ** 2)

print("Seu IMC é: \033[32m{:.2f}\033[m".format(IMC))

if IMC < 18.5:
    print("Vocé está abaixo do peso.")
elif IMC < 25:
    print("Parabéns, você está no seu peso ideal.")
elif IMC < 30:
    print("Vpcê está acima do peso.")
elif IMC < 40:
    print("Cuidado, você está bem acima do peso, considerado obsidade.")
else:
    print("Procure um médico, você está muito acima do peso, considerado obesisdade mórbida.")
