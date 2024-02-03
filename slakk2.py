jogo = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]
ganhador = False
empatado = False
cont = 0
print('Bem vindo ao jogo da velha!')
while True:
    print('Vez do jogador 1')
    print(jogo[0])
    print(jogo[1])
    print(jogo[2])
    while True:
        l = int(input('Linha do "x": '))
        c = int(input('Coluna do "x": '))
        if 'x' in jogo[l - 1][c - 1] or 'o' in jogo[l - 1][c - 1]:
            print('Já há um elemento neste quadrado. Tente novamente.')
        else:
            jogo[l - 1][c - 1] = 'x'
        if 'x' in jogo[0][0] and 'x' in jogo[0][1] and 'x' in jogo[0][2]:
            ganhador = True
            print('O jogador 1 ganhou o jogo!')
            print(jogo[0])
            print(jogo[1])
            print(jogo[2])
            break
        elif 'x' in jogo[1][0] and 'x' in jogo[1][1] and 'x' in jogo[1][2]:
            ganhador = True
            print('O jogador 1 ganhou o jogo!')
            print(jogo[0])
            print(jogo[1])
            print(jogo[2])
            break
        elif 'x' in jogo[2][0] and 'x' in jogo[2][1] and 'x' in jogo[2][2]:
            ganhador = True
            print('O jogador 1 ganhou o jogo!')
            print(jogo[0])
            print(jogo[1])
            print(jogo[2])
            break
        elif 'x' in jogo[0][0] and 'x' in jogo[1][0] and 'x' in jogo[2][0]:
            ganhador = True
            print('O jogador 1 ganhou o jogo!')
            print(jogo[0])
            print(jogo[1])
            print(jogo[2])
            break
        elif 'x' in jogo[0][1] and 'x' in jogo[1][1] and 'x' in jogo[2][1]:
            ganhador = True
            print('O jogador 1 ganhou o jogo!')
            print(jogo[0])
            print(jogo[1])
            print(jogo[2])
            break
        elif 'x' in jogo[0][2] and 'x' in jogo[1][2] and 'x' in jogo[2][2]:
            ganhador = True
            print('O jogador 1 ganhou o jogo!')
            print(jogo[0])
            print(jogo[1])
            print(jogo[2])
            break
        elif 'x' in jogo[0][0] and 'x' in jogo[1][1] and 'x' in jogo[2][2]:
            ganhador = True
            print('O jogador 1 ganhou o jogo!')
            print(jogo[0])
            print(jogo[1])
            print(jogo[2])
            break
        elif 'x' in jogo[0][2] and 'x' in jogo[1][1] and 'x' in jogo[2][0]:
            ganhador = True
            print('O jogador 1 ganhou o jogo!')
            print(jogo[0])
            print(jogo[1])
            print(jogo[2])
            break
        for linha in range(0, 3):
            for coluna in range(0, 3):
                if 'x' in jogo[linha][coluna] or 'o' in jogo[linha][coluna]:
                    cont += 1
        if cont == 9:
            empatado = True
            print('O jogo empatou!')
            break
        else:
            cont = 0
            break
    if ganhador:
        break
    if empatado:
        break
    print('Vez do jogador 2')
    print(jogo[0])
    print(jogo[1])
    print(jogo[2])
    while True:
        l = int(input('Linha do "o": '))
        c = int(input('Coluna do "o": '))
        if 'x' in jogo[l - 1][c - 1] or 'o' in jogo[l - 1][c - 1]:
            print('Já há um elemento neste quadrado. Tente novamente.')
        else:
            jogo[l - 1][c - 1] = 'o'
        if 'o' in jogo[0][0] and 'o' in jogo[0][1] and 'o' in jogo[0][2]:
            ganhador = True
            print('O jogador 2 ganhou o jogo!')
            print(jogo[0])
            print(jogo[1])
            print(jogo[2])
            break
        elif 'o' in jogo[1][0] and 'o' in jogo[1][1] and 'o' in jogo[1][2]:
            ganhador = True
            print('O jogador 2 ganhou o jogo!')
            print(jogo[0])
            print(jogo[1])
            print(jogo[2])
            break
        elif 'o' in jogo[2][0] and 'o' in jogo[2][1] and 'o' in jogo[2][2]:
            ganhador = True
            print('O jogador 2 ganhou o jogo!')
            print(jogo[0])
            print(jogo[1])
            print(jogo[2])
            break
        elif 'o' in jogo[0][0] and 'o' in jogo[1][0] and 'o' in jogo[2][0]:
            ganhador = True
            print('O jogador 2 ganhou o jogo!')
            print(jogo[0])
            print(jogo[1])
            print(jogo[2])
            break
        elif 'o' in jogo[0][1] and 'o' in jogo[1][1] and 'o' in jogo[2][1]:
            ganhador = True
            print('O jogador 2 ganhou o jogo!')
            print(jogo[0])
            print(jogo[1])
            print(jogo[2])
            break
        elif 'o' in jogo[0][2] and 'o' in jogo[1][2] and 'o' in jogo[2][2]:
            ganhador = True
            print('O jogador 2 ganhou o jogo!')
            print(jogo[0])
            print(jogo[1])
            print(jogo[2])
            break
        elif 'o' in jogo[0][0] and 'o' in jogo[1][1] and 'o' in jogo[2][2]:
            ganhador = True
            print('O jogador 2 ganhou o jogo!')
            print(jogo[0])
            print(jogo[1])
            print(jogo[2])
            break
        elif 'o' in jogo[0][2] and 'o' in jogo[1][1] and 'o' in jogo[2][0]:
            ganhador = True
            print('O jogador 2 ganhou o jogo!')
            print(jogo[0])
            print(jogo[1])
            print(jogo[2])
            break
        for linha in range(0, 3):
            for coluna in range(0, 3):
                if 'x' in jogo[linha][coluna] or 'o' in jogo[linha][coluna]:
                    cont += 1
        if cont == 9:
            empatado = True
            print('O jogo empatou!')
            break
        else:
            cont = 0
            break
    if ganhador:
        break
    if empatado:
        break
