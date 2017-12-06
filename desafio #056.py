"""
desafio #056

Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo
- Qual o nome do homem mais velho
- Quantas mulheres tem menos de 20 anos.

"""
somaidade = 0
maisvelho = 0
nomevelho = ''
qtd_mulher = 0
for p in range(1, 5):
    print(' ------ {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if sexo in 'mM':
        if idade > maisvelho:
            maisvelho = idade
            nomevelho = nome
    if sexo in 'fF':
        if idade < 20:
            qtd_mulher += 1

mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O nome do homem mais velho é {}'.format(nomevelho))
print('São {} mulheres com menos de 20 anos.'.format(qtd_mulher))
