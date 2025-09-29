from helper_functions import clear_screen
clear_screen()

# ===========================
# CUSTOM FUNCTIONS - PRACTICE
# ===========================

# 1. MATH FUNCTION PRACTICE
# write a function that accepts 2 numbers, then divides
# the first by the second and multiplies it by 100
# don't worry about cases where you'd divide zero.
# just ignore that possibility. this is just simple practice.
# call the function and print the result

def math_function(num_1, num_2):
    result = (num_1 / num_2) * 100
    return result

result = math_function(20, 60)
print(result)
