# # symbol = [[['1' for col in range(2)] for col in range(2)] for row in range(3)] 
# import enum


# symbol = [[['r1', 'r1'], ['r1', 'r1']], [['r2', 'r2'], ['r2', 'r2']], [['r3', 'r3'], ['r3', 'r3']]]
# print(symbol)
# print(len(symbol))

# for col in range(2):
#     for row in range(3):
#         print(symbol[row][col])

# for row in symbol:
#     for col in row:
#         print(row, end = " ")
#     print()

# addition = ['$','$'] # inserting $ symbol in the existing list
# symbol.insert(2, addition)
# print('Updated List is: ', symbol)
# for row in symbol:
#     for col in row:
#         print(row, end = " ")
#     print()
# print(symbol[0])
# print(len(symbol))
# symbol.insert(len(symbol), ['a', 'a'])
# for row in symbol:
#     for col in row:
#         print(col, end = " ")
#     print()
# # print(f'{symbol[0][0]} | {symbol[1][0]}')
# # print(f'{symbol[0][1]}')
# symbol2 = [[1, 2, 3], [3, 3, 3]]
# for row in symbol2:
#     for col in symbol2:
#         print(row, end='')
#     print('by row')

# for row in symbol2:
#     for col in symbol2:
#         print(col, end=' ')
#     print('by col')

# for row in range(0, 2):
#     for col in range(0, 2):
#         print(symbol2[0][col])

# '''
# access a column
# '''
# x = [row[2] for row in symbol2]
# print(x)
# for row in x:
#     for col in range(0, 1):
#         print(f'access col {row} {x[col]}')
# print()
# for row in x:
#     for col in range(0, 1):
#         print(f'{x[col]}')
# print()
# alist = [[[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10], [12, 13, 14]]]
# for row in alist: #One way to loop through nested lists
#     for col in row:
#         print(col)

# for row in range(len(alist)): #A less Pythonic way to loop through lists
#     for col in range(len(alist[row])):
#        print(alist[row][col])

# for row in range(len(alist)): #A less Pythonic way to loop through lists
#     for col in range(len(alist[row])):
#        print(alist[1][col])
# print()
# print(alist[0][0:])
# #[[8, 9, 10], 15, [12, 13, 14]]
# print()
# # print by row
# for row in range(len(alist)):
#     print(alist[row][:])
# table = [['cat', 123, 'yellow'],
#           ['dog', 12345, 'green'],
#           ['horse', 123456, 'red']]

# for line in table:
#     print("|", end='')
#     for word in line:
#         print (f" {word}".ljust(10) + "|", end='')
#     print()

# matrix = [] 
# for i in range(2): 
#     # create empty row (a sublist inside our list)
#     matrix.append([]) 
#     for j in range(5): 
#         matrix[i].append(j)
# print(matrix)
#  # print all matrix

# '''
#  1
# '''
# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
#     print()

# '''
#  2
# '''
# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# for row in a:
#     for elem in row:
#         print(elem, end=' ')
#     print()
# print('one liner')
# for row in a:
#     print(' '.join([str(elem) for elem in row]))

# for row in a[1:]:
#     for col in range(0, 1):
#         print(a[col])
# '''
# https://www.kite.com/python/answers/how-to-print-a-list-of-lists-in-columns-in-python
# '''
# """

# """
''' print table by column '''
# for row in range(len(table)):
#     print(table[row][0])
# x = [row[2] for row in table]
# print(x)

# table = [['kH38Jm#&', 'Lieselotte Rainey', 'hv8@qsuotla508.com', '1'], ['kH14Ju#&', 'Adrianna Verduzco', 'i-4371v-.rhck@qe8yy3d.com', '0'], ['eH34Jd#&ere', 'Maude TollHom', 't1ytt@vpm5xkvn.com3ra', '1']]
# # user_ID = 'eH34Jd#&ere'
# # updated_user = ['eH34Jd#&ere', 'matilda', 'samanta', '1']
# # ID_col = [row[0] for row in table]
# # for item in range(len(ID_col)):
# #     if ID_col[item] == user_ID:
# #         row_index = item
# # print(f'item {row_index}')

