import random


def generate_complex_password(numbers, letters, symbols, dimension):
    password = ''
    for i in range(0, dimension):
        letter = random.choice(letters)
        number = random.choice(numbers)
        symbol = random.choice(symbols)
        password += letter + str(number) + symbol

    return password


def generate_simple_password(list, dimension):
    password = ''
    for i in range(0, dimension):
        character = random.choice(list)
        password += str(character)
    return password

    
def main():
    dimension = 5
    numbers = [0, 6, 3, 7, 4, 9, 1, 5, 2, 8]
    letters = ['h', 'r', 'b', 'u', 'd', 'q', 'o', 'l', 's', 'a', 'y', 'e', 'k', 'i', 'w', 'g', 'j', 'm', 'x', 'p', 'z', 'v', 'f', 't', 'b', 'n']
    symbols = ['%', '-', '&', '$', ')', '!', '*', '@', '_', '(', '+', '#', '=']
    print("Password with Letters, Numbers and Symbols: " + generate_complex_password(numbers, letters, symbols, dimension))
    print("Password with Letters: " + generate_simple_password(numbers, dimension))
    print("Password with Symbols: " + generate_simple_password(symbols, dimension))

if __name__ == "__main__":
    main()