import random
import json
import time
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
    
    
import math
def adicionar_bonus(tabuleiro): # isto não esta feito
    
    if not tabuleiro or not tabuleiro[0]:
        raise ValueError("O tabuleiro está vazio ou inválido!")

    while True:
        aleatorio_col = random.randint(0, len(tabuleiro) - 1)
        aleatorio_lin = random.randint(0, len(tabuleiro[0]) - 1)
        
        if tabuleiro[aleatorio_col][aleatorio_lin] == '🔳':
            bonus = [aleatorio_col, aleatorio_lin]
            print(f"Bônus adicionado na posição: {bonus}")
            return bonus






def visualizar_pontuacao(matriz):
    for jogador in matriz:
        print(f"{jogador['Nome']}: {jogador['Pontuação']}")

def associar_peca_jogador(lista_jogadores):
    cores = ["azul", "verde", "amarelo", "vermelho"]
    for jogador in lista_jogadores:
        while True:

            print(f"Escolha uma cor disponível: {', '.join(cores)}")
            p = input(f"Qual a cor desejada, {jogador['Nome']}? ").lower()
            if p in cores:
                if p == "azul":
                    jogador["Index"] = "1"
                    jogador["Peça"] = "🟦"
                    
                elif p == "amarelo":
                    jogador["Peça"] = "🟨"
                    jogador["Index"] = "2"
                elif p == "vermelho":
                    jogador["Index"] = "3"
                    jogador["Peça"] = "🟥"
                elif p == "verde": 
                    jogador["Index"] = "4" 
                    jogador["Peça"] = "🟩"
                jogador['NUMERO_PEÇAS'] = 21
                cores.remove(p)  # Remove a cor escolhida
                break
            else:
                print("Cor inválida. Escolha novamente.")     
    return lista_jogadores
    
def jogadas(tabuleiro, lista_jogadores, j, ij_n_jogador, contador):
    print(f"\nÉ a vez de {lista_jogadores[j]['Nome']} {lista_jogadores[j]['Peça']}")
    #imprimir_tabuleiro(tabuleiro)
    print (lista_jogadores)

    while True: 
        try:
            if lista_jogadores[j]["NUMERO_PEÇAS"] < 1:
                print("fim de jogo")
                # programar a função de fim de jogo
                break
            if contador == 0:
                print("Jogada 1 pré-difinida")
                lin_alterar = 1 - 1
                col_alterar = 1 - 1
                
            else:
                lin_alterar = int(input("Qual linha deseja alterar? ")) - 1
                col_alterar = int(input("Qual coluna deseja alterar? ")) - 1

                if not (0 <= lin_alterar < len(tabuleiro)) or not (0 <= col_alterar < len(tabuleiro[0])):
                    print("Fora dos limites do tabuleiro. Tente novamente.")
                    continue
                if tabuleiro[lin_alterar][col_alterar] != '🔳':
                    print("Posição ocupada! Escolha outra.")
                    continue
                #if com o bonus
            # Marca a jogada
            # retirar uma peça a cada jogada
            tabuleiro[lin_alterar][col_alterar] = lista_jogadores[j]["Peça"]
            lista_jogadores[j]["NUMERO_PEÇAS"] -= 1
            print(lista_jogadores[j]["NUMERO_PEÇAS"])
            time.sleep(2)
            contador += 1
            break 
        except ValueError:
            print("Entrada inválida. Insira apenas números.")

    imprimir_tabuleiro(tabuleiro)
    return (j + 1) % len(lista_jogadores), contador  # Passa para o próximo jogador
       
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
    # números das colunas
    print("     " + "  ".join(f"{i+1}" for i in range(len(tabuleiro[0]))))
    # numero das linhas
    for i, line in enumerate(tabuleiro):
        print(f"{i + 1:2}" + "".join(line))  
     
#isto controla as jogadas no tabuleiro

    
def atualizar_tabuleiro(tabuleiro, vlr_novo, lin_alterar, col_alterar):     
    while True:
        if not (0 <= lin_alterar < len(tabuleiro)) or not (0 <= col_alterar < len(tabuleiro[0])):
            print("Fora dos limites! Tente novamente.")  
            continue
        elif tabuleiro[lin_alterar][col_alterar] != '🔳':
            print("Posição ocupada! Tente novamente.")
            continue
        else:
            lin_alterar -= 1   #apagar caso se queira começar com coordenadas 0,0 
            col_alterar -= 1
            tabuleiro[lin_alterar][col_alterar] = vlr_novo
            imprimir_tabuleiro(tabuleiro)
            break
       

def inicio_jogo(tabuleiro, lista_jogadores, j, ij_n_jogador, contador):  
    while True:
        j, contador = jogadas(tabuleiro, lista_jogadores, j, ij_n_jogador, contador)
        fim = input("\nDeseja continuar? (sim/nao): ").strip().lower()
        if fim == 'nao':
            break
       

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
