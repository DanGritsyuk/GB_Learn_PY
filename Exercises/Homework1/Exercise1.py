# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise1(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        dayNum = int(input('День недели: '))
        match dayNum:
            case 1:
                print('Понедельник')
            case 2:
                print('Вторник')
            case 3:
                print('Среда')
            case 4:
                print('Четверг')
            case 5:
                print('Пятница')
            case 6:
                print('Суббота')
            case 7:
                print('Воскресенье')
            case _:
                print('Нет такого дня недели!')
