# Создайте игру в крестики-нолики.
from Exercises.Homework5.XOgame.Gameplay import Gameplay
from Exercises.ExerciseAbstract import ExerciseAbstract
from MenuRender import MenuRender


class Exercise19(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        isMultiplayer, botIsFirstCheck = Exercise19._MakeChoice()
        if isMultiplayer == None:
            print('ИГРА ОТМЕНЕНА')
        else:
            game = Gameplay(isMultiplayer, botIsFirstCheck)
            game.StartGame()

    @staticmethod
    def _MakeChoice() -> int:
        answer = MenuRender.StartRenderMenu(
            {
                'ИГРА КРЕСТИКИ НОЛИКИ\n':
                ['||| Игрок X против игрока O', '||| Игрок X против компьютера', '||| Компьютер против Игрока O', '||| ВЫХОД']
            },
            0,
            0,
            True,
            False,
            '➤ ',
            '|||'
        )
        match answer:
            case 0:
                return None, None 
            case 1:
                return True, False 
            case 2:
                return False, False 
            case 3:
                return False, True 
            case 4:
                return None, None