"""
desafio #036

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que esta não pode exceder 30% do salário ou então o emprestimo será
negado.
"""

sal = float(input("Digite sua renda? R$ "))
valor_imovel = float(input("Digite o valor do imóvel: R$ "))
qtd_anos = int(input("Em quantos anos deseja pagar? "))
qtd_parcelas = qtd_anos * 12
sal_limite = sal * 0.3
valor_parcela = valor_imovel / qtd_parcelas

if valor_parcela >= sal_limite:
    print("O valor da parcela de R${:.2f}, excede o seu limite possível para compra.\n"
          "Por favor, selecione um prazo maior para pagamento.\n"
          "\033[31mNão é possível prosseguir com o financiamento.\033[m".format(valor_parcela))
else:
    print("Para a compra de um imóvel de R$ {:.2f} em {} anos, o valor da parcela será de {:.2f}.".format(valor_imovel, qtd_anos, valor_parcela))
