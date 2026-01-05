# leitura do preço de um produto e um percentual de desconto.
desconto = float (input("Digite o valor do produto: "))
porcentagem = float (input("Digite quantos porcento de desconto você quer: "))

final = desconto - (desconto*(porcentagem/100))
#Valor com desconto
print(f"O valor com desconto é: {final}")