# # for row in range(len(table)):
# #     for index in range(len(table)):
# #         print(index)
# #         # table[2][0] = user_ID
# #         # table[2][1] = updated_user[1]
# #         # table[2][2] = updated_user[2]
# #         table[row_index][index] = updated_user[index]
# # # print(table)
# # for row in table:
# #     for index in range(len(updated_user)):
# #         if row[0] == updated_user[0]:
# #             row[index] = updated_user[index]


# # print(table)

# strin = '1993-04-04'
# print(strin[0: 4])
# print(strin[5: 7])
# print(strin[8: 10])

# # data = [title] + list(zip(title))

#     # for i, d in enumerate(table):
#     #     line = '|'.join(str(x).ljust(12) for x in d)
#     #     print(line)
#     #     if i == 0:
#     #         print('-' * len(line))
#         # for item in title:
#     #     print(item, '      |         ', end='')
#     # for item in table:
#     #     print("  ")
#     #     for data in item:
#     #         print(data, "       |         ", end='')
#     #     print()

#        # for row in title:
#     #     print("|{: ^27} |{: ^27} | {: ^27} | {: ^27} |".format(*row))
#     # for row in table:
#     #     print("|{: ^27} | {: ^27} | {: ^27} | {: ^27} |".format(*row)) 

# # for row in table:
# #     for cell in row:
# #         print(f'{row[0]}')
# #         print(f'{row[1]}')
# #         # print(f'{cell[1]} {cell[1]} {cell[2]} {cell[3]}')
# #         # print(f'{cell[2]} {cell[1]} {cell[2]} {cell[3]}')
# #         # print(f'{cell[3]} {cell[1]} {cell[2]} {cell[3]}')

# table_dogs_cats = [['cat', 123, 'yellow'],
#           ['dog', 12345, 'green'],
#           ['horse', 123456, 'red']]


# # for line in table_2:
# #     print("|", end='')
# #     for word in line:
# #         print(f" {word}".center(27) + "|", end='')
# #     print()
# # row_format = "{:^22}" * (len(header) + 1)
# # print(row_format.format("", *header))
# # for team, row in zip(header, table_2):
# #     print(row_format.format(table_2, *row))
# # a, b, c, d = header
# # print('<' + a)
# # for i in header:
#     # print(''.join('_'))
#     # print('|{0:s} | {0:s} | {0:s} | {0:s} |'.format("-"))

#     # for row in table_2:
#     #     print(f'{row[0]} | {row[1]} | {row[2]} | {row[3]}')
#     #     print('--------------------------------------')
#     # print(table_2[0][0])
#     # print("{: >20} {: >20} {: >20} {:^20}".format(*row))
#     # for idx, row in enumerate(table_2):
#     #     if idx == 0:
#     #         print("-"*85)

#         # string format mini language:
#         #  {:<20} means take the n-th provided value and right align in 20 spaces
#         # print(f"|{:<10}|{:<25}|{:<27}|{:<15}|") # *row == row element wise
#     #     print(f'{row[0]} | {row[1]} | {row[2]} | {row[3]}')
#     #     if idx == 0:
#     #         print("-"*85)
#     # print("-"*85)
    
from unittest import result


table_2 = [['kH14Ju#&', 'r', 'r', 'r'], ['kH14Ju#&', 'Adrianna Verduzco', 'i-4371v-.rhck@qe8yy3d.com', '0'], ['kH38Jm#&', 'john', 'email', '1'], [''], ['kH38Jm#&'], ['er', 'name', 'email', '0'], ['tototot', 'rororo', 'romnn', '1']]
title_2 = ['id', 'name', 'email', 'subscribed']

