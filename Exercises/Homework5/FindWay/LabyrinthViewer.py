from collections import deque
from Exercises.Homework5.FindWay.LabyrinthModel import LabyrinthModel

class LabyrinthViewer:
    def __init__(self, labyrinth: LabyrinthModel, isFinishing: bool, path: deque):
        self.labyrinth = labyrinth
        self.yCount = len(labyrinth.data)
        self.xCount = len(labyrinth.data[0])
        self.isFinishing = isFinishing
        self.path = path

    def DrawLabyrinth(self):
        self.labyrinth.data[0][0] = -1
        self.labyrinth.data[self.xCount][0] = -2
        print('┏' + '━━' * self.xCount, end='┓\n')
        for i in range(self.yCount):
            printChar = lambda str: print(str, end='')
            printChar('┃')
            for j in range(self.xCount):
                match self.labyrinth.data[i][j]:
                    case 0:
                        printChar('██')
                    case 1:
                        printChar('  ')
                    case -1:
                        printChar('Ⓢ ')
                    case -2:
                        printChar('Ⓕ ')
                    #case _ :
                        #raise Exception('Labirinth data is corrupt')
            print('┃')
        print('┗' + '━━' * self.xCount, end='┛\n')