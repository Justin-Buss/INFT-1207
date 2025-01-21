#Names: Justin Buss, Alexander Papachristu
#Date: January 21, 2025
#Date Last Modifed: January 21, 2025
#Discription: A random password generator that use a user inputed values to generate a password.

#https://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python

import random
import string
from string import punctuation

def get_user_input(prompt, min_value, max_value):

    pass
def generate_password(length, num_letters, num_digits, num_specials):
    pass

random_letter = random.choice(string.ascii_letters)
print(f"Random Letter: {random_letter}")

random_number = random.choice(string.digits)
print(f"Random Number: {random_number}")

random_special = random.choice(string.punctuation)
print(f"Random Special Character: {random_special}")

print("This is a commit")