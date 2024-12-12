from controller import *

def main():

    jogadores = [ ]

    while True:
        opcao = int(input("""
                        **** MENU - JOGO TERRITÓRIO ****
                      1-> REGISTAR JOGADOR
                      2-> INICIAR JOGO
                      3-> VISUALIZAR PONTUAÇÃO
                      4-> SAIR
                      QUAL A OPÇÃO QUE QUER ESCOLHER? """))
        
        match opcao:
            
            case 1:
                n_jogadores = int(input("Insira o número de jogadores: \n"))
                if (n_jogadores >= 2 and n_jogadores <= 4):
                    nome = input("Introduza o seu nome: ").upper
                    registar_jogador(jogadores, nome)
                    print(f"{jogadores} registado com sucesso.")
        
                else:
                    print("\nNúmero inválido de jogadores\n")

            
            case 2:
                nome_1 = input("Introduza o nome do jogador 1:\n ").upper
                nome_2 = input("Introduza o número do jogador 2:\n ").upper
                if verificar_jogador(nome_1, jogadores) and verificar_jogador(nome_2, jogadores) == True:
                    print(f"{nome_1} e {nome_2} registados com sucesso!")
                else:
                    print("Os jogadores não foram resistados. Registe os jogadores")
                    break

                # Aqui fica o código da criação do tabuleiro
                
                cores = ["Vermelho", "Verde", "Amarelo", "Azul"]
                print("\nCORES DISPONÍVEIS: ")
                for cor in cores:
                    print(cor)

                

                # Lista para guardar as cores escolhidas pelos jogadores
                cores_jogadores = []

                # Adiciona a cor escolhida à lista associada ao jogador
                escolha_cor = input("\nEscolha uma cor: ").upper
                if escolha_cor in cores:
                    cores_jogadores.append((nome_1, escolha_cor))
                    print(f"\n{escolha_cor} escolhida com sucesso para {nome_1}!")
                else:
                    print("\nCor inválida!")


                

            case 3:
                visualizar_pontuacao(jogadores)

            case 4:
                print("Obrigado por jogar! Até à próxima!")
                break

            case _:
                print("\nOpção inválida!\n")

                















    #aqui vai ficar o código principal
    print("Hello world!")
    n_jogadores = int(input("insira o número de jogadores: \n"))
    if (n_jogadores >= 2 and n_jogadores <= 4):
        #o código irá correr
        print("")
    else:
        print("\nNúmero inválido de jogadores\n")