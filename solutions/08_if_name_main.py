from helper_functions import clear_screen
clear_screen()

# ==========
# MAIN LOGIC
# ==========

'''
OVERVIEW
--------
You can see the name of a module by looking at the special __name__ variable.
You can prevent code from running when you import it from another module by
using an if statement to check the value of __name__ to see if it is equal to
__main__
'''

# 1. IMPORT MODULE
# Try to import example_module_02 and get access to the divide_2_numbers 
# function. Notice anything that prints from that file?
from example_module_02 import divide_2_numbers


# 2. __name__
# Print out __name__ Notice that example_module_02 also is printing out __name__
# If you start python from a file, the module's name will be "__main__". You can
# use that to put stuff in your module that will only run if you started python
# from that file.
print(__name__)