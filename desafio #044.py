"""
desafio #044

Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
de pagamento:

- À vista dinheiro / cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até duas vezes no cartão: Preço normal
- 3x ou mais no cartão: 20% de juros
"""

print('{:=^40}'.format(' LOJAS 0T3B '))

preco = float(input("Digite o preço do produto: R$ "))
print("""Digite a forma de pagamento:
                          
[1] => À vsta dinheiro / cheque
[2] => Á vista no cartão
[3] => Em até 2x no cartão
[4] => 3x ou mais no cartão

""")

opcao = int(input('Digite uma opção e pressione Enter: '))

"""
print("")
if opcao == 1:
    print("O valor a ser pago será de R${:.2f}".format(preco - preco * 0.1))
elif opcao == 2:
    print("O valor a ser pago será de R${:.2f}".format(preco - preco * 0.05))
elif opcao == 3:
    print("O valor total a ser pago será de R${:.2f}".format(preco))
elif opcao == 4:
    print("O valor total a ser pago será de R${:.2f}".format(preco + preco * 0.2))
else:
    print("Opção inválida! Tente outra vez.")
"""
valida_ok = 0

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} sem juros.'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    qtd_parcela = int(input('Quantas parcelas? '))
    parcela = total / qtd_parcela
    print('Sua compra será parcelada em {}x de R$ {:.2f} com juros.'.format(qtd_parcela, parcela))
else:
    total = 0
    print('OPÇÃO INVALIDA de pagamento. Tente novamente!')
    valida_ok = 1

if valida_ok == 0:
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preco, total))