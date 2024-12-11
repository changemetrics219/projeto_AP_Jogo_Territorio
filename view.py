from controller import *

def main():
   tabuleir = criar_tabuleiro_dicionarios(3,4)
   imprimir_tabuleiro(tabuleir)

def imprimir_tabuleiro(tabuleiro):
    # Imprime o tabuleiro de forma legível
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)


def criar_tabuleiro_listas(linhas, colunas):
    tabuleiro = []
    for i in range(linhas): 
        linha = []
        for j in range(colunas):  
            linha.append("X")  
        tabuleiro.append(linha)  
    return tabuleiro

#############  Exemplo de função para criar tabuleiro com dicionários ############# 
def criar_tabuleiro_dicionarios(linhas, colunas):
    tabuleiro = []
    for i in range(linhas):  # Linhas
        for j in range(colunas):  # Colunas
            celula = {"Linha": i, "Coluna": j, "Peça": "X"}  
            tabuleiro.append(celula) 
    return tabuleiro