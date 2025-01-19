from controller import *
import os
import time 


def main():
    a = 0
    os.system('cls')
    while True:
        
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
            #os.system('cls')
            opcao = input("""
                            **** MENU - JOGO TERRITÓRIO ****
                        RJ - REGISTAR JOGADOR
                        IJ - INICIAR JOGO
                        VP - VISUALIZAR PONTUAÇÃO
                        L - Ler
                        G - Gravar
                        R - Remover jogador
                        D - Definições de Bônus   
                        I - Instruções
                        S - Sair
                        Escolha uma opção: """).upper()
            match opcao: 
                case "RJ": #registar jogador
                    while True:
                        nome = input("insira o nome do jogador:\n")
                        verificar_jogador(jogadores, nome)
                        var = registar_jogador(jogadores, nome)
                        if var == False:
                            print("jogador já registado\n")
                            continue
                        else:
                            print(f"Jogador adicionado com sucesso: {jogadores}\n")
                            n_jogadores = verificar_numero_jogadores(jogadores)
                            escrever_ficheiro_json("jogadores.json", jogadores)  

                            break
                            
                case "IJ": # iniciar jogo 
                    os.system('cls')
                    ij_n_jogador = int(input("Insira quantas pessoas vão jogar:\n"))
                    lista_jogadores = [] 
                    contador = 0
                    print(f"{lista_jogadores}\n {jogadores}\n")
                    j=0
                    #é necessário verificar quantos jogadores estao registados no jogadores.json
                    
                    if ij_n_jogador > 4 or ij_n_jogador < 2:
                        print("Número de jogadores insuficiente\n Tente novamente")
                        main()
                    elif len(jogadores) < 2 and len(jogadores) < ij_n_jogador:
                        print("Registe mais jogadores\n Tente novamente")
                        main()
                    else:  
                        for i in range(0, ij_n_jogador):
                            nome = input("Insira o nome do jogador:\n")
                            if verificar_jogador(jogadores, nome) == True:
                                
                                lista_jogadores.append({'Nome':nome})
                                if i < ij_n_jogador:
                                    print("Nome válido insira o próximo nome\n")
                                elif i == ij_n_jogador:
                                    print("Jogadores inseridos com sucesso\n")       
                            else:
                                print("Jogador não registado\n Tente novamente\n")
                                nome = input("Insira o nome do jogador:\n")
                           
                        for jogador in lista_jogadores:
                            while True:
                                cores = ["azul", "verde", "amarelo", "vermelho"]
                                print(f"Escolha uma cor disponível: {', '.join(cores)}") 
                                p = input(f"Qual a cor desejada, {jogador['Nome']}? ").lower() 

                                if p not in cores:
                                    print("Cor inválida. Escolha novamente.")
                                    p = input(f"Qual a cor desejada, {jogador['Nome']}? ").lower()
                                break
                        lista_jogadores = associar_peca_jogador(lista_jogadores,p)
                        cols = int(input("Insira o tamanho do tabuleiro: "))
                        tabuleiro = criar_tabuleiro(cols)
                        coordenadasbonus = {}
                        vizinhos=[]
                        coordenadasbonus["coordenadas"] = adicionar_bonus(tabuleiro)
                        coordenadasbonus["visivel"] = input("Digite (1) para bonus oculto ou (2) para bonus visivel:") == "2"
                        
                        if coordenadasbonus["visivel"]:
                            for posicao in coordenadasbonus["coordenadas"]:
                                tabuleiro[posicao[0]][posicao[1]] = "⭐"

                        
                            
                                    
                        inicio_jogo(tabuleiro, lista_jogadores, j, ij_n_jogador, contador, coordenadasbonus)
                        
                    
                        if jogadas(tabuleiro, lista_jogadores, j, ij_n_jogador, contador, vizinhos, coordenadasbonus):
                            print (f"\nÉ a vez de {jogadores[j]['Nome']}")

                            if jogador["NUMERO_PEÇAS"] < 1 :
                                print(f"{jogador['Nome']} não tem mais peças. Fim de jogo para este jogador.") 
                            
                            if verificar_fim_de_jogo(lista_jogadores, tabuleiro, j, vizinhos) == True:  #RESOLVER COM JOOGADAS
                                vencedor = verificar_vencedor(lista_jogadores)
                                print("Fim do jogo!")
                                print("Vencedor:", vencedor) 
                                break
                case "VP": # Visualizar pontuação
                    os.system('cls')
                    print("**** PONTUAÇÕES ****")
                    for jogadores in jogadores:
                        print(f"{jogadores['Nome']}: {jogadores['Pontuação']}")
                    input("Pressione uma tecla para continuar...\n")
                    main()
                case "L": # ler ficheiro
                    os.system('cls')
                    jogadores = ler_ficheiro_json("jogadores.json")
                    print(jogadores)  
                case "G": # gravar ficheiro
                    os.system('cls')
                    print("Ficheiro gravado com sucesso")
                    escrever_ficheiro_json("jogadores.json", jogadores)  
                            
                case "I": # instruções 
                    os.system('cls')
                    continuar = input("""\n               ******* INSTRUÇÕES DO JOGO TERRITÓRIO *******
                        1 - O JOGO CONSISTE EM CONQUISTAR O MAIOR NÚMERO DE TERRITÓRIOS NUM TABULEIRO DE DIMENSÃO VARIÁVEL.
                        2 - CADA JOGADOR RECEBE 21 PEÇAS.
                        3 - O JOGO PODE TER ENTRE 2 E 4 JOGADORES.
                        4 - NA OPÇÃO RJ (REGISTAR JOGADOR) PEDE-SE O NOME DOS JOGADORES. ATENÇÃO: OS NOMES NÃO PODEM SER IGUAIS E TÊM DE SER ADICIONADOS PELO MENOS 2 JOGADORES.
                        5 - NA OPÇÃO IJ (INICIAR JOGO) PEDE-SE O NÚMERO DE JOGADORES. ATENÇÃO: O NÚMERO DE JOGADORES NÃO PODE SER MENOR QUE 2 OU MAIOR QUE 4, de seguida devem escrever os nomes adicionados em RJ.
                        6 - O JOGO COMEÇA SENDO PEDIDA QUAL A COR QUE OS JOGADORES ESCOLHEM (AZUL/VERDE/AMARELO/VERMELHO).
                        7 - O TABULEIRO É IMPRESSO COM A DIMENSÃO ESCOLHIDA PELOS JOGADORES E A PRIMEIRA JOGADA para o jogador azul é PRÉ-DEFENIDA na coordenada (1,1) DO TABULEIRO.
                        8 - A PARTIR DA 2ª JOGADA O JOGADOR INSERE SEMPRE QUAL A LINHA E COLUNA EM QUE DESEJA INSERIR A PEÇA.
                        9 - A PEÇA NÃO DEVE SER COLOCADA FORA DAS DIMENSÕES DO TABULEIRO NEM NUMA POSIÇÃO JÁ OCUPADA.
                        10 - O JOGO É FEITO NO SENTIDO DOS PONTEIROS DO RELÓGIO.
                        11 - EXISTEM BÓNUS DISPONÍVEIS. 
                        12 - O JOGO TERMINA CASO UM JOGADOR NÃO TENHA MAIS PEÇAS E OS OUTROS JOGADORES JÁ NÃO TENHAM MAIS ESPAÇOS PARA INSERIR PEÇAS.
                        13 - CADA JOGADOR CONTA O NÚMERO DE QUADRADOS NAS PEÇAS QUE RESTARAM. CADA QUADRADO VALE UM PONTO.
                        14 - VENCE O JOGADOR COM MENOS PONTOS.
                        BOA SORTE ✌️         
                        DESEJA VOLTAR JÁ PARA O MENU? (sim/não)\n      """).upper()
                    if continuar == "SIM":
                        main()
                    else:
                        print("Em 30 segundos voltará para o menu principal\n")
                        time.sleep(30)
                        main()
                
                case "R":
                    os.system('cls')
                    a=0
                    print(jogadores)
                    remover = input("Insira o nome do jogador a remover: ")
                    for i, jogador in enumerate(jogadores):
                        if remover == jogador['Nome']:
                            del jogadores[i]
                            a = 1
                            break
                    if a == 0:
                        print("jogador não encontrado")
                        time.sleep(3)
                    elif a == 1:
                        print(jogadores)
                        escrever_ficheiro_json("jogadores.json", jogadores)
                        print("jogador removido com sucesso")
                        time.sleep(3)
                        
                    main()
                case "S": #sair
                    print("Bye 👋")
                    break
                    
                case _:
                    os.system('cls')
                    print("Opção inválida\n Tente novamente!")  