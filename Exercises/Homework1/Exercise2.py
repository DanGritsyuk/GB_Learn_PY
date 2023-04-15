# Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
from Exercises.ExerciseAbstract import ExerciseAbstract
from Exercises.Homework1.Point2D import Point2D


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
