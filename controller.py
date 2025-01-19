from random import randint
import json
import time
import os

def registar_jogador(matriz, nome):
    if verificar_jogador(matriz, nome) == False:
        j = {"Nome": nome, "Pontuação":0}
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
    
        linha = len(tabuleiro)
        coluna = len(tabuleiro[0])

        raiz = math.sqrt(coluna)

        if raiz < 2.6:
            num_bonus = math.floor(raiz)
        else:
            num_bonus = math.ceil(raiz)

        coordenadasbonus = []# guardar as coordenadas do bonus 

        for i in range(num_bonus): # adicionar x bonus conforme o tamanho do tabuleiro
        # Coordenadas aleatorias para o bonus
            linha_aleatoria = randint(0, linha-1)
            coluna_aleatoria = randint(0, coluna-1)

            coordenadasbonus.append([linha_aleatoria,coluna_aleatoria])

        return coordenadasbonus
def associar_peca_jogador(jogador,p):
    cores = ["azul", "verde", "amarelo", "vermelho"]
    if p in cores:
        for i in range(len(jogador)):
            if p == "azul":
                jogador[i]["Index"] = "1"
                jogador[i]["Peça"] = "🟦"
            elif p == "amarelo":
                jogador[i]["Index"] = "2"
                jogador[i]["Peça"] = "🟨"
            elif p == "vermelho":
                jogador[i]["Index"] = "3"
                jogador[i]["Peça"] = "🟥"
            elif p == "verde": 
                jogador[i]["Index"] = "4" 
                jogador[i]["Peça"] = "🟩"
    cores.remove(p)  # Remove a cor escolhida        
    for i in range (len(jogador)):
        jogador[i]['NUMERO_PEÇAS'] = 21
        jogador[i]['Inativo'] = False
        jogador[i]['linhas'] = []
        jogador[i]['colunas'] = []
        jogador[i]['Pontuação'] = [0]       
    
    return jogador
import time
def obter_vizinhos(tabuleiro, lista_jogadores, j, lin_alterar, col_alterar, vizinhos):
    vizinhos.clear() 
    linhas_tabuleiro = len(tabuleiro)
    colunas_tabuleiro = len(tabuleiro[0]) if linhas_tabuleiro > 0 else 0

    # Verifica se as listas existem e não estão vazias
    if 'linhas' in lista_jogadores[j] and lista_jogadores[j]['linhas'] and 'colunas' in lista_jogadores[j] and lista_jogadores[j]['colunas']:
        linha = lista_jogadores[j]['linhas'][-1]
        coluna = lista_jogadores[j]['colunas'][-1]
    
    for d_linha in [-1, 0, 1]:
        for d_colunas in [-1, 0, 1]:
            if d_linha == 0 and d_colunas == 0:
                continue
            nova_linha, nova_coluna = linha + d_linha, coluna + d_colunas
            if 0 <= nova_linha < linhas_tabuleiro and 0 <= nova_coluna < colunas_tabuleiro:
                vizinhos.append((nova_linha, nova_coluna))
                lista_jogadores[j]['linhas'].append(nova_linha)
                lista_jogadores[j]['colunas'].append(nova_coluna)
    return vizinhos  

