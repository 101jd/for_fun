'''
Special thanks for Valery, Artem for testing :>
'''

from phonebook import PhoneBook
from menu import menu

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
