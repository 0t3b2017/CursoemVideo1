"""
desafio #026
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "a"
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece pela última vez.
"""
frase = str(input("Digite um frase: ")).lower().strip()
print("Aparece a letra a {} vezes nesta frase.".format(frase.lower().count("a")))
print("A letra 'a' aparece pela primeira vez na posição {}".format(frase.find("a")+1))
print("A letra 'a' aparece pela última vez na posição {}".format(frase.rfind("a")+1))
