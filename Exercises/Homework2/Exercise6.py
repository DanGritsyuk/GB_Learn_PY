# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
import os


class Exercise6:

    @staticmethod
    def Start():
        os.system('cls')
        print('решение 6 задачи\n')

        print('X | Y | Z | ¬(X ∧ Y) ∨ Z')
        for x in range(0, 2):
            for y in range(0, 2):
                for z in range(0, 2):
                    print(f'{x} | {y} | {z} | {int(not (x and y) or z)}')

        input("\nДля продолжения нажмите Enter...")
