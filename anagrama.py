# Enunciado:
#Um anagrama é uma palavra ou frase formada rearranjando as letras de outra palavra ou frase. Crie um
#programa que peça duas palavras ao usuário e determine se elas são anagramas uma da outra. O
#programa não deve diferenciar maiúsculas de minúsculas e deve ignorar espaços.
#Requisitos Técnicos: Utilizar input(), print(), if/else e manipulação de strings/listas.
print("===== Verificador de Anagramas =====")

# Entrada de dados
plvr1 = input("Digite a primeira palavra: ")
plvr2 = input("Digite a segunda palavra: ")

# Remover espaços e converter para minúsculas
p1 = plvr1.replace(" ", "").lower()
p2 = plvr2.replace(" ", "").lower()

# Verificar se são anagramas usando sorted()
if sorted(p1) == sorted(p2):
    print(f'"{plvr1}" e "{plvr2}" são anagramas.')
else:
    print(f'"{plvr1}" e "{plvr2}" não são anagramas.')
