from Exercises.Homework1.Exercise1 import Exercise1
from Exercises.Homework1.Exercise2 import Exercise2
from Exercises.Homework1.Exercise3 import Exercise3
from Exercises.Homework1.Exercise4 import Exercise4
from Exercises.Homework2.Exercise5 import Exercise5
from Exercises.Homework2.Exercise6 import Exercise6
from Exercises.Homework2.Exercise7 import Exercise7
from Exercises.Homework2.Exercise8 import Exercise8
from Exercises.ExerciseAbstract import ExerciseAbstract


class ExerciseBuilder:

    @staticmethod
    def GetExersice() -> ExerciseAbstract:
        correctEnter = False
        while not correctEnter:
            taskNum = int(input('Введите номер задачи: '))
            match taskNum:
                case 0:
                    return None
                case 1:
                    return Exercise1('Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.')
                case 2:
                    return Exercise2('Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.')
                case 3:
                    return Exercise3('Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).')
                case 4:
                    return Exercise4('Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.')
                case 5:
                    return Exercise5('Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.')
                case 6:
                    return Exercise6('Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.')
                case 7:
                    return Exercise7('Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй')
                case 7:
                    return Exercise7('Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй')
                case 8:
                    return Exercise8('Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.')
                case _:
                    print('Такой задачи нет. Повторите попытку...\n')
                    continue
