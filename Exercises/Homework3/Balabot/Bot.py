import json
import random

class Bot:
    def __init__(self):
        self.name = 'Бот'
        self.varsion = 'pre-alpha 0.0000'
        # try:
        self.themes = self._LoadFromFile()
        # except:
        #     self._GenerateThemes()

        self.endPhrases = {'EndPhrases': 
                            [
                                'доскорого',
                                'пока',
                                'досвидания',
                                'всегохорошего',
                                'ещеувидимся',
                                'наэтомвсе',
                            ], 
                            'answers': 
                            [
                                'Всего наилучшего',
                                'Пока',
                                'Всего хорошего',
                                'Еще спишемся',
                                'Как скажешь',
                                'Иницирую отключение...',
                            ]}
        self.isSaidBuy = False
        self.onReadMode = False

    def ReadMessage(self, message: str) -> str:
        if message == 'как твое имя' or message == 'как тебя зовут':
            return f'Мое имя: {self.name}. Не очень креативное, т.к. я все еще {self.varsion} версии.'
        for key in self.themes:
            if message == key:
                i = random.randint(0, len(self.themes[key])-1)
                return self.themes[key][i]
        for phrase in self.endPhrases['EndPhrases']:
            if message == phrase:
                self.isSaidBuy = True
                return self.endPhrases['answers'][random.randint(0, len(self.endPhrases['answers']) - 1)]
        self.onReadMode = True
        self.themes[message] = []
        return 'Я не знаю ответа. Подскажите мне?'
    
    def SetToMemory(self, key: str, value: str) -> str:
        self.themes[key].append(value)
        self.onReadMode = False
        self._SaveToFile()
        return 'Я запомнил. Спасибо!'
        
    def _GenerateThemes(self):
        self.themes = {
            'привет':
            [
                'Привет! Рад пообщаться!', 'Здравствуйте! Чем могу быть полезен?'
            ],
            'какдела':
            [
                'Хорошо!', 'Сижу без дела...', 'Идут не спешно.'
            ]
        }
        self._SaveToFile()

    def _SaveToFile(self):
        with open('Exercises/Homework3/Balabot/botMemory.json', 'w', encoding='utf8') as botMemory:
            json.dump(self.themes, botMemory, ensure_ascii=False)

    def _LoadFromFile(self) -> str:
        with open('Exercises/Homework3/Balabot/botMemory.json', 'r', encoding='utf8') as botMemory:
            data = json.load(botMemory)
        return data
