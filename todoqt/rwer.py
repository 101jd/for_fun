import json.scanner
import marshal
from Task import Task
import json
import pickle

class ReadWriter():
    def write(self, tasks, path):
        
        with open(path, 'wb') as file:
            pickle.dump(tasks, file)
        
    def read(self, path):
        with open(path, 'rb') as file:
            return pickle.load(file)
