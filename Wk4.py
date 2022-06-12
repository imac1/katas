import enum
from itertools import permutations
import csv
import itertools
from datetime import datetime
from isort import file
# def apparently(string):
# string = 'It was great and I have never been on live television before but sometimes I dont watch this.'
# if 'and' in string:
#     print('correct')
#     x = string.find('and')
    
#     print(x)

# def scrolling_text(text):
#     new = text.upper()
#     if not new:
#         yield new
#     else:
#         for i in range(len(new)):
#             rest = new[:i]+new[i+1:]
#             for x in scrolling_text(rest):
#                 yield new[i:i+1]+x
#                 print(list(scrolling_text(text)))           


# 1st solution
    # permut = [''.join(p) for p in permutations(text)]
    # print(permut)
    # return permut
# # 2nd solution
#     new_txt = text.upper()
#     permutation_list = []
#     if len(new_txt) == 1:
#         return [new_txt]
#     else:
#         for char in new_txt:
#             [permutation_list.append(char + a) for a in scrolling_text(new_txt.replace(char, "", 1))]
#     return permutation_list

# 3rd solution
# from itertools import permutations
# for i in permutations('stack'):
#     print(''.join(i))


# print(scrolling_text('abc'))

# def permute(seq):
#     new = seq.upper()
#     if not new:
#         yield new
#     else:
#         for i in range(len(new)):
#             rest = new[:i]+new[i+1:]
#             for x in permute(rest):
#                 yield new[i:i+1]+x

# print(list(permute('abc')))
# def scrolling_text(text):
#     text = text.upper()
#     return [text[i:] + text[:i] for i in range(len(text))]

# print(scrolling_text('abc'))

# def filter_list(l):
#     li = []
#     val = 0
#     for i in l:
#         if i in range(0, 300):
#             li.append(i)

#     print(li)
    #     if val.isdigit():
    #         li.append(val)
    # return li

# print(filter_list([1, 2, 'a', 'b']))

# def stray(arr):
#     '''Finds the stray number in an array'''
#     first_num = arr[0]
#     second_num = arr[1]
#     if first_num != second_num:
#         third_num = arr[2]
#         if third_num == second_num:
#             return first_num
#         else:
#             return second_num
#     for num in arr:
#         if num != first_num:
#             return num

# print(stray([2, 3, 2, 2, 2]))

# def max_diff(arr):

#     dif = max(arr)-min(arr)

    
#     return dif

# print(max_diff([2, -3, 2]))

# a = [ [1, 2, 3],
#     [3, 2, 1],
#     [1, 1, 1] ]

# b = [ [2, 2, 1],
#     [3, 2, 3],
#     [1, 1, 3] ]

# def matrix_addition(a, b):

    # maxList = max(a, key = len)
    # maxLength = max(map(len, a))
    # print(maxList)
    # print(maxLength)
    # matrix = []

    # for r in range(0, maxLength):
    #     matrix.append([0 for c in range(0, maxLength)])

    # print(matrix)
    # aa = []
    # for row in range(len(a)):
    #     for col in range(len(a)):
    #         aa.append(a[row][col])
    # # print(aa)
    # bb = []
    # for row in range(len(b)):
    #     for col in range(len(b)):
    #         bb.append(b[row][col])

    # # print(bb)
    # cc = []
    # for (i1, i2) in zip(aa, bb):
    #     cc.append(i1 + i2)
    # dd = []
    # n = len(cc)

    # for i in range(len(cc)):
    #     dd.append([])
    #     for j in range(len(cc)):
    #         dd[i].append(j)
          
    # print(dd)
    # for row in range(len(a)):
    #     for index in range(len(a)):
    #         a[row][index] += b[row][index]
    # return a

    #     for i in range(len(a)):
    #     for j in range(len(a[0])):
    #         a[i][j] += b[i][j]
    # return a

    # L = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]   
    # for list in L:
    #     for number in list:
    #         print(number, end=' ')


    


# print(matrix_addition(a, b))


# k = {"flour": 500, "sugar": 200, "eggs": 1}

