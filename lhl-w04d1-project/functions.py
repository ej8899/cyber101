# W03D2
# FUNCTIONS


# Write a function that takes in a first name and a last name, and prints out a nicely formatted full name, in a sentence. Your sentence could be as simple as, "Hello, full_name."

def print_full_name(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

# f-strings allow us to embed expressions inside strings using {}.  It can be easier to use than  the older way:
# print("Hello, " + first_name + " " + last_name + "!")
# vs print(f"Hello, {first_name} {last_name}!")

# print_full_name("Jane", "Doe")

###################

# write a function that takes two numbers and adds them together.  function shold print out a sentence showing the two numbers and result.

def add_numbers_and_print(a,b):
    print(f"Here's your calculated output of {a} + {b}.\nThe result is {a+b}")

add_numbers_and_print(1,2)

