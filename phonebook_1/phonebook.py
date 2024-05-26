import json
import os

class PhoneBook:
    def __init__(self) -> None:
        self.book = []
        self.lst = []
        self.rec = {}
        try:
            self.config = open('config.txt', 'a+')
        finally:
            self.config.close()
        self.load()
        
    def add_rec(self, record:str, i):
        self.lst = record.split(';')
        self.rec['#'] = i
        self.rec['Name'] = self.lst[0]
        self.rec['Number'] = str(self.lst[1])
        if len(self.lst) > 2:
            self.rec['Address'] = self.lst[2]
        else:
            self.rec['Address'] = "-"
        
        self.book.append(self.rec)
        self.rec = {}
    def print(self):
        for el in self.book:
            print('\n'.join(str(el).split('},')).replace('{', '').replace('[', '').replace('}', '').replace(']', '').replace('\'', ''))
            
    def sort_by(self, skey:str):
        self.book = sorted(self.book, key=lambda x: x[skey] if isinstance(x, dict) and skey in x else "")
        
    def search(self, substring:str):
        check = False
        strings = []
        for el in self.book:
            if substring.lower() in str(el).lower():
                check = True
                strings.append(el)
        if check:
            print('\n'.join(str(strings).split(',')).replace('{', '').replace('[', '').replace('}', '').replace(']', '').replace('\'', ''))
        else:
            print(f'There is no entries with {substring}')
            
    def edit(self, num:int, key:str, val:str):
        self.test = []
        for el in self.book:
            if el != "":
                self.test.append(json.loads(el.replace("'", '"')))
        self.book = self.test
        for el in self.book:
            print(type(el), el)
        for el in self.book:
            if num in el.values():
                el[key] = val
                print(el)
        with open('book.txt', 'w') as file:
            for el in self.book:
                file.write(f'{str(el)}%')
                
    def delete(self, num):
        if len(self.book) > 1:
            self.test = []
            for el in self.book:
                el = str(el)
                if el != "":
                    self.test.append(json.loads(el.replace("'", '"')))
            self.book = self.test
            self.temp = []
            for el in self.book:
                if num in el.values():
                    continue
                self.temp.append(el)
            self.book = self.temp
        else:
            self.book = []
        with open('book.txt', 'w') as file:
            for el in self.book:
                file.write(f'{str(el)}%')
        
    def save(self):
        with open('book.txt', 'r') as file:
            self.saved = str(file.readlines()).replace('"', '').replace('[', '').replace(']', '').split('%')
        with open('book.txt', 'a+') as file:
            self.saved.pop()
            print('check\n', self.saved)
            print('book\n', self.book)
            for el in self.book:
                if str(el) not in self.saved:
                    file.write(f'{str(el)}%')
        with open('book.txt', 'r') as file:
            self.saved = str(file.readlines()).replace('"', '').replace('[', '').replace(']', '').split('%')
                
    def load(self):
        if not os.path.exists('book.txt'):
            try:
                file = open('book.txt', 'w')
                self.book = []
            finally:
                file.close()
        else:
            with open('book.txt', 'r') as file:
                self.book = str(file.readlines()).replace('"', '').replace('[', '').replace(']', '').split('%')
                self.book.pop()
                for el in self.book:
                    if el != "":
                        el = json.loads(el.replace("'", '"'))
            self.test = []
            for el in self.book:
                if el != "":
                    self.test.append(json.loads(el.replace("'", '"')))
            self.book = self.test
                        
    def is_changes(self):
        with open('book.txt', 'r') as file:
            self.check = str(file.readlines()).replace('"', '').replace('[', '').replace(']', '').split('%')
            self.check.pop()
        return str(self.book) == str(self.check)            
