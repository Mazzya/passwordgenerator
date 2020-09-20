#!/usr/bin/env python
# This script has been developed by Mazzya
# Github : https://github.com/Mazzya
# Repository address : https://github.com/Mazzya/passwordgenerator
# This script allows you to generate strong passwords and save them

import string
from io import open
from colorama import init, Fore, Style
import secrets


def GeneratePassword():
    """ This function generates strong passwords with the character length that the user wants. """

    current_version = "2.3.3"

    init(autoreset=True)

    # Creation of the variable where the generated password is stored
    password = ""

    chars = list(string.digits) + list(string.ascii_letters) + list(string.printable[:-9])

    try:
        
        print(f"{Fore.CYAN}{Style.BRIGHT}Welcome to Password Generator {current_version}\n")
        

        length = int(input("How many characters do you want the password to have ?: "))


        # If the user enters 4 characters or more, the password is generated
        if (length >= 4):

            for i in range(length):
                password += secrets.choice(chars)

            # The generated password is displayed next to a message
            print(f"{Fore.GREEN}{Style.BRIGHT}Password generated successfuly : {password}\n")
            
            # Asks the user if they want to save the password to a file.
            choice = input("Do you want save this password in a file ? (Yes or No): ")

            # If the user wants to save the password in a file.
            if (choice.lower() == "yes"):
                with open('password.txt', 'a+') as f:
                    f.write(f"Password : {password}" + "\n")
                print(f"{Fore.GREEN}{Style.BRIGHT}File saved successfully")

            # If the user don't wants to save the password in a file.
            elif (choice.lower() == "no"):
                print(f"{Fore.BLUE}{Style.BRIGHT}Closing...")
            
            # If the user enters another word that is neither 'yes' nor 'no'
            else:
                print(f"{Fore.RED}{Style.BRIGHT}Remember that you can only answer yes or no")

        # If the user enters less than 4 characters, the password is not generated
        else:
            print(f"{Fore.RED}{Style.BRIGHT}Enter a minimum of 4 characters")

    except ValueError:

        #If the user enters a letter or float instead of an integer
        print(f"{Fore.RED}{Style.BRIGHT}You have to enter an integer")

    except:
        print(f"{Fore.RED}{Style.BRIGHT}Something is wrong...")