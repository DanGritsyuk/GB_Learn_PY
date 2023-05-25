from collections import deque
from Exercises.ExerciseAbstract import ExerciseAbstract
from Exercises.Homework5.FindWay.FindController import FindController
from Exercises.Homework5.FindWay.LabyrinthViewer import LabyrinthViewer
from Exercises.Homework5.FindWay.LabyrinthModel import LabyrinthModel

class Exercise20(ExerciseAbstract):
    def __init__(self, description: str):
        super().__init__(description)

    @staticmethod
    def Body():
        labyrinth = LabyrinthModel(5, 5)
        isFinishing, path = FindController.GetWay(labyrinth.data)
        viewer = LabyrinthViewer(labyrinth, isFinishing, path)
        viewer.DrawLabyrinth()