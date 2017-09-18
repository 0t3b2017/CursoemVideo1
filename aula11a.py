## Aula 011 - Cores no terminal

"""
print("\033[1;33;46mOla mundo!!!\033[m")
print("\033[7;33;46mOla mundo!!!\033[m")
print("\033[0;30;41mOlá mundo!!!\033[m")
print("\033[7;30;41mOlá mundo!!!\033[m")
print("\033[4;33;44mOlá mundo!!!\033[m")
print("\033[1;35;43mOlá mundo!!!\033[m")
print("\033[30;42mOlá mundo!!!\033[m")
print("\033[mOlá mundo!!!")
print("\033[7;30mOlá mundo!!!\033[m")
print("\033[1;30;45mOlá mundo!!!\033[m")
"""

"""
a = 3
b = 5
print("Os valores são \033[7;31m{}\033[m e \033[0;31m{}\033[m!!!!".format(a, b))
"""

"""
nome = 'OTEB'
print("Olá! Muito prazer em te conhecer, {}{}{}!!!".format('\033[7m', nome, '\033[m'))
"""

nome = 'OTEB'
cores = {"limpa": "\033[m",
         "azul": "\033[1;34m",
         "vermelho": "\033[1;31m",
         "amarelo": "\033[1;33m",
         "pretoebranco": "\033[7;30m"}

print("Olá! Muito prazer em te conhecer, {}{}{}!!!".format(cores['amarelo'],nome, cores["limpa"]))
print("Hoje está {}{}{}".format(cores['vermelho'], 'muito calor!', cores["limpa"]))
print("Hoje está {}{}{}".format(cores['azul'], 'muito frio!', cores["limpa"]))
