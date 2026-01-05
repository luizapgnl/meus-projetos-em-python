#Ler o nome e exiba a primeira letra do seu nome 
nome = input("Digite seu nome: ")

# Primeira letra do nome
primeira_letra = nome[0]

# Quantidade de caracteres do nome
tamanho = len(nome)

# Resultado
print(f"A primeira letra do seu nome é '{primeira_letra}' e ele possui {tamanho} caracteres.")