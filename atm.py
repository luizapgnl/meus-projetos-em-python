#• Enunciado:
#Crie um programa que simule as operações de um caixa eletrônico. O programa deve iniciar com um
#saldo (ex: R$ 1000,00) e apresentar um menu com as opções: 1. Ver Saldo, 2. Sacar, 3. Depositar, 4.
#Sair. O programa deve continuar rodando até que o usuário escolha a opção "Sair".
#Requisitos Técnicos: Utilizar input(), print(), um laço while, e if/elif/else para o menu.
# Função ou Lógica Nova Aprendida a ser utilizada:
# # A formatação :.2f garante que o saldo seja exibido com duas casas decimais. 3+= ou -=
# Exemplo de Entrada e Saída:
#o Menu: ... 1. Ver Saldo ... -> Entrada: 2 -> Saída: Qual valor deseja sacar? R$50 -> Saque realizado. Saldo atual: R$ 950.00

saldo = 1000.00
while True:
    print("Menu:")
    print("1. Ver Saldo")
    print("2. Sacar")
    print("3. Depositar")
    print("4. Sair")
    
    escolha = input("Escolha uma opção (1-4): ")
    
    if escolha == '1':
        print(f"Seu saldo atual é: R${saldo:.2f}\n")
    elif escolha == '2':
        valor_saque = float(input("Qual valor deseja sacar? R$"))
        if valor_saque > saldo:
            print("Saldo insuficiente para este saque.\n")
        else:
            saldo -= valor_saque
            print(f"Saque realizado. Saldo atual: R${saldo:.2f}\n")
    elif escolha == '3':
        valor_deposito = float(input("Qual valor deseja depositar? R$"))
        saldo += valor_deposito
        print(f"Depósito realizado. Saldo atual: R${saldo:.2f}\n")
    elif escolha == '4':
        print("Saindo do programa. Obrigado por usar o caixa eletrônico!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.\n") 