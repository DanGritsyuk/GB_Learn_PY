import os
from Exercises.Homework1.Exercise1 import Exercise1
from Exercises.Homework1.Exercise2 import Exercise2
from Exercises.Homework1.Exercise3 import Exercise3
from Exercises.Homework1.Exercise4 import Exercise4


class ExerciseBuilder:

    @staticmethod
    def StartExersice():
        correctEnter = False
        while not correctEnter:
            taskNum = int(input('Введите номер задачи: '))
            match taskNum:
                case 0:
                    os.system('cls')
                    return True
                case 1:
                    Exercise1.Start()
                case 2:
                    Exercise2.Start()
                case 3:
                    Exercise3.Start()
                case 4:
                    Exercise4.Start()
                case _:
                    print('Такой задачи нет. Повторите попытку.../n')
                    continue
            correctEnter = True
        return False
