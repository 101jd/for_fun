from Task import Task

class CompletedList:
    __completed:list
    def __init__(self):
        self.__completed = []
        

    def add_task(self, task:Task):
        self.__completed.append(task)
        
    def clear(self):
        self.__completed.clear()