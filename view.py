from controller import *
import os
def main():
    os.system('cls')
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
                      X - adicionar remover jogador
                      X - Definições de Bônus
                      6 - Instruções
                      0 - Sair
                      Escolha uma opção: """))
        if opcao == '0':
            print("Bye 👋")
            break
        else:
            match opcao: 
                case 1: #registar jogador
                    while True:
                        nome = input("insira o nome do jogador:\n")
                        if registar_jogador(jogadores, nome) == True: 
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
                        if ij_n_jogador > 4 or ij_n_jogador < 2:
                            print("Numero de jogadores insuficiente\n Tente novamente")
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
                        lista_jogadores = associar_peca_jogador(ij_n_jogador, lista_jogadores)   
                        print(lista_jogadores)     
                        criar_tabuleiro()   #aqui vai começar o jogo  
                        
                        
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

