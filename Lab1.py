#Names: Justin Buss, Alexander Papachristu
#Date: January 21, 2025
#Date Last Modifed: January 21, 2025
#Discription: A random password generator that use a user inputed values to generate a password.

#https://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python

import random
import string
from random import shuffle
from string import punctuation

MIN_LENGTH = 8


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

def get_user_input():
    sum = 0
    num_letters = 0
    num_digits = 0
    num_specials = 0
    # Getting input from user
    try:
        length = input("Enter the total length of the password: ")
        length = int(length)
        if length < MIN_LENGTH:
            print(f"Please enter a value greater than {MIN_LENGTH}")
        else:
            get_user_input()
        num_letters = input("Enter the number of letters desired in the password: ")
        num_letters = int(num_letters)
        sum += num_letters
        num_digits = input("Enter the number of digits desired in the password: ")
        num_digits = int(num_digits)
        sum += num_digits
        num_specials = input("Enter the number of special characters desired in the password: ")
        num_specials = int(num_specials)
        sum += num_specials
    except:
        print("Not a valid input. Please input an integer value.")
        get_user_input()

    generate_password(num_letters, num_digits, num_specials)
    pass

get_user_input()