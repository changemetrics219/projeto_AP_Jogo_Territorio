from controller import *
def main():
    #aqui vai ficar o código principal
    criar_tabuleiro()
    n_jogadores = int(input("insira o número de jogadores: \n"))
    if (n_jogadores >= 2 and n_jogadores <= 4):
        #o código irá correr
        print("")
    else:
        print("\nNúmero inválido de jogadores\n")