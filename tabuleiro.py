import os

tabuleiro = []

def criar_tabuleiro(linha, coluna):
    global tabuleiro
    # Cria um tabuleiro de tamanho 'linha' x 'coluna' preenchido com _
    tabuleiro = [["_" for _ in range(linha)] for _ in range(coluna)]

def imprimir_tabuleiro():
    global tabuleiro
    for linha in tabuleiro: print(" ".join(map(str, linha)))

def atualizar_tabuleiro(linha, coluna, jogada):
    #verifica se o sistema é windows
    if os.name == "nt": os.system("cls")
    #verifica se a posicao jogada está livre e marca a jogada  
    if tabuleiro[linha][coluna] == '_': tabuleiro[linha][coluna] = jogada
    else: print("Posição já ocupada!")
