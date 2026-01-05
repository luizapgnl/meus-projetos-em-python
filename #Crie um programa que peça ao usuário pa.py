#Crie um programa que peça ao usuário para digitar sua idade. O programa deve garantir que o valor
#digitado seja um número inteiro e que esteja dentro de um intervalo válido (ex: 1 a 120 anos). O
#programa não deve prosseguir (e deve continuar pedindo) até que uma entrada válida seja fornecida.

while True:
    idade = input("Por favor, digite sua idade (1-120 anos): ")
    if idade.isdigit():
        idade_int = int(idade)
        if 1 <= idade_int <= 120:
            print(f"Obrigado! Sua idade é {idade_int} anos.")
            break
        else:
            print("Idade inválida. Por favor, insira um número entre 1 e 120.")
    else:
        print("Entrada inválida. Por favor, insira um número inteiro.")
        