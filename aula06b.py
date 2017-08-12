"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

"""

x=input("Digite algo: ")

print("O tipo do valor é {}".format(type(x)))

print("O valor digitado é decimal? ",x.isdecimal())
print("O valor digitado é alfanum? ",x.isalnum())
print("O valor digitado é alfa? ",x.isalpha())
print("O valor digitado é printable? ",x.isprintable())
print("O valor digitado é maiuculo? ",x.isupper())


