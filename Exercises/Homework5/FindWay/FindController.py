from collections import deque
from Exercises.Homework5.FindWay.LabyrinthModel import LabyrinthModel
from Exercises.Homework5.FindWay.LabyrinthViewer import LabyrinthViewer


class FindController:

    @staticmethod
    def Start(x: int = 5, y: int = 5):
        labyrinth = LabyrinthModel(x, y)
        isFinishing, labyrinth.data = FindController.bfs(labyrinth.data)
        viewer = LabyrinthViewer(labyrinth, isFinishing)
        viewer.DrawLabyrinth()

    @staticmethod
    def bfs(maze):
        start = [0, 0]
        queue = deque([start])
        maze[0][0] = 2

        # проходим по очереди, пока она не пуста
        while queue:
            current = queue.popleft()
            x, y = current[0], current[1]
            # проверяем соседей
            if x > 0 and maze[x-1][y] == 1:
                queue.append([x-1, y])
                maze[x-1][y] = maze[x][y] + 1
            if x < len(maze)-1 and maze[x+1][y] == 1:
                queue.append([x+1, y])
                maze[x+1][y] = maze[x][y] + 1
            if y > 0 and maze[x][y-1] == 1:
                queue.append([x, y-1])
                maze[x][y-1] = maze[x][y] + 1
            if y < len(maze)-1 and maze[x][y+1] == 1:
                queue.append([x, y+1])
                maze[x][y+1] = maze[x][y] + 1

        # проверяем, достигнута ли точка [4, 4]
        return maze[4][4] > 1, queue
    
    @staticmethod
    def _BuildPath(maze, queue: deque) -> list[list[int]]:
        print()
