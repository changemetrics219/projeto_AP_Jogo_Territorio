import random
import json

def registar_jogador(matriz, nome):
    if verificar_jogador(matriz, nome) == False:
        j = {'ID':len(matriz) + 1,"Nome": nome, "Pontuação":0}
        matriz.append(j)
    else:
        return True
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

def associar_peca_jogador(ij_n_jogador, jogadores):#-------------------
    cores = ["azul","verde","amarelo","vermelho"] 
    for i in range(0, ij_n_jogador):
        print(f"Escolha uma cor{cores}")
        
        p = input (f"{jogadores[i]['Nome']}, qual a peça?")
        if p == "azul":
s            jogadores.append({"Peça":"🟦", 'NUMERO_PEÇAS':21})
            p = "🟦"
        elif p == "verde":
            p = "🟩"
        elif p == "amarelo":
            p = "🟨"
        elif p == "vermelho":
            p = "🟥"
        
def dessassociar_peca_jogador(ij_n_jogador, jogadores):
    jogadores.pop("Peça")
    
    
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
        #associar o jogador á peça e vice-versa
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
    
def ler_ficheiro_json(nome_ficheiro):
    with open(nome_ficheiro) as f:
        data = json.load(f)
    return data 

def adicionar_bonus(matriz, tabuleiro): # isto não esta feito
    aleatorio = random.randint(0, len(tabuleiro) - 1)

def escrever_ficheiro_json(nome_ficheiro, d):
    json_string = json.dumps(d)
    json_file = open(nome_ficheiro, "w")
    json_file.write(json_string)
    json_file.close()
    #---------------------------------------------------------------------------------------------------------              
