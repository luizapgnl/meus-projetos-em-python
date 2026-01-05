#Crie uma calculadora que funciona no console. O programa deve pedir ao usuário o primeiro número, o
#segundo número e a operação desejada (+, -, *, /). Utilize a estrutura match case para selecionar a
#operação correta e exibir o resultado.
import math  # Importa a biblioteca matemática
           
print("===== Calculadora Simples! =====")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
    print(f"O resultado de {num1} + {num2} é: {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"O resultado de {num1} - {num2} é: {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"O resultado de {num1} * {num2} é: {resultado}")
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado de {num1} / {num2} é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida! Por favor, escolha entre +, -, * ou /.")

