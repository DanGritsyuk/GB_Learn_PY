from typing import List
from ConsoleManager import ConsoleManager
from Exercises.Homework1.Point2D import Point2D


class MenuRender:
    @staticmethod
    def StartRenderMenu(
        menuData: dict[str, list[str]],
        index: int = 0,
        showHelpControl: bool = False,
        isEscActive: bool = True,
    ) -> int:
        def StartDraw():
            MenuRender._DrawMenu(menuData, cursorStartPosition, index, showHelpControl)

        cursorStartPosition = ConsoleManager.GetCursorCoordinate()
        index = 0
        StartDraw()
        while True:
            key = ConsoleManager.GetKeyEvent()

            match key:
                case 'enter':
                    return index + 1
                case 'up':
                    if index > 0:
                        index -= 1
                case 'down':
                    if index < MenuRender._LineCount(menuData) - 1:
                        index += 1
                case 'esc':
                    if isEscActive:
                        return 0
            StartDraw()

    @staticmethod
    def _DrawMenu(
        menuData: dict[str, list[str]],
        cursorStartPosition: Point2D,
        selectedIndex: int,
        showHelpControl: bool,
    ):
        largestLine = MenuRender._LargesLineLength(menuData)
        ConsoleManager.SetCursorPosition(cursorStartPosition)
        blockIdCount = 0
        for key in menuData:
            if blockIdCount > 0:
                print()
            print(f'{key}')
            for i, line in enumerate(menuData[key]):
                i += blockIdCount
                isSelected = i == selectedIndex
                prefix = '>' if isSelected else ' '
                print(f'{prefix} {line}')
            blockIdCount += len(menuData[key])

        if showHelpControl:
            padding = '=' * (largestLine)
            print(
                f'{padding}\n↑ ↓ - перемещаться между строками. Enter - выбрать задачу. Для выхода нажмите Esc.'
            )
        print()

    @staticmethod
    def _LineCount(menuData: dict[str, list[str]]):
        count = 0
        for key in menuData:
            count += len(menuData[key])
        return count

    @staticmethod
    def _LargesLineLength(menuData: dict[str, list[str]]):
        largesLineLength = 0
        for key in menuData:
            maxLength = max([len(line) for line in menuData[key]])
            if largesLineLength < maxLength:
                largesLineLength = maxLength
        return largesLineLength
