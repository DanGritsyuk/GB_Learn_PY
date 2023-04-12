# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise5(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        num = int(input('Введите число N: '))

        lstFactorials = []

        for i in range(1, num+1):
            factorial = 1
            for j in range(1, i+1):
                factorial *= j
            lstFactorials.append(factorial)

        print(f'N = {num} -> {lstFactorials}')