from Task import Task
class TaskBuilder:
    __number = 0
    
    def __init__(self, number):
        self.__number = number
    
    def new_task(self, priority:int, description:str):
        task = Task(self.__number, priority, description)
        self.__number += 1
        return task
    
        