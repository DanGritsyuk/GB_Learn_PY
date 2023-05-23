# Задача 2. Создайте декоратор, повторяющий функцию заданное количество раз.
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise25(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        name = input('Введите имя: ')
        Exercise25.PrintHello(name)

    def Repeat(numRepeats):
        def Decorator(func):
            def Wrapper(*args):
                for i in range(numRepeats):
                    func(*args)
            return Wrapper
        return Decorator
    
    @Repeat(4)
    def PrintHello(name):
        print(f"Привет, {name}!")