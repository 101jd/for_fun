from Task import Task

class TodoLost:
    __todolist:list
    def __init__(self, lst=[]):
        self.__todolist = lst
        
    def add_task(self, task:Task):
        self.__todolist.append(task)

    def get_task(self, number:int):
        # item:Task
        # for item in self.__todolist:
        #     if item.get_number() == number+1:
        #         task:Task = item
        #         return task
        return self.__todolist[number]
                
    def complete_task(self, number:int):
        # item:Task
        # for item in self.__todolist:
        #     if item.get_number() == number:
        #         self.__todolist.remove(item)
        task = self.__todolist.pop(number)
        return task
        
    def get_todo_list(self):
        return self.__todolist
    
    def sort_by_num(self):
        return sorted(self.__todolist, key=lambda x : x.get_number())
    
    def sort_by_priority(self):
        return sorted(self.__todolist, key=lambda x : x.get_priority()) 
    
    def is_empty(self):
        return self.__todolist == []