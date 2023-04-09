# Задача 8. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
import os


class Exercise8:

    @staticmethod
    def Start():

        def ShiftElements(lstNums, shift):
            length = len(lstNums)
            for i in range(shift):
                x = lstNums[length-1]
                for i in range(length-1, -1, -1):
                    lstNums[i] = lstNums[i-1]
                lstNums[0] = x

        os.system('cls')
        print('решение 8 задачи\n')
        num = abs(int(input('Введите число N: ')))

        lstNums = []
        for i in range(-num, num+1):
            lstNums.append(i)

        print(ShiftElements(lstNums, 2))

        input("\nДля продолжения нажмите Enter...")
