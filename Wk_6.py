import datetime

def accum(s):
    s_list = list(s)
    new = []
    for i in range(0, len(s_list)):
        print(i, s_list[i])
        new.append(s_list[i] * (i + 1))
    print(new)
    new_l = []
    for value in new:
        new_l.append(value.capitalize())
    return '-'.join(new_l)    


def get_middle(s):
    i = int(len(s))
    if (i % 2 == 0):
        return f'{s[int(i/2-1)] }{s[int(i/2)] }'
    else:
        return f'{s[int(i/2)] }'


def find_short(s):
    # your code here
    word_lengths = []
    print(list(s.split(' ')))
    for word in list(s.split(' ')):
        word_lengths.append(len(word))

    return min(word_lengths)


def to_jaden_case(string):
    new = string.split(' ')
    l = []
    for word in new:
        l.append(word.capitalize())
    print(l)
    return ' '.join(l)


def min_max(lst):
    lst.sort()
    return [lst[0], lst[len(lst)-1]]


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    curr_m, curr_d, curr_y = current_date.split(' ')
    
    exp_m, exp_d, exp_y = expiration_date.split(' ')
    print(curr_m)
    print(curr_d[:-1])
    print(curr_y)
    x = datetime.datetime(int(curr_y), 6, int(curr_d[:-1]))
    month_date = datetime.datetime.strptime(curr_m[0:3], "%b")
    month_numb = month_date.month
    print(month_numb)

    print('date ' + x.strftime("%Y" + "%B" + "%d"))


       
       
        

if __name__ == "__main__":
    print(check_coupon('123', '123', 'September 5, 2014', 'October 1, 2014'))
    