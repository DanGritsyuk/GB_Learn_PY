# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
import os


class Exercise7:

    @staticmethod
    def Start():

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

        os.system('cls')
        print('решение 7 задачи\n')
        substring = input('Введите строку: ')
        phrase = DeleteDoubleChars(input('Введите фразу: '))
        phraseLength = len(phrase)

        countList = GetCharsCount(substring, phrase)

        for i in range(phraseLength):
            print(f'{phrase[i]} – {countList[i]}')

        input("\nДля продолжения нажмите Enter...")
