import json.scanner
import marshal
from Task import Task
import json
import pickle

class ReadWriter():
    
    lst:list
    
    def __init__(self) -> None:
        self.lst = []
    
    def write(self, tasks, completed, path):
        self.lst.append(tasks)
        self.lst.append(completed)
        with open(path, 'wb') as file:
            pickle.dump(self.lst, file)
        
    def read(self, path):
        with open(path, 'rb') as file:
            return pickle.load(file)
