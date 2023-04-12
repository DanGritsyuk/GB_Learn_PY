import os
from abc import ABC, abstractmethod

class ExerciseAbstract(ABC):
    def __init__(self, description: str):
        self._description = description

    @abstractmethod
    def Body(self):
        pass

    def Start(self):
        def DrawHeader():
            os.system('cls')
            print(self._description)
            print("==========================================")

        done = False
        while not done:
            DrawHeader()  
            try:
                self.Body()
            except:
                DrawHeader()                
                print('\nОшибка выполнения...')
            done = self.End()

    def End(self):
        print()
        print("Вернуться в главное меню?")
        
        flag = True
        while flag:
            answer = str(input("Введите (y/n): "))
            if answer.lower() == 'y':
                return True
            elif answer.lower() == 'n' :
                flag = False
            else:
                print("Ошибка ввода данных. Повторите попытку...")