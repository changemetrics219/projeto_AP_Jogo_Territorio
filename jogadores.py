jogadores = []

def criar_jogador(nome):
    global jogadores
    ## verifica se já atingiu o limite de jogadores por partida
    if len(jogadores) == 4: return False

    ## ÚNICAS PEÇAS PERMITIDAS NO JOGO
    pecas = ["X", "H", "O", "T"]

    jogadores.append({'ID':len(jogadores) + 1 ,'JOGADOR':nome, 'NUMERO_PEÇAS': 21,'PEÇA':pecas[len(jogadores)], 'JOGADA':[[],[]]})
    return True


def mostrar_jogadores():
    global jogadores
    for jogador in jogadores:
        print(jogador)


    ## Percorre o vetor a lista de jogadores, encontra o jogador com ID passado no parametro e retorna as posições que já jogou 
def jogada_do_jogador(id):
    global jogadores
    for jog in range(len(jogadores)): 
        if jogadores[jog]['ID'] == id: return jogadores[jog]['JOGADA']
        