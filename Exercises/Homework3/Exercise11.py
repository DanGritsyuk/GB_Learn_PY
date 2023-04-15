# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. 
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.
import os
import re
from Exercises.ExerciseAbstract import ExerciseAbstract
from Exercises.Homework3.Balabot.Bot import Bot


class Exercise11(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        bot = Bot()
        print('БОТ ЗАПУЩЕН\n')
        onDialog = True
        while onDialog:
            question = Exercise11._GetCleanText(input(' |> ').lower())
            answer = bot.ReadMessage(question)
            print(f'\n — {answer}\n')
            onDialog = not bot.isSaidBuy
            if bot.onReadMode:
                answer = bot.SetToMemory(question, input(' |> '))
                print(f'\n — {answer}\n')
        input('Бот вышел из чата. Нажми Enter...')
        os.system('cls')
        

    @staticmethod
    def _GetCleanText(word: str) -> str:
        word = re.sub('[^a-zа-яё-]', '', word, flags=re.IGNORECASE)
        word = word.strip('-')
        return word
