# Задача 1. Создайте пользовательский аналог метода map().
import random
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise24(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        nums = list(random.randint(0, 9) for _ in range(15))
        print(f'Массив чисел: {nums}')
        num = int(input('Введите число N: '))
        done = list(Exercise24.OurMap(lambda x: x + num, nums))
        print(f'При помощи собственной функции map, к значениям списка прибавляем {num} и получаем:')
        print(done)
        
    @staticmethod
    def OurMap(func, lstArray):
        for key in lstArray:
            yield func(key)