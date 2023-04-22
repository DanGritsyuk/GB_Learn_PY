from Exercises.Homework1.Exercise1 import Exercise1
from Exercises.Homework1.Exercise2 import Exercise2
from Exercises.Homework1.Exercise3 import Exercise3
from Exercises.Homework1.Exercise4 import Exercise4
from Exercises.Homework2.Exercise5 import Exercise5
from Exercises.Homework2.Exercise6 import Exercise6
from Exercises.Homework2.Exercise7 import Exercise7
from Exercises.Homework2.Exercise8 import Exercise8
from Exercises.Homework3.Exercise9 import Exercise9
from Exercises.Homework3.Exercise10 import Exercise10
from Exercises.Homework3.Exercise11 import Exercise11
from Exercises.Homework4.Exercise12 import Exercise12
from Exercises.Homework4.Exercise13 import Exercise13
from Exercises.Homework4.Exercise14 import Exercise14
from Exercises.Homework5.Exercise16 import Exercise16

from Exercises.ExerciseAbstract import ExerciseAbstract
from Exercises.ExerciseData import ExerciseData


class ExerciseBuilder:
    @staticmethod
    def GetExersice(taskNum) -> ExerciseAbstract:
        taskDataIndex = taskNum - 1
        taskText = ExerciseData().GetTaskText(taskDataIndex)
        correctEnter = False
        while not correctEnter:
            match taskNum:
                case 0:
                    return None
                case 1:
                    return Exercise1(taskText)
                case 2:
                    return Exercise2(taskText)
                case 3:
                    return Exercise3(taskText)
                case 4:
                    return Exercise4(taskText)
                case 5:
                    return Exercise5(taskText)
                case 6:
                    return Exercise6(taskText)
                case 7:
                    return Exercise7(taskText)
                case 7:
                    return Exercise7(taskText)
                case 8:
                    return Exercise8(taskText)
                case 9:
                    return Exercise9(taskText)
                case 10:
                    return Exercise10(taskText)
                case 11:
                    return Exercise11(taskText)
                case 12:
                    return Exercise12(taskText)
                case 13:
                    return Exercise13(taskText)
                case 14:
                    return Exercise14(taskText)
                case 16:
                    return Exercise16(taskText)
                case _:
                    print("Такой задачи нет. Повторите попытку...\n")
                    break
