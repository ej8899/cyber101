# Write a function that takes in a first name and a last name, and prints out a nicely formatted full name,
#  in a sentence. Your sentence could be as simple as, "Hello, full_name."


# def print_full_name(first, last):
#     print(f'Greetings, {first} {last}.')

# def print_name_reverse(first, last):
#       print(f'Hello, {last}, {first}.')



# print_full_name('Jane', "Doe")
# print_name_reverse('Jane', "Doe")


# Write a function that takes in two numbers, and adds them together. 
# Make your function print out a sentence showing the two numbers, and the result.

# def add_numbers(number_one,number_two):
#     result = number_one + number_two
#     print(f'Here is the result of adding {number_one} and {number_two}: {result}')

# add_numbers(1,2)


# Modify the above function to return the sum instead of printing inside the function
# def add_numbers(a,b):
#   result = a + b
#   return result

# the_answer_is = add_numbers(1,2)
# print(f"the sum of our math problem is: {the_answer_is}")


# Write a Python function to sum all the numbers in a list.
# my_numbers_list = [1,2,3,4,5];

# def sum_all_my_numbers(my_list):
#     total = 0
#     for each_number in my_list:
#         total = total + each_number
#     return total

# my_sum = sum_all_my_numbers(my_numbers_list)
# print (f"The sum of {my_numbers_list} is {my_sum}")


# Write a Python function to sum all the numbers in a list.
# my_string = "the dog is red and 3 years old"  
# expected output: dcba4321

# def reverse_string(my_string):
#     reversed_string = ""
#     # figure out how to revrse the string
#     for each_letter in my_string:
#         # reversed_string = reversed_string + each_letter
#         reversed_string = each_letter + reversed_string
#     return reversed_string

# print (reverse_string(my_string))


# Inputs: number, tuple of min and max
# Outputs: True/False
my_range = (3,10)
my_number = 5

def is_number_in_range(number, range_tuple):
    min_range = range_tuple[0]
    max_range = range_tuple[1]
    if number >= min_range and number <= max_range:
        return True
    else:
        return False

my_answer = is_number_in_range(my_number, my_range)
print (f"is {my_number} in range between {my_range[0]} and {my_range[1]}: {my_answer}")





