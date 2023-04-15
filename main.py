import os

from Exercises.ExerciseBuilder import ExerciseBuilder
from Exercises.ExerciseData import ExerciseData
from MenuRender import MenuRender

done = False
while not done:
    os.system('cls')
    taskId = MenuRender.StartRenderMenu(ExerciseData().Descriptions, True)

    exercise = ExerciseBuilder.GetExersice(taskId)
    if exercise != None:
        exercise.Start()
    else:
        done = True

os.system('cls')
print('Программа закрыта.')