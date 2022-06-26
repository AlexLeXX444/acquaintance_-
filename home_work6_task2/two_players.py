# играют два игрока

from random import randint

def game_start (candys):
    player_1 = [input('Введите имя игрока 1: ')]
    player_2 = [input('Введите имя игрока 2: ')]

    # жеребьевка
    element = randint(1,2)
    if element == 1: 
        player_1.append(1)
        player_2.append(2)
    else: 
        player_1.append(2)
        player_2.append(1)

    if player_1[1] == 1:
        print(f'Начинает игрок {player_1[0]}.')
    else:
        print(f'Начинает игрок {player_2[0]}.')

    while candys > 0:
        print(f'Конфет осталось: {candys}.')
        candys_minus = 29
        if player_1[1] == 1:
            while candys_minus > 28:
                candys_minus = int(input(f'Ходите, игрок {player_1[0]}: '))
        else:
            candys_minus = int(input(f'Ходите, игрок {player_2[0]}: '))

        candys -= candys_minus

        player_1[1] += player_2[1]
        player_2[1] = player_1[1] - player_2[1]
        player_1[1] -= player_2[1]

    if player_1[1] == 2:
        print(f'Победил игрок {player_1[0]}')
    else:
        print(f'Победил игрок {player_2[0]}')