from collections import deque
from Exercises.Homework5.FindWay.LabyrinthModel import LabyrinthModel
from Exercises.Homework5.FindWay.LabyrinthViewer import LabyrinthViewer


class FindController:

    @staticmethod
    def Start(x: int = 5, y: int = 5):
        labyrinth = LabyrinthModel(x, y)
        labyrinth = LabyrinthModel(x, y)
        isFinishing, path = FindController.bfs(labyrinth.data)
        viewer = LabyrinthViewer(labyrinth, isFinishing, path)
        viewer.DrawLabyrinth()

    @staticmethod
    def bfs(maze):
        queue = deque([(0, 0)])   # Очередь для хранения координат клеток
        visited = set([(0, 0)])   # Множество для хранения посещенных клеток
        findPath = {(0, 0): None} # Список координат всех вариантов пути
        while queue:
            x, y = queue.popleft()
            if x == 4 and y == 4:
                return True, FindController._BuildPath(findPath)
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx > 4 or ny > 4 or maze[nx][ny] == 0 or (nx, ny) in visited:
                    continue
                queue.append((nx, ny))
                visited.add((nx, ny))
                findPath[(nx, ny)] = (x, y)
        return False, list(findPath)
    
    @staticmethod
    def _BuildPath(findPath: list) -> list:
        path = []
        curr = (4, 4)
        while curr is not None:
            path.append(curr)
            curr = findPath[curr]        
        path.reverse()
        return path