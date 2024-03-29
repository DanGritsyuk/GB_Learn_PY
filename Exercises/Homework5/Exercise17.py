# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
import random
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise17(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        nums = [random.randint(1, 9) for i in range(10)]

        for i in range(len(nums)):
            print(f'{nums[i:]} -> {Exercise17._GetUpsList(nums[i:])}\n')
    
    @staticmethod
    def _GetUpsList(nums):
        upsList = [nums[0]]
        for i in nums:
            if i > max(upsList):
                upsList.append(i)
        return upsList