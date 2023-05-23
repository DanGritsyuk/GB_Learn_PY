# Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. 
# Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.
import random
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise22(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        nums = list(random.randint(0, 9) for _ in range(15))
        print(f'Массив чисел: {nums}')
        num = int(input('Введите число N: '))
        strList = ''.join(str(n) for n in nums)
        
        if str(num) in strList:
            print('В массиве есть последовательность, совпадающая с введённым числом.')
        else:
            print('В массиве нет последовательности, совпадающей с введённым числом.')