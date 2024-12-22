jogadores = []

def criar_jogador(nome):
    global jogadores
    ## verifica se já atingiu o limite de jogadores por partida
    if len(jogadores) == 4: return False
    
    ## ÚNICAS PEÇAS PERMITIDAS NO JOGO
    pecas = ["X", "H", "O", "T"]

    jogadores.append({'ID':len(jogadores) + 1 ,'JOGADOR':nome, 'NUMERO_PEÇAS': 21,'PEÇA':pecas[len(jogadores)]})
    return True

def mostrar_jogadores():
    global jogadores
    for jogador in jogadores:
        print(jogador)

 ## Percorre o vetor a lista de jogadores, encontra o jogador com ID e retorna True se o encontrou

def encontrar_jogador_id(id):
    global jogadores
    for jogador in range(len(jogadores)):
        if jogadores[jogador]['ID'] == id: return True
  
   
    ## CONTINUAR: criar funcao mostrar dados jogador via id
    ## CONTINUAR: i