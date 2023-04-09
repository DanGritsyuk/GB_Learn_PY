# Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
import os


class Exercise4:

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
