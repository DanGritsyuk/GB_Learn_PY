from Exercises.Homework5.XOgame.Player import Player
from Exercises.Homework5.XOgame.User import User
from Exercises.Homework5.XOgame.GameBot import GameBot
from ConsoleManager import ConsoleManager

class Gameplay:
    def __init__(self, isMultiplayer: bool, botIsFirst: bool = False):
        player1 = None
        player2 = None
        if isMultiplayer:
            player1 = User(1, "Игрок X", '>', 'A')
            player2 = User(2, "Игрок O", '<', 'B')
        else:
            if botIsFirst:
                player1 = GameBot(1, 'Компьютер', '>', 'A')
                player2 = User(2, "Игрок O", '<', 'B')
            else:
                player1 = User(1, "Игрок X", '>', 'A')
                player2 = GameBot(2, 'Компьютер', '<', 'B')        
        self.player1 = player1
        self.player2 = player2
        self.playerStep = 1
        self.winner = 0
        self.boardData = [[0,0,0],[0,0,0],[0,0,0]]
        self.CursorPosition = ConsoleManager.GetCursorCoordinate()
        
    def StartGame(self):
        self._DrawHeader()
        winLine = False
        gameOver = False
        while not gameOver:
            if self.playerStep == 1:
                winLine, gameOver = self._PlayerCheck(self.player1)
            else:
                winLine, gameOver = self._PlayerCheck(self.player2)
            if gameOver:
                self._EndGame(winLine)
            

    def _DrawHeader(self):
        print(f'{self.player1.name} против {self.player2.name}')
        self.CursorPosition = ConsoleManager.GetCursorCoordinate()
        print('\n')

    def _PlayerCheck(self, player: Player):
        winLine = []
        playerCheck = player.Check(self.boardData)
        gameOver = playerCheck == 0
        if gameOver: return winLine, gameOver
        isFieldFree = self._PlayerMove(player.id, playerCheck)
        if isFieldFree:
            winLine, isWinner = self._IsWinner(player.id)
            if isWinner:
                self.winner = player.id
                gameOver = True
            else:
                gameOver = self._isBoardFull()                    
                if player.id == 1:
                    self.playerStep = 2
                else:
                    self.playerStep = 1        
        return winLine, gameOver

    def _PlayerMove(self, playerId: int, fieldId: int) -> bool:
            i, j, isFieldFree = self._IsFieldFree(fieldId)
            if isFieldFree:
                self.boardData[i][j] = playerId
                self._ShowMessage('            ')
            else:
                self._ShowMessage('ПОЛЕ ЗАНЯТО!')
            return isFieldFree

    def _IsFieldFree(self, fieldId):
        for i in range(len(self.boardData)):
            for j in range(len(self.boardData[i])):
                if fieldId == 1:
                    return j, i, self.boardData[j][i] == 0
                else:
                    fieldId -= 1
    
    def _isBoardFull(self) -> bool:
        nullList = list(filter(lambda line: len(list(filter(lambda num: num == 0, line))) > 0, self.boardData))
        return len(nullList) == 0

    def _ShowMessage(self, message: str):        
        ConsoleManager.SetCursorPosition(self.CursorPosition)
        print(f'\n{message}')
    
    def _EndGame(self, winLine: list[int]):
        ConsoleManager.SetCursorPosition(self.CursorPosition)
        print('\nИГРА ЗАВЕРШЕНА:\n')
        boardRender = self._GetRenderMap(winLine)
        for line in boardRender:
            print(line)
        playerPrefix = 'игрок'
        message = f'{playerPrefix} победитель'
        if self.winner == 1:
            message = message.replace(playerPrefix, self.player1.name)
        elif self.winner == 2:
            message = message.replace(playerPrefix, self.player2.name)
        else:
            message = 'Победителя нет!'
        print(message)

    def _IsWinner(self, playerId: int):
        if (self.boardData[0][0] == playerId and self.boardData[0][1] == playerId and self.boardData[0][2] == playerId):
            return [1, 2, 3], True
        elif    (self.boardData[1][0] == playerId and self.boardData[1][1] == playerId and self.boardData[1][2] == playerId):
            return [4, 5, 6], True
        elif    (self.boardData[2][0] == playerId and self.boardData[2][1] == playerId and self.boardData[2][2] == playerId):
            return [7, 8, 9], True
        elif    (self.boardData[0][0] == playerId and self.boardData[1][0] == playerId and self.boardData[2][0] == playerId):
            return [1, 4, 7], True
        elif    (self.boardData[0][1] == playerId and self.boardData[1][1] == playerId and self.boardData[2][1] == playerId):
            return [2, 5, 8], True
        elif    (self.boardData[0][2] == playerId and self.boardData[1][2] == playerId and self.boardData[2][2] == playerId):
            return [3, 6, 9], True
        elif    (self.boardData[0][0] == playerId and self.boardData[1][1] == playerId and self.boardData[2][2] == playerId):
            return [1, 5, 9], True
        elif    (self.boardData[0][2] == playerId and self.boardData[1][1] == playerId and self.boardData[2][0] == playerId):
            return [3, 5, 7], True
        else:
            return [], False
        
    def _GetRenderMap(self, winLine: list[int]) -> list[str]:
        return  f' {self._GetStatus(winLine, 0, 0)} │ {self._GetStatus(winLine, 0, 1)} │ {self._GetStatus(winLine, 0, 2)} \n───┼───┼───', \
                f' {self._GetStatus(winLine, 1, 0)} │ {self._GetStatus(winLine, 1, 1)} │ {self._GetStatus(winLine, 1, 2)} \n───┼───┼───', \
                f' {self._GetStatus(winLine, 2, 0)} │ {self._GetStatus(winLine, 2, 1)} │ {self._GetStatus(winLine, 2, 2)} \n',

    def _GetStatus(self, winLine: list[int], row: int, col: int) -> str:
        txtStyleTag = ''
        tstStyleEnd = ''
        for index in winLine:
            i, j, _ = self._IsFieldFree(index)
            if i == col and j == row:
                txtStyleTag = '\033[1m'
                tstStyleEnd = '\033[0m'
                break
        if self.boardData[row][col] == 0:
            return ' '
        elif self.boardData[row][col] == 1:
            return f'{txtStyleTag}X{tstStyleEnd}'
        elif self.boardData[row][col] == 2:
            return f'{txtStyleTag}O{tstStyleEnd}'
        else:
            Exception('Board status compromise...')