current_date = list(input('Введите дату через пробел: ').split())

current_day = int(current_date[0])
current_month = int(current_date[1])
current_year = int(current_date[2])
start_year = 2024

days_in_week = 7

def is_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False

def fill_months(days, year=start_year):
    month = []
    for i in range(1, days + 1):
        month.append(i)
        
    if is_leap(year) and days < 30:
        month.append(29)
        
    return month

jan = fill_months(31)
feb = fill_months(28)
mar = fill_months(31)
apr = fill_months(30)
may = fill_months(31)
jun = fill_months(30)
jul = fill_months(31)
aug = fill_months(31)
sep = fill_months(30)
oct = fill_months(31)
nov = fill_months(30)
dec = fill_months(31)

all_months = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]

def print_day(cnt):
    switcher = {
        1:"Monday",
        2:"Tuesday",
        3:"Wednesday",
        4:"Thursday",
        5:"Friday",
        6:"Saturday",
        7:"Sunday"
    }
    return switcher[cnt]
    

def is_weekend(months, day=current_day, month=current_month, year=start_year, cur_year=current_year, din=days_in_week):
    if year <= cur_year:
        cnt = 1
        while year <= cur_year:
            months[1] = fill_months(28, year)
            for el in range(len(months)):
                for i in range(len(months[el])):
                    if cnt > din:
                        cnt = 1
                    if months[el][i] == day and el+1 == month and year == cur_year:
                        return print_day(cnt)
                    cnt += 1
            year += 1
            months[1].clear()
            
    else:
        cnt = 7
        year -= 1
        while year >= cur_year:
            months[1] = fill_months(28, year)
            for el in range(len(months)-1, -1, -1):
                for i in range(len(months[el])-1, -1, -1):
                    if cnt <= 0:
                        cnt = 7
                    if months[el][i] == day and el+1 == month and year == cur_year:
                        return print_day(cnt)
                    cnt -= 1
            year -= 1
            months[1].clear()
    return print_day(cnt)

print(is_weekend(all_months))