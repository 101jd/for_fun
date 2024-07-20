class Task:
    __number:int
    __priority:int
    __description:str
    
    def __init__(self, number:int, priority:int, description:str):
        self.__number = number
        self.__priority = priority
        self.__description = description
        
        
    def get_number(self):
        return self.__number
    
    def get_priority(self):
        return self.__priority
    
    def get_description(self):
        return self.__description
        
    def edit(self, priority:int, description:str):
        self.__priority = priority
        self.__description = description
        
    def to_string(self):
        return f'# {self.__number} prior: {self.__priority} = {self.__description}'
    
    def get_number(self):
        return self.__number