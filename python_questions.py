# Question #1: Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below:
def hello_name(user_name):
    print(f"hello_{user_name}, how are you?")

name = hello_name(input("What is your name? ").upper())

# Question #2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    first_odds = 0
    for i in range(1, 100, 2):
        odd_numbers = i + first_odds
        print(odd_numbers)

first_odds()

# Question #3: Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

#solution #1
max_list = [50, 10, 100, 1, 25]
largest_number = max_list[0]
def max_num_in_list(a_list):
    return max_list

print(max(max_list))

# Solution #2
for number in max_list:
    if number > largest_number:
        largest_number = number

print(largest_number)

# Question #4: Write a function to return if the given year is a leap year. A leap year is divisible by 4.
# but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    leap = a_year % 4
    if leap == 0:
        return True
    else:
        return False
year = int(input("Do you want to know if it's leap year? What year are we in? Enter the 4 digit: "))
print(is_leap_year(year))

# Question #5: # Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

my_list = [2, 3, 4, 5, 6]
def is_consecutive(my_list):
    test = list(range(min(my_list), max(my_list)+1))
    if test == my_list:
        return True
    else:
        return False

print(is_consecutive(my_list))