from controller import *
def main():

    jogadores = []
    while True:
        opcao = int(input("""****JOGO TERRITÓRIO****
                            1-> REGISTAR JOGADOR
                            2-> INICIAR JOGO
                            3-> SAIR DO JOGO
                            INTRODUZA A OPÇÃO: """))
        
        match opcao:
            case 1:
                
                n_jogadores = int(input("Insira o número de jogadores (entre 2 e 4): \n"))
                if (n_jogadores >= 2 and n_jogadores <= 4):
                
                    print("\nJogadores registados com sucesso!\n")
                else:
                    print("\nNúmero inválido de jogadores\n")
                
                for i in range (n_jogadores):
                    nome = input(f"Introduza o nome do jogador {i + 1}: ").lower
                    jogadores.append(nome)
                    #falta verificar se há nomes repetidos e como fazer print da matriz com pontuação 0

            case 2:

                criar_tabuleiro()

        




