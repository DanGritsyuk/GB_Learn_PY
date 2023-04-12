# Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise3(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        planeNum = int(input('Введите номер четверти: '))
        match planeNum:
            case 1:
                print('x > 0, y > 0')
            case 2:
                print('x < 0, y > 0')
            case 3:
                print('x < 0, y < 0')
            case 4:
                print('x > 0, y < 0')
            case _:
                print('Нет такой четверти!')
