#Esse sistema: 
#1. Cadastra produtos;
#2. Salva os dados em arquivo .txt;
#3. Lê os dados salvos;
#4. Analisa o nível de estoque;
#5. Gera relatórios (matriz, tags);
#6. Exporta tudo para Excel;
#7. Funciona por menu interativo no terminal.

import time
import os
import pandas
from openpyxl import Workbook  
start_time = time.time()
for i in range(8000000):
    pass 
def salvar_produtos_txt(produtos):
    
    with open('produtos.txt', 'w', encoding='utf-8') as arq:
        for p in produtos:
            linha = f"{p['id']};{p['nome']};{p['preco']};{p['quantidade']}\n"
            arq.write(linha)


def carregar_produtos_txt():
    produtos = []
    if os.path.exists('produtos.txt'):
        with open('produtos.txt', 'r', encoding='utf-8') as arq:
            for linha in arq:
                dados = linha.strip().split(';')
                produtos.append({
                    'id': int(dados[0]),
                    'nome': dados[1],
                    'preco': float(dados[2]),
                    'quantidade': int(dados[3])
                })
    return produtos

def exportar_para_excel(produtos):
    
    if not produtos:
        print(" Nenhum produto para exportar!\n")
        return

    wb = Workbook()
    ws = wb.active
    ws.title = "Estoque"

    ws.append(["ID", "Nome", "Preço (R$)", "Quantidade", "Status"])

    for p in produtos:
        qtd = p["quantidade"]
        if qtd > 100:
            status = "ALTO"
        elif qtd > 20:
            status = "MÉDIO"
        else:
            status = "BAIXO"

        ws.append([p["id"], p["nome"], p["preco"], p["quantidade"], status])

    wb.save("estoque.xlsx")
    print("Arquivo 'estoque.xlsx' exportado com sucesso!\n")

def cadastrar_produto(produtos):
    print("\n                |=== CADASTRAR NOVO PRODUTO ===|")
    nome = input("           |Digite o nome do produto:     |").strip().title()
    preco = float(input("    |Digite o preço unitário (R$): |"))
    quantidade = int(input(" |Digite a quantidade inicial:  |"))

    novo_id = len(produtos) + 1
    produtos.append({
        "id": novo_id,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    })

    print(f"\n O produto foi \"{nome}\" (ID {novo_id}) cadastrado com sucesso!\n")


def listar_produtos(produtos):
    print("\n|=== LISTAGEM DE PRODUTOS ===|")
    if not produtos:
        print("Nenhum produto foi cadastrado!!!.\n")
        return
    for p in produtos:
        print(f"ID {p['id']} - {p['nome']} (R$ {p['preco']:.2f}) - {p['quantidade']} em estoque")
    print()


def verificar_desempenho(produtos):
    print("\n|--- NÍVEL DE DESEMPENHO DO ESTOQUE ---|")
    if not produtos:
        print("Nenhum produto foi cadastrado.\n")
        return
    for p in produtos:
        qtd = p["quantidade"]
        if qtd > 100:
            status = "+ALTO+"
        elif qtd > 20:
            status = "_MÉDIO_"
        else:
            status = "-BAIXO-"
        print(f"{p['nome']}: {qtd} unidades - Status: {status}")
    print()


def gerar_matriz_estoque(produtos):
    print("\n|--- ANÁLISE DO ESTOQUE POR CORREDOR (Matriz 3x3) ---|")
    matriz = [[0 for _ in range(3)] for _ in range(3)]

    for i, p in enumerate(produtos[:3]): 
        matriz[i][0] = p["quantidade"]

    for i, corredor in enumerate(matriz, start=1):
        print(f"Corredor {i}\t", end="")
        for j, prateleira in enumerate(corredor, start=1):
            print(f"Prateleira {j}: {prateleira} und.\t", end="")
        print()
    print()


def gerar_nuvem_tags(produtos):
    print("\n|--- NUVEM DE TAGS ÚNICAS NO ESTOQUE  ---|")
    if not produtos:
        print("Nenhum produto foi cadastrado!!!\n")
        return
    tags = {p["nome"].lower() for p in produtos}
    print(tags)
    print(f"Total de tags únicas: {len(tags)}\n")

def sistema_principal():
    produtos = carregar_produtos_txt()
    while True:
        print("|========================================================|")
        print("|                       LISTA DO MENU                    |")
        print("|========================================================|")
        print("|         1. Cadastrar Novo Produto                      |")
        print("|         2. Listar Produtos em Estoque                  |")
        print("|         3. Verificar Nível de Desempenho               |")
        print("|         4. Gerar Matriz de Estoque por Corredor        |")
        print("|         5. Gerar Nuvem de Tags Únicas                  |")
        print("|         6. Exportar Estoque para Excel                 |")
        print("|         0. Salvar e Sair                               |")
        print("|========================================================|")
        opcao = input("|   Escolha uma opção:                           |")
        print("|========================================================|")

        match opcao:
            case "1":
                cadastrar_produto(produtos)
            case "2":
                listar_produtos(produtos)
            case "3":
                verificar_desempenho(produtos)
            case "4":
                gerar_matriz_estoque(produtos)
            case "5":
                gerar_nuvem_tags(produtos)
            case "6":
                exportar_para_excel(produtos)
            case "0":
                salvar_produtos_txt(produtos)
                print("\n Os dados foram salvos com sucesso.")
                print(" Obrigado por usar o programa!!")
                break
            case _:
                print(" Opção inválida! Digite uma opção válida (0-5)\n")
end_time = time.time()
execution_time = end_time - start_time

if __name__ == "__main__":
    sistema_principal()


