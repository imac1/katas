'''
nth power
1. ridic la putere fiecare termen
2. fac suma puterilor
2. scad suma termenilor initiali
'''


def modified_sum(a, n):
    sum_powers = 0
    sum_initial_list = 0
    for i in a:
        sum_powers += i**n
        sum_initial_list += i
        

    return sum_powers - sum_initial_list


# print(modified_sum([1, 2, 3], 3))
url = "www.codewars.com#about"

def remove_url_anchor(url):
    new_url = ''
    for i in url:
        if i not in '!@#$%^&*_':
            new_url += i
    print(new_url)

def remove_url_anchor(url):
    return url.split('#')[0]

# print(remove_url_anchor(url))

# l = url.split('#')
# print(l)

l = [1, 2, 3]
print(l*2)
for i in l:
    # print(l.append(i*2))
