# Задача 2. В списке находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise10(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        fruitsList = [
            'Абрикос', 'Авокадо', 'Айва', 'Аки', 'Алиберция','Алыча', 'Апельсин', 
            'Бакау', 'Балия', 'Банан', 'Виноград', 'Вишня','Гандария', 'Генипа', 'Груша', 'Яблоко'
        ]

        frChr = str(input('Введите букву:')).upper()

        noneFrits = True
        for frute in fruitsList:
            if frute[0] == frChr:
                print(frute, end=' ')
                noneFrits = False
        if noneFrits:
            print('не знаю таких фруктов :(')