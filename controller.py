#def(function):
    #aqui vão ficar as funçoes
def criar_tabuleiro():
    lins = int(input("Insira o num de linhas: "))
    cols = int(input("Insira o num de colunas: "))

    #cria uma lista com o "X" aparecendo tantas vezes quando o nºde colunas
    table = []
    for i in range(lins):
        table.append(list('X'*cols))

    #une as listas sem nenhum espaco para mostrar na tela
    for line in table:
        print(''.join(line))

    #pergunta qual linha e coluna deseja alterar
    lin_alterar = int(input("Qual linha deseja alterar?: "))
    col_alterar = int(input("Qual coluna deseja alterar?: "))

    #qual o valor novo a ser inserido
    vlr_novo = 'P'

    #altera o item da posicao escolhida para o vlr_novo
    table[lin_alterar - 1][col_alterar - 1] = vlr_novo

    #une as listas sem nenhum espaco para mostrar na tela
    for line in table:
        print(''.join(line))