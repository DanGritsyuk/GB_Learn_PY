# Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise23(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        print('Задача 3')