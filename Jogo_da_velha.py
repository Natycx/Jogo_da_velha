def desenho_jogo(matriz):
    for i in range(0, 3):
        for j in range(0, 3):
            print(f'{matriz[i][j]}', end='')
        print("")


def troca_jogador(jogador):
    if jogador == 'x':
        jogador = 'o'
    else:
        jogador = 'x'
    return jogador


def valida_vencedor(matriz):
    venceu = False
    condicao_vitoria = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (1, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 1)]
    ]

    for x in condicao_vitoria:
        posicao1 = matriz[x[0][0]][x[0][1]]
        posicao2 = matriz[x[1][0]][x[1][1]]
        posicao3 = matriz[x[2][0]][x[2][1]]
        if '_' not in [posicao1, posicao2, posicao3]:
            if posicao1 == posicao2 == posicao3:
                venceu = True
                break

    return venceu


def gerador_dica(matriz, jogador):
    possibilidades = []
    oponente = troca_jogador(jogador)
    condicao_vitoria = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (1, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 1)]
    ]

    for x in condicao_vitoria:
        posicao1 = matriz[x[0][0]][x[0][1]]
        posicao2 = matriz[x[1][0]][x[1][1]]
        posicao3 = matriz[x[2][0]][x[2][1]]
        if posicao1 == posicao2 == jogador and posicao3 == '_':
            possibilidades.append(x[2])
        elif posicao2 == posicao3 == jogador and posicao1 == '_':
            possibilidades.append(x[0])
        elif posicao1 == posicao3 == jogador and posicao2 == '_':
            possibilidades.append(x[1])

    if not bool(possibilidades):
        for x in condicao_vitoria:
            posicao1 = matriz[x[0][0]][x[0][1]]
            posicao2 = matriz[x[1][0]][x[1][1]]
            posicao3 = matriz[x[2][0]][x[2][1]]
            if posicao1 == posicao2 == oponente and posicao3 == '_':
                possibilidades.append(x[2])
            elif posicao2 == posicao3 == oponente and posicao1 == '_':
                possibilidades.append(x[0])
            elif posicao1 == posicao3 == oponente and posicao2 == '_':
                possibilidades.append(x[1])

    if not bool(possibilidades):
        for x in condicao_vitoria:
            posicao1 = matriz[x[0][0]][x[0][1]]
            posicao2 = matriz[x[1][0]][x[1][1]]
            posicao3 = matriz[x[2][0]][x[2][1]]
            if posicao1 == jogador and [posicao2, posicao3].count('_') == 2:
                possibilidades.extend([x[1], x[2]])
            elif posicao2 == jogador and [posicao1, posicao3].count('_') == 2:
                possibilidades.extend([x[0], x[2]])
            elif posicao3 == jogador and '_' and [posicao1, posicao2].count('_') == 2:
                possibilidades.extend([x[0], x[1]])

    return possibilidades


def print_dica(matriz, jogador):
    dicas = gerador_dica(matriz, jogador)
    if bool(dicas):
        print(f'Possibilidades de vitoria {dicas}')


def main():

    matriz = [['_', '_', '_'],
              ['_', '_', '_'],
              ['_', '_', '_']]

    jogador = ''
    fim_jogo = False
    while True:
        if jogador != 'x' and jogador != 'o':
            jogador = input('Digite x ou o: ')
        else:
            break
    while True:
        print(f'Agora é a vez do {jogador} ')

        print_dica(matriz, jogador)

        for i in range(0, 3):
            entrada = ''
            for j in range(0, 3):
                if matriz[i][j] not in ['x', 'o']:
                    entrada = input(f'Digite {jogador} para preencher a posição {i}, {j}: ')
                    if entrada == jogador:
                        matriz[i][j] = entrada
                        break

            if entrada != '':
                break

        desenho_jogo(matriz)

        if valida_vencedor(matriz):
            print(f'{jogador} Ganhou!')
            break

        jogador = troca_jogador(jogador)


if __name__ == '__main__':
    main()