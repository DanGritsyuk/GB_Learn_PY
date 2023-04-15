import msvcrt

from Exercises.Homework1.Point2D import Point2D


class ConsoleManager:
    @staticmethod
    def GetCursorCoordinate() -> Point2D:
        print('\033[A\033[6n')
        buff = ''

        def DelWeedSymbols(line: str) -> str:
            first = 0
            if line[0] < '1' or line[0] > '9':
                first = 1
            for i, chr in enumerate(line):
                if chr == 'R':
                    return line[first:i]
            return line

        keep_going = True
        while keep_going:
            buff += msvcrt.getch().decode('ASCII')
            keep_going = msvcrt.kbhit()

        newbuff = DelWeedSymbols(buff.replace('\x1b[', ''))

        return Point2D(
            int(newbuff.partition(';')[2]),
            int(newbuff.partition(';')[0]),
        )

    @staticmethod
    def SetCursorPosition(toPosition: Point2D):
        correntPosition = ConsoleManager.GetCursorCoordinate()

        yDistance = correntPosition.y - toPosition.y
        if yDistance > 0:
            print('\033[A' * yDistance, end='')

        xDistance = correntPosition.x - toPosition.x
        if xDistance > 0:
            print('\033[D' * xDistance, end='')

    @staticmethod
    def GetKeyEvent() -> str:
        match msvcrt.getch():
            case b'\r':
                return 'enter'
            case b'\x00':
                key = msvcrt.getch()
                if key == b'H':
                    return 'up'
                elif key == b'P':
                    return 'down'
            case b'\x1b':
                return 'esc'
