"""
Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y).
"""

number = int(input('Введите номер четверти: '))
if number < 1 or number > 4:
    print('Ошибка, это не номер четверти')
else:
    if number == 1:
        print('x > 0, y > 0')
    else:
        if number == 2:
            print('x < 0, y > 0')
        else:
            if number == 3:
                print('x < 0, y < 0')
            else:
                if number == 4:
                    print('x > 0, y < 0')
