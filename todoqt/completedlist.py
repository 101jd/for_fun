from Task import Task

class CompletedList:
    __completed:list
    def __init__(self, lst:list):
        self.__completed = lst
        

    def add_task(self, task:Task):
        self.__completed.append(task)
        
    def clear(self):
        self.__completed.clear()
        
    def get_list(self):
        return self.__completed