#!/usr/bin/env python
# This script has been developed by Mazzya
# Github : https://github.com/Mazzya
# Repository address : https://github.com/Mazzya/passwordgenerator
# This script allows you to generate strong passwords and save them
# Current version : 2.2.4

import string
from io import open
import secrets


def GeneratePassword():
    """ This function generates strong passwords with the character length that the user wants. """

    # Creation of the variable where the generated password is stored
    password = ""

    chars = list(string.digits) + list(string.ascii_letters) + list(string.printable[:-9])

    try:

        length = int(input("How many characters do you want the password to have ?: "))

        # If the user enters 4 characters or more, the password is generated
        if (length >= 4):

            for i in range(length):
                password += secrets.choice(chars)

            # The generated password is displayed next to a message
            print(f"Password generated successfuly : {password}")
            
            # Asks the user if they want to save the password to a file.
            choice = input("Do you want save this password in a file ? (Yes or No): ")

            # If the user wants to save the password in a file.
            if (choice.lower() == "yes"):
                file = open("password.txt", "a+")
                file.write(f"Password : {password}" + "\n")
                file.close()
                print("File saved successfully")

            # If the user don't wants to save the password in a file.
            elif (choice.lower() == "no"):
                print("Bye !")
            
            # If the user enters another word that is neither 'yes' nor 'no'
            else:
                print("Remember that you can only answer yes or no")

        # If the user enters less than 4 characters, the password is not generated
        else:
            print("Enter a minimum of 4 characters")

    except ValueError:

        #If the user enters a letter or float instead of an integer
        print("You have to enter an integer")

    except:
        print("Something is wrong...")