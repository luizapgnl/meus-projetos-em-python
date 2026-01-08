movieName = "Top Gun"

movieDescription = """
Um filme de 1986 dirigido por Tony Scott, estrelado por Tom Cruise como um jovem piloto de caça da Marinha dos Estados Unidos, 
que frequenta a escola de elite de pilotos conhecida como "Top Gun". O filme é famoso por suas cenas de ação aérea emocionantes,
 trilha sonora icônica e pela exploração de temas como camaradagem, competição e romance.
"""
print(movieName.upper())  # transforma toda a string em maiúscula
print(movieName.lower())  # transforma toda a string em minúscula
print(movieName.title())  # transforma a primeira letra de cada palavra em maiúscula
print(movieName.capitalize())  # transforma a primeira letra da string em maiúscula
print(len(movieName))  # retorna o tamanho da string
print(movieName.count("o"))  # conta quantas vezes a letra "o" aparece na string
print(movieName.find("Gun"))  # retorna o índice onde a palavra "Gun" começa
print(movieName.replace("Top", "New"))  # substitui "Top" por "New"
print("PILOT" in movieDescription)  # verifica se a palavra "PILOT" está na descrição do filme
print(movieDescription.strip())  # remove espaços em branco no início e no final da string
print(movieDescription.split())  # divide a string em uma lista de palavras
print("-".join(movieName))  # junta os caracteres da string com "-" entre eles
print(movieName.startswith("Top"))  # verifica se a string começa com "Top"
print(movieName.endswith("Gun"))  # verifica se a string termina com "Gun"
print(movieName.isalpha())  # verifica se todos os caracteres são letras
print(movieName.isdigit())  # verifica se todos os caracteres são dígitos
print(movieName.center(20, "*"))  # centraliza a string em um campo de 20 caracteres, preenchendo com "*"
print(movieName.find("u")) # retorna o índice da primeira ocorrência de "u"  
