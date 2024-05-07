class Todolist:
    def __init__(self):
        self.items = []
        self.task = dict()
        
    def is_empty(self):
        return self.items == []        
    
    def add(self, item, priority):
        self.task[priority] = item
        self.items.insert(0, self.task)
        self.task = {}
    
    def get_val_first(self):
        if not self.is_empty():
            print(self.items[len(self.items) - 1])
        else: print("The todolist is empty")
    
    def get_val_last(self):
        if not self.is_empty():
            print(self.items[0])
        else: print("The todolist is empty")
    
    def get_first(self):
        if not self.is_empty():
            print(self.items.pop())
        else: print("The todolist is empty")
    
    def get_last(self):
        if not self.is_empty():
            print(self.items.pop(0))
        else: print("The todolist is empty")

    
    def size(self):
        return len(self.items)
    
    def sort_by_priority(self):
        if not self.is_empty():
            self.items = sorted(self.items, key=max, reverse=True)
                
    def print(self):
        if not self.is_empty():
            print(self.items)
        else: print("The todolist is empty")
        
    def clear(self):
        self.items.clear()
        
def menu():
    print('========\n\'A\' to add task\n\'F\' to show first task\n\'L\' to show last task\n\'CF\' to complete first task\n\'CL\' to complete last task\n\'S\' to sort tasks by priority\n\'N\' to get numer of tasks\n\'P\' to print todolist\n\'C\' to clear todolist\n\'Q\' to quit\n========')


todo = Todolist()
todo.__init__

flag_menu = True
menu()
while flag_menu:
    inp = str.lower(input('Enter command (\'M\' to see menu): '))
    if inp == 'a':
        string = input('введите задачу: ')
        priority = int(input('Введите приоритет: '))
        todo.add(string, priority)
    elif inp == 'f':
        todo.get_val_first()
    elif inp == 'l':
        todo.get_val_last()
    elif inp == 'cf':
        todo.get_first()
    elif inp == 'cl':
        todo.get_last()
    elif inp == 's':
        todo.sort_by_priority()
        todo.print()
    elif inp == 'n':
        print(f'There is {todo.size()} tasks in list')
    elif inp == 'p':
        todo.print()
    elif inp == 'c':
        todo.clear()
    elif inp == 'q':
        flag_menu = False
    elif 'm':
        menu()