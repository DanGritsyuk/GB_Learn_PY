# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise6(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        print('X | Y | Z | ¬(X ∧ Y) ∨ Z')
        for x in range(0, 2):
            for y in range(0, 2):
                for z in range(0, 2):
                    print(f'{x} | {y} | {z} | {int(not (x and y) or z)}')
