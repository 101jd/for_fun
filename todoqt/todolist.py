from Task import Task

class TodoLost:
    __todolist:list
    __last_number:int
    
    def size(self):
        return len(self.__todolist)
    
    def __init__(self, lst=[]):
        self.__todolist = lst
        
    def add_task(self, task:Task):
        self.__todolist.append(task)
        self.__last_number = task.get_number()

    def get_task(self, number:int):
        return self.__todolist[number]
                
    def complete_task(self, number:int):
        task = self.__todolist.pop(number)
        return task
        
    def get_todo_list(self):
        return self.__todolist
    
    def sort_by_num(self):
        self.__todolist = sorted(self.__todolist, key=lambda x : x.get_number())
        return self.__todolist
    
    def sort_by_priority(self):
        self.__todolist = sorted(self.__todolist, key=lambda x : x.get_priority())
        return self.__todolist
    
    def is_empty(self):
        return self.__todolist == []
    
    def get_last_number(self):
        if not self.is_empty():
            self.sort_by_num()
            return self.__todolist[len(self.__todolist) - 1].get_number()
        else: return 0
    