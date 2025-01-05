import random
import json

def registar_jogador(matriz, nome):
    if verificar_jogador(matriz, nome) == False:
        j = {'ID':len(matriz) + 1,"Nome": nome, "Pontuação":0}
        matriz.append(j)
        escrever_ficheiro_json("jogadores.json", matriz)
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

def associar_peca_jogador(ij_n_jogador, lista_jogadores):
    cores = ["azul", "verde", "amarelo", "vermelho"]
    while True:
        for jogador in lista_jogadores:
            print(f"Escolha uma cor disponível: {', '.join(cores)}")
            p = input(f"Qual a cor desejada, {jogador['Nome']}? ").lower()
            if p in cores:
                if p == "azul":
                    jogador["Peça"] = "🟦"
                elif p == "verde":
                    jogador["Peça"] = "🟩"
                elif p == "amarelo":
                    jogador["Peça"] = "🟨"
                elif p == "vermelho":
                    jogador["Peça"] = "🟥"
                jogador['NUMERO_PEÇAS'] = 21
                cores.remove(p)  # Remove a cor escolhida
                continue
            else:
                print("Cor inválida. Escolha novamente.")
        
        return lista_jogadores
#isto é apenas o tabuleiro            
import os
def criar_tabuleiro():
    cols = int(input("Insira o tamanho do tabuleiro: "))
    os.system('cls')
    lins = cols
    tabuleiro = []
    for i in range(lins):
        tabuleiro.append(list('🔳'*cols))
    imprimir_tabuleiro(tabuleiro)
    return tabuleiro
def imprimir_tabuleiro(tabuleiro): # enumera o tabuleiro
    # Cabeçalho com números das colunas
    print("     " + "  ".join(f"{i+1}" for i in range(len(tabuleiro[0]))))
    # Linhas com índice das linhas
    for i, line in enumerate(tabuleiro):
        print(f"{i + 1:2}" + "".join(line)) 
    atualizar_tabuleiro(tabuleiro)     
def atualizar_tabuleiro(tabuleiro):     
    while True:
        lin_alterar = int(input("Qual linha deseja alterar?: "))
        col_alterar = int(input("Qual coluna deseja alterar?: "))  
        lin_alterar -= 1   #apagar caso se queira começar com coordenadas 0,0 
        col_alterar -= 1
        #verifica se a linha e a coluna estao dentro do intervalo do tabuleiro
        if not (0 <= lin_alterar < len(tabuleiro)) or not (0 <= col_alterar < len(tabuleiro[0])):
            print("Fora dos limites! Tente novamente com outros valores")  
            continue     
        #verifica se a coordenada está livre ou não
        if tabuleiro[lin_alterar][col_alterar] != '🔳':
            print("Posição está ocupada! Tente novamente.")
            continue    
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
        if 1+1==2: # sem isto fica out of range. Problema do vs code???
           imprimir_tabuleiro(tabuleiro)  

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
