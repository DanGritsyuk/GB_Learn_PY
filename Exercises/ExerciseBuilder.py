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
#from Exercises.Homework4.Exercise15 import Exercise15
from Exercises.Homework5.Exercise16 import Exercise16
from Exercises.Homework5.Exercise17 import Exercise17
from Exercises.Homework5.Exercise18 import Exercise18
from Exercises.Homework5.Exercise19 import Exercise19
from Exercises.Homework5.Exercise20 import Exercise20
from Exercises.Homework6.Exercise21 import Exercise21
from Exercises.Homework6.Exercise22 import Exercise22
from Exercises.Homework6.Exercise23 import Exercise23
from Exercises.Homework7.Exercise24 import Exercise24
from Exercises.Homework7.Exercise25 import Exercise25

from Exercises.ExerciseAbstract import ExerciseAbstract
from Exercises.ExerciseData import ExerciseData


class ExerciseBuilder:
    @staticmethod
    def GetExersice(exerciseData: ExerciseData, taskNum: int) -> ExerciseAbstract:
        taskDataIndex = taskNum - 1
        taskText = exerciseData.GetTaskText(taskDataIndex)
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
                case 17:
                    return Exercise17(taskText)
                case 18:
                    return Exercise18(taskText)
                case 19:
                    return Exercise19(taskText)
                case 20:
                    return Exercise20(taskText)
                case 21:
                    return Exercise21(taskText)
                case 22:
                    return Exercise22(taskText)
                case 23:
                    return Exercise23(taskText)
                case 24:
                    return Exercise24(taskText)
                case 25:
                    return Exercise25(taskText)
                case _:
                    raise Exception('Такой задачи нет или она еще в разработке...')
                    
