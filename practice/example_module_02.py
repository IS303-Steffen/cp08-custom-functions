'''
This file exists to show what if __name__ == '__main__' does
'''

def divide_2_numbers(num_1, num_2):
    product_num = num_1 / num_2
    return product_num 

print(f"The current name of this file is {__name__}")

print("NOTICE THIS IS PRINTING OUT! WHAT IF YOU ONLY WANT THE FUNCTION? BUT "
      "NOT THE OTHER STUFF IN THE FILE?")

if __name__ == "__main__":
    print("You must have run this python file first if you're seeing this")
