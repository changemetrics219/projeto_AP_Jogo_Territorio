import os
import time
from controller import (
    ler_ficheiro_json,
    escrever_ficheiro_json,
    registar_jogador,
    criar_tabuleiro,
    adicionar_bonus,
    associar_peca_jogador,
    verificar_fim_de_jogo,
    verificar_vencedor,
    realizar_jogada
)

def imprimir_tabuleiro(tabuleiro):
    """Exibe o tabuleiro no console."""
    print("\n     " + "  ".join(str(i + 1) for i in range(len(tabuleiro[0]))))
    for i, linha in enumerate(tabuleiro):
        print(f"{i + 1:2} " + "  ".join(linha))

def main():
    jogadores = ler_ficheiro_json("jogadores.json")
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        opcao = input("""
        **** MENU - JOGO TERRITÓRIO ****
        RJ - REGISTRAR JOGADOR
        IJ - INICIAR JOGO
        VP - VISUALIZAR PONTUAÇÃO
        S  - SAIR
        Escolha uma opção: """).upper()

        if opcao == "RJ":
            nome = input("Digite o nome do jogador: ")
            if registar_jogador(jogadores, nome):
                print(f"Jogador {nome} registrado com sucesso!")
            else:
                print("Jogador já registrado.")
            time.sleep(2)

        elif opcao == "IJ":
            if len(jogadores) < 2:
                print("Número insuficiente de jogadores. Registre pelo menos 2 jogadores.")
                time.sleep(2)
                continue

            num_jogadores = int(input("Quantos jogadores irão jogar? (2-4): "))
            if not (2 <= num_jogadores <= 4):
                print("Número inválido. Escolha entre 2 e 4 jogadores.")
                time.sleep(2)
                continue

            jogadores_partida = [j for j in jogadores[:num_jogadores]]
            jogadores_partida = associar_peca_jogador(jogadores_partida)

            tamanho_tabuleiro = int(input("Digite o tamanho do tabuleiro: "))
            tabuleiro = criar_tabuleiro(tamanho_tabuleiro)

            coordenadas_bonus = adicionar_bonus(tabuleiro)
            visivel = input("Deseja bônus visíveis? (S/N): ").upper() == "S"
            if visivel:
                for lin, col in coordenadas_bonus:
                    tabuleiro[lin][col] = "⭐"

            imprimir_tabuleiro(tabuleiro)

            jogador_atual = 0
            while not verificar_fim_de_jogo(tabuleiro, jogadores_partida):
                tabuleiro = realizar_jogada(tabuleiro, jogadores_partida[jogador_atual], coordenadas_bonus)
                imprimir_tabuleiro(tabuleiro)  # Exibe o tabuleiro após cada jogada
                jogador_atual = (jogador_atual + 1) % len(jogadores_partida)

            vencedor = verificar_vencedor(jogadores_partida)
            print(f"Fim do jogo! O vencedor é {vencedor['Nome']} com {vencedor['Pontuação']} pontos!")
            time.sleep(5)

        elif opcao == "VP":
            print("**** PONTUAÇÕES ****")
            for jogador in jogadores:
                print(f"{jogador['Nome']}: {jogador['Pontuação']} pontos")
            input("Pressione Enter para continuar...")

        elif opcao == "S":
            print("Saindo... Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)