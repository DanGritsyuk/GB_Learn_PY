import os


class Exercise4:
    """Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)."""

    @staticmethod
    def Start():
        os.system('cls')
        print('решение 4 задачи\n')
        Num = abs(int(input('Введите число: ')))
        i = int(2)

        while i <= Num:
            print(f'{i}', end=' ')
            i += 2

        input("\nДля продолжения нажмите Enter...")
