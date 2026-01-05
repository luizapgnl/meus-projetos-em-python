import random

print("===== Jogo: Pedra, Papel e Tesoura =====")

opcoes = ["pedra", "papel", "tesoura"]

while True:
    jogador = input("Digite sua escolha (pedra, papel, tesoura ou sair): ").lower()

    if jogador == "sair":
        print("Jogo encerrado. Obrigado por jogar!")
        break

    if jogador not in opcoes:
        print("Opção inválida! Tente novamente.\n")
        continue

    computador = random.choice(opcoes)
    print(f"Computador escolheu: {computador}")

    # Determinar o vencedor
    if jogador == computador:
        print("Empate!\n")
    elif jogador == "pedra":
        if computador == "tesoura":
            print("Você venceu! Pedra quebra tesoura.\n")
        else:
            print("Você perdeu! Papel cobre pedra.\n")
    elif jogador == "papel":
        if computador == "pedra":
            print("Você venceu! Papel cobre pedra.\n")
        else:
            print("Você perdeu! Tesoura corta papel.\n")
    elif jogador == "tesoura":
        if computador == "papel":
            print("Você venceu! Tesoura corta papel.\n")
        else:
            print("Você perdeu! Pedra quebra tesoura.\n")
                                                                                                                                                            