def jogadas(tabuleiro, lista_jogadores, j, ij_n_jogador, contador, coordenadasbonus, vizinhos):
    """Executa uma jogada."""
    jogador = lista_jogadores[j]  # Simplifica o acesso ao jogador atual
   
    if jogador["NUMERO_PEÇAS"] == 0:
        jogador['Inativo'] = True
        jogadores_ativos = [jogador for jogador in lista_jogadores if 'Inativo' not in jogador]
        if not jogadores_ativos:
            return -1, contador
        novo_j = (j + 1) % len(lista_jogadores)
        while 'Inativo' in lista_jogadores[novo_j]:
            novo_j = (novo_j + 1) % len(lista_jogadores)
        return novo_j, contador

    if contador == 0:
        lin_alterar = 0
        col_alterar = 0
        
    else:
        while True:  # Loop para tratamento de erros de input
            try:
                lin_alterar = int(input("Qual linha deseja alterar? ")) - 1 #ir para a view
                col_alterar = int(input("Qual coluna deseja alterar? ")) - 1 #ir para a view
                if not (0 <= lin_alterar < len(tabuleiro) and 0 <= col_alterar < len(tabuleiro[0])):
                    print("Fora dos limites do tabuleiro. Tente novamente.") #ir para a view
                    continue  # Volta para o início do loop while
                if tabuleiro[lin_alterar][col_alterar] != "🔳" and tabuleiro[lin_alterar][col_alterar] != "⭐":
                    print("Posição ocupada! Escolha outra.") #ir para a view
                    continue  # Volta para o início do loop while
                break  # Sai do loop while se o input for válido
            except ValueError:
                print("Entrada inválida. Insira apenas números.")#ir para a view
            except IndexError:
                print("posição inválida") #ir para a view

    jogador['linhas'].append(lin_alterar)
    jogador['colunas'].append(col_alterar)
    tabuleiro[lin_alterar][col_alterar] = jogador["Peça"]
    jogador["NUMERO_PEÇAS"] -= 1
          

    if contador > len(lista_jogadores) - 1: #so verifica a adjacencia apartir da segunda jogada
        adjacente = False
        for i in range(len(jogador['linhas']) - 1):
            if abs(jogador['linhas'][i] - lin_alterar) <= 1 and abs(jogador['colunas'][i] - col_alterar) <= 1:
                adjacente = True
                break

        if not adjacente:
            print("Jogada inválida, não está adjacente a nenhuma peça sua!")#ir para a view
            jogador['linhas'].pop()
            jogador['colunas'].pop()
            tabuleiro[lin_alterar][col_alterar] = "🔳" #volta a meter o sitio onde estava a jogar a branco
            jogador["NUMERO_PEÇAS"] += 1 #volta a adicionar a peça ao jogador
            return j, contador

        print("Jogada válida") #ir para a view
        vizinhos = obter_vizinhos(tabuleiro, lista_jogadores, j, lin_alterar, col_alterar, vizinhos) # Obtém os vizinhos da última jogada

    for coordenadas in coordenadasbonus:
        if coordenadas[0] == lin_alterar and coordenadas[1] == col_alterar:
            jogador['Pontuação'] += 9
            
    print(jogador) #ir para a view
    time.sleep(1)
    imprimir_tabuleiro(tabuleiro)
    contador += 1
    return (j + 1) % len(lista_jogadores), contador, vizinhos

def criar_tabuleiro(cols):
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
            print("Fora dos limites! Tente novamente.")  #ir para a view    
            continue
        elif tabuleiro[lin_alterar][col_alterar] != '🔳':
            print("Posição ocupada! Tente novamente.") #ir para a view
            continue
        else:
            lin_alterar -= 1   #apagar caso se queira começar com coordenadas 0,0 
            col_alterar -= 1
            tabuleiro[lin_alterar][col_alterar] = lista_jogadores[j]["Peça"]
            imprimir_tabuleiro(tabuleiro)
            break
       
def inicio_jogo(tabuleiro, lista_jogadores, j, ij_n_jogador, contador, coordenadasbonus):  
    coordenadasbonus = [] 
    vizinhos = [] 
    while True:
        j, contador, vizinhos = jogadas(tabuleiro, lista_jogadores, j, ij_n_jogador, contador, vizinhos, coordenadasbonus)
        if not verificar_fim_de_jogo(lista_jogadores, tabuleiro, j, vizinhos):
            break
def verificar_fim_de_jogo(lista_jogadores, tabuleiro, j, vizinhos):
    for linha in tabuleiro:
        for coluna in linha:
            if coluna == '🔳': 
                return False
    if vizinhos == []:
        return False
    for jogador in lista_jogadores:
        if jogador['Inativo'] == True  and jogador['NUMERO_PEÇAS'] == 0:
            return False
        else:
            return True
    

def verificar_vencedor(lista_jogadores):
    vencedores = []
    for i in range(len(lista_jogadores)):
        for p in range(i + 1, len(lista_jogadores)):
            if ((lista_jogadores[i]["NUMERO_PEÇAS"] > lista_jogadores[p]["NUMERO_PEÇAS"]) or
                ((lista_jogadores[i]["NUMERO_PEÇAS"] == lista_jogadores[p]["NUMERO_PEÇAS"]) and
                 (lista_jogadores[i]["Pontuação"] < lista_jogadores[p]["Pontuação"]))):
                lista_jogadores[i], lista_jogadores[p] = lista_jogadores[p], lista_jogadores[i]
            elif ((lista_jogadores[i]["NUMERO_PEÇAS"] == lista_jogadores[p]["NUMERO_PEÇAS"]) and
                   (lista_jogadores[i]["Pontuação"] == lista_jogadores[p]["Pontuação"])):
                vencedores.append(lista_jogadores[i])
                vencedores.append(lista_jogadores[p])
    if len(vencedores) == 0:
        vencedor = lista_jogadores[0]
        return vencedor["Nome"], vencedor["Pontuação"]
    else:
        return "Empate", vencedores
    
       

def ler_ficheiro_json(nome_ficheiro):
    with open(nome_ficheiro) as f:
        data = json.load(f)
    return data 
def escrever_ficheiro_json(nome_ficheiro, d):
    json_string = json.dumps(d)
    json_file = open(nome_ficheiro, "w")
    json_file.write(json_string)
    json_file.close()