import argparse

parser = argparse.ArgumentParser()
parser.add_argument('test_number', type=int, help='test case number')
args = parser.parse_args()
test_number = args.test_number

print(f'Running test: {test_number}')

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Question 1
# Print the sum of all the elements in numbers
# Use a for loop!
if test_number == 1:
    # TODO:
    pass

# Question 2
# Print the following using the numbers array
# and the `range` keyword
# 0
# 2
# 4
# 6
# 8

if test_number == 2:
    # TODO:
    pass

# Question 3
# Print the following using the numbers array
# and the `range` keyword
# 1
# 4
# 7

if test_number == 3:
    # TODO:
    pass

# Question 4
# Print the following using the numbers array
# and the `range` keyword
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0

if test_number == 4:
    # TODO:
    pass

# Question 5
# Implement the following method
# It should take in an integer x
# return True if x is even
# return False if x is odd

def is_even(x):
    # TODO:
    pass

# Don't change these prints
if test_number == 5:
    print(is_even(0))   # True
    print(is_even(1))   # False
    print(is_even(2))   # True
    print(is_even(3))   # False
    print(is_even(4))   # True
    print(is_even(-1))  # False


