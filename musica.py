import time

musica = {
    "titulo": "Te amo de graça",
    "artista": "Baco Exu do Blues",
    "estrutura": [
        "Bebendo vinho, quebrando as taça",
        "Fudendo por toda casa",
        "Se eu divido o maço, eu te amo desgraça",
        "Te amo desgraça",
        "Bebendo vinho e quebrando as taça",
        "Fudendo por toda casa",
        "Se divido o maço, eu te amo desgraça",
        "Te amo, desgraça",  
        "Eu te amo, desgraça",
        "Eu te amo de graça",
        "Te amo, desgraça"
    ],
    "duracao_segundos": 60
}

print(f"Tocando: {musica['titulo']} - {musica['artista']}\n")

inicio = time.time()
indice = 0

while time.time() - inicio < musica["duracao_segundos"]:
    print(f"♪ {musica['estrutura'][indice % len(musica['estrutura'])]}")
    time.sleep(5)  # troca a cada 5 segundos
    indice += 1

print("\n⏹ Música finalizada (1 minuto).")