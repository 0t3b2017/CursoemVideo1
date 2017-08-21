## Testes

frase = "Curso em Video Python"
frase = "This is my incredible phrase in a exciting cryptography algorith"
a = frase[::2]
b = frase[1::2]
la = len(a)
lb = len(b)
na = 0
nb = 0
print('a = ',a)
print('b = ',b)
print('a + b = ',end='')
while na < la:
    print(a[na], end='')
    na = na + 1
    if nb < lb:
        print(b[nb], end='')
        nb = nb + 1