# for attr, value in k.items():
#         # print(attr, value)
#         print(f'{attr} {value}')

# Convert 2 lists into a dict
 # initializing lists
# test_keys = ["Rash", "Kil", "Varsha"]
# test_values = [1, 4, 5]
  
# Printing original keys-value lists
# print ("Original key list is : " + str(test_keys))
# print ("Original value list is : " + str(test_values))
  
# using naive method
# to convert lists to dictionary
# res = {}
# for key in test_keys:
#     for value in test_values:
#         res[key] = value
#         # test_values.remove(value)
#         break  
  


# Printing resultant dictionary 
# print ("Resultant dictionary is : " +  str(res))
#nested dict
# D = dict.fromkeys(test_keys, test_values)
# print(D)
# D = dict(zip(test_keys, test_values))
# print(D)
# birthdate = "1/1/2000"

# first = [ "The Evil","The Vile","The Cruel", "The Trashy","The Despicable", "The Embarrassing", "The Disreputable","The Atrocious", "The Twirling",  "The Orange","The Terrifying", "The Awkward"]
# last = ["Mustache", "Pickle", "Hood Ornament", "Raisin", "Recycling Bin", "Potato", "Tomato", "House Cat", "Teaspoon", "Laundry Basket"]
# # your code here
# date = birthdate.split('/')
# print(date)
# print(date[0])
# d = int(date[0])
# m = int(date[1])
# print(m)

# for i in range(0, len(first)):
#     if i == d:
#         print(first[i])



# return sum(x * (x > 0 and x or 1) * (i % 3 and 1 or 3) * (i % 5 and 1 or -1) for i, x in enumerate(a, 1))
# fifth  = lambda i, x: x if i%5 else -x
# third  = lambda i, x: x if i%3 else 3*x
# square = lambda x   : x if x<0 else x*x

# def calc(a):
#     return sum(fifth(i, third(i, square(x))) for i,x in enumerate(a, 1))

#     res = 0
#     for i in range(len(a)):
#         x = a[i]
#         if a[i] > 0:
#             x = x ** 2
#         if (i + 1) % 3 == 0:
#             x *= 3
#         if (i + 1) % 5 == 0:
#             x = -x
#         res += x
#     return res

    
    
# def calc(a):
#     total = 0

#     for i, x in enumerate(a):
#         n = x*x if x > 0 else x
#         if (i + 1) % 3 == 0: n *= 3
#         if (i + 1) % 5 == 0: n *= -1
#         total += n

#     return total

"""
Apparently-Modifying Strings
For every string, after every occurrence of 'and' 
and/or 'but', insert the substring 'apparently' directly after the occurrence(s).

If input does not contain 'and' or 'but', return the same string. 
If a blank string, return ''.

If substring 'apparently' is already directly after an 'and' and/or '
but', do not add another. (Do not add duplicates).
"""
def apparently_modifying_strings(string):
    string_list = list(string.split(' '))
    print(string_list)
    for word in string_list:
        if word == 'and':
            and_index = string_list[word]
    for index, value in enumerate(string_list):
        if value == 'and':
            string_list.insert(index + 1, 'apparently')
        elif 



''' Reversed Strings '''


def reversed_strings(word):
    return word[::-1]

def print_tables(table):
    ''' print rows as columns '''
    for row in table:
        for col in row:
            print(col)
        print('all columns')
    for row in range(len(table)):
        for col in range(len(table[row])):
            print(table[0][0])
        print()
    columns = list(zip(*table))

    print("column[0] = {}".format(columns[0]))
    print("column[1] = {}".format(columns[1]))
    print("column[2] = {}".format(columns[2]))
    for row in table:
        for col in table:
            print(col[2])
        print()

def main():
    # print(reversed_strings('word'))
    # table = [['p1', 'p2', 'p3'], [0, 1, 2]]
    string = 'It was great and apparently I have never been on live television before but sometimes I dont watch this.'
    print(apparently_modifying_strings(string))
    # print(print_tables(table))


if __name__ == '__main__':
    main()