### Estruturas condicionais aninhadas.

nome = str(input('Qual é o seu nome? '))
if nome == 'Roberto':
    print('\033[32mQue nome Bonito você tem {}!\033[m'.format(nome))
elif nome == 'Lorena' or nome == 'Daysa':
    print('Você é da família Rocha Lima!!!')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino!')
else:
    print('\033[31mSeu nome é tão comum {}.\033[m'.format(nome))
print('\033[30mTenha um ótimo dia.\033[m'.format(nome))
