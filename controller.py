<<<<<<< Updated upstream
#def(function):
    #aqui vão ficar as funçoes

def verificar_jogador(matriz, nome):
    for jogador in matriz:
        if nome == jogador ["Nome"]:
            return True
    return False
    
def num_jogadores(jogadores):
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




def registar_jogador(matriz, nome):
    if verificar_jogador(matriz, nome) == False:
        j = {"Nome": nome, "Pontuação": 0}
        matriz.append(j)

def visualizar_pontuacao(matriz):
    for jogador in matriz:
        print(f"{jogador['Nome']}: {jogador['Pontuação']}")


def adicionar_bonus(matriz, table):
    aleatorio = random.randint(0, len(table) - 1)

















def criar_tabuleiro():
    lins = int(input("Insira o num de linhas: "))
    cols = int(input("Insira o num de colunas: "))

    #cria uma lista com o "X" aparecendo tantas vezes quando o nºde colunas
    table = []
    for i in range(lins):
        table.append(list('X'*cols))

    #une as listas sem nenhum espaco para mostrar na tela
    for line in table:
        print(''.join(line))

    #pergunta qual linha e coluna deseja alterar
    lin_alterar = int(input("Qual linha deseja alterar?: "))
    col_alterar = int(input("Qual coluna deseja alterar?: "))

    #qual o valor novo a ser inserido
    vlr_novo = 'P'

    #altera o item da posicao escolhida para o vlr_novo
    table[lin_alterar - 1][col_alterar - 1] = vlr_novo

    #une as listas sem nenhum espaco para mostrar na tela
    for line in table:
        print(''.join(line))
=======
#aqui vão ficar as funçoes
def registar_jogador(matriz, nome):
    if verificar_jogador(matriz,nome) == False:
        j = {"Nome": nome, "Pontuação": 0}
        matriz.append(j)

def verificar_jogador(matriz, nome):
    for jogador in matriz:
        if nome == jogador["Nome"]:
            return True
    return False   
>>>>>>> Stashed changes
