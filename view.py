from controller import *
import os
def main():

    jogadores = ler_ficheiro_json("jogadores.json")
    #tabuleiro = criar_tabuleiro()  
    while True:
        opcao = int(input("""
                        **** MENU - JOGO TERRITÓRIO ****
                      1 - REGISTAR JOGADOR
                      2 - INICIAR JOGO
                      3 - VISUALIZAR PONTUAÇÃO
                      4 - Ler
                      5 - Gravar
                      6 - Instruções
                      0 - Sair
                      Escolha uma opção: """))
        if opcao == '0':
            print("Bye 👋")
            break
        else:
                match opcao: 
                    case 1: #registar jogador
                        nome = input("insira o nome do jogador:\n")
                        if registar_jogador(jogadores, nome) == True: 
                            print(f"Jogador já registado\n")
                        else:
                            print(f"Jogador adicionado com sucesso: {jogadores}\n")
                        
                        n_jogadores = verificar_numero_jogadores(jogadores)
                        if n_jogadores == True:
                            print(f"Já está pronto para começar o jogo\n")
                        else:
                            print(f"Numero de jogadores insuficiente: {jogadores}\n")
                    
                    case 2: # iniciar jogo que nao funciona
                        os.system('cls')
                        ij_n_jogador = int(input("insira quantas pessoas vão jogar:"))
                        lista_jogadores = []
                        try: 
                            if ij_n_jogador > 4 or ij_n_jogador < 2:
                                print("Numero de jogadores insuficiente\n Tente novamente")
                        except:
                            for i in range(0, ij_n_jogador):
                                nome = input("insira o nome do jogador:\n")
                                try:
                                    if verificar_jogador(jogadores, nome) == True:
                                        if i < ij_n_jogador:
                                            print("nome válido insira o próximo nome\n")
                                        else:
                                            print("Jogadores inseridos com sucesso\n")
                                            criar_tabuleiro()   #aqui vai começar o jogo
                                except:
                                        print("jogador não registado\n Tente novamente\n")    
                        
                        
                        for i in range(0, len(jogadores)): # escolha de cores de cada jogador
                            cores=int(input("Escolha uma cor:\n1 - azul\n2 - vermelho\n3 - Amarelo\n4 - verde\n"))
                            i=1+1
                            match cores:
                                case 1:
                                    print("azul\n")   
                                    #definir que o jogador i é azul
                                case 2:
                                    print("vermelho\n")
                                    #definir que o jogador i é vermelho
                                case 3:
                                    print("amarelo\n")
                                    #definir que o jogador i é amarelo
                                case 4:
                                    print("verde\n")
                                    #definir que o jogador i é verde
                                case _:
                                    print("opçao inválida\n")
                    case 3: # Visualizar pontuação
                        os.system('cls')
                        print("**** PONTUAÇÕES ****")
                        for j in jogadores:
                            print(f"Jogador: {j["Nome"]}, pontuação: {j["Pontuação"]}")
                            visualizar_pontuacao(jogadores)
                    case 4: # ler ficheiro
                        os.system('cls')
                        jogadores = ler_ficheiro_json("jogadores.json")
                        print(jogadores)  
                    case 5: # gravar ficheiro
                        os.system('cls')
                        print("Ficheiro gravado com sucesso")
                        escrever_ficheiro_json("jogadores.json", jogadores)   
                    case 6: # instruções 
                        print("instruções")
                    case 0: #sair
                        print("Bye 👋")
                        break
                    case _:
                        os.system('cls')
                        print("Opção inválida\n Tente novamente!")        

                    
