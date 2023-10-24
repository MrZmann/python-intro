# TODO: 
#
# Provide implementation for each of the following questions.
# When opening files, be sure to use the 'with' syntax

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('test_number', type=int, help='an integer for the test number')
args = parser.parse_args()
test_number = args.test_number

print(f'Running test {test_number}')

# Question 1
# Open text/emoji.txt and print all of its contents

if test_number == 1:
    # TODO:
    pass

# Question 2
# Open text/lines.txt 
# Print each line with a line number
# Should look something like this
#
# 1: <contents of the first line>
# 2: <contents of the second line>
# ...
#
# If you are printing extra newlines,
# add end='' to your print method call

if test_number == 2:
    # TODO:
    pass

# Question 3
# Create a file called text/numbers.txt
# Write each number 100 through 1 descending
# Then save the file
# Should look something like this:
#
# 100
# 99
# 98
# ...
# 3
# 2
# 1

if test_number == 3:
    # TODO:
    pass

