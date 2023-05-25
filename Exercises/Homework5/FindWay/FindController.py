from collections import deque

class FindController:

    @staticmethod
    def GetWay(maze):
        xLast = len(maze)-1
        yLast = len(maze[0])-1
        queue = deque([(0, 0)])   # Очередь для хранения координат клеток
        visited = set([(0, 0)])   # Множество для хранения посещенных клеток
        findPath = {(0, 0): None} # Список координат всех вариантов пути
        while queue:
            x, y = queue.popleft()
            if x == xLast and y == yLast:
                return True, FindController._BuildPath(findPath, xLast, yLast)
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx > xLast or ny > yLast or maze[nx][ny] == 0 or (nx, ny) in visited:
                    continue
                queue.append((nx, ny))
                visited.add((nx, ny))
                findPath[(nx, ny)] = (x, y)
        return False, list(findPath)
    
    @staticmethod
    def _BuildPath(findPath: list, xLast: int, yLast: int) -> list:
        path = []
        curr = (xLast, yLast)
        while curr is not None:
            path.append(curr)
            curr = findPath[curr]        
        path.reverse()
        return path