'''
v 1 input.split
v 2 uniq num, Name, number, address to list of dicts 
v 3 sort by keys
v 4 search by substring
v 5 edit by key
v 6 delete el by uniq num
7 menu
'''
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
        # print(self.book)
            
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
        # self.check = self.book.copy()
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
            # for el in self.book:
            #     file.write(f'{str(el)}%')
                
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
                
def menu():
    print('========PHONE BOOK========')
    print('\'A\' to add record\n\'P\' to print')
    print('\'Srt\' -- sort by:\n\t\'num\' -- by phone number\n\t\'nam\' -- by name')
    print('\t\'#\' -- by unique number')
    print('\'Src\' to search\n\'E\' to edit\n\t\'nam\' -- name\n\t\'num\' -- number\n\t\'adr\' -- address')
    print('\'D\' to delete record')
    print('\'S\' to save book\n\'Q\' to quit')
pb = PhoneBook()

flag = True

menu()

with open('config.txt', 'r') as config_r:
    val = str(*config_r)
    if len(val) < 1:
        i = 1
    else: i = int(val)

while flag:
    inp = str.lower(input('Enter command (\'M\' to see menu)'))
    if inp == 'a':
        print('Enter the name, phone number, address (optional), separated by a semicolon (;)')
        pb.add_rec(input(), i)
        i += 1
    
    # print
    elif inp == 'p':
        pb.print()
    # sort
        # unique
    elif inp == 'srt #':
        pb.sort_by('#')
        pb.print()
        # nam
    elif inp == 'srt nam':
        pb.sort_by('Name')
        pb.print()
        # num
    elif inp == 'srt num':
        pb.sort_by('Number')
        pb.print()
    # search
    elif inp == 'src':
        pb.search(input('Enter search key: '))
    # edit
    elif inp == 'e nam':
        pb.edit(int(input('Enter number of record: ')), 'Name', 
                input('Enter new value: '))
    elif inp == 'e num':
        pb.edit(int(input('Enter number of record: ')), 'Number', 
                input('Enter new value: '))
    elif inp == 'e adr':
        pb.edit(int(input('Enter number of record: ')), 'Address', 
                input('Enter new value: '))
    # delete
    elif inp == 'd':
        pb.delete(int(input('Enter number of record to delete: ')))
    # save  
    elif inp == 's':
        pb.save()
        with open('config.txt', 'w') as config_w:
            config_w.write(str(i))
    
    elif inp == 'q':
        if not pb.is_changes():
            save = input('Save changes? Y/n: ').lower()
            if save == 'y':
                pb.save()
                with open('config.txt', 'w') as config_w:
                    config_w.write(str(i))
            elif save == 'n':
                flag = False
        flag = False
        
    elif inp == 'm':
        menu()
