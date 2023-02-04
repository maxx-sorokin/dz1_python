"""
Напишите программу для проверки истинности утверждения
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
"""

flag = True
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            f = not (x or y or z) == (not x and not y and not z)
            if f == False:
                flag = False
            print(x, y, z, f)
if flag:
    print('Доказано')
else:
    print('Нет, не во всех случаях')

# x = int(input('Введите число X: '))
# y = int(input('Введите число Y: '))
# z = int(input('Введите число Z: '))

# left = not (x or y or z)
# right = not x and not y and not z
# print(left == right)
