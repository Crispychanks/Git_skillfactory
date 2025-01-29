# консоль для игры на двоих в крестики-нолики

print('''Let's play''')

# создаем матрицу для игры

matrix = [[" "]*3 for i in range(3)]
def show_field():
    print("   | 1 | 2 | 3 | ")
    print("   -------------")
    for i, row in enumerate(matrix):
        print(f" {i} | {' | '.join(row)} |")
show_field()

# функция для проверки результатов хода

def check_equals(player):
    for row in matrix:
        if all(player == elem == row[0] for elem in row): # по горизонтали
            return '''выиграли ''', player
        elif all(player == elem == row[n] for elem, n in zip(row, range(3))): # по вертикали
            return '''выиграли ''', player
        elif any([
            player == matrix[0][0] == matrix[1][1] == matrix[2][2], # первая диагональ
            player == matrix[2][0] == matrix[1][1] == matrix[0][2]]): # вторая диагональ
            return '''выиграл игрок ''', player
    print('''следующий ход''')
    return

# функция запуска игры и последующих ходов

def turn():
    i, j = map(int, input('''Введите координаты: ''').split())
    player = str(input('''Введите Х или О: '''))
    if matrix[i][j] == 'X' or matrix[i][j] == 'O': # проверка на занятость клетки
        print('''value is full''')
        return turn()
    matrix[i][j] = player
    show_field()
    result = check_equals(player)
    if result:
        print(result)
        return
    else:
        return turn()

turn()
