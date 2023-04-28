from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, playerId: int,  playerName: str, prefix: str, prefixMark: str):
        self.id = playerId
        self.name = playerName
        self.lastCheck = 0
        self.prefix = prefix
        self.prefixMark = prefixMark

    @abstractmethod
    def Check(self, boardData: list[list[int]]) -> int:
        pass

