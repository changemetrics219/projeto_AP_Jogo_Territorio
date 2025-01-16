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
                jogador['linhas'] = []
                jogador['colunas'] = []
                
                cores.remove(p)  # Remove a cor escolhida
                break
            else:
                print("Cor inválida. Escolha novamente.")     
    return lista_jogadores
    

def update(tabuleiro, lin_alterar, col_alterar, lista_jogadores, j, contador):
    tabuleiro[lin_alterar][col_alterar] = lista_jogadores[j]["Peça"]
    lista_jogadores[j]["NUMERO_PEÇAS"] -= 1
    print(lista_jogadores[j]["NUMERO_PEÇAS"])
    time.sleep(2)
    return contador, lista_jogadores, tabuleiro

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
                jogador['linhas'] = []
                jogador['colunas'] = []
                
                cores.remove(p)  # Remove a cor escolhida
                break
            else:
                print("Cor inválida. Escolha novamente.")     
    return lista_jogadores
import time
def obter_vizinhos_hvd(tabuleiro, lista_jogadores, j, lin_alterar, col_alterar):
    linhas_tabuleiro = len(tabuleiro)
    colunas_tabuleiro = len(tabuleiro[0]) if linhas_tabuleiro > 0 else 0

    # Verifica se as listas existem e não estão vazias
    if 'linhas' in lista_jogadores[j] and lista_jogadores[j]['linhas'] and 'colunas' in lista_jogadores[j] and lista_jogadores[j]['colunas']:
        linha = lista_jogadores[j]['linhas'][-1]
        coluna = lista_jogadores[j]['colunas'][-1]
    else:
        return  # Sai da função se não houver jogadas anteriores

    for d_linha in [-1, 0, 1]:
        for d_colunas in [-1, 0, 1]:
            if d_linha == 0 and d_colunas == 0:
                continue
            nova_linha, nova_coluna = linha + d_linha, coluna + d_colunas
            if 0 <= nova_linha < linhas_tabuleiro and 0 <= nova_coluna < colunas_tabuleiro:
                lista_jogadores[j]['linhas'].append(nova_linha)
                lista_jogadores[j]['colunas'].append(nova_coluna)
def jogadas(tabuleiro, lista_jogadores, j, ij_n_jogador, contador):
    """Executa uma jogada."""
    jogador = lista_jogadores[j]  # Simplifica o acesso ao jogador atual
    print(f"\nÉ a vez de {jogador['Nome']} {jogador['Peça']}")

    if jogador["NUMERO_PEÇAS"] < 1:
        print(f"{jogador['Nome']} não tem mais peças. Fim de jogo para este jogador.")
        jogador['Inativo'] = True
        jogadores_ativos = [jogador for jogador in lista_jogadores if 'Inativo' not in jogador]
        if not jogadores_ativos:
            return -1, contador
        novo_j = (j + 1) % len(lista_jogadores)
        while 'Inativo' in lista_jogadores[novo_j]:
            novo_j = (novo_j + 1) % len(lista_jogadores)
        return novo_j, contador

    if contador == 0:
        print("Jogada 1 pré-definida")
        lin_alterar = 0
        col_alterar = 0
    else:
        while True:  # Loop para tratamento de erros de input
            try:
                lin_alterar = int(input("Qual linha deseja alterar? ")) - 1
                col_alterar = int(input("Qual coluna deseja alterar? ")) - 1
                if not (0 <= lin_alterar < len(tabuleiro) and 0 <= col_alterar < len(tabuleiro[0])):
                    print("Fora dos limites do tabuleiro. Tente novamente.")
                    continue  # Volta para o início do loop while
                if tabuleiro[lin_alterar][col_alterar] != "🔳":
                    print("Posição ocupada! Escolha outra.")
                    continue  # Volta para o início do loop while
                break  # Sai do loop while se o input for válido
            except ValueError:
                print("Entrada inválida. Insira apenas números.")
            except IndexError:
                print("posição inválida")

    jogador['linhas'].append(lin_alterar)
    jogador['colunas'].append(col_alterar)
    tabuleiro[lin_alterar][col_alterar] = jogador["Peça"]
    jogador["NUMERO_PEÇAS"] -= 1

    if contador > len(lista_jogadores): #so verifica a adjacencia apartir da segunda jogada
        adjacente = False
        for i in range(len(jogador['linhas']) - 1):
            if abs(jogador['linhas'][i] - lin_alterar) <= 1 and abs(jogador['colunas'][i] - col_alterar) <= 1:
                adjacente = True
                break

        if not adjacente:
            print("Jogada inválida, não está adjacente a nenhuma peça sua!")
            jogador['linhas'].pop()
            jogador['colunas'].pop()
            tabuleiro[lin_alterar][col_alterar] = "🔳" #volta a meter o sitio onde estava a jogar a branco
            jogador["NUMERO_PEÇAS"] += 1 #volta a adicionar a peça ao jogador
            return j, contador

        print("Jogada válida")
        obter_vizinhos_hvd(tabuleiro, lista_jogadores, j, len(tabuleiro), len(tabuleiro[0])) # Obtém os vizinhos da última jogada

    print(jogador)
    time.sleep(1)
    imprimir_tabuleiro(tabuleiro)
    contador += 1
    return (j + 1) % len(lista_jogadores), contador
