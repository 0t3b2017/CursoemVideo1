"""
desafio #040

Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
nédia atingida.

- Média abaixo de 5.0: Reprovado
- Media entre 5.0 e 6.9: Recuperação
- Média 7.0 ou superior: Aprovado
"""

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
print("Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}".format(n1, n2, media))

if media < 5.0:
    print("\033[31mAluno reprovado. :(\033[m")
elif media < 6.9:
    print("\033[33mAluno em recuperação. :|\033[m")
else:
    print("\033[32mAluno aprovado. Parabéns!!! :)\033[m")
