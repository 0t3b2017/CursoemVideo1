"""
desafio #044

Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
de pagamento:

- À vista dinheiro / cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até duas vezes no cartão: Preço normal
- 3x ou mais no cartão: 20% de juros
"""

preco = float(input("Digite o preço do produto: R$ "))
forma_pgmt = int(input("""Digite a forma de pagamento:
                          
1 => À vsta dinheiro / cheque
2 => Á vista no cartão
3 => Em até 2x no cartão
4 => 3x ou mais no cartão
                          
Digite um número e pressione Enter: """))

print("")
if forma_pgmt == 1:
    print("O valor a ser pago será de R${:.2f}".format(preco - preco * 0.1))
elif forma_pgmt == 2:
    print("O valor a ser pago será de R${:.2f}".format(preco - preco * 0.05))
elif forma_pgmt == 3:
    print("O valor total a ser pago será de R${:.2f}".format(preco))
elif forma_pgmt == 4:
    print("O valor total a ser pago será de R${:.2f}".format(preco + preco * 0.2))
else:
    print("Opção inválida! Tente outra vez.")