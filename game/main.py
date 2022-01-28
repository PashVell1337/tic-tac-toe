field = [[" "] * 3 for i in range(3)]

def play_field():
    print(f"  0 1 2")
    for i in range(3):
        line_number = " ".join(field[i])
        print(f"{i} {line_number}")

def check():
    win_coordinate = (((0, 0), (0, 1), (0, 2)),
                ((1, 0), (1, 1), (1, 2)),
                ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)),
                ((0, 0), (1, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)),
                ((0, 2), (1, 2), (2, 2)))

    for coordinate in win_coordinate:
        symbols = []
        for c in coordinate:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграли крестики")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграли нолики")
            return True
    return False

def enter():
    while True:
        x, y = map(int, input("         Ваш ход: ").split())

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue


        return x, y




count = 0
while True:
    count += 1
    play_field()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = enter()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check():
        break

    if count == 9:
        print(" Ничья!")
        break