# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise8(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():

        def ShiftElements(lstNums, shift):
            length = len(lstNums)
            for i in range(shift):
                x = lstNums[length-1]
                for i in range(length-1, -1, -1):
                    lstNums[i] = lstNums[i-1]
                lstNums[0] = x
            return lstNums

        num = abs(int(input('Введите число N: ')))

        lstNums = []
        for i in range(-num, num+1):
            lstNums.append(i)

        print(ShiftElements(lstNums, 2))
