import os
from ConsoleManager import ConsoleManager

from Exercises.ExerciseBuilder import ExerciseBuilder
from Exercises.ExerciseData import ExerciseData
from MenuRender import MenuRender

CONST_MENU_COUNT = 30
exerciseData = ExerciseData()
taskId = 1
appIsRun = True
while appIsRun:
    os.system('cls')
    taskId = MenuRender.StartRenderMenu(
        exerciseData.Descriptions, taskId - 1, CONST_MENU_COUNT, True, True
    )
    try:
        exercise = ExerciseBuilder.GetExersice(exerciseData, taskId)
        if exercise != None:
            exercise.Start()
        else:
            appIsRun = False
    except Exception as ex:
        print(ex)
        ConsoleManager.GetKeyEvent()

os.system('cls')
print('Программа закрыта.')