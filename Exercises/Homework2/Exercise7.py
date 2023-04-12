# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
from Exercises.ExerciseAbstract import ExerciseAbstract


class Exercise7(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():

        def DeleteDoubleChars(strLine):
            chars = []
            length = len(strLine)

            for i in range(length):
                isOne = True
                for chr in chars:
                    if strLine[i] == chr:
                        isOne = False
                if isOne:
                    chars.append(strLine[i])

            return ''.join(chars)

        def GetCharsCount(_substring, _phrase):
            length_substring = len(_substring)
            length_phrase = len(_phrase)
            chrsCount = []

            for chrPhrase in _phrase:
                count = 0
                for chrSubstring in _substring:
                    if chrPhrase == chrSubstring:
                        count += 1
                chrsCount.append(count)
            return chrsCount

        substring = input('Введите строку: ')
        phrase = DeleteDoubleChars(input('Введите фразу: '))
        phraseLength = len(phrase)

        countList = GetCharsCount(substring, phrase)

        for i in range(phraseLength):
            print(f'{phrase[i]} – {countList[i]}')
