#Atividade 5: Desenhando um Triângulo com Laços Aninhados
#Enunciado:
#Peça ao usuário um número inteiro que representará a altura de um triângulo. O programa deve então
#desenhar no console um triângulo retângulo usando asteriscos (*) com a altura informada.
# Requisitos Técnicos:
#Utilizar input(), print() e laços for aninhados (um dentro do outro).
# Função ou Lógica Nova Aprendida a ser utilizada:
# print('*', end='') #imprimi na mesma linha sem pular linha
# print() #pula para próxima linha
# Exemplo de Entrada e Saída: o Entrada: 5 o Saída:
# Solicita a altura do triângulo ao usuário
altura = int(input("Digite a altura do triângulo: "))

# Laço externo - controla as linhas
for i in range(1, altura + 1):
    # Laço interno - imprime os asteriscos de cada linha
    for j in range(i):
        print('*', end='')  # imprime sem pular linha
    print()  # pula para a próxima linha