def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    table = [title_list] + table
    print(table)
    col_width = list()
    ''' acces a column'''


        # print(table[row][1])
    # x = [row[1] for row in table]
    # print(x)



    # for line in table:
    #     print("|", end='')
    #     for word in line:
    #         print(f" {word}" + "|", end='')
    #     print()
    ''' one loop'''
    # for row in table: #One way to loop through nested lists
    #     for col in row:
    #         print(row[1])
    ''' less pythonic'''
    # for row in range(len(table)): #A less Pythonic way to loop through lists
    #     for col in range(len(table[row])):
    #         print(table[row])
    """ row with slices"""
    print(table[0][:])
    print(table[3])
    print(table[3][1])
    row = table[0][:]
    print(len(row))
    ''' access column with slices'''

    for j in range(0, len(row)):
        print(table[0][j])

    ''' access with indices'''
    for i in range(len(table)):
        for j in range(len(table[i])):
            print(table[i][j], end=' ')
        print()

    # for i, title in enumerate(title_list):
    #     col_width.append(len(title))

    # for items in table:
    #     for i, item in enumerate(items):
    #         try:
    #             if col_width[i] < len(str(item)):
    #                 col_width[i] = len(str(item))
    #         except:
    #             col_width.append(len(item))

    # table_size = 1
    # for dash in col_width:

    #     table_size += (dash + 3)
    # print("|", end="")
    
    # for i, title in enumerate(title_list):
    #     if i == 0:
    #         print('/' + '---'*len(table) + '\\')
        
    #     print('{:{width}} |'.format(title, width=col_width[i]), end="")

    # print('\n' + '|' + ('--------' * (len(title))) + '|')
    
    # for items in table:
    #     for i, item in enumerate(items):
    #         if i == 0: 
    #             print('|', end="")
    #         print('{:{width}} |'.format(item, width=col_width[i]), end="")
    #     print('\n' + '---'*len(table))

# print(print_table(table_2, title_2))
# print(print_table(table_2, title_2))

# print(table_2[0])
# print(table_2[1])
# price = 50
# sales = [['ff', 'kkkkkkk', '154.0'], ['fff', 'ggg', '100.0']]

# ID_col = [row[2] for row in sales]
# print(ID_col)
# biggest_gain = max(map(int, ID_col))
# print(biggest_gain)
# b = ['123.4', '111.4']
# for index, value in enumerate(b):
#     index_of_dot = value.index('.')
#     stripped_val = value[0: index_of_dot]
#     if stripped_val in value:
#         index_to_search = index

# index = b.index('123.4')

# print(index)

# stripped_prices = []

# for item in b:
#     index_of_dot = item.index('.')
#     stripped_val = item[0: index_of_dot]
#     stripped_prices.append(stripped_val)

# print(stripped_prices)
# print(stripped_prices.index('111'))
# print(b.index('111'))
# months = ['01', '02']
# int_months = [int(x) for x in months]
# print(int_months)
# for item in range(len(months)):
#     if item == 0:
#         months[item] = 'popo'
# print(months)
# print(sales)
# print(sales[1][2])
# sales[1][2] = 'popo'
# print(sales)

sales = [['ff', 'kkkkkkk', '154.0'], ['fff', 'ggg', '100.0']]
# col_width = []
# for row in sales:
#     col = 

leng = [3, 5, 4]
print(max(leng))
print(max(sales))
print('_ '*max(leng))

# for i in range(len(sales)):
#     for row in sales:
#         x = max(row[i])
#         leng.append(x)

print(leng)

for items in sales:
    for i, item in enumerate(items):
        if i == 0: 
            print('|', end="")
        print('{:{width}} |'.format(item, width=leng[i]), end="")
    
    print('\n' + '_______'*len(leng)) 
    print()


alist = [[[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10], [12, 13, 14]]]
points = [(1, 2), (3, 4), (5, 6)]
for i in points:
    for q in points:
        print(f'{q[1]} ')

''' transpose a matrix'''
print('transpose')
blist = [[1, 2], [3, 4], [5, 6]]

for i in range(len(blist[0])):
    for j in range(len(blist)):
        blist[j][i]

print(blist[j][i])
''' with range '''
print('with range')
res = [[0, 0, 0], [0, 0, 0]]
# iterate through rows
for i in range(len(blist)):
   # iterate through columns
   for j in range(len(blist[0])):
       res[j][i] = blist[i][j]
print(res[j][i])
print('with zip')
''' with zip'''
blist = [[1, 2], [3, 4], [5, 6]]
for i in zip(*blist):
    print(list(i))