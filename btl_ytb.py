import random

HIDDEN_BOARD = [['0'] * 5 for i in range(5)]
# print(HIDDEN_BOARD)
GUESS_BOARD = [['0'] * 5 for i in range(5)]
letters_convert = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}

def print_board(board):
    for row in board:
        row_number = 0
        print('%d %s' % (row_number, '|'.join(row)))
        row_number += 1
    pass


def get_ship_location():

    pass

def count_hit_ships():
    pass

def create_ships(board):
    for ships in range(5):
        ship_row, ship_column = random.randint(0, 7), random.randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = random.randint(0, 7), random.randint(0, 7)
    pass

# create_ships()
# turn = 10
# while turn > 0:

def ship_dict(dictionary, row, col):
    dictionary = {'ship2': {'patrat1': (3, 3), 'patrat2': (3, 4)}, 'ship1': {'patrat1': (2, 0)}}
    # 'ship3': {'patrat1': (0, 0), 'patrat2': (0, 1), 'patrat3': (0, 2)},
    print(dictionary['ship2']['patrat1'])
    for key, value in dictionary.items():
    # Iterating through nested dictionary
    # Display each student data
        print(key)
        for nested_key, nested_value in value.items():
            if row in nested_value and col in nested_value:

                pass                



# def newf():
#     person = {"name": "Jessa", "country": "USA", "telephone": 1178}

# # access value using key name in []
#     print(person['name'])


def start():
    print(ship_dict(dictionary, row, col))


if __name__ == "__main__":
    
    dictionary = {'ship2': {'patrat1': (3, 3), 'patrat2': (3, 4)}, 'ship1': {'patrat1': (2, 0)}}
    # 'ship3': {'patrat1': (0, 0), 'patrat2': (0, 1), 'patrat3': (0, 2)},
    dictionary['ship2']['patrat1'] = (3, 3, 'H')
    print(dictionary['ship2']['patrat1']) 
    A = [[0, 0, 0], [0, 0, 0]]
    B = [[1, 1, 1], [1, 1, 1]]
    for row in A:
        for col in B:
            C = [x + y for x, y in zip(A, B)]
            print(C)
    
    print(C)
