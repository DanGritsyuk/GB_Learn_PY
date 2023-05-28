# Задача 2. Создайте двумерный массив, размером 5х5. Определите, есть ли в нём одинаковые строки.

import numpy as np
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise27(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        size = (5, 5)
        numbers = np.random.randint(0, 2, size)
        print(numbers, end='\n\n')

        equalCount = 0
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if np.array_equal(numbers[i], numbers[j]):
                    print(f'Найдены одинаковые строки: {numbers[i]}')
                    equalCount += 1
                    break
        
        if equalCount == 0:
            print('Нет одинаковых строк.')