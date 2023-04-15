# Задача 1. Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise9(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():        
        n = int(input("Введите число N: "))
        fibFirstSecond = 1            
        lstFib = [fibFirstSecond] * n
    
        for i in range(2, n):
            lstFib[i] = lstFib[i-2] + lstFib[i-1]
        
        print(lstFib)