"""
def verificar_adjacencia(tabuleiro, lin_alterar, col_alterar, peça_atual, lista_jogadores, j):

    Função que verifica se a peça colocada está adjacente a outra peça do mesmo jogador.

    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Cima, Baixo, Esquerda, Direita
    for lin_offset, col_offset in direcoes:
        lin_vizinha = lin_alterar + lin_offset
        col_vizinha = col_alterar + col_offset

        if 0 <= lin_vizinha < len(tabuleiro) and 0 <= col_vizinha < len(tabuleiro[0]):
            if tabuleiro[lin_vizinha][col_vizinha] == peça_atual:
                return True  # Se a peça vizinha for do mesmo jogador, retorna True (adjacente)
    return False  # Se não encontrar nenhuma peça adjacente

def jogadas(tabuleiro, lista_jogadores, j, ij_n_jogador, contador): 
    print(f"\nÉ a vez de {lista_jogadores[j]['Nome']} {lista_jogadores[j]['Peça']}")
    print(lista_jogadores)

    while True: 
        try:
            if lista_jogadores[j]["NUMERO_PEÇAS"] < 1:
                print("Fim de jogo")
                # Programar a função de fim de jogo
                break
            if contador == 0:
                print("Primeira jogada, sem verificação de adjacência.")
                lin_alterar = int(input("Qual linha deseja alterar? ")) - 1
                col_alterar = int(input("Qual coluna deseja alterar? ")) - 1
            else:
                # Jogadas seguintes com verificação de adjacência
                lin_alterar = int(input("Qual linha deseja alterar? ")) - 1
                col_alterar = int(input("Qual coluna deseja alterar? ")) - 1

                if not (0 <= lin_alterar < len(tabuleiro)) or not (0 <= col_alterar < len(tabuleiro[0])):
                    print("Fora dos limites do tabuleiro. Tente novamente.")
                    continue
                if tabuleiro[lin_alterar][col_alterar] != '🔳':
                    print("Posição ocupada! Escolha outra.")
                    continue
                
                peça_atual = lista_jogadores[j]["Peça"]
                if not verificar_adjacencia(tabuleiro, lin_alterar, col_alterar, peça_atual, lista_jogadores, j):
                    print("A peça não está adjacente a outra peça do mesmo jogador. Tente novamente.")
                    continue

            # Marca a jogada
            tabuleiro[lin_alterar][col_alterar] = lista_jogadores[j]["Peça"]
            lista_jogadores[j]["NUMERO_PEÇAS"] -= 1
            print(f"Peças restantes para {lista_jogadores[j]['Nome']}: {lista_jogadores[j]['NUMERO_PEÇAS']}")
            time.sleep(2)  # Pausa entre as jogadas
            contador += 1
            break 

        except ValueError:
            print("Entrada inválida. Insira apenas números.")

    # Imprimir o tabuleiro após cada jogada
    imprimir_tabuleiro(tabuleiro)

    # Passa para o próximo jogador
    return (j + 1) % len(lista_jogadores), contador  # Passa para o próximo jogador
"""
def imprimir_tabuleiro(tabuleiro):
    """
    Função para imprimir o tabuleiro de forma legível.
    """
    for linha in tabuleiro:
        print(" ".join(linha))

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


def atualizar_tabuleiro(tabuleiro, lin_alterar, col_alterar, lista_jogadores, j):     
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
            tabuleiro[lin_alterar][col_alterar] = lista_jogadores[j]["Peça"]
            imprimir_tabuleiro(tabuleiro)
            break
       

def inicio_jogo(tabuleiro, lista_jogadores, j, ij_n_jogador, contador):  
    while True:
        j, contador = jogadas(tabuleiro, lista_jogadores, j, ij_n_jogador, contador)
        
        fim = input("\nDeseja continuar? (sim/nao): ").strip().lower()
        if fim != 'sim':
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
