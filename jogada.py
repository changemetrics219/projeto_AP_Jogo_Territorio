from jogadores import encontrar_jogador_id
## id jogador, e as suas jogadas
## {'ID': 1, 'JOGADA':[[],[]]}
jogada = []

##CONTINUAR:: Implementar lógica das jogadas, E Criar Movimentação das peças no tabuleiro

def jogada_do_jogador(id, jogada_):
    #Verificar se o jogada existe na estrutura de Jogadores ## É um  pedaço de código desnecessário.. mas...
   # if not encontrar_jogador_id(id): return False

    ## verifica se o jogador já jogou; se não, faz pra ele a primeira jogada
    if verificar_se_jogador_ja_jogou(id): marcar_jogada(id, jogada_)
    else: marcar_primeira_jogada(id, jogada_)
               
## Marca jogadas 
def marcar_jogada(id, jogada_, jogada):
    for jogadores in range(len(jogada)):
        if jogada[jogadores]["ID"] == id:
            jogada[jogadores]["JOGADA"]["LINHA"].append(jogada_[0])
            jogada[jogadores]["JOGADA"]["COLUNA"].append(jogada_[1])

## Cria a primeira tupla para o jogador
def marcar_primeira_jogada(id, jogada_):
    global jogada
    jogada.append({"ID":id, "JOGADA":{"LINHA":jogada_[0], "COLUNA":jogada_[1]}})

## Verificar se o jogador com ID (id) já tem fez uma jogada
def verificar_se_jogador_ja_jogou(id):
    global jogada
    if verificar_se_aconteceu_uma_jogada():
        for jogada_ in range(len(jogada)):
            if jogada[jogada_]["ID"] == id:
                return True

def verificar_se_aconteceu_uma_jogada():
    global jogada
    if len(jogada) != 0: return True

def retorna_ultima_jogada():
    global jogada
    return jogada[len(jogada) - 1]