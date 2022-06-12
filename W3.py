'''
Mario and Luigi 
Looks like some hoodlum plumber and his brother has been running around 
and damaging your stages again.

The pipes connecting your level's stages together need to be fixed 
before you receive any more complaints. Each pipe should be connecting, 
since the levels ascend, you can assume every number in the sequence after 
the first index will be greater than the previous and that there will be no duplicates.

Task

Given the a list of numbers, return the list so that the values increment by 
1 for each index up to the maximum value.
Example
Input: 1,3,5,6,7,8
Output: 1,2,3,4,5,6,7,8
'''
# def pipe_fix(nums):
#     return [i for i in range(nums[0], nums[-1] + 1)]

'''
Number-Star ladder
Using n as a parameter in the function pattern, where n>0, 
complete the codes to get the pattern (take the help of examples):
Note: There is no newline in the end (after the pattern ends)

Examples

pattern(3) should return "1\n1*2\n1**3", e.g. the following:

1
1*2
1**3
'''

# def pattern(n):
#     s = ''
#     for i in range(n):
#         if i == 0:
#             s += '1\n'
#         else:
#             s += '1{}{}\n'.format('*' * i, i + 1)
    
#     return s.rstrip('\n')

'''
Sum of Array Averages
Program a function sumAverage(arr) where arr is an array containing arrays full of numbers, for example:

sum_average([[1, 2, 2, 1], [2, 2, 2, 1]]);
First, determine the average of each array. Then, return the sum of all the averages.

All numbers will be less than 100 and greater than -100.
arr will contain a maximum of 50 arrays.
After calculating all the averages, add them all together, then round down, as shown in the example below:
The example given: sumAverage([[3, 4, 1, 3, 5, 1, 4], [21, 54, 33, 21, 77]]), the answer being 44.

Calculate the average of each individual array:
[3, 4, 1, 3, 5, 1, 4] = (3 + 4 + 1 + 3 + 5 + 1 + 4) / 7 = 3
[21, 54, 33, 21, 77] = (21 + 54 + 33 + 21 + 77) / 5 = 41.2
Add the average of each array together:
3 + 41.2 = 44.2
Round the final average down:
import math
math.floor(44.2) = 44

'''

# from statistics import mean
# from math import floor

# def sum_average(arr):
#     return floor(sum(map(mean, arr)))

# def sum_average(arr):
#     total = 0
#     for x in arr:
#         total += sum(x)/len(x)
#     return math.floor(total)

'''
Maximum Triplet Sum (Array Series #7)
Task

Given an array/list [] of n integers , find maximum triplet sum in the array Without duplications .

Notes :

Array/list size is at least 3 .

Array/list numbers could be a mixture of positives , negatives and zeros .

Repetition of numbers in the array/list could occur , So (duplications are not included when summing).

Input >> Output Examples

1- maxTriSum ({3,2,6,8,2,3}) ==> return (17)
Explanation:

As the triplet that maximize the sum {6,8,3} in order , their sum is (17)

Note : duplications are not included when summing , (i.e) the numbers added only once .


'''








'''

Count the Monkeys!
You take your son to the forest to see the monkeys. You know that there are a certain number there (n), but your son is too young to just appreciate the full number, he has to start counting them from 1.

As a good parent, you will sit and count with him. Given the number (n), populate an array with all numbers up to and including that number, but excluding zero.

For example:

monkeyCount(10) # --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
monkeyCount(1) # --> [1]
'''



'''
Reverse List Order
In this kata you will create a function that takes in a list and returns a list with the reverse order.

Examples

reverse_list([1,2,3,4]) == [4,3,2,1]
reverse_list([3,1,5,4]) == [4,5,1,3]
'''


'''
Add Length
What if we need the length of the words separated by a space to be added at the end of that same word and have it returned as an array?

add_length('apple ban') => ["apple 5", "ban 3"]
add_length('you will win') => ["you 3", "will 4", "win 3"]
Your task is to write a function that takes a String and returns an Array/list with the length of each word added to each element .

Note: String will have at least one element; words will always be separated by a space.
'''


'''
Jenny's secret message
Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.

Can you help her?
'''


def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


'''
I'm new to coding and now I want to get the sum of two arrays...
actually the sum of all their elements. I'll appreciate for your help.

P.S. Each array includes only integer numbers. Output is a number too.

'''


def array_plus_array(arr1, arr2):

    return sum(arr1) + sum(arr2)
    pass


'''
Parse nice int from char problem

Ask a small girl - "How old are you?". She always says strange things... 
Lets help her!

For correct answer program should return int from 0 to 9.

Assume test input string always valid and may look like "1 year old" or
 "5 years old", etc.. The first char is number only.
'''
def get_age(age):
    print(f'{age[0]} years old')

def hello_world():
  return (f"Hello World")
    

def is_greater(number_a, number_b):
    print("Is number_a greater than number_b?")
    if number_a > number_b:
        print("YES")
    else:
        print("NO")
    


def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz!')
    elif number % 5 == 0:
        print('Buzz!')
    elif number % 3 == 0:
        print('Fizz!')
    else:
        print(number)


def count_vowels(text):
    VOWELS = "aeiou"
    num_vowels = 0
    for char in text.lower():
        if char in VOWELS:
            num_vowels = num_vowels+1
            print(num_vowels)
    # lowercase = text.lower()
    # vowel_counts = {}
    # for vowel in VOWELS:
    #     count = lowercase.count(vowel)
    #     vowel_counts[vowel] = count
    # print(vowel_counts)
        



def start():
    # greet("James")
    # print(greet("james"))
    # print(array_plus_array([1, 2, 3], [4, 5, 6]))
    get_age("2 years old")
    print(hello_world())
    print(is_greater(1, 2))
    print(fizz_buzz(15))
    print(count_vowels('ana'))


if __name__ == '__main__':
    start()