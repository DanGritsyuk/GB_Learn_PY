from Exercises.Homework5.XOgame.Player import Player
from MenuRender import MenuRender


class User(Player):
    def __init__(self, playerId: int,  playerName: str, prefix: str, prefixMark: str):
        super().__init__(playerId,  playerName, prefix, prefixMark)

    def Check(self, boardData: list[list[int]]) -> int:
        toRender = User._GetRenderMap(boardData, self.prefixMark, ' ') if self.id == 1 else User._GetRenderMap(boardData, ' ', self.prefixMark)
        return MenuRender.StartRenderMenu(toRender, 0, 0, True, False, self.prefix, self.prefixMark)  

    @staticmethod
    def _GetRenderMap(boardData: list[list[int]], player1Mark: str, player2Mark: str):
        return {' ':
                [f'{player1Mark}{User._GetStatus(boardData, 0, 0)}{player2Mark}│ {User._GetStatus(boardData, 0, 1)} │ {User._GetStatus(boardData, 0, 2)} \n───┼───┼───',
                f'{player1Mark}{User._GetStatus(boardData, 1, 0)}{player2Mark}│ {User._GetStatus(boardData, 1, 1)} │ {User._GetStatus(boardData, 1, 2)} \n───┼───┼───',
                f'{player1Mark}{User._GetStatus(boardData, 2, 0)}{player2Mark}│ {User._GetStatus(boardData, 2, 1)} │ {User._GetStatus(boardData, 2, 2)} \n'],
                '  ':
                [f' {User._GetStatus(boardData, 0, 0)} │{player1Mark}{User._GetStatus(boardData, 0, 1)}{player2Mark}│ {User._GetStatus(boardData, 0, 2)} \n───┼───┼───',
                f' {User._GetStatus(boardData, 1, 0)} │{player1Mark}{User._GetStatus(boardData, 1, 1)}{player2Mark}│ {User._GetStatus(boardData, 1, 2)} \n───┼───┼───',
                f' {User._GetStatus(boardData, 2, 0)} │{player1Mark}{User._GetStatus(boardData, 2, 1)}{player2Mark}│ {User._GetStatus(boardData, 2, 2)} \n'],
                '   ':
                [f' {User._GetStatus(boardData, 0, 0)} │ {User._GetStatus(boardData, 0, 1)} │{player1Mark}{User._GetStatus(boardData, 0, 2)}{player2Mark}\n───┼───┼───',
                f' {User._GetStatus(boardData, 1, 0)} │ {User._GetStatus(boardData, 1, 1)} │{player1Mark}{User._GetStatus(boardData, 1, 2)}{player2Mark}\n───┼───┼───',
                f' {User._GetStatus(boardData, 2, 0)} │ {User._GetStatus(boardData, 2, 1)} │{player1Mark}{User._GetStatus(boardData, 2, 2)}{player2Mark}\n']}
    
    @staticmethod
    def _GetStatus(boardData: list[list[int]], row: int, col: int) -> str:
        if boardData[row][col] == 0:
            return ' '
        elif boardData[row][col] == 1:
            return 'X'
        elif boardData[row][col] == 2:
            return 'O'
        else:
            Exception('Board status compromise...')