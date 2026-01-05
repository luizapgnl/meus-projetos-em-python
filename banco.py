#Simule um sistema bancário que decide se um cliente é elegível para um empréstimo. Peça ao usuário
#sua idade, salário mensal e se ele possui nome negativado ("sim" ou "não"). As regras são: o cliente
#deve ter entre 25 e 65 anos, um salário de pelo menos R$ 2000,00, E não pode ter o nome negativado.
#Utilizar input(), print(), if/else e operadores lógicos and/or.
#• Função ou Lógica Nova Aprendida a ser utilizada:
#• .lower()
#• .upper()
#• not
print("===== Sistema de Análise de Empréstimo =====")

# Entrada de dados
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário mensal (R$): "))
negativado = input("Seu nome está negativado? (sim/não): ").lower()

# Verificação das condições
# Regras: idade entre 25 e 65, salário >= 2000 e não estar negativado
if (idade >= 25 and idade <= 65) and (salario >= 2000) and (negativado == "não" or negativado == "nao"):
    print("\nParabéns! Você é elegível para o empréstimo.")
else:
    print("\nInfelizmente, você NÃO atende aos requisitos para o empréstimo.")

# Exemplo de uso do .upper()
print("\nObrigado por usar o sistema!".upper())
