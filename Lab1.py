#Names: Justin Buss, Alexander Papachristu
#Date: January 21, 2025
#Date Last Modifed: January 21, 2025
#Discription: A random password generator that use a user inputed values to generate a password.

#https://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python

import random
import string
from random import shuffle
from string import punctuation

def get_user_input(prompt, min_value, max_value):

    pass

def generate_password(num_letters, num_digits, num_specials):
    #letter loop
    letter_list = []
    for loop in num_letters:
        random_letter = random.choice(string.ascii_letters)
        letter_list.append(random_letter)
        if loop == num_letters:
            break
    #Number Loop
    number_list = []
    for loop in num_digits:
        random_number = random.choice(string.digits)
        number_list.append(random_number)
        if loop == num_digits:
            break
    #Special Loop
    special_list = []
    for loop in num_specials:
        random_special = random.choice(string.punctuation)
        special_list.append(random_special)
        if loop == num_specials:
            break
    random_password = letter_list + number_list + special_list
    return random_password
