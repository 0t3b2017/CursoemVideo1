"""
desafio #053
Crie um programa que leia uma frase qualquer e diga se ela é um polindromo, desconsiderando os espaços.

Ex.
apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona
"""

print("Sua frase é um Políndromo? Vamos ver...")
frase = str(input("Digite uma frase: "))

# Remove white spaces and make lower case
f = frase.lower().strip().replace(' ','')

f_len = len(f) - 1
reverse_frase = ''
n = f_len

# Write the reverse phrase
while n >= 0:
    letter = f[n]
    reverse_frase = reverse_frase + letter
    n -= 1

# Compare if it is a polindromo
if f == reverse_frase:
    print("\033[33mA frase '{}' é um políndromo\033[m".format(frase))
else:
    print("\033[31mA frase '{}' não é um políndromo\033[m".format(frase))
