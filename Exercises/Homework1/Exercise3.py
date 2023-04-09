# Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
import os


class Exercise3:

    @staticmethod
    def Start():
        os.system('cls')
        print('решение 3 задачи\n')
        planeNum = int(input('Введите номер четверти: '))
        match planeNum:
            case 1:
                print('x > 0, y > 0')
            case 2:
                print('x < 0, y > 0')
            case 3:
                print('x < 0, y < 0')
            case 4:
                print('x > 0, y < 0')
            case _:
                print('Нет такой четверти!')
        input("\nДля продолжения нажмите Enter...")
