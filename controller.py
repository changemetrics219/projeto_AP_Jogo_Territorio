#def(function):
    #aqui vão ficar as funçoes
import random
import json

def registar_jogador(matriz, nome):
    if verificar_jogador(matriz, nome) == False:
        j = {"Nome": nome, "Pontuação":0}
        matriz.append(j)
def verificar_jogador(matriz, nome):
    for jogador in matriz:
         if nome == jogador["Nome"]:
             return True
    return False
       
def verificar_numero_jogadores(jogadores):
    if len(jogadores) >= 2:
        return True
    else:
        return False

def visualizar_pontuacao(matriz):
    for jogador in matriz:
        print(f"{jogador['Nome']}: {jogador['Pontuação']}")


def adicionar_bonus(matriz, tabuleiro): # isto não esta feito
    aleatorio = random.randint(0, len(tabuleiro) - 1)

import os
def criar_tabuleiro():
    cols = int(input("Insira o tamanho do tabuleiro: "))
    os.system('cls')
    lins = cols
    tabuleiro = []
    for i in range(lins):
        tabuleiro.append(list('🔳'*cols))
    for line in tabuleiro:
       print(''.join(line))
    while True:
        lin_alterar = int(input("Qual linha deseja alterar?: "))
        col_alterar = int(input("Qual coluna deseja alterar?: "))
        lin_alterar -= 1   #apagar caso se queira começar com coordenadas 0,0 
        col_alterar -= 1
        
        var = int(input("qual peça?"))
        match var:
            case 1:
                vlr_novo = '🟦'
            case 2:
                vlr_novo = '🟩'
            case 3:
                vlr_novo = '🟨'
            case 4:
                vlr_novo = '🟥'
        os.system('cls')
        tabuleiro[lin_alterar][col_alterar] = vlr_novo
        for line in tabuleiro:
            print(''.join(line)) 
                 
def atualizar_tabuleiro(linha, coluna, jogada, tabuleiro): # proxima coisa a mudar----------------------------
    if tabuleiro[linha][coluna] == '_': tabuleiro[linha][coluna] = jogada
    else: print("Posição já ocupada!")
"""
def num_jogadores(jogadores):# transformar isto varias funçoes
    # for j in jogadores:
         #if len(jogadores) == 2:

    for j in len(jogadores):
        if j == 2:
            nome_1 = input("Introduza o nome do jogador 1: ").upper
            nome_2 = input("Introduza o nome do jogador 2: ").upper
            if verificar_jogador(jogadores, nome_1) and verificar_jogador(jogadores, nome_2):
                print(f"\nJogadores: {jogadores} \n {nome_1} vs {nome_2}")
            else:
                print(f"\n Jogadores inválidos!\n Os jogadores {nome_1} ou {nome_2} não estão registados.")
                break
                    
        elif j == 3:
            nome_1 = input("Introduza o nome do jogador 1: ").upper
            nome_2 = input("Introduza o nome do jogador 2: ").upper
            nome_3 = input("Introduza o nome do jogador 3: ").upper
            if verificar_jogador(jogadores, nome_1) and verificar_jogador(jogadores, nome_2) and verificar_jogador(jogadores, nome_3):
                print(f"\nJogadores: {jogadores} \n {nome_1} vs {nome_2} vs {nome_3} ")
            else:
                print(f"\n Jogadores inválidos!\n Os jogadores {nome_1} ou {nome_2} ou {nome_3} não estão registados.")
                break

        elif j == 4:
            nome_1 = input("Introduza o nome do jogador 1: ").upper
            nome_2 = input("Introduza o nome do jogador 2: ").upper
            nome_3 = input("Introduza o nome do jogador 3: ").upper
            nome_4 = input("Introduza o nome do jogador 4: ").upper
            if verificar_jogador(jogadores, nome_1) and verificar_jogador(jogadores, nome_2) and verificar_jogador(jogadores, nome_3) and verificar_jogador(jogadores, nome_4):
                print(f"\nJogadores: {jogadores} \n {nome_1} vs {nome_2} vs {nome_3} vs {nome_4} ")
            else:
                print(f"\n Jogadores inválidos!\n Os jogadores {nome_1} ou {nome_2} ou {nome_3} ou {nome_4} não estão registados.")
                break
        else:
            print("Introduziu um número de jogadores inválido.")
            break
"""
def ler_ficheiro_json(nome_ficheiro):
    with open(nome_ficheiro) as f:
        data = json.load(f)
    return data 

def escrever_ficheiro_json(nome_ficheiro, d):
    json_string = json.dumps(d)
    json_file = open(nome_ficheiro, "w")
    json_file.write(json_string)
    json_file.close()
    #---------------------------------------------------------------------------------------------------------        