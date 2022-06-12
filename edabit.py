'''
drunken Python
'''
numbers_dict = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 0: '0'}


def int_to_str(num):
    for key, val in numbers_dict.items():
        if key == num:
            return val
    else:
        return (f'not a number')


def str_to_int(num):
    for key, val in numbers_dict.items():
        if num == val:
            return key
    else: 
        return(f'not a number')


def main():
    print(int_to_str(4))
    print(str_to_int('4'))
    for i in range(0 , 3):
        print(i)


if __name__ == '__main__':
    main()