# Задача 5. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
import os


class Exercise5:

    @staticmethod
    def Start():
        os.system('cls')
        print('решение 5 задачи\n')
        num = int(input('Введите число N: '))

        lstFactorials = []

        for i in range(1, num+1):
            factorial = 1
            for j in range(1, i+1):
                factorial *= j
            lstFactorials.append(factorial)

        print(f'N = {num} -> {lstFactorials}')

        input("\nДля продолжения нажмите Enter...")
