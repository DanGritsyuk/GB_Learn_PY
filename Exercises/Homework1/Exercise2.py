# Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise2(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        point1 = Point2D(int(input('Введите координату x первой точки: ')), int(
            input('Введите координату y первой точки: ')))
        point2 = Point2D(int(input('Введите координату x второй точки: ')), int(
            input('Введите координату y второй точки: ')))

        print(f'Расстояние равно: {Point2D.GetDistance(point1, point2)}')


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def GetDistance(point1, point2):
        return ((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2) ** (0.5)
