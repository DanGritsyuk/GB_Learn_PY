# Задача 3. Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.
import os
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise15(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        def GetPolynomialString(strPoly):
            if os.path.isabs(strPoly) and os.path.isfile(strPoly):
                return Exercise15._LoadFromFile(strPoly)
            else:
                return strPoly

        print('Напишите требуемый многочлен или укажите полный путь до файла, где он хранится.')
        polynomial1 = GetPolynomialString(input('Введите первый многочлен: '))
        polynomial2 = GetPolynomialString(input('Введите второй многочлен: '))
        
        coefficients, powers = Exercise15._ParsePolynomial(polynomial1)
        print(coefficients)
        print(powers)
        coefficients, powers = Exercise15._ParsePolynomial(polynomial2)
        print(coefficients)
        print(powers)

    @staticmethod
    def _LoadFromFile(filePath: str) -> str:
        with open(filePath, 'r', encoding='utf8') as txtFile:
            data = txtFile.read()
        return data
    
    @staticmethod
    def _ParsePolynomial(strPolynomial):
        print('In progres')