# Урок 1. Знакомство с Python
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# Решение
#date = int(input('введите число от 1 до 7: '))
#if date > 0 and date < 8:
#    if date < 6:
#        print("Будний день!!!")
#    else:
#        print("Выходной!!!")
#else:
#    print("Забыл цифры? тебя же просили ввести число от 1 до 7.")


# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
#Решение
# num_1 = int(input('введите число ≠ 0: '))
# print('X = ' + str(num_1)) 
# num_2 = int(input('введите число ≠ 0: '))
# print('Y = ' + str(num_2)) 

# if num_1 > 0 and num_2 > 0:
#     print('первая четверть')
# if num_1 > 0 and num_2 < 0:
#     print('вторая четверть')
# if num_1 < 0 and num_2 < 0:
#     print('третья четверть')
# if num_1 < 0 and num_2 > 0:
#     print('четвертая четверть')
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# Решение
#var = int(input('введите число от 1 до 4: '))
#if var == 1:
#    print("Координаты X от 0 до плюс бесконечности")
#    print("Координаты Y от 0 до плюс бесконечности")
#if var == 2:
#    print("Координаты X от 0 до плюс бесконечности")
#    print("Координаты Y от 0 до минус бесконечности")
#if var == 3:
#    print("Координаты X от 0 до минус бесконечности")
#    print("Координаты Y от 0 до минус бесконечности")
#if var == 4:
#    print("Координаты X от 0 до минус бесконечности")
#    print("Координаты Y от 0 до плюс бесконечности")
#if var < 1 or var > 4:
#    print("Не ту четверть ты выбрал сынок)")
