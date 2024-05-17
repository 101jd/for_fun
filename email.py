def is_email(string:str):
    if string.count('@') == 1 and string[string.find('@')+2:].count('.') == 1:
        pos = string.find('@')
        tmp = string[pos+1:]
        dot = tmp.find('.')
        if len(string[:pos]) > 0 and len(tmp[:dot]) > 0 and len(tmp[dot+1:]) > 0:
            return True
    return False

def parse_email(string:str):
    if is_email(string):
        pos = string.find('@')
        username = string[:pos]
        tmp = string[pos+1:]
        dot = tmp.find('.')
        post_service = tmp[:dot]
        domain = tmp[dot+1:]
        return f'username: {username}, post service: {post_service}, domain: {domain}'

def check_input(string):
    if not is_email(string):
        print('Invalid e-mail')

inp = ''

while not is_email(inp):
    inp = input('Enter e-mail: ')
    check_input(inp)
    
print(parse_email(inp))