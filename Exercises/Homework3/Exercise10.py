# Задача 2. В списке находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise10(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        print()