
# Mostrar se um aluno foi aprovado ou reprovado (média 7)
n1 = float(input("Digite a sua primeira nota: ")) #n1 = nota 1
n2 = float(input("Digite a sua segunda nota: ")) #n2 = nota 2
n3 = float(input("Digite a sua terceira nota: ")) #n3 = nota 3

#Calcular as três notas dividir por 3
media = (n1 + n2 + n3) / 3
#Agora entra se (if) 

if media > 7:
    print(f"Parabéns! Você foi aprovado com média: {media}")
elif media == 7:
    print(f"Você ficou exatamente na média!: {media}")
else:
    print(f"Infelizmente você não atingiu a média. Sua média foi : {media}")