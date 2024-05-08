import re

class Todolist:
    def __init__(self):
        self.items = []
        self.task = dict()
        self.elem = dict()
        
    def is_empty(self):
        return self.items == []        
    
    def add(self, item, priority, i):
        self.task[f'({priority})'] = item
        self.elem[f'№{i}'] = self.task
        self.items.insert(0, self.elem)
        self.task = {}
        self.elem = {}
        
    
    def get_val_first(self):
        if not self.is_empty():
            print(str(self.items[len(self.items) - 1]).replace('{', '').replace('}', '').replace('\'', '')
                  .replace(':', ''))
        else: print("The todolist is empty")
    
    def get_val_last(self):
        if not self.is_empty():
            print(str(self.items[0]).replace('{', '').replace('}', '').replace('\'', '')
                  .replace(':', ''))
        else: print("The todolist is empty")
    
    def get_first(self):
        if not self.is_empty():
            print(str(self.items.pop()).replace('{', '').replace('}', '').replace('\'', '')
                  .replace(':', ''))
        else: print("The todolist is empty")
    
    def get_last(self):
        if not self.is_empty():
            print(str(self.items.pop(0)).replace('{', '').replace('}', '').replace('\'', '')
                  .replace(':', ''))
        else: print("The todolist is empty")
        
    def del_task(self, number):
        self.complete = ''
        self.lst = []
        for i in self.items:
            if f'dict_keys([\'№{number}\'])' == str(i.keys()):
                self.complete = str(i)
                continue
            self.lst.append(i)
            
        print(f'{self.complete.replace('{', '').replace('}', '').replace('\'', '').replace(':', '')} complete')
        self.items = self.lst

    def size(self):
        return len(self.items)
    
    def sort_by_number(self):
        if not self.is_empty():
            self.items = sorted(self.items, key=max, reverse=True)
    
    def sort_by_priority(self):
            self.lst = []
            for el in self.items:
                for key in el.values():
                    self.lst.append(key)
            self.result = sorted(self.lst, key=max, reverse=True)
            
            self.dic = dict()
            self.sortd = []
            for i in range(len(self.result)):
                for j in range(len(self.items)):
                    self.key_items = re.findall(r'\d', str(self.result[i].keys()))[0]
                    self.key_result = re.findall(r'\d+', str(self.items[j].items()))[1]
                    print(self.key_items)
                    if self.key_items == self.key_result and self.items[j] not in self.sortd:
                        self.sortd.append(self.items[j])
            self.items = self.sortd

    
    def print(self):
        if not self.is_empty():
            print(str(self.items).replace('{', '').replace('}', '').replace('\'', '')
                  .replace(':', ''))
        else: print("The todolist is empty")
        
    def clear(self):
        self.items.clear()
        
def menu():
    print('========\n\'A\' to add task\n\'F\' to show first task\n\'L\' to show last task')
    print('\'CF\' to complete first task\n\'CL\' to complete last task\n\'SN\' to sort tasks by number')
    print('\'SP\' to sort by priority\n\'N\' to get numer of tasks\n\'P\' to print todolist')
    print('\'C\' to clear todolist\n\'D\' to delete task by number\n\'Q\' to quit\n========')

todo = Todolist()
todo.__init__

flag_menu = True
menu()
i = 1
while flag_menu:
    inp = str.lower(input('Enter command (\'M\' to see menu): '))
    if inp == 'a':
        string = input('Enter a task: ')
        priority = int(input('Enter priority: '))
        todo.add(string, priority, i)
        i += 1
    elif inp == 'f':
        todo.get_val_first()
    elif inp == 'l':
        todo.get_val_last()
    elif inp == 'cf':
        todo.get_first()
    elif inp == 'cl':
        todo.get_last()
    elif inp == 'sn':
        todo.sort_by_number()
        todo.print()
    elif inp == 'sp':
        todo.sort_by_priority()      # !
        todo.print()
    elif inp == 'n':
        print(f'There is {todo.size()} tasks in list')
    elif inp == 'p':
        todo.print()
    elif inp == 'd':
        number = input('Enter the number of task: ')
        todo.del_task(number)
    elif inp == 'c':
        todo.clear()
        i = 1
    elif inp == 'q':
        flag_menu = False
    elif 'm':
        menu()