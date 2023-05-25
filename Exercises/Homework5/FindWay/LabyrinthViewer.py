from collections import deque
from Exercises.Homework5.FindWay.LabyrinthModel import LabyrinthModel

class LabyrinthViewer:
    def __init__(self, labyrinth: LabyrinthModel, isFinishing: bool, path: list):
        self.labyrinth = labyrinth
        self.yCount = len(labyrinth.data)
        self.xCount = len(labyrinth.data[0])
        self.isFinishing = isFinishing
        self.path = path

    def DrawLabyrinth(self):
        for x, y in self.path:
            self.labyrinth.data[x][y] = 2
        if not self.isFinishing:
            lastPoint = self.path[len(self.path)-1]
            self.labyrinth.data[lastPoint[0]][lastPoint[1]] = 3
        self.labyrinth.data[0][0] = 4
        self.labyrinth.data[self.yCount - 1][self.xCount - 1] = 5
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
                    case 2:
                        printChar('• ')
                    case 3:
                        printChar('X ')
                    case 4:
                        printChar('Ⓢ ')
                    case 5:
                        printChar('Ⓕ ')
                    #case _ :
                        #raise Exception('Labirinth data is corrupt')
            print('┃')
        print('┗' + '━━' * self.xCount, end='┛\n')