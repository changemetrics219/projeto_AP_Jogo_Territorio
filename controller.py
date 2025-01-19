import json
import math
from random import randint
import os

def ler_ficheiro_json(nome_ficheiro):
    """Lê dados de um arquivo JSON."""
    if not os.path.exists(nome_ficheiro):
        return []  # Retorna uma lista vazia se o arquivo não existir
    with open(nome_ficheiro, 'r') as f:
        return json.load(f)

def escrever_ficheiro_json(nome_ficheiro, dados):
    """Escreve dados em um arquivo JSON."""
    with open(nome_ficheiro, 'w') as f:
        json.dump(dados, f, indent=4)

def registar_jogador(jogadores, nome):
    """Registra um novo jogador se ele ainda não estiver na lista."""
    if not verificar_jogador(jogadores, nome):
        jogadores.append({"Nome": nome, "Pontuação": 0})
        escrever_ficheiro_json("jogadores.json", jogadores)
        return True
    return False

def verificar_jogador(jogadores, nome):
    """Verifica se o jogador já está registrado."""
    return any(jogador["Nome"] == nome for jogador in jogadores)

def criar_tabuleiro(tamanho):
    """Cria um tabuleiro quadrado com o tamanho especificado."""
    return [["🔳" for _ in range(tamanho)] for _ in range(tamanho)]

def adicionar_bonus(tabuleiro):
    """Adiciona bônus ao tabuleiro."""
    num_bonus = math.ceil(math.sqrt(len(tabuleiro)))
    coordenadas_bonus = []

    while len(coordenadas_bonus) < num_bonus:
        linha, coluna = randint(0, len(tabuleiro) - 1), randint(0, len(tabuleiro[0]) - 1)
        if [linha, coluna] not in coordenadas_bonus:
            coordenadas_bonus.append([linha, coluna])

    return coordenadas_bonus

def associar_peca_jogador(jogadores):
    """Atribui peças aos jogadores."""
    cores = ["azul", "verde", "amarelo", "vermelho"]
    for jogador in jogadores:
        while True:
            print(f"Escolha uma cor disponível: {', '.join(cores)}")
            cor = input(f"Qual a cor desejada, {jogador['Nome']}? ").lower()
            if cor in cores:
                cores.remove(cor)
                jogador.update({
                    "Cor": cor,
                    "Peça": {"azul": "🟦", "verde": "🟩", "amarelo": "🟨", "vermelho": "🟥"}[cor],
                    "NUMERO_PEÇAS": 21,
                    "Pontuação": 0,
                    "Linhas": [],
                    "Colunas": []
                })
                break
            print("Cor inválida. Escolha novamente.")
    return jogadores

def verificar_fim_de_jogo(tabuleiro, jogadores):
    """Verifica se o jogo terminou."""
    if all(jogador['NUMERO_PEÇAS'] == 0 for jogador in jogadores):
        return True
    if all(celula != "🔳" for linha in tabuleiro for celula in linha):
        return True
    return False

def verificar_vencedor(jogadores):
    """Determina o vencedor com base na pontuação e peças restantes."""
    jogadores.sort(key=lambda x: (-x['Pontuação'], x['NUMERO_PEÇAS']))
    return jogadores[0]

def realizar_jogada(tabuleiro, jogador, coordenadas_bonus):
    """Executa a jogada de um jogador."""
    while True:
        try:
            lin = int(input(f"{jogador['Nome']}, escolha a linha: ")) - 1
            col = int(input(f"{jogador['Nome']}, escolha a coluna: ")) - 1

            if not (0 <= lin < len(tabuleiro) and 0 <= col < len(tabuleiro)):
                print("Coordenadas fora do tabuleiro. Tente novamente.")
                continue

            if tabuleiro[lin][col] != "🔳":
                print("Posição ocupada. Escolha outra.")
                continue

            tabuleiro[lin][col] = jogador['Peça']
            jogador['Linhas'].append(lin)
            jogador['Colunas'].append(col)
            jogador['NUMERO_PEÇAS'] -= 1

            if [lin, col] in coordenadas_bonus:
                jogador['Pontuação'] += 9

            return tabuleiro  # Retorna o tabuleiro atualizado
        except ValueError:
            print("Entrada inválida. Use números inteiros.")