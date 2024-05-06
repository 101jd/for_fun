import random

clubs, diamonds, hearts, spades, result, result_comp = [], [], [], [], [], []
score = 21
player_diff = 0
comp_diff = 0

def fill_deck(lst:list):
    for i in range(8):
        lst.append(i+2)
    for i in range(4):
        lst.append(10)
    lst.append(11)   
    
# выдать карту

def bank_card(lst:list, res:list):
    flag = True
    r0 = 0
    r1 = 0
    while flag:
        r0 = random.randint(0, len(deck)-1)
        if deck[r0] != []:
            flag = False
    r1 = random.randint(0, len(deck[r0])-1)
    
    card = deck[r0][r1]
    res.append(card)
    del deck[r0][r1]
    return card

def bank_card_comp(lst:list, res:list):
    flag = True
    r0 = 0
    r1 = 0
    while flag:
        r0 = random.randint(0, len(deck)-1)
        if deck[r0] != []:
            flag = False
    r1 = random.randint(0, len(deck[r0])-1)
    
    card = deck[r0][r1]
    res.append(card)
    del deck[r0][r1]
    
def calculate(result:list):
    sum_ = 0
    for el in result:
        sum_ += el
    return sum_

fill_deck(clubs)
fill_deck(diamonds)
fill_deck(hearts)
fill_deck(spades)

deck = [clubs, diamonds, hearts, spades]

# сдаём две карты

bank_card_comp(deck, result_comp)
bank_card_comp(deck, result_comp)
print('Your cards:\n', bank_card(deck, result), bank_card(deck, result), end=' ')
print('\n Press \'Y\' to calculate score or \'N\' to take another card')

# игра
flag = True
while len(deck) != 0 and flag:
    key = input()
    if str.lower(key) == 'y':
        flag = False
    if str.lower(key) == 'n':
        print(bank_card(deck, result))
        bank_card_comp(deck, result_comp)
        check = 0
        for el in result_comp:
            check += el
        if check >= score:
            flag = False
                
# calculate score
sum_player = calculate(result)
sum_comp = calculate(result_comp)
if sum_player == score:
    print('Your score is:\n', sum_player)
    print('Comp\'s score is:\n', sum_comp)
    print('You\'re winner!')
elif calculate(result) < score:
    player_diff = score - sum_player
    comp_diff = score - sum_comp
    if sum_player >= sum_comp:
        print('Your score is:\n', sum_player)
        print('Comp\'s score is:\n', sum_comp)
        print('You\'re winner!')
    else:
        print("You loose :(")
elif sum_player > score or sum_comp == score:
    print('Your score is:\n', sum_player)
    print('Comp\'s score is:\n', sum_comp)
    print("You loose :(")