import os
from abc import ABC, abstractmethod
from MenuRender import MenuRender


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
            print('==========================================')

        done = False
        while not done:
            DrawHeader()
            try:
                self.Body()
            except Exception as ex:
                DrawHeader()
                print(ex)
            done = self.End()

    def End(self) -> bool:
        print()
        answer = MenuRender.StartRenderMenu(
            {'Выберите следующий шаг:': ['Выход в главное меню.', 'Начать заново.']}
        )
        return answer == 1