from controller import *
import os

a = 0
def main():
    os.system('cls')
    while True:
        global a
        if a == 0:
            print("""
                
                
                
                
                                        Bem vindos ao nosso jogo! 🕹️
                
                
                
                """)
            a=a+1
            time.sleep(2)
            os.system('cls')
        else:
            jogadores = ler_ficheiro_json("jogadores.json")
            #tabuleiro = criar_tabuleiro()  
            os.system('cls')
            opcao = int(input("""
                            **** MENU - JOGO TERRITÓRIO ****
                        1 - REGISTAR JOGADOR
                        2 - INICIAR JOGO
                        3 - VISUALIZAR PONTUAÇÃO
                        4 - Ler
                        5 - Gravar
                        6 - adicionar remover jogador
                        7 - Definições de Bônus   
                        9 - Instruções
                        0 - Sair
                        Escolha uma opção: """))
            match opcao: 
                case 1: #registar jogador
                    while True:
                        nome = input("insira o nome do jogador:\n").upper
                        print("insira C para cancelar \n")
                        if nome == 'C':  
                            main()     
                        elif registar_jogador(jogadores, nome) == True:
                            print(f"Jogador já registado, tente novamente\n")
                        else:
                            print(f"Jogador adicionado com sucesso: {jogadores}\n")
                            n_jogadores = verificar_numero_jogadores(jogadores)
                            if n_jogadores == True: 
                                print(f"Já está pronto para começar o jogo\n")
                            else:
                                print(f"Numero de jogadores insuficiente: {jogadores}\n")
                                break
                            
                case 2: # iniciar jogo 
                    os.system('cls')
                    ij_n_jogador = int(input("insira quantas pessoas vão jogar:"))
                    lista_jogadores = [] 
                    contador = 0
                    print(f"{lista_jogadores}\n {jogadores}\n")
                    j=0
                    #é necessário verificar quantos jogadores estao registados no jogadores.json
                    if ij_n_jogador > 4 or ij_n_jogador < 2:
                        print("Número de jogadores insuficiente\n Tente novamente")
                    elif len(jogadores) < 2:
                        print("Registe mais jogadores\n Tente novamente")
                        main()
                    else:  
                        for i in range(0, ij_n_jogador):
                            nome = input("insira o nome do jogador:\n")
                            if verificar_jogador(jogadores, nome) == True:
                                
                                lista_jogadores.append({'Nome':nome})
                                if i < ij_n_jogador:
                                    print("nome válido insira o próximo nome\n")
                                elif i == ij_n_jogador:
                                    print("Jogadores inseridos com sucesso\n")       
                                else:
                                    print("jogador não registado\n Tente novamente\n")
                        if ij_n_jogador == 4:
                            mod = input("Quer modo de duplas?\n S/N").upper   
                            if mod == "S":
                                #modo duplas 
                                print("modo duplas")
                            else:
                                lista_jogadores = associar_peca_jogador(lista_jogadores)
                                tabuleiro = criar_tabuleiro()
                                inicio_jogo(tabuleiro, lista_jogadores, j, ij_n_jogador, contador)
                        else:
                            lista_jogadores = associar_peca_jogador(lista_jogadores)
                            tabuleiro = criar_tabuleiro()
                            inicio_jogo(tabuleiro, lista_jogadores, j, ij_n_jogador, contador)
                case 3: # Visualizar pontuação
                    os.system('cls')
                    print("**** PONTUAÇÕES ****")
                    visualizar_pontuacao(jogadores)
                    time.sleep(input("Pressione uma tecla para continuar..."))
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
