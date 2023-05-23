from collections import deque
from Exercises.ExerciseAbstract import ExerciseAbstract
from Exercises.Homework5.FindWay.FindController import FindController

class Exercise20(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        FindController.Start()