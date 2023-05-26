# Задача 3. Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.
import os

from ConsoleManager import ConsoleManager
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise15(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        print('Напишите требуемый многочлен или укажите полный путь до файла, где он хранится.')
        polynomial1 = Exercise15._GetPolynomialString('Введите первый многочлен: ')
        polynomial2 = Exercise15._GetPolynomialString('Введите второй многочлен: ')        
        polynomial1 = Exercise15._ParsePolynomial(polynomial1)
        polynomial2 = Exercise15._ParsePolynomial(polynomial2)

        polynomial1 = Exercise15._SimplifyExpression(polynomial1)
        polynomial2 = Exercise15._SimplifyExpression(polynomial2)

        polyResoult = Exercise15._SumPolynomial(polynomial1, polynomial2)
        print('\nРезультат:', end=' ')
        print(Exercise15._StringPolynomial(polyResoult))

    @staticmethod
    def _LoadFromFile(filePath: str) -> str:
        with open(filePath, 'r', encoding='utf8') as txtFile:
            data = txtFile.read()
        return data
    
    @staticmethod
    def _ParsePolynomial(strPolynomial: str):
        expression = strPolynomial.replace(' ', '').replace('-', '+-')
        if '+x' in expression:
            expression = expression.replace('+x', '+1x')
        elif '-x' in expression:
            expression = expression.replace('-x', '-1x')
        expression = Exercise15._DelFirstPlus(expression)
        expression = expression.split('+')
        expressionCount = range(len(expression))
        for i in expressionCount:
            if not 'x^' in expression[i]:
                if 'x' in expression[i]:
                    expression[i] = expression[i].replace('x', 'x^1')
                else:
                    expression[i] = expression[i] + 'x^0'
        expression = [[int(i) for i in sublist] for sublist in [i.split('x^') for i in expression]]
        return expression
        
    @staticmethod
    def _GetPolynomialString(strMessage):
        point = ConsoleManager.GetCursorCoordinate()
        strPoly = input(strMessage).replace('"', '')
        if os.path.isabs(strPoly) and os.path.isfile(strPoly):
            ConsoleManager.SetCursorPosition(point)
            strPolyLenght = len(strPoly)
            clearInput = ' ' * strPolyLenght
            backspace = '\b' * strPolyLenght                
            strPoly = Exercise15._LoadFromFile(strPoly)
            print(strMessage + clearInput + backspace + strPoly)
            return strPoly
        else:
            return strPoly

    @staticmethod
    def _SimplifyExpression(expressionArray: list[list[int]]) -> dict[int, int]:            
        expression = dict(map(lambda x: (x[1], int(0)), expressionArray))
        for item in expressionArray:
            expression[item[1]] += item[0]
        return expression
    
    @staticmethod
    def _SumPolynomial(expression1: dict[int, int], expression2: dict[int, int]) -> dict[int, int]:
        def AddNonePower(expression: dict[int, int], i: int):
            if not i in expression:
                expression[i] = 0
        maxPower = max([max(expression1), max(expression2)])
        expressionRes = dict()
        for i in range(maxPower+1):
            AddNonePower(expression1, i)
            AddNonePower(expression2, i)
            if expression1[i] != 0 or expression2[i] != 0:
                expressionRes[i] = expression1[i] + expression2[i]
        return expressionRes
    
    @staticmethod
    def _StringPolynomial(expression1: dict[int, int]) -> str:
        strExpression = ''
        for key, value in expression1.items():
            if key == 0:
                char = ''
                if value > 0:
                    char = '+'
                else:
                    char = '-'
                strExpression = char + str(value) + strExpression
            elif key == 1:
                if value == 1:
                    strExpression = '+x' + strExpression
                elif value == -1:
                    strExpression = '-x' + strExpression
                elif value > 0:
                    strExpression = '+' + str(value) + 'x' + strExpression
                else:
                    strExpression = str(value) + 'x' + strExpression
            else:
                if value == 1:
                    strExpression = '+x^' + str(key) + strExpression
                elif value == -1:
                    strExpression = '-x^' + str(key) + strExpression
                elif value > 0:
                    strExpression = '+' + str(value) + 'x^' + str(key) + strExpression
                else:
                    strExpression = str(value) + 'x^' + str(key) + strExpression
        strExpression = Exercise15._DelFirstPlus(strExpression).replace('-', ' - ').replace('+', ' + ')
        return strExpression

    @staticmethod
    def _DelFirstPlus(expression: str) -> str:
        if expression[0] == '+':
            return expression[1:]
        return expression