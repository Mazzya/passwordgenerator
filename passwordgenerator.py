# This script has been developed by Mazzya
# Github : https://github.com/Mazzya
# Repository address : https://github.com/Mazzya/passwordgenerator
# This script allows you to generate strong passwords and save them
# Current version : 2.2.1

import string
from io import open
import secrets


def GeneratePassword():
    password = ""
    """ Creation of the variable where the generated password is stored """

    chars = list(string.digits) + list(string.ascii_letters) + list(string.printable[:-9])

    try:

        length = int(input("How many characters do you want the password to have ?: "))

        if (length >= 4):

            for i in range(length):
                password += secrets.choice(chars)

            print(f"Password generated successfuly : {password}")
            
            choice = input("Do you want save this password in a file ? (Yes or No): ")

            if (choice.lower() == "yes"):
                file = open("password.txt", "a+")
                file.write(f"Password : {password}" + "\n")
                file.close()
                print("File saved successfully")
            elif (choice.lower() == "no"):
                print("Bye !")
            else:
                print("Remember that you can only answer yes or no")
        else:
            print("Enter a minimum of 4 characters")

    except ValueError:
        """If the user enters a letter or float instead of an integer"""
        print("You have to enter an integer")
    except:
        print("Something is wrong...")

GeneratePassword()