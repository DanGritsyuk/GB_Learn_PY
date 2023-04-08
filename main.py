import os
from Exercises.Homework1.Exercise1 import Exercise1
from Exercises.Homework1.Exercise2 import Exercise2
from Exercises.Homework1.Exercise3 import Exercise3
# from Exercises.Homework1.Exercise4 import Exercise4

done = False
while not done:
    os.system('cls')
    print('Домашнее задание №1')
    print('Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.')
    print('Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.')
    print('Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).')
    print('Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.')
    print('')
    print('0 - выход из программы.')

    correctEnter = False
    while not correctEnter:
        taskNum = int(input('Введите номер задачи: '))
        match taskNum:
            case 0:
                os.system('cls')
                done = correctEnter = True
            case 1:
                Exercise1.Start()
            case 2:
                Exercise2.Start()
            case 3:
                Exercise3.Start()
            case 4:
                print('решение 4  задачи\n')
            case _:
                print('Такой задачи нет. Повторите попытку.../n')
                continue
        correctEnter = True
print('Программа закрыта.')
