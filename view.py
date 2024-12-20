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
                num_jogadores(jogadores)

                # Aqui fica o código da criação do tabuleiro - função criar_tabuleiro()
                
                cores = ["Vermelho", "Verde", "Amarelo", "Azul"]
                print("\nCores Disponíveis: \n")
                for c in cores:
                    print(c)

                # Lista para guardar as cores escolhidas pelos jogadores
                cores_jogadores = [ ]
                


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
                print("\nObrigado por jogar! Até à próxima!\n")
                print(f"\nPontuações finais:\n{jogadores}")
                break

            case _:
                print("\nOpção inválida!\n")

                