# Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise23(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        def Check(x, y):
            for division in range(2, x + 1):
                if x % division == 0 and y % division == 0:
                    return False
            return True

        for y in range(2, 12):
            for x in range(1, y):
                if Check(x, y):
                    print(f'{x}/{y}', end=' ')
            print()