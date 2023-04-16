# Задача 1. Дано натуральное число N. Напишите метод, который вернёт список простых множителей числа N и количество этих множителей.
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise12(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        num = int(input('Введите число N: '))
        primeFactor = []
        d = 2
        while d * d <= num:
            if num % d == 0:
                primeFactor.append(d)
                num //= d
            else:
                d += 1
        if num > 1:
            primeFactor.append(num)
        print(primeFactor)