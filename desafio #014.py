"""
desafio conversor de temperatura
Converter entre ºC e ºF
"""

cores = {"amarelo": "\033[33m", "limpa": "\033[m"}

a = input("""Which conversion do?
{}(F|f) = from Fahrenheit to Celsius
(C|c) = from Celsius to Fahrenheit{}
Enter (F or C):""".format(cores["amarelo"], cores["limpa"]))

if a == "C" or a == "c":
    c = float(input("Enter a temperature in ºC: "))
    f = c * 1.8 + 32
    print("Em Fahrenheit {}ºC is {}ºF".format(c, f))
elif a == "F" or a == "f":
    f = float(input("Enter a temperature in ºF: "))
    c = (f - 32) / 1.8
    print("Em Celcius {}ºF is {}ºC".format(f, c))
else:
    print("\033[31mERROR: YOU SHOULD CHOOSE BETWEEN C OR F!\033[m")
