from Task import Task
class TaskBuilder:
    __number = 0
    
    def __init__(self, number):
        self.__number = number
    
    def new_task(self, priority:int, description:str):
        task = Task(self.__number, priority, description)
        self.__number += 1
        return task
    
    def new_from_task(self, peretask:Task):
        return Task(peretask.get_number(), peretask.get_priority(), peretask.get_description())
        