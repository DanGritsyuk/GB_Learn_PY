# Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise4(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        Num = abs(int(input('Введите число: ')))
        i = int(2)

        while i <= Num:
            print(f'{i}', end=' ')
            i += 2
