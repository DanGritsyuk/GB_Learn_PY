from typing import List
from ConsoleManager import ConsoleManager
from Exercises.Homework1.Point2D import Point2D
from PageData import PageData


class MenuRender:
    @staticmethod
    def StartRenderMenu(
        menuData: dict[str, list[str]],
        index: int = 0,
        consoleLines: int = 0,
        isEscActive: bool = False,
        showHelpControl: bool = False,
        prefix: str = '> '
    ) -> int:
        HEADER_LINE_COUNT = 2
        largeKey = MenuRender._LargesKeyTasks(menuData) + HEADER_LINE_COUNT + 1
        consoleLines = largeKey if largeKey > consoleLines else consoleLines

        def StartDraw():
            MenuRender._DrawMenu(page, pageCount, cursorStartPosition, consoleLines, showHelpControl, prefix)
        def GetNextPage(_page: PageData, step: int) -> PageData:
            ConsoleManager.SetCursorPosition(cursorStartPosition)
            MenuRender._ClearConsoleText(MenuRender._GetLargesLineLength(_page.pageData) + len(prefix), consoleLines)
            currentIndex = _page.currentLineIndex
            _page = list(filter(lambda p: p.pageId == _page.pageId + step, pagesMap))[0]
            _page.currentLineIndex = currentIndex if currentIndex < _page.linesCount else _page.linesCount - 1
            return _page
        def GetCheckCoordinates() -> PageData:
            for page in pagesMap:
                if page.startLineIndex <= index < page.startLineIndex + page.linesCount :
                    page.currentLineIndex = index - page.startLineIndex
                    return page
            raise Exception('Page not found!')
        

        pagesMap = MenuRender._SplitDataToPages(menuData, consoleLines, HEADER_LINE_COUNT)
        page = GetCheckCoordinates()
        pageCount = len(pagesMap)

        cursorStartPosition = ConsoleManager.GetCursorCoordinate()
        ConsoleManager.HideCursor(True)
        StartDraw()
        while True:
            key = ConsoleManager.GetKeyEvent()
            match key:
                case 'enter':
                    ConsoleManager.HideCursor(False)
                    return page.currentLineIndex + page.startLineIndex + 1
                case 'up':
                    if page.currentLineIndex > 0:
                        page.currentLineIndex -= 1
                case 'down':
                    if page.currentLineIndex < MenuRender._LineCount(page.pageData) - 1:
                        page.currentLineIndex += 1
                case 'left':
                    if page.pageId > 1:
                        page = GetNextPage(page, -1)
                case 'rigth':
                    if page.pageId < pageCount:
                        page = GetNextPage(page, 1)
                case 'esc':
                    if isEscActive:
                        return 0
            StartDraw()

    @staticmethod
    def _SplitDataToPages(menuData: dict[str, list[str]], linesPage: int, headerLineCount: int) -> set():        
        pageLineCount = 0
        pageFirstIndex = 0
        pageId = 1
        pageData = dict()
        pagesMap = set()
        for i, key in enumerate(menuData):
            countLinesKeyTasks = len(menuData[key])
            if countLinesKeyTasks + headerLineCount + pageLineCount >= linesPage:
                page = PageData(pageId, pageFirstIndex, pageData)
                pagesMap.add(page)
                pageLineCount = 0
                pageId += 1
                pageFirstIndex += page.linesCount
                pageData.clear()
            pageLineCount += countLinesKeyTasks + 2
            pageData[key] = menuData[key]
            if i == len(menuData) - 1:
                pagesMap.add(PageData(pageId, pageFirstIndex, pageData))
        return pagesMap

    @staticmethod
    def _DrawMenu(
        page: PageData,
        pagesCount: int,
        cursorStartPosition: Point2D,
        linesCount: int,
        showHelpControl: bool,
        prefix: str
    ):
        ConsoleManager.SetCursorPosition(cursorStartPosition)
        blockIdCount = 0
        for key in page.pageData:
            if blockIdCount > 0:
                print()
            print(f'{key}')
            for i, line in enumerate(page.pageData[key]):
                i += blockIdCount
                isSelected = i == page.currentLineIndex
                prToConsole = prefix if isSelected else str(' ' * len(prefix))
                print(f'{prToConsole}{line}')
            blockIdCount += len(page.pageData[key])
        if showHelpControl:
            strPageNumbers = ''
            if pagesCount > 1 :
                strPageNumbers = ('▪' * pagesCount)
                strPageId = str(page.pageId)
                for i in range(len(strPageId)):
                    strPageNumbers = strPageNumbers[:page.pageId - 1 + i] + strPageId[i] + strPageNumbers[page.pageId + i:]
            indent = ' ' * 50
            if pagesCount > 2:
                if page.pageId > 1:
                    strPageNumbers = '← ' + strPageNumbers
                else:
                    strPageNumbers = '  ' + strPageNumbers
                if page.pageId < pagesCount:
                    strPageNumbers = strPageNumbers + ' →'
            print('\n' * int(linesCount - page.linesCount - len(page.pageData) * 2), end=f'{indent}{strPageNumbers}\n')
            
            padding = '=' * int(MenuRender._GetLargesLineLength(page.pageData))
            pagesSwitchInfo = '← → - переключать страницы. ' if pagesCount > 1 else ''
            print(f'{padding}\n↑ ↓ - перемещаться между строками. {pagesSwitchInfo}Enter - выбрать задачу. Для выхода нажмите Esc.')
        print()

    @staticmethod
    def _LineCount(menuData: dict[str, list[str]]):
        count = 0
        for key in menuData:
            count += len(menuData[key])
        return count

    @staticmethod
    def _GetLargesLineLength(menuData: dict[str, list[str]]):
        largesLineLength = 0
        for key in menuData:
            maxLength = max([len(line) for line in menuData[key]])
            if largesLineLength < maxLength:
                largesLineLength = maxLength
        return largesLineLength
    
    @staticmethod
    def _LargesKeyTasks(menuData: dict[str, list[str]]) -> int:        
        largesKeyTasks = 0
        for key in menuData:
            lengthKeyTasks = len(menuData[key])
            largesKeyTasks = lengthKeyTasks if lengthKeyTasks > largesKeyTasks else largesKeyTasks
        return largesKeyTasks

    @staticmethod
    def _ClearConsoleText(charsCount: int, linesCount: int):        
        for _ in range(linesCount): print(' ' * charsCount)
