# Задача 1. Дано натуральное число N. Напишите метод, который вернёт список простых множителей числа N и количество этих множителей.
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise13(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        rangeShop = { 'Сливочное', 'Бурёнка', 'Вафелька', 'Сладкоежка' }
        inStock = { 'Сливочное', 'Вафелька', 'Сладкоежка' }

        print(rangeShop - inStock)