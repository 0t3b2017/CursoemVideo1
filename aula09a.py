"""
aula09 - Manipulando cadeia de caracteres (Strings)
C u r s o   e m   V  i  d  e  o     P  y  t  h  o  n
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
"""

frase="Curso em Video Python"
#print(frase[9:14])
#print(len(frase))
#print(frase[9:21])
#print(frase[9:21:2])
#print(frase[:5])
#print(frase[15:])
#print(frase[9::3])
#print(frase[::2]) ## The entire string but each two
#print(frase.count('o',0,13))
#print(frase.count('deo'))
#print(frase.find('deo'))
#print(frase.find('Android'))
#print('Curso' in frase)
#print(frase.replace("Python","Android"))
#print(frase.upper())
#print(frase.lower())
#print(frase.capitalize())
#print(frase.title())
frase="   Aprenda Python  "
#print(frase.strip()) #### Remove spaces from beginning and ending
#print(frase.rstrip()) ### Remove spaces in the right side (end)
#print(frase.lstrip()) ### Remove spaces in the left side (begin)
#print(len(frase.split()))) ### list with
#print((frase.split())) ### Divide strings in a list obj by spaces (by default)
#print(len(frase.split()))) ### list with 4
#print("-".join(frase)) # Use symbol hyphen "-" as a separator from characteres
#print("-".join(frase.split())) # Use symbol hyphen "-" as a separator from list's obj
#print(frase.lower().find("Video")) # Find (case insensitive)
#print("""
#This is my text
# with multiple
# lines
#""")
#print(frase[1:15:2])
#print(frase[::2])
#print(frase.count('O'))
#print(frase.upper().count('O'))





frase="Curso em Video Python"
#print(len(frase.strip()))
print(frase.replace('Python','Android'))
print(frase)
frase = frase.replace('Python','Android')
print(frase)



print(frase.find('Video'))
print(frase.find('video'))
print(frase.lower().find('video'))



print(frase.split())
dividido = frase.split()
print(dividido[1:])
print(dividido[:2])
print(dividido[::2])
print(dividido[2][3])
print(dividido[3])
print(frase)
print(dividido[3][0:3]) ## Do 0 a 3 (-1) da terceira palavra
print(len(dividido[0])) ## Primeira palavra
print(len(frase.split()[0])) ## Tamanho da primeira palavra


