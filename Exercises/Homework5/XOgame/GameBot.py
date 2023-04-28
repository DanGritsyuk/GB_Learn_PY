import random
from Exercises.Homework5.XOgame.Player import Player


class GameBot(Player):
    def __init__(self, playerId: int,  playerName: str, prefix: str, prefixMark: str):
        super().__init__(playerId,  playerName, prefix, prefixMark)

    def Check(self, boardData: list[list[int]]) -> int:
        boardLine = GameBot._CollectBoardDataToLine(boardData)
        possibleMoves = [x for x, letter in enumerate(boardLine) if letter == 0]
        move = 0

        queueCheck =[]
        if self.id == 1:
            queueCheck = [1, 2]
        else:
            queueCheck = [2, 1]
        for let in queueCheck:
            for i in possibleMoves:
                boardCopy = boardLine[:]
                boardCopy[i] = let
                if GameBot._isWin(boardCopy, let):
                    move = i + 1
                    return move

        corners_open = []
        for i in possibleMoves:
            if i in [1, 3, 7, 9]:
                corners_open.append(i)

        if len(corners_open) > 0:
            move = GameBot.SelectRandom(corners_open)
            return move + 1

        if 5 in possibleMoves:
            move = 6
            return move

        edges_open = []
        for i in possibleMoves:
            if i in [2, 4, 6, 8]:
                edges_open.append(i)

        if len(edges_open) > 0:
            move = GameBot.SelectRandom(edges_open)

        return move + 1
    
    @staticmethod
    def _CollectBoardDataToLine(boardData: list[list[int]]) -> list[int]:
        boardLine = []
        for i in range(len(boardData)):
            for j in range(len(boardData[i])):
                boardLine.append(boardData[j][i])
        return boardLine
    
    @staticmethod
    def SelectRandom(li):
        ln = len(li)
        r = random.randrange(0, ln)
        return li[r]
    
    @staticmethod
    def _isWin(board, letter):
        return (board[0] == letter and board[1] == letter and board[2] == letter) or \
            (board[3] == letter and board[4] == letter and board[5] == letter) or \
            (board[6] == letter and board[7] == letter and board[8] == letter) or \
            (board[0] == letter and board[3] == letter and board[6] == letter) or \
            (board[1] == letter and board[4] == letter and board[7] == letter) or \
            (board[2] == letter and board[5] == letter and board[8] == letter) or \
            (board[0] == letter and board[4] == letter and board[8] == letter) or \
            (board[2] == letter and board[4] == letter and board[6] == letter)
